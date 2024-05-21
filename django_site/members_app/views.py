from django.shortcuts import render


def input_info(request):
    return render(request, "input_page.html")


def output_info(request):
    return render(request, "output_page.html")
