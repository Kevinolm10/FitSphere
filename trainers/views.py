from django.shortcuts import render, get_object_or_404
from .models import Trainer

# Create your views here.
def trainers(request):
    # Query the database to get all trainers
    trainers = Trainer.objects.all()

    # Pass the trainers to the template as context
    return render(request, 'trainers/trainers.html', {'trainers': trainers})

def trainer_profile(request, trainer_id):
    # Get the trainer by ID, or return a 404 if not found
    trainer = get_object_or_404(Trainer, id=trainer_id)
    return render(request, 'trainer_profile.html', {'trainer': trainer})