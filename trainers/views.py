from django.shortcuts import render, get_object_or_404
from .models import Trainer, TrainerFeedback

# Create your views here.

# View to display all trainers
def trainers(request):
    # Query the database to get all trainers
    trainers = Trainer.objects.all()

    # Pass the trainers to the template as context
    return render(request, 'trainers/trainers.html', {'trainers': trainers})

# View to display a specific trainer profile along with feedback
def trainer_profile(request, trainer_id):
    # Get the trainer by ID, or return a 404 if not found
    trainer = get_object_or_404(Trainer, id=trainer_id)
    
    # Get all feedbacks for the trainer
    feedbacks = TrainerFeedback.objects.filter(trainer=trainer)

    # Calculate the average rating for the trainer
    avg_rating = trainer.get_average_rating()

    # Create a list of star numbers (for looping in the template)
    stars_range = range(1, 6)

    # Pass the trainer, feedbacks, average rating, and star range to the template
    return render(request, 'trainer_profile.html', {
        'trainer': trainer,
        'feedbacks': feedbacks,
        'avg_rating': avg_rating,
        'stars_range': stars_range,  # This will be passed to the template
    })