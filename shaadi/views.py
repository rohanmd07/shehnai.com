from django.shortcuts import render
from .models import Category, Dealer, Help, Customer, Book
from .forms import loginForm, create_customerForm, detailForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import redirect

def home(request, customer_id):
	category = Category.objects.all()
	customer = Customer.objects.get(pk=customer_id)
	context = {
		'category':category,
		'customer':customer,
	}
	return render(request, "shaadi/home.html", context)

def dealer(request, customer_id, category_id):
	category = Category.objects.get(pk=category_id)
	dealer = Dealer.objects.filter(category=category_id)
	customer = Customer.objects.get(pk=customer_id)
	context = {
		'dealer':dealer,
		'customer':customer,
		'category':category,
	}
	return render(request, "shaadi/dealer.html", context)

def dealer_info(request, customer_id, category_id, dealer_id):
	category = Category.objects.get(pk=category_id)
	dealer = Dealer.objects.get(pk=dealer_id)
	customer = Customer.objects.get(pk=customer_id)
	context = {
		'dealer':dealer,
		'customer':customer,
		'category':category,
	}
	return render(request, "shaadi/dealer_info.html", context)

def login(request):
	customer = Customer.objects.all()
	if request.method == 'POST':
		form = loginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			for customer in customer:
				if email == customer.email and password == customer.password:
					context = {
						'detail' : Book.objects.get(customer=customer),
						'customer' : customer,
					}
					return render(request, "shaadi/registered_detail.html", context)
			else:
				return HttpResponseRedirect("")
	else:
		form = loginForm()
	context = {
		'form' : form,
	}
	return render(request, 'shaadi/login.html', context)

def create_customer(request):
	if request.method == 'POST':
		form = create_customerForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			phone = form.cleaned_data['phone']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			address = form.cleaned_data['address']
			state = form.cleaned_data['state']
			city = form.cleaned_data['city']
			customer = Customer.objects.create(name=name, phone=phone, email=email, password=password, address=address, state=state, city=city)
			customer.save()
			customer_id = customer.id
			response = reverse('shaadi:home', kwargs={'customer_id':customer_id})
			return redirect(response)

	else:
		form = create_customerForm()
	context = {
		'form' : form,
	}
	return render(request, 'shaadi/create_customer.html', context)

def detail(request, customer_id, category_id, dealer_id):
	customer = Customer.objects.get(pk=customer_id)
	category = Category.objects.get(pk=category_id)
	dealer = Dealer.objects.get(pk=dealer_id)
	if request.method == 'POST':
		form = detailForm(request.POST)
		if form.is_valid():
			start_date = form.cleaned_data['start_date']
			end_date = form.cleaned_data['end_date']
			marriage_date = form.cleaned_data['marriage_date']
			book = Book.objects.create(start_date=start_date, end_date=end_date, marriage_date=marriage_date, dealer=dealer, customer=customer)
			book.save()
			return HttpResponse("You have succesfully registered")
	else:
		form = detailForm()
	context = {
		'form':form,
		'customer':customer,
		'dealer':dealer,
		'category':category,
	}
	return render(request, 'shaadi/detail.html', context)
