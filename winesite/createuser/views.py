from django.http import HttpResponse


def index(request):
    return HttpResponse("Aaaaha, he wants to sign up")
