
from submit import views
from django.urls import path

urlpatterns = [
    
    path('', views.add_show,name='base1'), 
    path('delete/<int:id>/', views.delete_data,name='deletedata'),
    path('<int:id>/', views.update_data,name='updatedata'),
]   