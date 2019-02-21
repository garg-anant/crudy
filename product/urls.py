from django.urls import path, include
from . import views

app_name='product'

urlpatterns=[
	path('', views.index, name='views'),
	path('logout', views.logout_view, name='logout'),
	path('register', views.register, name='register'),
	path('main', views.main, name='main'),
	# path('main_vendor', views.main_vendor, name='main_vendor'),
	path('addproduct', views.add_prod, name='addproduct'),
	path('viewproduct', views.view_product, name='viewproduct'),
	# path('<int:product_id>/updateproduct/', views.up_prod, name='up_prod'),
	path('<int:product_id>/updateproduct/', views.updateproduct, name='updateproduct'),
	path('<int:product_id>/deleteproduct', views.del_prod, name='deleteproduct'),
	# path('<int:user_id>/cart', views.my_cart, name='cart'),
	path('main_vendor', views.main_vendor, name='main_vendor'),
	path('change_price/<int:row_id>/', views.change_price, name='change_price')
]
