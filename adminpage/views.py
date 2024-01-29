from django.shortcuts import render

# Create your views here.


def admin_homepage(request):
    return render(request, "admins/dashboard.html")
