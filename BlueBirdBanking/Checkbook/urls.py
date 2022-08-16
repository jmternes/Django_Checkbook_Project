from django.urls import path
from . import views

urlpatterns = [
    #this sets the url path to home page index.html
    path('', views.home, name='index'),
    #this sets the url path to create new account page
    path('create/', views.create_account, name='create'),
    #sets the url path to balanced sheet page
    path('<int:pk>/balance/', views.balance, name='balance'),
    #sets the url path to add new transaction page
    path('transaction/', views.transaction, name='transaction'),
]