from django.urls import path
from . import views
from .views import RegistrationView,UserNameValidationView, EmailValidationView, LoginView
#Cross-Site Request Forgery
#from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('list/',views.list_todo_items),
    path('insert_todo/',views.insert_todo_item,name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/',views.delete_todo_item,name='delete_todo_item'),
    path('register/', RegistrationView.as_view(), name = 'register'),
    path('validate-username',  UserNameValidationView.as_view(), name = 'validate-username'),
    path('validate-email',  EmailValidationView.as_view(), name = 'validate-email'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('out/',views.out),
 #   path('templates/signin/', views.signin),
]