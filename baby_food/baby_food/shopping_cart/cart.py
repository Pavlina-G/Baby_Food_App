from django.conf import settings
from django.http import request

from baby_food.accounts.models import Child
from baby_food.menu_app.models import Menu
from baby_food.order.models import OrderItem


# import product/the menus/

class Cart(object):
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    # iterate through the items in the shopping_cart
    def __iter__(self):
        for m in self.cart.keys():
            self.cart[str(m)]['menu'] = Menu.objects.get(pk=m)

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, menu, quantity=1, update_quantity=False):
        menu_id = str(menu.id)
        user_id = self.request.user.id
        children = Child.objects.filter(parent_id=user_id)
        kids = {}

        for child in children:
            kids[f'{child.id}'] = f'{child.first_name} {child.last_name}'

        if menu_id not in self.cart:
            self.cart[menu_id] = {

                'quantity': 1,
                'kids': kids,
                'menu_id': menu_id,
                'price': menu.price,
                'name': menu.name,
                'date': menu.date.strftime("%d.%m.%Y"),
                'age': str(menu.age),
            }

        # if update_quantity:
        else:
            self.cart[menu_id]['quantity'] += int(quantity)
            # self.cart[menu_id]['price'] = self.cart[menu_id]['quantity'] * (menu.price)

            if self.cart[menu_id]['quantity'] == 0:
                self.remove(menu)

        self.save()

    def remove(self, menu):
        menu_id = str(menu.id)
        if menu_id in self.cart:
            del self.cart[menu_id]
            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())
