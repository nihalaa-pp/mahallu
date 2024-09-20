# In mahallu/urls.py
from django.urls import path
from . import views 
from .views import register, login, logout, create_household

urlpatterns = [
     # List all households
   path('', views.create_household, name='create_household'),  # Maps 'create/' to the create household view
   path('<int:household_id>/member/', views.create_household_member, name='create_household_member'),
   path('households/', views.household_list, name='household_list'),
   path('household/<int:pk>/edit/', views.edit_household, name='edit_household'),
   path('household/<int:pk>/delete/', views.delete_household, name='delete_household'),
   path('household/members/', views.household_member_list, name='household_member_list'),
   path('household/member/create/', views.create_household_member, name='create_household_member'),
   path('household/member/<int:pk>/edit/', views.edit_household_member, name='edit_household_member'),
   path('household/member/<int:pk>/delete/', views.delete_household_member, name='delete_household_member'),
   path('register/', register, name='register'),
   path('login/', login, name='login'),
   path('logout/', logout, name='logout'),
   path('create-household/', views.create_household, name='create_household'),

]
