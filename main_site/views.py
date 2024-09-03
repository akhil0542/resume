from django.shortcuts import render

# Create your views here.
def home(request):
    context={'home': 'active'}
    return render(request, 'main_site/home.html', context=context)

def contact(request):
    context = {'contact': 'active'}
    return render(request, 'main_site/contact.html', context)