

from django.urls import path
from . import views

urlpatterns = [


path('',views.index,name="index"),
path('display_account',views.display_account,name="display_account"),
path('displayall',views.displayall,name="displayall"),
path('inputdata',views.inputdata,name="inputdata"),


]

