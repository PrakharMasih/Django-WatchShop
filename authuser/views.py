
from django.shortcuts import render , redirect
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Product,Category , Customer


def home(request):
    return render(request, "signin.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username alreay exist! please try some other username")
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('signup')

        if len(username)>10:
            messages.error(request, "Usename must be 10 characters")
            return redirect('signup')
        if pass1 != pass2:
            messages.error(request, "password not matched")
            return redirect('signup')
            
        if not username.isalnum():
            messages.error(request, "username must be alpha-Numeric")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created!!")

        return redirect('/')

    return render(request, "signup.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username , password=pass1)

        if user is not None:
            login(request, user)
            fname= user.first_name
            return redirect('index')
            # return render(request, "index.html", {'fname':fname})


        else:
            messages.error(request, "User not registered")
            return redirect('/')
    return render(request, "signin.html")

def signout(request):
    logout(request)
    messages.success(request, "logged out successfully!!")
    return redirect('')

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    categoryID = request.GET.get('category')

    if categoryID:
        products = Product.get_all_products_by_id(categoryID)
    else:
        products = Product.objects.all()
    data = { 
        'products':products,
        'categories':categories
    }
    return render(request, 'index.html', data)


def one(request):
    return render(request, '1/1.html')

def two(request):
    return render(request, '2/2.html')

def three(request):
    return render(request, '3/3.html')

def four(request):
    return render(request, '4/4.html')

def five(request):
    return render(request, '5/5.html')

def six(request):
    return render(request, '6/6.html')

def seven(request):
    return render(request, '7/7.html')

def eight(request):
    return render(request, '8/8.html')