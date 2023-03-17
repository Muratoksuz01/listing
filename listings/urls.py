from .views import *
from django.urls import path,include
urlpatterns = [
    path("",listing_list,name="listing_list"),
    path("retrieve/<int:id>",listing_retrieve,name="listing_retrieve"),
    path("create",listing_create,name="listing_create"),
    path("update/<int:id>",listing_update,name="listing_update"),
    path("delete/<int:id>",listing_delete,name="listing_delete"),


]
