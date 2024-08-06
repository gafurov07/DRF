from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from apps.models import Category, Product, User


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name'
        read_only_fields = 'slug',


class ProductModelSerializer(serializers.ModelSerializer):
    # category = CategoryModelSerializer()


    class Meta:
        model = Product
        # fields = '__all__'
        exclude = 'created_at', 'updated_at'
        read_only_fields = 'slug',

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['category'] = CategoryModelSerializer(instance.category).data
        return repr




class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'password', 'first_name'

        extra_kwargs = {
            'password': {'write_only': True}
        }

