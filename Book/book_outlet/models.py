from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    country_name=models.CharField(max_length=200)
    country_code=models.CharField(max_length=200)

    class Meta:
        db_table = 'author_country'
        managed = True
        verbose_name = 'author_country'
        verbose_name_plural = 'Country of the Authors'

    def __str__(self) -> str:
        return f"{self.country_name}"

class Address(models.Model):
    street=models.CharField(max_length=80)
    postal_code=models.CharField(max_length=50)
    city=models.CharField(max_length=60)

    def __str__(self) -> str:
        return f"{self.street} {self.postal_code} {self.city}"


class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    # One to One relationship
    author=models.OneToOneField(Address,on_delete=models.CASCADE,null=True)
    
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullname()
    

class Booklist(models.Model):
    title=models.CharField(max_length=20)
    rating=models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )
    # Many to One relationship
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    is_bestSelling=models.BooleanField(default=False)
    slug=models.SlugField(default="",blank=True, db_index=True)
    
    # Many to Many relationship
    published_country=models.ManyToManyField(Country)

   
    def get_absolute_url(self):
        return reverse("details", args=[self.slug])
    
    def get_published_countries(self):
        return ",".join([country.country_name for country in self.published_country.all()])
    
    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"

