from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView, Dashboard, AddItem, EditItem, DeleteItem
from django.contrib.auth import views as auth_views

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Index, Dashboard, AddItem, EditItem, DeleteItem, SignUpView

from .views import CustomLogoutView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('add-item/', AddItem.as_view(), name='add-item'),
    path('edit-item/<int:pk>/', EditItem.as_view(), name='edit-item'),
    path('delete-item/<int:pk>/', DeleteItem.as_view(), name='delete-item'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # No need to specify template_name for LogoutView
    path('logout/', CustomLogoutView.as_view(next_page='login'), name='logout'),

]
