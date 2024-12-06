from django.urls import path 
from shopping.views import* 
app_name='shirt' 

urlpatterns=[
    path=('shirt/',shirt,name='shirt'),
]