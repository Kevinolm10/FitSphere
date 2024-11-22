from django.shortcuts import render

# Create your views here.
def pt(request):
    return render(request, 'base.html')


