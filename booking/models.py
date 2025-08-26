from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TravelOption(models.Model):
    TRAVEL_TYPES = (
        ('Flight','Flight'),
        ('Bus','Bus'),
        ('Train','Train'),
    )

    type = models.CharField(max_length=10,choices=TRAVEL_TYPES)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available_seats = models.PositiveIntegerField()

    def __str__ (self):
        return f"{self.type} from {self.source} to {self.destination}"

class Booking(models.Model):
    STATUS_CHOICES = (
        ('Confirmed','Confirmed'),
        ('Cancelled','Cancelled'),
    ) 

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption,on_delete=models.CASCADE)
    num_of_seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10,decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='Confirmed')

    def __str__ (self):
        return f"Booking {self.id} by {self.user.username}"


