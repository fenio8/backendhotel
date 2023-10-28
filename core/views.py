from django.shortcuts import render

# Vistas de la aplicación principal

def Home(request):
    return render(request,"core/home.html")

def AboutUs(request):
    return render(request,"core/about.html")

def Rooms(request):
    return render(request,"core/rooms.html")

# def Blog(request):
#     return render(request,"blog/blog.html")

