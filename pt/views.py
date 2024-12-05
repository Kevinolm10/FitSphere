from django.shortcuts import render, redirect

def pt(request):
    if request.user.is_authenticated:
        return redirect('trainers:trainers')  # Redirect to the trainers page in the 'trainers' app
    return render(request, 'pt/index.html')