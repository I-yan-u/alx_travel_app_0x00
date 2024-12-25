from django.db import models

# In listings/models.py, define Listing, Booking, and Review models based on the provided structure.
# Each model should have appropriate fields, relationships, and constraints.

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=3, decimal_places=2)
    garage = models.BooleanField(default=False)
    sqft = models.DecimalField(max_digits=5, decimal_places=2)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.listing.title} - {self.user.username}'


class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.listing.title} - {self.user.username}'