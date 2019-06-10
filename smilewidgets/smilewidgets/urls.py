from django.conf.urls import include, url


urlpatterns = [
    url('api/', include('products.urls'))
]
