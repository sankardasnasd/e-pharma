from django.db import models

# Create your models here.
class Login(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=50)
    Type=models.CharField(max_length=50)

class Customer(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    Name=models.CharField(max_length=50)
    Phone=models.CharField(max_length=10)
    Email=models.CharField(max_length=50)
    House_Name=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    Post=models.CharField(max_length=100)
    District=models.CharField(max_length=100)
    Pin=models.CharField(max_length=10)
    Status=models.CharField(max_length=100,default='0')

class Stocks(models.Model):

    Product_Name=models.CharField(max_length=100)
    Product_image=models.CharField(max_length=200)
    Manufacturer_Name=models.CharField(max_length=100)
    Category=models.CharField(max_length=20)
    Product_Type = models.CharField(max_length=100)
    Quantity=models.CharField(max_length=100)
    Netvoldos=models.CharField(max_length=100)
    Price=models.CharField(max_length=100)

class Inventory(models.Model):
    PRODUCT=models.ForeignKey(Stocks,on_delete=models.CASCADE)
    Expiry_Date=models.CharField(max_length=100)
    Shelf_Code=models.CharField(max_length=20)
    Shelf_Rowno=models.CharField(max_length=20)
    Shelf_Colno=models.CharField(max_length=20)

class Prescription(models.Model):
    USER=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Date = models.DateField()
    File=models.FileField(max_length=300)
    Status=models.CharField(max_length=50)

class Available_Products(models.Model):
    PRESCRIPTION=models.ForeignKey(Prescription,on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(Stocks,on_delete=models.CASCADE)
    Status=models.CharField(max_length=50)
    Quantity=models.CharField(max_length=100)

class Order(models.Model):
    Date = models.DateField()
    CUSTOMER=models.ForeignKey(Customer,on_delete=models.CASCADE)
    PRESCRIPTION = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    Total_Amount=models.CharField(max_length=20)

    Status = models.CharField(max_length=50)
    Place = models.CharField(max_length=100)
    Landmark=models.CharField(max_length=100)
    Post = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    Pin = models.CharField(max_length=10)

class OrderSub(models.Model):
    ORDER=models.ForeignKey(Order,on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(Stocks,on_delete=models.CASCADE)
    Quantity = models.CharField(max_length=100)

class Payment(models.Model):
    ORDER=models.ForeignKey(Order,on_delete=models.CASCADE)
    CUSTOMER= models.ForeignKey(Customer,on_delete=models.CASCADE)
    Total_Amount = models.CharField(max_length=20)
    Date = models.DateField()
    Status = models.CharField(max_length=50)

class Complaint(models.Model):
    CUSTOMER=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Date = models.DateField()
    Complaint = models.CharField(max_length=200)
    Status=models.CharField(max_length=100)
    Reply = models.CharField(max_length=200)

class Feedback(models.Model):
    CUSTOMER=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Date = models.DateField()
    Feedback = models.CharField(max_length=200)

class Bank(models.Model):
    Account_Holder=models.CharField(max_length=100)
    Account_Number=models.CharField(max_length=100)
    Card_Number=models.CharField(max_length=100)
    CVV=models.CharField(max_length=100)
    Expiry_Date=models.DateField()
    Balance_Amount=models.CharField(max_length=100)


