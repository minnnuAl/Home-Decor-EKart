from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=35)
    email=models.EmailField()
    description=models.TextField(max_length=250)
    phonenumber=models.IntegerField()

    def __str__(self):
        return self.name
    # for returning name of the customer who has submitted their contact information
 
 
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=150)
    category=models.CharField(max_length=150,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=250)
    image=models.ImageField(upload_to='images/images')
    
    def __str__(self):
        return self.product_name
    
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json =  models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)    
    oid=models.CharField(max_length=150,blank=True)
    # oid=order id
    amountpaid=models.CharField(max_length=500,blank=True,null=True)
    paymentstatus=models.CharField(max_length=20,blank=True)
    phone = models.CharField(max_length=100,default="")
    def __str__(self):
        return self.name

# class ProductBuy(models.Model):
#     Buy_id=models.IntegerField(primary_key=True)
#     Product_id=models.IntegerField()
#     ProductName=models.CharField(max_length=20)
#     Quantity=models.IntegerField()
#     Price=models.IntegerField()
#     Customer_id=models.IntegerField()
#     name = models.CharField(max_length=20, default="")
#     email = models.CharField(max_length=20, default="")
#     address = models.CharField(max_length=50)
#     phone_number = models.IntegerField()
#     Status = models.CharField(max_length=20,default="")
#     payment_type=models.CharField(max_length=20,default="")
#     Transportor_id=models.IntegerField(default=0)
#     Transport_name=models.CharField(max_length=20,default='Not Taken Yet')
#     Transportor_phone=models.IntegerField(default=0)
    

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    delivered=models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
    
    

# class Customer_login(models.Model):
#     Customer_id=models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=20, default="")
#     email = models.CharField(max_length=20, default="")
#     password = models.CharField(max_length=20, default="")
#     address = models.CharField(max_length=20)
#     district = models.CharField(max_length=20)
#     current_location = models.CharField(max_length=20)
#     phone_number = models.IntegerField()