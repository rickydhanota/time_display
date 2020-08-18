from django.shortcuts import render
from time import gmtime, strftime

def index(request):
    context = {
        "Time":strftime("%H:%M %p, %m-%d-%Y", gmtime())
        }
    return render(request,'time_display1.html', context)


# def index(request):
#     return HttpResponse("hey hey heyyy")

# def display_time(request):
#     pass