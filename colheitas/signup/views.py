from django.shortcuts import render

# Create your views here.
def signup(request):  
    return render(request, 'signup/signup.html')

def buyer_signup(request):
    return render(request, 'signup/buyer_signup.html')

def seller_signup(request):
    return render(request, 'signup/seller_signup.html')