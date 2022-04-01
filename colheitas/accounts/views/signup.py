from django.shortcuts import render

def SignUpView(request):
    return render(request, 'registration/signup.html')