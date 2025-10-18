from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>My world it fucking worked</h1>")

