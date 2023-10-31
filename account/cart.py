from django.conf import settings

from core.models import Produk

class Cart(object):
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart

    #looping
    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Produk.objects.get(pk=p)

        for item in self.cart.values():
            item['total_price'] = int(item['product'].harga * item['quantity']) / 100

            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        self.session[settings.CART_sESSION_ID] = self.cart
        self.session.modifed = True

    def add(self,produk_id,quantity=1,update_produk=False):
        produk_id = str(produk_id)

        if produk_id not in self.cart:
            self.cart[produk_id] = {'quantity':int(quantity),'id':produk_id}
        elif update_produk:
            self.cart[produk_id]['quantity'] += int(quantity)

            if self.cart[produk_id]['quantity'] == 0:
                self.remove(produk_id)

        self.save()

    def remove(self,produk_id):
        if produk_id in self.cart:
            del self.cart[produk_id]
            self.save()
    
    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Produk.objects.get(pk=p)

        return int(sum(item['product'].price * item['quantity'] for item in self.cart.values()))/100
        