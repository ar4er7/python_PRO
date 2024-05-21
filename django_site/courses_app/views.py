from django.shortcuts import render


def is_authenticated(request):
    return render(request, "authentication_information.html")