from django.urls import path
from . import views

app_name = 'shaadi'

urlpatterns = [
	path("", views.login, name="login"),
	path('create_customer/', views.create_customer, name="create_customer"),
	path('<int:customer_id>/home/', views.home, name="home"),
	path('<int:customer_id>/home/<int:category_id>/', views.dealer, name="dealer"),
	path('<int:customer_id>/home/<int:category_id>/<int:dealer_id>/', views.dealer_info, name="dealer_info"),
	path('<int:customer_id>/home/<int:category_id>/<int:dealer_id>/details', views.detail, name="detail"),
]
