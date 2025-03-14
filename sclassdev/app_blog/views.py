from django.shortcuts import render

# Create your views here.
def viewblog(request):
    return render(request, 'app_blog/index.html')