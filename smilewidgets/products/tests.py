from django.test import TestCase, Client

from .models import ProductPrice, Product, GiftCard

c = Client()

class MyTest(TestCase):
    def makeSettings(self):
        product_big = Product.objects.create(
            name="Big Widget",
            code="big_widget"
        )
        GiftCard.objects.create(
            code="10OFF",
            amount=1000,
            date_start="2018-07-01",
            date_end=None
        )
        ProductPrice.objects.create(
            name="default",
            price=100000,
            product=product_big
        )

    def testForBigProduxt(self):
        response = c.get('/api/get-price', {
            'productCode': 'big_widget', 
            'date': '2018-07-01', 
            'giftCardCode': '10OFF'
        })
        self.assertEqual(response.status_code, 200)