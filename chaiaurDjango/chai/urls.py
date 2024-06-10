from django.urls import path
from . import views


urlpatterns = [
    # localhost:8000/chai
    path('', views.all_chai, name='all_chai'),
    # localhost:8000/chai/order
    #path('order/', views.order, name='order'),
    path('<int:chai_id>/', views.chai_details, name='chai_detail')

]

#just adding a line to see the change. 
