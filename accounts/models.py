from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12, null=True)
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField()
    details = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.name + " - " + str(self.price) + " SAR."


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Done', "Done"),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    package = models.ForeignKey(Package, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=10, choices=STATUS)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): return str(self.customer) + " | " + self.status + " | " + str(self.created_date)
