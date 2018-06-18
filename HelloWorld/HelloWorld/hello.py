from django.http import HttpResponse


def index(request):
    return HttpResponse("<html>Hello, world! <a href=\"again/\">link</a> </html>")