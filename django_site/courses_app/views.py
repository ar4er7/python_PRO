from django.shortcuts import render


def is_authenticated(request):
    context = {"message": f"This is the Courses page: user - {request.user.username}"}
    if request.user.is_anonymous:
        context.update({"message": "You have no permissions to view this page!"})
        return render(request, "authentication_information.html", context)
    return render(request, "authentication_information.html", context)
