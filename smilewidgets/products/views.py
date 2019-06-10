from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from datetime import date, datetime
from products.serializers import ProductPriceSerializer
from products.models import Product, GiftCard, ProductPrice

class GetPriceViewSet(APIView):
    def get(self, request):
        query_date = request.query_params.get("date")
        gift_card_code = request.query_params.get("giftCardCode", None)
        if 'productCode' not in request.query_params:
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        else:
            product_code = request.query_params.get("productCode")
            product_id = 1 if product_code == "big_widget" else 2
        try:
            date_checker = datetime.strptime(query_date, '%Y-%m-%d')
        except:
            content = {'Invalid Date Format': 'Must Be: YYYY-MM-DD'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductPriceSerializer(data = request.query_params)
        serializer.is_valid(raise_exception=True)
        rezult_price = Product.objects.filter(code = product_code).values('price')[0]['price']
        if GiftCard.objects.all().filter(code = gift_card_code).count() != 0:
            discont = GiftCard.objects.filter(code = gift_card_code).values('amount')[0]['amount']
            rezult_price -= discont
        benefits = ProductPrice.objects.all().values('name')
        for benefit in benefits:
            time_range = ProductPrice.objects.filter(name = benefit['name']).filter(product = product_id).values('date_start','date_end','price')[0]
            if time_range['date_end'] == None:
                if date_checker.date() >= time_range['date_start']:
                    rezult_price = time_range['price']
            else:
                if date_checker.date() >= time_range['date_start'] and date_checker.date() <= time_range['date_end']:
                    rezult_price = time_range['price']    
        return Response({'product': product_code, 'price': rezult_price}, status=200)