from django.shortcuts import render, redirect


def input_info(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input')
        request.session['user_input'] = user_input
        return redirect("output_information")
    else:
        return render(request, "input_page.html")


def output_info(request):
    context = {"user_input": request.session.get("user_input")}
    return render(request, "output_page.html", context)


def index(request):
    return render(request, "index.html")