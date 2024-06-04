from django.urls import path
from . import views


urlpatterns = [
    # localhost:8000/chai
    path('', views.all_chai, name='all_chai'),
    # localhost:8000/chai/order
    #path('order/', views.order, name='order'),

]

#just adding a line to see the change. 
