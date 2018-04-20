from django.contrib import admin
from api.models import Book, Author, Category, Cart

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Cart)