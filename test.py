import json
from os.path import join

from config.settings import BASE_DIR


def product_id( num):
    with open(join(BASE_DIR, "dumpy", "products.json")) as f:
        data = json.load(f).get('products')
        print(data)
    # for product in data:
    #     if product.get('id') == num:
    #         return product
    # return 'not found'
    # return JsonResponse({'message':"Bunday product yo'q"})

product_id(4)