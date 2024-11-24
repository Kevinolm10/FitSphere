from django.shortcuts import render
from .models import Trainer

# Create your views here.
def trainers(request):
    # Query the database to get all trainers
    trainers = Trainer.objects.all()

    # Pass the trainers to the template as context
    return render(request, 'trainers/trainers.html', {'trainers': trainers})