from django.urls import path

from apps.views import user_list, jobs_list

# from apps.views import carts, product_id, username, search_view, minmax, path_query, hello_django, temp_context

urlpatterns = [
       # path('carts/', carts),
       # path('product/<int:num>', product_id),
       # path('user/<str:username>', username),
       # path('search/', search_view),
       # path('number/', minmax),
       # path('book/<int:id>/details/', path_query),
       # path('hellodjango', hello_django),
       # path('contaxt/<str:text>/', temp_context),
       path('user/list', user_list),
       path('jobs/list', jobs_list)
]
