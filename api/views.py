from django.shortcuts import render
from api.models import Author, Book, Category
from api.serializers import BookSerializer, AuthorSerializer, CategorySerializer, CartSerializer
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def book_list(request):
  if request.method == "GET":
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)
  

