from django_filters import rest_framework
from rest_framework.generics import ListCreateAPIView

from apps.filters import ProductFilter
from apps.models import Category, Product, User
from apps.serializers import CategoryModelSerializer, ProductModelSerializer, UserModelSerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     # queryset = queryset.annotate(product_set_count=0)
    #     return queryset


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = rest_framework.DjangoFilterBackend,
    filterset_class = ProductFilter

    # def filter_queryset(self, queryset):
    #     return queryset.filter(productimage__image__isnull=False)


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
