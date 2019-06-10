from django.conf.urls import url
from products.views import GetPriceViewSet

urlpatterns = [
    url('get-price', GetPriceViewSet.as_view(), name='get_price'),
]