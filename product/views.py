from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from .models import Product, User
from .models import Product, ProfileUser, VendorAndProduct
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from .forms import RegisterUser
from django.core.files.storage import FileSystemStorage
# import xlrd
import csv
from django.db.models import Max, Count
import os
# from django.contrib.auth.models import User

# Create your views here.




# @login_required
def index(request):
	if request.method == 'POST':
		# print (request.POST)
		user_id = request.POST.get('username')
		user_pass = request.POST.get('password')
		user = ProfileUser.objects.filter(username=user_id, password=user_pass).exists()
		user = authenticate(username=user_id, password=user_pass)
		# return render(request, 'product/main.html')

		if user is not None:
			if user.is_vendor:
				login(request, user)
				# print('vendor yeasssss')
				return HttpResponseRedirect(reverse('product:main_vendor'))
				# return render(request, 'product/main_vendor.html', {'user': user})	
			else:
				login(request, user)
				return HttpResponseRedirect(reverse('product:main'))
				# return render(request, 'product/main.html',{'user':user})

	# print("not")
	return render(request, 'product/index.jinja', {})

# @login_required
def main(request):
	if not request.user.is_authenticated:
		# print('not authenticated')
		return render(request, 'product/index.jinja')
	# print('authenticated')
	return render(request, 'product/main.jinja', {})	

def change_price(request, row_id):
	if request.method == 'POST':
		print(request.POST)
		# name = VendorAndProduct.objects.get()
		# amount = request.POST.get('str(row_id)')
		# amount = amount
		print(row_id,'yoyoyoyoyoyo')
		update_price = VendorAndProduct.objects.get(pk=row_id)
		amount = request.POST.get(update_price.product_name)
		print(update_price.product_price,'heheheheh')
		print(type(amount),'lolololol')
		print(amount)
		update_price.product_price = amount
		update_price.save()

		return HttpResponseRedirect(reverse('product:main_vendor')) 

def main_vendor(request):

	ctx = {}
	if request.user.is_authenticated:
		username = request.user.username
		userid = request.user.id
		# print(username)

		ctx1 = {
			'username': username
		}

		if request.method == 'POST':
			# print('123')
			userid = request.user.id
			print (userid, "I AM HERE")
			myfile = request.FILES['myfile']
			# print(myfile)
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			path = '/home/anant/Desktop/new_project/project/media/'+filename
			
			os.system('mv /home/anant/Desktop/new_project/project/media/'+filename+' /home/anant/Desktop/new_project/project/media/vendor.csv')
			path = '/home/anant/Desktop/new_project/project/media/'+'vendor.csv'
			a=open(path)
			data = csv.reader(a)
			
			
			data=list(data)
			#working till here

			list_products = VendorAndProduct.objects.filter(profileuser_id=userid)

			list_of_products = []

			for objs in list_products:
				list_of_products.append(objs.product_name) 	
				list_of_products.append(objs.profileuser)


			#working from here
			for row in data[1:]:
				if row[0] in list_of_products:
					if userid == (list_of_products.index(row[0]))+1:
						print('helloooo')
						reccurring_product = VendorAndProduct.objects.get(product_name=row[0], profileuser_id=userid)
						reccurring_product.product_colour=row[1] 
						reccurring_product.product_screen_size=row[2]
						reccurring_product.product_os=row[3]
						reccurring_product.product_ram=row[4]
						reccurring_product.product_memory=row[5]
						reccurring_product.product_price=row[6]
						# print(row[6])
						# print(reccurring_product.product_price)
						reccurring_product.save()

				else:
					vendorandproduct = VendorAndProduct.objects.create(
						product_name=row[0], product_colour=row[1], product_screen_size=row[2],
						 product_os=row[3], product_ram=row[4], product_memory=row[5],
						  product_price=row[6], profileuser_id=userid
					)
			
			
			os.system('rm /home/anant/Desktop/new_project/project/media/vendor.csv')
			
			return render(request, 'product/main_vendor.jinja', ctx1)

		list_products = VendorAndProduct.objects.filter(profileuser_id=userid)

		# print(list_products)

		ctx = {
		'username': username,
		'list_products': list_products 
		}

		return render(request, 'product/main_vendor.jinja', ctx)	
	return render(request, 'product/index.jinja', ctx)



def register(request):
	form = RegisterUser(request.POST)
	if request.method == 'POST':
		# print("1")
		
		if form.is_valid():
			# print('123')
			data = form.save()
			# u = ProfileUser.objects.get(user=request.user)
			# print (request.POST.get('password'), "1")
			data.set_password(request.POST.get('password'))
			data.save()
		
			return HttpResponseRedirect(reverse('product:main'))
		return render(request, 'product/register.jinja', {'form':form})
	return render(request, 'product/register.jinja', {'form':form})	



def view_product(request):
	
	
	o = []
	a = VendorAndProduct.objects.all().order_by('-product_price')
	for i in a:
		if i.product_name not in o:
			o.append(i.product_name)
			o.append(i.pk)
	
	vendor_and_products=[]
	for j in o[1::2]:
		vendor_and_products.append(VendorAndProduct.objects.get(id=j))	
	# print(vendor_and_products[0].product_colour)
	return render(request, 'product/viewproduct.jinja',{'vendor_and_products':vendor_and_products})
	

	# a = VendorAndProduct.objects.values('product_name').annotate(c=Count('product_name')).filter(c__gt=1)



def add_prod(request):

	if request.method == 'POST':
		prod_name = request.POST.get('prod_name')
		prod_price = request.POST.get('prod_price')
		prod_quan = request.POST.get('prod_quan')
		#print(prod_name,prod_price, prod_quan, "1")

		product,_ = Product.objects.get_or_create(prod_name=prod_name, price=prod_price, quantity=prod_quan)

		return HttpResponseRedirect(reverse('product:viewproduct'))
		#return redirect('')
	return render(request, 'product/addproduct.jinja', {})

def del_prod(request, product_id):
	
		# prod_id = request.POST.get('hidden_prod_id')
		#print(type(prod_id))
	prod = Product.objects.get(id=product_id)
	prod.delete()
	return HttpResponseRedirect(reverse('product:viewproduct'))
		
			


def updateproduct(request, product_id):

	product = Product.objects.get(id=product_id)

	if request.method == 'POST':
		# prod_id = request.POST.get('prod_id')
		prod_name = request.POST.get('prod_name')
		prod_price = request.POST.get('prod_price')
		prod_quan = request.POST.get('prod_quan')

		# product,_ = Product.objects.get_or_create(prod_name=prod_name, price=prod_price, quantity=prod_quan)
		prod = Product.objects.get(id=product_id)

		prod.prod_name = prod_name
		prod.price = float(prod_price)
		prod.quantity = prod_quan
		prod.save()

		return HttpResponseRedirect(reverse('product:viewproduct'))
	return render(request, 'product/updateproduct.jinja',{'product':product})	
'''
def login(request):
	#if request.method=='POST':



	return render(request, 'product:views',{})	
'''	

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('product:views'))