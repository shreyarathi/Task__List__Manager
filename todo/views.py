from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo
#json help to store and pass the data from server to web page. It is javascript library
import json
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.models import User
from validate_email import validate_email
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.utils.decorators import method_decorator
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import boto3
from django.conf import settings

client=boto3.client("ses", region_name='us-east-1', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, 
                    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY) 

# Create your views here.
class EmailValidationView(View):
    def post(self, request):
        #stored in dictionary of python library
        data = json.loads(request.body)
        email = data['email']
        #built in function for validation of email
        if not validate_email(email):
            return JsonResponse({'email error': 'Email is Invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'sorry email in use,choose another one '}, status=400)
        return JsonResponse({'email_valid': True})

class UserNameValidationView(View):
    def post(self, request):
        #stored in dictionary of python library
        data = json.loads(request.body)
        username = data['username']
        #built in function of python
        if not str(username).isalnum():
            return JsonResponse({'username error': 'username should contain only alphanumeric character'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'sorry username in use,choose another one '}, status=400)
        return JsonResponse({'username_valid': True})

  #  todo = register(content = request.POST['username', 'email', 'password'])
  #  todo.save()
  #  return redirect(request, '/todos/list/')


class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        
        response=client.get_identity_verification_attributes(Identities= [email])['VerificationAttributes'][email]['VerificationStatus']

        print(response)
        if response !=:
            client.verify_email_identity(EmailAddress = email)
            return HttpResponse('Verification mail has been sent to your email address. Verify the email address and try to create account')
        #context = User(username = username, email = email, password = password)
        #context.save()
        #login(request, context)
        #send_mail(
        #    'Account successfully created',   #subject
        #    'your account is ready to use and your username is '+ username,   #message
        #    'shreyarathi14@gmail.com',  #sender mail id
        #    [email] #receiver mail id
        #    )
        #return redirect('/todo/list/')

@login_required
def list_todo_items(request):
    context = {'todo_list' : Todo.objects.all()}
    return render(request, 'todos/todo_list.html',context)

@csrf_exempt
def insert_todo_item(request):
    if request.is_ajax():
        content = request.POST.get('content', '')
        todo = Todo(content=content)
        todo.save()
        todo_list = []
        for todo in Todo.objects.all():
            todo_list.append({'content': todo.content, 'id': todo.id})

        
        json_response = {'todo_list' : todo_list}
        print(json_response)
        return HttpResponse(json.dumps(json_response), status= 200,
            content_type='application/json')

    return render(request, 'todo_list.html', {'todo_list': ''})

def delete_todo_item(request,todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todo/list/')

class LoginView(View):
    def get(self, request):
        print('go')
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST['username']
        print('write')
        password = request.POST['password']
     #   print(email, password)
        if username and password:
            user = User.objects.get(username=username , password=password)
            login(request, user)
            if user:
                print('Logged in Successfully')
                return redirect('/todo/list/')
            print('Invalid credentials,try again')
            return render(request, 'authentication/login.html')
        else:
            logout(request)

def out(request):
    logout(request)
    return redirect('/todo/login/')
