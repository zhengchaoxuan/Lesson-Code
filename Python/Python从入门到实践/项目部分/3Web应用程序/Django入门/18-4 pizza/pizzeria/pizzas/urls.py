'''pizzas的url模式'''
from django.urls import path,include
from . import views

app_name = 'pizzas'
urlpatterns =[
    path('',views.index,name = 'pizzas')
]

