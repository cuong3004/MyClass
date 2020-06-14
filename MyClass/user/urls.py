from django.urls import path
from .views import list_class, image_class

urlpatterns = [
    path('', list_class, name="class"),
    # id member for class
    path('<int:list_id>', image_class, name="image"),
]
