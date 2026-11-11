from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'fishcommunity/home.html')

def angler_posts(request):
    return render(request, 'fishcommunity/angler_posts.html')

def conservation_info(request):
    return render(request, 'fishcommunity/conservation.html')