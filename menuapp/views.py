from django.shortcuts import render
from menuapp.models import MenuItem

def home(request):
    return render(request, 'menuapp/menu_template.html')
def about(request):
    return render(request, 'menuapp/about_template.html')


# Create your views here.
