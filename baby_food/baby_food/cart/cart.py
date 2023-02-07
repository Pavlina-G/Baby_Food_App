# from django.conf import settings
#
# from baby_food.menu_app.models import Menu
#
#
# # import product/the menus/
#
# class Cart(object):
#     def __init__(self, request):
#         self.session = request.session
#         cart = self.session.get(settings.CART_SESSION_ID)
#
#         if not cart:
#             cart = self.session[settings.CART_SESSION_ID]
#
#         self.cart = cart
#
#     # iterate through the items in the cart
#     def __iter__(self):
#         for m in self.cart.keys():
#             self.cart[str(m)]['menu'] = Menu.objects.get(pk=m)
#
#     def __len__(self):
#         return sum(item['quantity'] for item in self.cart.values())
#
#     def save(self):
#         self.session[settings.CART_SESSION_ID] = self.cart
#         self.session.modified = True
#
#     def add(self, product_id, quantity=1, update_quantity=False):
#         product_id = str(product_id)
#
#         if product_id not in self.cart:
#             self.cart[product_id] = {'quantity': 1, 'id': product_id}
#
#         if update_quantity:
#             self.cart[product_id]['quantity'] += int(quantity)
#
#             if self.cart[product_id]['quantity'] == 0:
#                 self.remove(product_id)
#
#         self.save()
#
#     def remove(self, product_id):
#         if product_id in self.cart:
#             del self.cart[product_id]
#             self.save()
#
#     def clear(self):
#         del self.session[settings.CART_SESSION_ID]
#         self.session.modified = True
#
#     def get_total_price(self):
#         # for m in self.cart.keys():
#         #     self.cart[str(m)]['menu'] = Menu.objects.get(pk=m)
#
#         return sum(item['menu'].price * item['quantity'] for item in self.cart.values())
#
