from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('View from main app')