from django.urls import path
from .views import index, item_page

urlpatterns = [
    path("home/", index, name="home"),
    path("item/", item_page, name="item"),
]