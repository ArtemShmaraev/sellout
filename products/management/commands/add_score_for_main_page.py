from itertools import count
from django.core.management.base import BaseCommand
import json
from products.models import Product, Category, Line, Gender, Brand, Tag, Collection, Color, Collab
from django.core.exceptions import ObjectDoesNotExist
import users.models


class Command(BaseCommand):

    def handle(self, *args, **options):
        def update_model_scores(model_class, file_name):

            with open(file_name, 'r', encoding="utf-8") as file:
                data = json.load(file)

            for item in data:
                model_name = item.get('name')
                score = item.get('score')
                score = score - 10 if score > 10 else score

                # Пытаемся найти запись по имени
                model_instance = model_class.objects.filter(name=model_name).first()

                # Если запись не найдена, создаем новую запись
                if model_instance:
                    # if "все" not in model_instance.name.lower() and "вся" not in model_instance.name.lower():
                    # Если запись найдена, обновляем поле score
                    model_instance.score_product_page = score
                    model_instance.save()
                    print(model_instance.name)
                else:
                    print(model_name)

        # update_model_scores(Category, "categories_score.json")
        update_model_scores(Collab, "collab_score_product_page.json")
        # update_model_scores(Brand, "brands_score.json")
        # update_model_scores(Line, "lines_score_product_page.json")

        print("Данные о брендах успешно обновлены.")

