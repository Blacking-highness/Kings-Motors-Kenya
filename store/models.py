from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from pprint import pprint
#from django.config import settings


# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

CAR_MODELS = (
	('select','SELECT'),
	('Toyota','TOYOTA'),
	('B.M.W','B.M.W'),
	('Subaru','SUBARU'),
	('Mercedes','MERCEDES'),
	('Isuzu','ISUZU'),
	('Nissan','NISSAN'),
	('Mazda','MAZDA'),
)
TRANSMISSIONS = (
	('select', 'SELECT'),
    ('Manual','MANUAL'),
    ('Automatic', 'AUTOMATIC'),
    ('Electric', 'ELECTRIC')
)

FUEL_TYPES = (
	('select', 'SELECT'),
    ('diesel','DIESEL'),
    ('petrol', 'PETROL')
)

ENGINE_UNITS = (
	('select', 'SELECT'),
    ('liter','LITER'),
    ('cc', 'CC')
)




class Product(models.Model):
	car_type = models.CharField(max_length=10, choices=CAR_MODELS, default='select', blank=True, null=True)
	name = models.CharField(max_length=200)
	model = models.CharField(max_length = 200)
	engine_capacity = models.FloatField(default=False, blank=True, null=True)
	engine_capacity_unit = models.CharField(max_length=10, choices=ENGINE_UNITS, default='select', blank=True, null=True)
	fuel_type = models.CharField(max_length=20, choices=FUEL_TYPES, default='select')
	transmission = models.CharField(max_length=20, choices=TRANSMISSIONS, default='select')
	price = models.FloatField()
	image = models.ImageField(null=True, blank=True)
	details = models.TextField(default=True, max_length=2000)
	
	
	
	image1  = models.ImageField(null=True, blank=True)
	image2  = models.ImageField(null=True, blank=True)
	image3  = models.ImageField(null=True, blank=True)
	image4  = models.ImageField(null=True, blank=True)
	image5  = models.ImageField(null=True, blank=True)
	image6  = models.ImageField(null=True, blank=True)
	image7  = models.ImageField(null=True, blank=True)
	image8  = models.ImageField(null=True, blank=True)
	image9  = models.ImageField(null=True, blank=True)
	image10 = models.ImageField(null=True, blank=True)
	image11 = models.ImageField(null=True, blank=True)
	image12 = models.ImageField(null=True, blank=True)
	image13 = models.ImageField(null=True, blank=True)
	image14 = models.ImageField(null=True, blank=True)
	image15 = models.ImageField(null=True, blank=True)
	image16 = models.ImageField(null=True, blank=True)
	image17 = models.ImageField(null=True, blank=True)
	image18 = models.ImageField(null=True, blank=True)
	image19 = models.ImageField(null=True, blank=True)
	image20 = models.ImageField(null=True, blank=True)
	

	


	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

	@property
	def image1URL(self):
		try:
			url = self.image1.url
		except:
			url = ''
		return url

	@property
	def image2URL(self):
		try:
			url = self.image2.url
		except:
			url = ''
		return url

	@property
	def image3URL(self):
		try:
			url = self.image3.url
		except:
			url = ''
		return url

	@property
	def image4URL(self):
		try:
			url = self.image4.url
		except:
			url = ''
		return url

	@property
	def image5URL(self):
		try:
			url = self.image5.url
		except:
			url = ''
		return url

	@property
	def image6URL(self):
		try:
			url = self.image6.url
		except:
			url = ''
		return url

	@property
	def image7URL(self):
		try:
			url = self.image7.url
		except:
			url = ''
		return url

	@property
	def image8URL(self):
		try:
			url = self.image8.url
		except:
			url = ''
		return url

	@property
	def image9URL(self):
		try:
			url = self.image9.url
		except:
			url = ''
		return url

	@property
	def image10URL(self):
		try:
			url = self.image10.url
		except:
			url = ''
		return url

	@property
	def image11URL(self):
		try:
			url = self.image11.url
		except:
			url = ''
		return url

	@property
	def image12URL(self):
		try:
			url = self.image12.url
		except:
			url = ''
		return url

	@property
	def image13URL(self):
		try:
			url = self.image13.url
		except:
			url = ''
		return url

	@property
	def image14URL(self):
		try:
			url = self.image14.url
		except:
			url = ''
		return url

	@property
	def image15URL(self):
		try:
			url = self.image15.url
		except:
			url = ''
		return url

	@property
	def image16URL(self):
		try:
			url = self.image16.url
		except:
			url = ''
		return url

	@property
	def image17URL(self):
		try:
			url = self.image17.url
		except:
			url = ''
		return url

	@property
	def image18URL(self):
		try:
			url = self.image18.url
		except:
			url = ''
		return url

	@property
	def image19URL(self):
		try:
			url = self.image19.url
		except:
			url = ''
		return url

	@property
	def image20URL(self):
		try:
			url = self.image20.url
		except:
			url = ''
		return url


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		#total = self.product.price * self.quantity
		total = 2
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address


@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, created, instance, **kwargs):
	if created:
		obj = sender.objects.last()

		Customer.objects.create(user=obj, name=obj.username, email=obj.email)

