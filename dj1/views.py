from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# from django.contrib.auth.models import User
# Create your views here.
# def fun1(request):
    # user=User.objects.create_user(username='abcd',password='abc123',email='a@gmail.com')
    # user.save()
    # user=User.objects.get(username='abcd')
    # if user.check_password('abc123'):
    #     return HttpResponse(f'user authentication ! succesfull ! username: {user.username}')
    # else:
    #     return HttpResponse('Incorrect  password')
    # user=User.objects.get(username='abcd')
    # user.is_staff=True
    # user.save()
    # return HttpResponse('staff')
    
# def registration_form(req):
#     if req.method == 'POST':
#         name=req.POST.get('u_name')
#         email=req.POST.get('email')
#         pas=req.POST.get('password')
#         phone=req.POST.get('number')
#         address=req.POST.get('address')
#         obj=CustomUser()
#         obj.username=name
#         obj.email=email
#         obj.password=pas
#         obj.phone_number=phone
#         obj.address=address
#         obj.save()
#         return HttpResponse('Registered')
#     return render(req,'user_registration.html')

# def customUser_form(req):
#     if req.method == 'POST':
#         form=customusercreationform(req.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form=customusercreationform()
#     return render(req,'custom_user.html',{'form':form})

def user_form(req):
    if req.method == 'POST':
        form=userForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
    else:
        form=userForm()
    return render(req,'userForm.html',{'form':form})


from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('name')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dash')
        else:
            messages.error(request,"invalid username")
            return HttpResponse("Invalid username or password")
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.info(request,"Logged out")
    return redirect('log')

@login_required
def dashboard(request):
    if request.user.groups.filter(name='admin').exists():
        value="Admin"
        return render(request,'admin_page.html',{'name':value})
    elif request.user.groups.filter(name='staff').exists():
        value="Staff"
        return render(request,'admin_page.html',{'name':value})
    elif request.user.groups.filter(name='customer').exists():
        value="Customer"
        return render(request,'admin_page.html',{'name':value})
    else:
        return HttpResponse("You do not have permission to this page")
