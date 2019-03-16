from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from ckeditor import static

class Category(models.Model):
	category = models.CharField(max_length=50, null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return f"{self.category}"

class Dealer(models.Model):
	company_name = models.CharField(max_length=100, null=True, blank=True)
	head_name = models.CharField(max_length=50, null=True, blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	exp = models.IntegerField(blank=True, null=True)
	stars = models.IntegerField(default=0, blank=True, null=True)
	suggestions = models.TextField(blank=True, null=True)
	logo = models.ImageField(blank=True, null=True)

	def __str__(self):
		return f"{self.company_name}"

class Help(models.Model):
	dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
	discount = RichTextField(max_length=100000, blank=True, null=True)
	offers = RichTextField(max_length=100000, blank=True, null=True)

	def __str__(self):
		return f"{self.dealer.company_name}"

class Customer(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	email = models.CharField(max_length=100, blank=True, null=True, unique=True)
	password = models.CharField(max_length=15, blank=True, null=True)
	phone = models.CharField(max_length=12, blank=True, null=True, unique=True)
	address = RichTextField(max_length=1000, blank=True, null=True)
	state = models.CharField(max_length=100, blank=True, null=True)
	city = models.CharField(max_length=100, blank=True, null=True)
	membership = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.name}"

class Book(models.Model):
	start_date = models.DateField()
	end_date = models.DateField()
	marriage_date = models.DateField()
	dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.dealer}"
