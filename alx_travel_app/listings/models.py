from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    booking_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user_name} for {self.listing.title} on {self.booking_date}"
    
class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user_name} for {self.listing.title}"
    
