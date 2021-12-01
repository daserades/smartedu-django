from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=50, null=True)
  slug = models.SlugField(max_length=50, unique=True, null=True)

  class Meta:
    verbose_name_plural = "Categories"
    verbose_name = "Category"

  def __str__(self):
    return self.name

class Course(models.Model):
  name = models.CharField(max_length=200, unique=True)
  category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
  description = models.TextField(max_length=500, blank=True, null=True)
  image = models.ImageField(upload_to="courses/%Y/%m/%d/", default="courses/default_image.jpg")
  date = models.DateTimeField(auto_now=True)
  available = models.BooleanField(default=True)

  def __str__(self):
    return self.name


