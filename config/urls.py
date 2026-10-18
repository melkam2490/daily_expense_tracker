from django.contrib import admin
from django.urls import path, include
from expenses.views import home, register, add_expense, delete_expense, edit_expense


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('add-expense/', add_expense, name='add_expense'),
    path('delete-expense/<int:expense_id>/',
         delete_expense, name='delete_expense'),
    path('edit-expense/<int:expense_id>/', edit_expense, name='edit_expense'),
]
