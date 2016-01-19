from django.db import models
from django.utils.encoding import python_2_unicode_compatible



class Products(models.model):
	Product_name = models.CharField(max_length=30)
	Short_Description = models.TextField(max_length=50)
	Long_Description = models.TextField(max_length=500)
	Min_amount_product = models.IntegerField(default=0)
	Cost_Price = models.IntegerField(default=0)
	Sale_price = models.IntegerField(default=0)

class Sales(models.model):
	Product_name = models.ForeignKey(Products)
	Date_of_sale = models.DateTimeField()
	Number_of_Documents = models.IntegerField(default=0)

	



