from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.hashers import check_password, make_password
from .forms import RegisterForm, LoginForm


# Register with CustomUser model
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Save CustomUser
            user = CustomUser(
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=make_password(form.cleaned_data['password1'])  # Manually hash the password
            )
            user.save()  # Save the user
            request.session['custom_user_id'] = user.id  # Store custom user's ID in session
            return redirect('home')  # Redirect to home
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


# Login with CustomUser model
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = CustomUser.objects.get(email=email)
                if check_password(password, user.password):  # Check the password
                    request.session['custom_user_id'] = user.id  # Store custom user's ID in session
                    return redirect('success')
                else:
                    form.add_error(None, "Invalid email or password")
            except CustomUser.DoesNotExist:
                form.add_error(None, "Invalid email or password")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


# Logout
def logout(request):
    request.session.flush()  # Clear the session
    return redirect('login')


def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')