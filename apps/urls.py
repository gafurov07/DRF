from django.urls import path

from apps.views import CategoryListCreateAPIView, ProductListCreateAPIView, UserListCreateAPIView

urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view()),
    path('product/', ProductListCreateAPIView.as_view()),
    path('user/', UserListCreateAPIView.as_view()),
]