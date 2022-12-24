from django.shortcuts import render

# Create your views here.
def indexPageView(request):
    return render(request, 'donnyapp/index.html')

def aboutPageView(request):
    return render(request, 'donnyapp/about.html')

def formPageView(request):
    return render(request, 'donnyapp/form.html')