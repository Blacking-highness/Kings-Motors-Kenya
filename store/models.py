from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

TRANSMISSIONS = (
	('select', 'SELECT'),
    ('Manual','MANUAL'),
    ('Automatic', 'AUTOMATIC'),
)

FUEL_TYPES = (
	('select', 'SELECT'),
    ('diesel','DIESEL'),
    ('petrol', 'PETROL'),
)

ENGINE_UNITS = (
	('select', 'SELECT'),
    ('liter','LITER'),
    ('cc', 'CC'),
)




class Product(models.Model):
	name = models.CharField(max_length=200)
	model = models.CharField(max_length = 200)
	engine_capacity = models.FloatField(default=False, blank=True, null=True)
	engine_capacity_unit = models.CharField(max_length=10, choices=ENGINE_UNITS, default='select', blank=True, null=True)
	fuel_type = models.CharField(max_length=20, choices=FUEL_TYPES, default='select')
	transmission = models.CharField(max_length=20, choices=TRANSMISSIONS, default='select')
	price = models.FloatField()
	digital = models.BooleanField(default=False,null=True, blank=True)
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

	


	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
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
		total = self.product.price * self.quantity
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


