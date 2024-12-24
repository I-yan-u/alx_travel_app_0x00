
# Create serializers in listings/serializers.py for Listing and Booking models.
# Use the ListingSerializer to serialize the Listing model.
# Use the BookingSerializer to serialize the Booking model.
# The ListingSerializer should include all fields from the Listing model.
# The BookingSerializer should include all fields from the Booking model.
# The BookingSerializer should include the user's username and email.
# The BookingSerializer should include the listing's title.

from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    listing = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = '__all__'

    def get_user(self, obj):
        return obj.user.username

    def get_listing(self, obj):
        return obj.listing.title
    

