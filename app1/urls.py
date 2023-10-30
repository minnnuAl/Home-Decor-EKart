
from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('checkout/', views.checkout, name="Checkout"),
    path('profile',views.profile,name="profile"),
    # path('handlerequest/', views.handlerequest, name="HandleRequest"),
    # path('payment',views.payment),
    path('add', views.adminside, name="adminside"),
    

]