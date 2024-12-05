from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages 
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
    trainer = get_object_or_404(Trainer, id=trainer_id)
    
    # Get all feedbacks for the trainer
    feedbacks = TrainerFeedback.objects.filter(trainer=trainer)

    # Calculate the average rating for the trainer and round it to 1 decimal place
    avg_rating = trainer.get_average_rating()

    # Round to 1 decimal place for easy template handling
    avg_rating = round(avg_rating, 1)

    # Create a list of star numbers (for looping in the template)
    stars_range = range(1, 6)

    # Pass the trainer, feedbacks, average rating, and star range to the template
    return render(request, 'trainer_profile.html', {
        'trainer': trainer,
        'feedbacks': feedbacks,
        'avg_rating': avg_rating,
        'stars_range': stars_range,
    })

def submit_feedback(request, trainer_id):
    # Ensure the user is authenticated before allowing feedback submission
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to leave feedback.")
        return redirect('login')

    trainer = get_object_or_404(Trainer, id=trainer_id)

    if request.method == 'POST':
        # Get the data from the form
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        # Make sure rating is valid
        if rating not in ['1', '2', '3', '4', '5']:
            messages.error(request, "Invalid rating. Please select a valid star rating.")
            return redirect('trainer_profile', trainer_id=trainer.id)

        # Create a new feedback object and save it
        feedback = TrainerFeedback(
            user=request.user,
            trainer=trainer,
            rating=int(rating),
            comment=comment
        )
        feedback.save()

        # Add a success message after feedback submission
        messages.success(request, "Thank you for your feedback! It has been successfully submitted.")

        # Redirect to the trainer profile page
        return redirect('trainer_profile', trainer_id=trainer.id)

    return render(request, 'trainer_profile.html', {'trainer': trainer})