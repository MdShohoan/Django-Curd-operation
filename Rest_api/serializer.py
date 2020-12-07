from rest_framework import serializers
from .models import Product

class PostSerilazer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','descriptions','price','stock')

