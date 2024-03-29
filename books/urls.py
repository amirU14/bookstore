from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('create/', views.BookCreateView.as_view(), name='book_create')
]

