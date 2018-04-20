from rest_framework import serializers
from api.models import Author, Category, Book, Cart

# ModelSerializer automatically generates a set of fields based on the model
class BookSerializer(serializers.ModelSerializer):


	class Meta:
		model = Book
		fields = '__all__'        # all fields in the model will be used

class AuthorSerializer(serializers.ModelSerializer):


	class Meta:
		model = Author
		fields = '__all__'		

class CategorySerializer(serializers.ModelSerializer):


	class Meta:
		model = Category
		fields = '__all__'


class CartSerializer(serializers.ModelSerializer):


	class Meta:
		model = Cart
		fields = '__all__'
