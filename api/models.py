from django.db import models


class Author(models.Model):
  author_id = models.CharField(max_length=100, blank=True)
  name = models.CharField(max_length=200, blank=True)


  def __str__(self):
    return self.name

class Category(models.Model):
  category_id = models.CharField(max_length=100, blank=True)
  title = models.CharField(max_length=200, blank=True)


  def __str__(self):
    return self.title

class Book(models.Model):
  book_id = models.CharField(max_length=100, blank=True)
  image_path = models.CharField(max_length=1000, blank=True)
  title = models.CharField(max_length=400, blank=True)
  author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
  price = models.DecimalField(max_digits=19, decimal_places=10)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
  quantity = models.IntegerField()
  updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


  def __str__(self):
   return self.title

class Cart(models.Model):
  # for user
  order_id = models.CharField(max_length=100, blank=True)
  book_id = models.ForeignKey(Book)
  price = models.DecimalField(max_digits=19, decimal_places=10)
  quantity = models.IntegerField()
   
  