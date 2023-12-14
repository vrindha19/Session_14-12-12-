from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User



# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phoneno = request.POST['phoneno']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        User.objects.create(username=username,email=email,phoneno=phoneno,password=password,confirmpassword=confirmpassword)
        messages.success(request, 'Registration successful. please login')
        return redirect('login')
    
    return render (request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()

        if user:
            request.session['user_id'] = user.id
            messages.success(request, 'login successful.')
            return redirect('dashboard')

        else :
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html')
        


def dashboard(request):
    user_id = request.session.get('user_id')
    if user_id:
        return render(request, 'dashboard.html', {'user_id': user_id})       
    else:
        messages.error(request, 'You are not logged in.')
        return redirect('login')
    
def logout(request):
    request.session.clear()
    messages.success(request, 'Logout successful.')
    return redirect('login')
    
   
