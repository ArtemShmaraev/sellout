from rest_framework import routers
from .api import ShoppingCartViewSet
from django.urls import path
from .views import UseBonus, ShoppingCartUser, SignAPIView, RedirectPaymentView, CheckOutView, AllOrdersView, UserOrdersView, DeliveryInfo, OrderView, ListProductUnitOrderView, ChangeStatusUnit, FactOfPaymentView

router = routers.DefaultRouter()
# router.register("", ShoppingCartViewSet, 'cart')

urlpatterns = router.urls
urlpatterns.append(path('cart/<int:user_id>/<int:product_unit_id>', ShoppingCartUser.as_view()))
urlpatterns.append(path('cart/<int:user_id>/<int:product_unit_id>/<int:new_product_unit_id>', ShoppingCartUser.as_view()))
urlpatterns.append(path('cart/<int:user_id>', ShoppingCartUser.as_view()))
urlpatterns.append(path('cart_list/<int:user_id>', ListProductUnitOrderView.as_view()))

urlpatterns.append(path('checkout/<int:user_id>', CheckOutView.as_view()))
urlpatterns.append(path('orders', AllOrdersView.as_view()))
urlpatterns.append(path('user_orders/<int:user_id>', UserOrdersView.as_view()))
urlpatterns.append(path('info/<int:order_id>', OrderView.as_view()))

urlpatterns.append(path('cart/use_bonus', UseBonus.as_view()))
urlpatterns.append(path('status_unit/<order_unit_id>', ChangeStatusUnit.as_view()))
urlpatterns.append(path('delivery_info', DeliveryInfo.as_view()))
urlpatterns.append(path('payment', RedirectPaymentView.as_view()))
urlpatterns.append(path('signature', SignAPIView.as_view(), name='signature-api'))
urlpatterns.append(path('fact_of_payment', FactOfPaymentView.as_view(), name='signature-api'))