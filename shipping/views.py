from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import ProductUnit
from .serializers import ProductUnitSerializer, DeliveryTypeSerializer
from wishlist.models import Wishlist
from products.models import Product, SizeTranslationRows
from products.serializers import ProductMainPageSerializer, ProductSerializer, SizeTranslationRowsSerializer
import json

class DeliveryForSizeView(APIView):
    def get(self, request, product_id, size_id):
        try:
            product = Product.objects.get(id=product_id)
            product_units = product.product_units.filter(size_id=size_id)
            s = []
            for product_unit in product_units:
                d = dict()
                d['id'] = product_unit.id
                d['final_price'] = product_unit.final_price
                d['start_price'] = product_unit.start_price
                d['available'] = product_unit.availability
                d['is_fast_shipping'] = product_unit.is_fast_shipping
                d['is_sale'] = product_unit.is_sale
                d['is_return'] = product_unit.is_return
                d['delivery'] = DeliveryTypeSerializer(product_unit.delivery_type).data
                s.append(d)
            return Response(s)


        except Product.DoesNotExist:
            return Response("Товар не найден", status=status.HTTP_404_NOT_FOUND)
        except SizeTranslationRows.DoesNotExist:
            return Response("Размер не найден", status=status.HTTP_404_NOT_FOUND)


class MinPriceForSizeView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            product_units = product.product_units.all()

            prices_by_size = {}

            # Проход по каждому элементу списка
            for item in product_units:
                size_id = item.size_id
                price = item.final_price
                available = item.availability

                # Проверка наличия размера в словаре
                if size_id not in prices_by_size:
                    prices_by_size[size_id] = {"price": [], "available": False, "is_fast_shipping": False, "is_sale": False, "is_return": False}

                prices_by_size[size_id]['price'].append(price)
                if available:
                    prices_by_size[size_id]["available"] = True
                if item.is_fast_shipping:
                    prices_by_size[size_id]["is_fast_shipping"] = True
                if item.is_sale:
                    prices_by_size[size_id]["is_sale"] = True
                if item.is_return:
                    prices_by_size[size_id]["is_return"] = True
            min_prices_by_size = {}
            s = []

            # Вычисление минимальной цены для каждого размера
            for size_id, prices in prices_by_size.items():

                min_price = min(prices['price'])
                d = dict()
                if len(prices) > 0:
                    d['min_price'] = min_price
                    d['available'] = prices['available']
                    d['is_fast_shipping'] = prices['is_fast_shipping']
                    d['is_sale'] = prices['is_sale']
                    d['is_return'] = prices['is_return']
                    d['size'] = SizeTranslationRowsSerializer(SizeTranslationRows.objects.get(id=size_id)).data
                    d['view_size'] = SizeTranslationRows.objects.get(id=size_id).EU
                min_prices_by_size[size_id] = d
                s.append(d)
            return Response(s)
        except Product.DoesNotExist:
            return Response("Товар не найден", status=status.HTTP_404_NOT_FOUND)

class ProductUnitProductView(APIView):
    # authentication_classes = [JWTAuthentication]

    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            serializer = ProductUnitSerializer(product.product_units.order_by('size_id'), many=True)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response("Товар не найден", status=status.HTTP_404_NOT_FOUND)


class ProductUnitProductSlugView(APIView):
    # authentication_classes = [JWTAuthentication]

    def get(self, request, slug):
        try:
            product = Product.objects.get(slug=slug)
            serializer = ProductUnitSerializer(product.product_units.order_by('size_id'), many=True)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response("Товар не найден", status=status.HTTP_404_NOT_FOUND)


def product_unit_product_main(product_id, user_id):
    # authentication_classes = [JWTAuthentication]
    try:
        product = Product.objects.get(id=product_id)
        ans = ProductSerializer(product).data
        if user_id > 0:
            try:
                wishlist = Wishlist.objects.get(user_id=user_id)
                ans['in_wishlist'] = wishlist.products.filter(product_id=product_id)
            except Wishlist.DoesNotExist:
                ans['in_wishlist'] = False
        return ans
    except Product.DoesNotExist:
        return Response("Товар не найден", status=status.HTTP_404_NOT_FOUND)


class ProductUnitProductMainView(APIView):
    # authentication_classes = [JWTAuthentication]

    def get(self, request, product_id, user_id):
        try:
            if Product.objects.filter(id=product_id).exists():
                if request.user.id == user_id or request.user.is_staff:
                    return Response(product_unit_product_main(product_id, user_id))
                else:
                    return Response(product_unit_product_main(product_id, 0))
            else:
                return Response("Товар не найден", status=status.HTTP_404_NOT_FOUND)
        except Product.DoesNotExist:
            return Response("Товар не найден", status=status.HTTP_404_NOT_FOUND)



class ListProductUnitView(APIView):
    # authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            s_product_unit = json.loads(request.body)["product_unit_list"]
            product_units = ProductUnit.objects.filter(id__in=s_product_unit)
            serializer = ProductUnitSerializer(product_units, many=True)
            return Response(serializer.data)
        except json.JSONDecodeError:
            return Response("Invalid JSON data", status=status.HTTP_400_BAD_REQUEST)
        except ProductUnit.DoesNotExist:
            return Response("One or more product units do not exist", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

