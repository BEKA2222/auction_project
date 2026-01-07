from rest_framework import serializers
from .models import *



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role', 'phone_number']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'brand_name']

class CarModelSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(read_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(), source='brand', write_only=True)

    class Meta:
        model = CarModel
        fields = ['id', 'car_model', 'brand', 'brand_id']

class CarSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(read_only=True)
    car_model = serializers.PrimaryKeyRelatedField(read_only=True)
    seller = serializers.PrimaryKeyRelatedField(read_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(), source='brand', write_only=True)
    car_model_id = serializers.PrimaryKeyRelatedField(queryset=CarModel.objects.all(), source='car_model', write_only=True)
    seller_id = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), source='seller', write_only=True)

    class Meta:
        model = Car
        fields = ['id', 'brand', 'car_model', 'year', 'fuel_type', 'transmission', 'mileage', 'price',
                  'description', 'image', 'seller', 'brand_id', 'car_model_id', 'seller_id']

class AuctionSerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(read_only=True)
    car_id = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), source='car', write_only=True)

    class Meta:
        model = Auction
        fields = ['id', 'car', 'start_price', 'min_price', 'start_time', 'end_time', 'status', 'car_id']

class BidSerializer(serializers.ModelSerializer):
    auction = serializers.PrimaryKeyRelatedField(read_only=True)
    buyer = serializers.PrimaryKeyRelatedField(read_only=True)
    auction_id = serializers.PrimaryKeyRelatedField(queryset=Auction.objects.all(), source='auction', write_only=True)
    buyer_id = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), source='buyer', write_only=True)

    class Meta:
        model = Bid
        fields = ['id', 'auction', 'buyer', 'amount', 'created_at', 'auction_id', 'buyer_id']

class FeedbackSerializer(serializers.ModelSerializer):
    seller = serializers.PrimaryKeyRelatedField(read_only=True)
    buyer = serializers.PrimaryKeyRelatedField(read_only=True)
    seller_id = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), source='seller', write_only=True)
    buyer_id = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), source='buyer', write_only=True)

    class Meta:
        model = Feedback
        fields = ['id', 'seller', 'buyer', 'rating', 'comment', 'created_at', 'seller_id', 'buyer_id']