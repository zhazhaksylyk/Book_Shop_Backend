from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('category_books', views.category_books, name="category_books"),
    
    #path('authors/', views.authors_list, name="author_list"),
    #path('authors/<int:author_id>', views.authors_details, name="author_details"),
    
]