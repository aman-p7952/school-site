from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import CustomUser, Candidate
from django.views.decorators.csrf import ensure_csrf_cookie
import re
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages 
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def check(email):

    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        return True
    return False


def landing_page(request):
    context = {"is_authenticated": request.user.is_authenticated}
    if request.user.is_authenticated:
        context["email"] = request.user.email
    print(context)
    return render(request, "home.html", context)


def about(request):
    context = {"is_authenticated": request.user.is_authenticated}
    if request.user.is_authenticated:
        context["email"] = request.user.email
    print(context)
    return render(request, "about.html", context)


def academics(request):
    context = {"is_authenticated": request.user.is_authenticated}
    if request.user.is_authenticated:
        context["email"] = request.user.email
    print(context)
    return render(request, "academics_home.html", context)


def academics_class1(request):
    context = {"is_authenticated": request.user.is_authenticated}
    if request.user.is_authenticated:
        context["email"] = request.user.email
    print(context)
    return render(request, "academics_class1.html", context)


def admission(request):
    context = {"is_authenticated": request.user.is_authenticated}
    if request.user.is_authenticated:
        context["email"] = request.user.email
    print(context)
    return render(request, "admission.html", context)



def register(request):
    if request.method == 'POST':
        # print(request.POST)
        fname = str(request.POST['fname'])
        lname = str(request.POST['lname'])
        email = str(request.POST['inputEmail'])
        gender = str(request.POST['selectgender'])
        dob = str(request.POST['date'])
        address1 = str(request.POST['inputAddress'])
        address2 = str(request.POST['inputAddress2'])
        city = str(request.POST['inputCity'])
        zip_code = str(request.POST['inputZip'])
        state = str(request.POST["inputState"])
        if not request.user.is_authenticated:
            return redirect("login")
        print(request.user.email)
        user = Candidate(login=request.user, firstname=fname, lastname=lname, email=email, gender=gender, dob=dob,
                    address1=address1, address2=address2, city=city, zip_code=zip_code, state=state)
        user.save()
        return redirect("landing_page")
    return render(request, 'register.html', {})


def signup(request):
    if request.method == 'POST':
        email = str(request.POST["email"])
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        user = CustomUser.objects.filter(email = email)
        if user.exists():
            messages.add_message(request,messages.INFO,"Email already registered")
            return redirect("signup")
        
        if password1 != password2:
            messages.add_message(request,messages.INFO,"Password do not match")
            return redirect("signup")
        user = CustomUser.objects.create(email=email)
        user.set_password(password1)
        user.save()
        user = authenticate(email=email, password=password1)
        if user is not None:
            login(request,user)
            return redirect("landing_page")
    return render(request,"signup.html")

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         print(form.errors)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(email=email, password=raw_password)
#             login(request, user)
#             return redirect('landing_page')
#         else:
#             return render(request, 'signup.html',{"error_html":form.errors})
#     else:
#         return render(request, 'signup.html')

# def signup(request):
#     if request.method == 'POST':
#         print(request.POST)
#         email = str(request.POST['inputEmail'])
#         if not check(email):
#             return render(request, "signup.html", {"error": "Invalid email"})
#         password = str(request.POST['password'])
#         password1 = str(request.POST['password1'])
#         if password1 != password:
#             return render(request, "signup.html", {"error": "passwords does not match"})
#         else:
#             login = Login(email=email, password=password)
#             login.save()
#             return render(request, 'home.html', {})
#     return render(request, 'signup.html', {})


def login1(request):
    print(request.user.is_authenticated)
    if request.method == 'POST':
        print(request.POST)
        email = request.POST['inputEmail']
        if not check(email):
            return render(request, "login.html", {"error": "Invalid email"})
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        print(user)
        print(request.user)
        if user is not None:
            login(request, user)
            return redirect("landing_page")
        else:
            return render(request, "login.html", {"error": "Login failed"})
    return render(request, "login.html")


def logout1(request):
    logout(request)
    context = {"is_authenticated": request.user.is_authenticated}
    if request.user.is_authenticated:
        context["email"] = request.user.email
    return redirect('landing_page')


def profile(request):
    context = {"is_authenticated": request.user.is_authenticated}
    return render(request, "profile.html", context)
