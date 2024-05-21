from django.shortcuts import render


def input_page(request):
    return render(request, "input_page.html")


def output_page(request):
    return render(request, "output_page.html")
