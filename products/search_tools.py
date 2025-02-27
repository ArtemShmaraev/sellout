import json
import re
from time import time

from django.core.cache import cache
from django.shortcuts import render
from elasticsearch import Elasticsearch
from elasticsearch_dsl.query import Match, MoreLikeThis

from sellout.settings import ELASTIC_HOST, CACHE_TIME
from .models import Line, Category, Color, Collab, Product
from .serializers import ProductMainPageSerializer
from elasticsearch_dsl import Search, SF
from django.db.models import Case, When, Value, IntegerField
from elasticsearch_dsl.search import Search, Q

from .documents import LineDocument

es = Elasticsearch(
    [ELASTIC_HOST],
    http_auth=("elastic", "espass2024word"),
    scheme="http",  # Используйте "https", если ваш сервер настроен для безопасного соединения
    port=9200,
)


def suggest_search(request):
    query = request.query_params.get('q')

    index_name = 'suggest_index'

    search = Search(index=index_name, using=es)
    search = search.suggest(
        'autocomplete',
        query,  # Часть слова, по которой будет выполняться поиск
        completion={
            'field': 'suggest',
            'size': 25,
            # 'analyzer': analyzer_name,
            'fuzzy': {  # Добавляем фильтр fuzzy для допуска опечаток
                'fuzziness': 'AUTO'  # Автоматический режим допуска опечаток
            }
            # Указываем соответствующий анализатор для поиска
        }
    )

    #
    # search = Search(index='suggest_index')
    # search = search.suggest(
    #     'autocomplete',
    #     query,  # Часть слова, по которой будет выполняться поиск
    #     completion={
    #         'field': 'suggest',
    #         'size': 10
    #     }
    # )

    response = search.execute()
    suggestions = response.suggest.autocomplete[0].options

    # Обработка полученных подсказок
    gender = False

    if request.user.id:
        gender = request.user.gender.name
        sp = []
        for suggestion in suggestions:
            sp.append({"name": suggestion._source.name, "type": suggestion._source.type,
                       "url": f"{suggestion._source.url}&gender={gender}"})
            #
    else:
        sp = []
        for suggestion in suggestions:
            sp.append({"name": suggestion._source.name, "type": suggestion._source.type, "url": suggestion._source.url})

    print(sp)

    search = Search(using='default', index='product_index')

    search = search.query(
        'function_score',
        query=Q('match', full_name={'query': query, 'fuzziness': 'AUTO'}),
        # Запрос по полю full_name с учетом расплывчатости
        functions=[
            SF('field_value_factor', field='rel_num', modifier='log1p')  # Учет поля rel_num в функции ранжирования
        ]
    )

    search = search.sort(
        {'_score': {'order': 'desc'}},
        {'rel_num': {'order': 'desc'}}
    )

    search = search[:5]
    response = search.execute()
    # with open('results.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(response.to_dict(), json_file, ensure_ascii=False, indent=4)
    product_ids = [hit.meta.id for hit in response.hits if hit.meta.score > 0.6]
    data = ProductMainPageSerializer(Product.objects.filter(id__in=product_ids, available_flag=True), many=True).data
    for i in data:
        i['type'] = "product"
        sp.append(i)

    # sp.append()

    return sp

    # # Создайте объект Search и настройте подсказки
    # search = Search(index=index_name)
    # s = search.suggest('user-input-suggestions', query, completion={'field': 'suggest', 'size': 100, 'fuzzy': {
    #     'fuzziness': 'AUTO'
    # }})
    #
    # # Выполнение запроса
    # response = s.execute()
    #
    # # Извлечение подсказок из ответа
    # suggestions = response.suggest['user-input-suggestions'][0]['options']
    # sp = []
    #
    # # Вывод подсказок
    # for suggestion in suggestions:
    #
    #     sp.append({"name": suggestion._source.name, "type": suggestion._source.type, "url": suggestion._source.url, "sug": suggestion._source.suggest})
    #     # sp.append(dict(suggestion._source))
    # return sp

    # Извлечение всех подсказок из ответа
    # suggestions = response.suggest['all-suggestions'][0]['options']

    # Вывод всех подсказок
    # for suggestion in suggestions:
    #     print(suggestion.text)


def similar_product(product):
    try:
        t = time()
        index_name = "product_index"
        search = Search(index=index_name, using=es)  # Замените на имя вашего индекса
        # print(search.count())

        # search = search.query(
        #     MoreLikeThis(
        #         like={'_id': product.id},
        #         fields=['main_category_eng^4', 'categories_eng', 'lines', "main_line", 'model', 'colorway',
        #                 'collab', "colors", "text_price", 'gender'],
        #         min_term_freq=1,
        #         min_doc_freq=1,
        #         max_query_terms=50,
        #         boost_terms=1.5,
        #         # boost=1.2
        #     )
        # )
        genders_rus = {"Male": "мужской", "Female": "женский", "Kids": "детский", "M": "мужской",
                       "F": "женский", "K": "детский"}
        gender = [genders_rus[gender.name] for gender in product.gender.all()]

        mlt_query = {
            "more_like_this": {
                "fields": [
                    "main_category_eng",
                    "text_price",
                    "categories_eng",
                    "lines",
                    "main_line^7",  # Устанавливаем вес 3 для поля main_line
                    "colorway",
                    "collab",
                    "colors^6"  # Устанавливаем вес 2 для поля colors
                ],
                "like": {"_id": product.id},
                "min_term_freq": 1,
                "min_doc_freq": 1,
                "max_query_terms": 50,
                "boost_terms": 1.5
            }
        }


        print("djn", gender)
        gender_filters = [Q("match", gender=gender_value) for gender_value in gender]

        # Объединяем фильтры с помощью оператора OR
        gender_filter = Q("bool", should=gender_filters, minimum_should_match=1)
        # Определяем фильтр по полю "gender" для поиска только товаров того же гендера
        # gender_filter = Q("term", gender=" ".join(gender))  # Замените product_gender на гендер заданного товара
        # mlt_query["more_like_this"]["filter"] = gender_filter
        # Применяем фильтр к поисковому запросу
        search = search.query(Q("bool", must=[mlt_query], filter=[gender_filter]))
        # search = search.query(Q("bool", must=[mlt_query]))


        # fields=['brands', 'categories', 'lines', 'model', 'colorway', 'collab']

        search = search[:36]

        # Выполните запрос
        response = search.execute()


        print(product.gender.all())

        product_ids = [hit.meta.id for hit in response.hits]
        product_ids = product_ids[:len(product_ids) // 2 * 2]

        queryset = Product.objects.filter(id__in=product_ids).filter(
            available_flag=True).filter(is_custom=False).exclude(spu_id=product.spu_id)
        print(list(queryset.values('gender__name')))

        # Определение порядка объектов в queryset
        preserved_order = Case(
            *[
                When(id=pk, then=pos) for pos, pk in enumerate(product_ids)
            ],
            default=Value(len(product_ids)),
            output_field=IntegerField()
        )

        # Применение порядка к queryset
        queryset = queryset.annotate(order=preserved_order).order_by('order')
        return queryset, True
    except:
        print(",kznm", time() - t)
        return [], False


def add_filter_search(request):
    query = request.query_params.get('q', '')

    res = {"collab": "",
           "category": "",
           "line": "",
           "color": "",
           'gender': ""}
    if request.user.id:
        gender = request.user.gender.name
        res['gender'] = gender

    print(res)
    return res
    search_line = search_best_line(query)
    search_category = search_best_category(query)
    search_color = search_best_color(query)
    search_collab = search_best_collab(query)

    if search_collab:
        res['collab'] = search_collab.name
    if search_category:
        res['category'] = search_category.eng_name
    if search_line:
        res['line'] = search_line.full_eng_name
    if search_color:
        res['color'] = search_color.name
    return res


def search_product(query, pod_queryset, page_number=1):
    cache_key = f"search:{re.sub(r'[^a-zA-Z0-9а-яА-Я]', '', query)}"
    cached_data = cache.get(cache_key)

    if cached_data is None:
        # search = search.query('bool', must=[
        #     {'match': {'full_name': {'query': query, 'fuzziness': 'AUTO'}}}])

        search = Search(index="product_index", using=es)

        one_search = search.query(
            Q('match_phrase', manufacturer_sku=query)
        )
        response = one_search.execute()
        total_hits = response.hits.total.value
        print(total_hits, query)
        if total_hits == 1:
            product_ids = [hit.meta.id for hit in response.hits]
        else:

            search = search.query(
                'function_score',
                query=Q('match', full_name={'query': query, 'fuzziness': 'AUTO'}),
                # Запрос по полю full_name с учетом расплывчатости
                functions=[
                    SF('field_value_factor', field='rel_num', modifier='log1p')  # Учет поля rel_num в функции ранжирования
                ]
            )

            search = search.sort(
                {'_score': {'order': 'desc'}},
                {'rel_num': {'order': 'desc'}}
            )

            search = search[:600]
            response = search.execute()
            # with open('results.json', 'w', encoding='utf-8') as json_file:
            #     json.dump(response.to_dict(), json_file, ensure_ascii=False, indent=4)
            product_ids = [hit.meta.id for hit in response.hits if hit.meta.score > 0.6]
        cache.set(cache_key, product_ids, CACHE_TIME)
    else:
        product_ids = cached_data

    # fields = ['manufacturer_sku^6', 'model^3', 'lines^2', 'colorway^1', "collab^4", "categories^3", 'brands^4']
    # search = search.query(Q("multi_match", query=query, fields=fields))
    # search = search.query('bool',
    #                       must=[
    #                           Q('multi_match',
    #                             query=query,
    #                             type="most_fields",
    #                             fields=['model^3', 'lines^2', 'colorway^1', 'categories^3', 'brands^4'],
    #                             fuzziness="AUTO")
    #                       ],
    #                       should=[
    #                           # Q('match', main_line={'query': query, 'boost': 2, 'fuzziness': 'AUTO'}),
    #                           Q('match', colorway={'query': query, 'fuzziness': 'AUTO'}),
    #                           Q('match', manufacturer_sku={"query": query, 'boost': 8, 'fuzziness': 2})
    #                       ]
    #                       )

    # search = search.query(
    #     'multi_match',
    #     query=query,
    #     fields=['manufacturer_sku', "full_name"],
    #     # Установите вес для каждого поля
    #     fuzziness='AUTO'
    # )

    # , should=[
    #     {'match': {'manufacturer_sku': {'query': query, 'fuzziness': 'AUTO', 'boost': 1}}}
    # ])

    # for hit in response['hits']['hits'][:10]:
    #     print(hit['_score'], hit['_source']['rel_num'])
    #
    #     result = json.dumps(hit['_source'].to_dict(), indent=4, ensure_ascii=False)
    #     # print(result)

    # Определите пороговое значение для подходящих результатов (50% от max_score)

    # Запись результатов в JSON файл
    # output_file = 'search_results.json'
    # with open(output_file, 'w', encoding="utf-8") as f:
    #     json.dump(response.to_dict(), f, indent=4)
    # max_score = response.hits.max_score
    # threshold = min(len(query) / 25, 0.8) * max_score

    queryset = pod_queryset.filter(id__in=product_ids)
    preserved_order = Case(
        *[
            When(id=pk, then=pos) for pos, pk in enumerate(product_ids)
        ],
        default=Value(len(product_ids)),
        output_field=IntegerField()
    )
    queryset = queryset.annotate(order=preserved_order).order_by('order')
    res = {"queryset": queryset}

    return res


def search_best_line(query_string):
    search = Search(index="line_index", using=es)
    search = search.query(
        'multi_match',
        query=query_string,
        fields=['name'],  # Поле для поиска
        fuzziness='AUTO'
    )
    # search = search.sort('_score')  # Сортировка по рейтингу убывающим образом
    response = search.execute()

    if response:
        if response.hits[0].meta.score > 4:
            # print("Line", Line.objects.get(id=response.hits[0].meta.id).name, response.hits.max_score)
            return Line.objects.get(name=response.hits[0].name)

    return None


def search_best_category(query_string):
    search = search = Search(index="category_index", using=es)
    search = search.query(
        'multi_match',
        query=query_string,
        fields=['name'],  # Поле для поиска
        fuzziness='AUTO'
    )
    # search = search.sort('_score')  # Сортировка по рейтингу убывающим образом
    response = search.execute()

    if response:
        if response.hits[0].meta.score > 4:
            # print("Category", Category.objects.get(id=response.hits[0].meta.id).name, response.hits.max_score)
            return Category.objects.get(id=response.hits[0].meta.id)
    return None


def search_best_color(query_string):
    search = Search(index="color_index", using=es)
    search = search.query(
        'multi_match',
        query=query_string,
        fields=['russian_name', 'eng_name'],  # Поле для поиска
        fuzziness='AUTO'
    )

    # search = search.sort('_score')  # Сортировка по рейтингу убывающим образом
    response = search.execute()

    if response:
        print("Color", Color.objects.get(id=response.hits[0].meta.id).name, response.hits.max_score)
        return Color.objects.get(id=response.hits[0].meta.id)
    return None


def search_best_collab(query_string):
    search = Search(index="collab_index", using=es)
    search = search.query(
        'multi_match',
        query=query_string,
        fields=['name'],  # Поле для поиска
        fuzziness='AUTO'
    )
    # search = search.sort('_score')  # Сортировка по рейтингу убывающим образом
    response = search.execute()

    if response:
        if response.hits[0].meta.score > 5:
            print("Collab", Collab.objects.get(id=response.hits[0].meta.id).name, response.hits.max_score)
            return Collab.objects.get(id=response.hits[0].meta.id)
        return None
    return None
