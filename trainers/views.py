from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Trainer, TrainerFeedback
from .forms import TrainerFeedbackForm

# View to display all trainers
def trainers(request):
    # Query the database to get all trainers
    trainers = Trainer.objects.all()

    # Pass the trainers to the template as context
    return render(request, 'trainers/trainers.html', {'trainers': trainers})

def trainer_profile(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    
    # Get feedbacks and average rating directly
    feedbacks = TrainerFeedback.objects.filter(trainer=trainer)
    avg_rating = trainer.get_average_rating()

    # Pass relevant data to the template
    return render(request, 'trainers/trainer_profile.html', {
        'trainer': trainer,
        'feedbacks': feedbacks,
        'avg_rating': round(avg_rating, 1),  # Round to one decimal place
        'stars_range': range(1, 6)  # For star rating display
    })

def submit_feedback(request, trainer_id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to leave feedback.")
        return redirect('login')

    trainer = get_object_or_404(Trainer, id=trainer_id)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        if rating not in ['1', '2', '3', '4', '5']:
            messages.error(request, "Invalid rating. Please select a valid star rating.")
            return redirect('trainers:trainer_profile', trainer_id=trainer.id)

        TrainerFeedback.objects.create(
            user=request.user,
            trainer=trainer,
            rating=int(rating),
            comment=comment
        )

        messages.success(request, "Thank you for your feedback!")
        return redirect('trainers:trainer_profile', trainer_id=trainer.id)

    return redirect('trainers:trainer_profile', trainer_id=trainer.id)

def edit_feedback(request, feedback_id):
    # Get the feedback object to be edited
    feedback = get_object_or_404(TrainerFeedback, id=feedback_id)
    trainer = feedback.trainer  # Get the associated trainer

    # Ensure the logged-in user is the owner of the feedback
    if request.user != feedback.user:
        messages.error(request, "You do not have permission to edit this feedback.")
        return redirect('trainers:trainer_profile', trainer_id=trainer.id)

    # Process the form submission (POST request)
    if request.method == 'POST':
        form = TrainerFeedbackForm(request.POST, instance=feedback)  # Populate form with existing data
        if form.is_valid():
            form.save()  # Save the updated feedback
            messages.success(request, "Feedback updated successfully!")
            return redirect('trainers:trainer_profile', trainer_id=trainer.id)
        else:
            print(form.errors)  # Log form errors for debugging
            messages.error(request, "There was an error updating your feedback.")
            return redirect('trainers:trainer_profile', trainer_id=trainer.id)

    else:
        form = TrainerFeedbackForm(instance=feedback)

    return render(request, 'trainer_profile.html', {
        'form': form,
        'feedback': feedback,
        'trainer': trainer,
    })



def delete_feedback(request, id):
    feedback = get_object_or_404(TrainerFeedback, id=id)
    trainer = feedback.trainer

    if feedback.user == request.user:
        feedback.delete()
        messages.success(request, "Feedback deleted successfully!")
    else:
        messages.error(request, "You can only delete your own feedback.")

    return redirect('trainers:trainer_profile', trainer_id=trainer.id)
