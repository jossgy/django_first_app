from django.http import HttpResponse

def hello(request):
    return HttpResponse("¡Hola, mundo!")

def about(request):
    return HttpResponse("Esto es la página 'About'.")
