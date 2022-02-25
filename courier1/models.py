from django.db import models
import uuid
from django.core.validators import RegexValidator

# Create your models here.
class Package_Sizes(models.Model):
    size = models.CharField(max_length=50)
    bill_amount = models.IntegerField()

    def __str__(self):
        return self.size


class Package_Category(models.Model):
    category = models.CharField(max_length=25)

    def __str__(self):
        return self.category

class Customer_quote(models.Model):
    quote_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Source_pincode = models.IntegerField(max_length=25)
    Destination_pincode = models.IntegerField(max_length=25)
    Package_size = models.CharField(max_length=25)
    Category = models.CharField(max_length=25)
    Package_value = models.IntegerField(max_length=25)
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status

class Pickup_Address(models.Model):
    name = models.CharField(max_length=25)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,12}$', message="Phone number must be entered in the format: "
                                                                    "'+999999999'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    Address = models.CharField(max_length=200)
    pincode = models.IntegerField(max_length=6)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Delivery_Address(models.Model):
    name = models.CharField(max_length=25)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,12}$', message="Phone number must be entered in the format:"
                                                                    " '+999999999'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    Address = models.CharField(max_length=200)
    pincode = models.IntegerField(max_length=6)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Pickup_Date(models.Model):
    pick_up_date = models.DateField()

    def __str__(self):
        return self.pick_up_date
