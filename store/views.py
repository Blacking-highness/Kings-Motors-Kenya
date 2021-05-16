from django.db.models import query
from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder
from .filters import ProductFilter
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models import Q


def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()

	myFilter = ProductFilter(request.GET, queryset=products)
	products = myFilter.qs


	context = {'products':products, 'cartItems':cartItems, 'myFilter': myFilter}
	return render(request, 'store/store.html', context)


def details(request):
	products = Product.objects.all()

	myFilter = ProductFilter(request.GET, queryset=products)
	products = myFilter.qs

	context = {'products': products,
				'myFilter': myFilter}
	return render(request, 'store/details.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

def search(request):
	if request.method == "POST":
		searched = request.POST.get('searched')
		search_items = Product.objects.filter(Q(name__contains=searched)
											| Q(fuel_type=searched)
											| Q(model=searched) 
											| Q(transmission=searched)
											| Q(details=searched)
											| Q(price=searched))


		context = {'searched': searched,
					'search_items': search_items}
	else:
		context = {}

	return render(request, 'store/results.html', context)


def contact(request):
	context = {}
	return render(request, 'store/contact.html', context)

def faq(request):
	context = {}
	return render(request, 'store/faq.html', context)