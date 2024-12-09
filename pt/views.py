from django.shortcuts import render, redirect


# Redirect the user to trainers if signed in
def pt(request):
    if request.user.is_authenticated:
        return redirect('trainers:trainers')
    return render(request, 'pt/index.html')
