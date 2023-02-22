from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')

        email = request.POST.get("email")

        phone = request.POST.get("contact")

        User.objects.create(name=name, email=email, contact=phone)
        
        # messages.success(request, 'User data saved!')

        return redirect('index')

    else:
        data = {
            'userData': User.objects.all()
        }

        return render(request, 'index.html', data)

def delete_user(request, id):
    User.objects.get(id=id).delete()
    return redirect('/')

def update_user(request, id):
    if request.method == 'POST':
        obj = User.objects.get(id=id)
        obj.name = request.POST.get('name')
        obj.email = request.POST.get('email')
        obj.contact = request.POST.get('contact')
        obj.save()

        return redirect('/')
    else:
        data = {
            'user': User.objects.get(id=id)
        }
        return render(request, 'update.html', data)