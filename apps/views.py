from django.contrib.auth.models import User
from django.shortcuts import render
from os.path import join
import json

from django.http import JsonResponse, HttpResponse

from apps.models import Jobs
from config.settings import BASE_DIR


# def carts(request):
#     with open(join(BASE_DIR, "dumpy", "carts.json")) as f:
#         data = json.load(f)
#     return JsonResponse(data)
#
#
# # task 1
# def product_id(request, num):
#     with open(join(BASE_DIR, "dumpy", "products.json")) as f:
#         data = json.load(f).get('products')
#     for product in data:
#         if product.get('id') == num:
#             return JsonResponse(product)
#     return JsonResponse({'message': "Bunday product yo'q"})
#
#
# # task 2
#
#
# def username(request, username):
#     with open(join(BASE_DIR, "dumpy", "users.json")) as f:
#         users = json.load(f).get('users')
#     for user in users:
#         if user.get('username') == username:
#             return JsonResponse(user)
#     return JsonResponse({"message": "Not found username"})
#
#
# # task 3
#
# def search_view(request):
#     data = request.GET.get("search", '')
#     return JsonResponse({'message': f"{data}"})
#
#
# def price_view(request):
#     data = request.GET.get("search", '')
#     return JsonResponse({'message': f"{data}"})
#
#
# def minmax(request):
#     min1 = request.GET.get('min_price')
#     max2 = request.GET.get('max_price')
#     return JsonResponse({'min_price': f'{min1}', "max_price": f"{max2}"})
#
#
# def path_query(request, id):
#     data = request.GET.get('author')
#     with open(join(BASE_DIR, 'dumpy', 'users.json')) as f:
#         users = json.load(f).get('users')
#     for user in users:
#         if user.get('id') == id:
#             user['author'] = data
#             return JsonResponse(user)
#     return JsonResponse({'message': "Not found author!"})
#
#
# def hello_django(request):
#     return render(request, "lesson_1/djangoHello.html")
#
# def temp_context(request, text):
#     return render(request, 'lesson_1/context.html', context={"message":text})

def user_list(request):
    users = User.objects.all()
    return render(request, 'users-list.html', context = {'users': users})

def jobs_list(request):
    jobs = Jobs.objects.all()
    return render(request, 'jobs-list.html', {"jobs":jobs})