import rest_framework.generics
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
import json
from .models import Product, Category, Line
from rest_framework import status
from .serializers import ProductMainPageSerializer, CategorySerializer, LineSerializer
from .tools import build_line_tree, build_category_tree, category_no_child, line_no_child


# Create your views here.


class ProductSlugView(APIView):
    # authentication_classes = [JWTAuthentication]

    def get(self, request, slug):
        try:
            product = Product.objects.get(slug=slug)
            serializer = ProductMainPageSerializer(product, context={'user_id': request.user.id})
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response("Товар не найден", status=status.HTTP_404_NOT_FOUND)


class ProductIdView(APIView):
    # authentication_classes = [JWTAuthentication]

    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            serializer = ProductMainPageSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response("Товар не найден", status=status.HTTP_404_NOT_FOUND)


class CategoryTreeView(APIView):
    # authentication_classes = [JWTAuthentication]

    def get(self, request):
        cats = CategorySerializer(Category.objects.all(), many=True).data
        return Response(build_category_tree(cats))


class CategoryNoChildView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        cats = CategorySerializer(Category.objects.all(), many=True).data
        return Response(category_no_child(build_category_tree(cats)))


class LineTreeView(APIView):
    # authentication_classes = [JWTAuthentication]

    def get(self, request):
        lines = LineSerializer(Line.objects.all(), many=True).data
        return Response(build_line_tree(lines))


class LineNoChildView(APIView):
    # authentication_classes = [JWTAuthentication]

    def get(self, request):
        lines = LineSerializer(Line.objects.all(), many=True).data
        return Response(line_no_child(lines))


class ProductUpdateView(APIView):
    # authentication_classes = [JWTAuthentication]

    def delete(self, request, product_id):
        product = Product.objects.get(id=product_id)
        product.delete()
        return Response("Товар успешно удален")

    def post(self, request, product_id):
        product = Product.objects.get(id=product_id)
        data = json.loads(request.body)
        if 'categories' in data:
            categories = data.get('categories', [])
            product.categories.clear()
            product.categories.add(*categories)

        if 'lines' in data:
            lines = data.get('lines', [])
            product.lines.clear()
            product.lines.add(*lines)

        if 'colors' in data:
            colors = data.get('colors', [])
            product.lines.add(*colors)

        if 'brands' in data:
            brands = data.get('brands', [])
            product.brands.clear()
            product.brands.add(*brands)

        if 'tags' in data:
            tags = data.get('tags', [])
            product.tags.clear()
            product.tags.add(*tags)

        # Обработайте остальные поля по аналогии
        if 'model' in data:
            product.model = data.get('model', product.model)
        if 'colorway' in data:
            product.colorway = data.get('colorway', product.colorway)
        if 'russian_name' in data:
            product.russian_name = data.get('russian_name', product.russian_name)
        if 'manufacturer_sku' in data:
            product.manufacturer_sku = data.get('manufacturer_sku', product.manufacturer_sku)
        if 'description' in data:
            product.description = data.get('description', product.description)
        if 'bucket_link' in data:
            product.bucket_link = data.get('bucket_link', product.bucket_link)
        if 'main_color' in data:
            product.main_color_id = data.get('main_color', product.main_color_id)
        product.slug = ""
        product.save()

        return Response(ProductMainPageSerializer(product).data, status=status.HTTP_200_OK)

# class ProductMainPageView(rest_framework.generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # pagination_class = PageNumberPagination
#     # permission_classes = [AllowAny,]
#     # filter_backends = [ProductFilter]
#
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context['user_id'] = self.request.user.id
#         return context


# возвращает список продуктов для главной странички всех товаров
# class ProductsView(APIView):
#
#     def get(self, request, page_number):
#         products = Product.objects.get_queryset().order_by('id')
#         page_number = self.request.query_params.get('page_number ', page_number)
#         page_size = self.request.query_params.get('page_size ', 5)
#         try:
#             products = Paginator(products, page_size).page(page_number)
#         except Exception as e:
#             print(e)
#             return Response("Ошибка")
#         list_products = []
#         if request.user.id:
#             for product in products:
#                 list_products.append(product_unit_product_main(product.id, request.user.id))
#         else:
#             for product in products:
#                 list_products.append(product_unit_product_main(product.id, 0))
#
#         ans = {"page number": page_number,
#                'items': list_products}
#         return Response(ans, status=status.HTTP_200_OK)
