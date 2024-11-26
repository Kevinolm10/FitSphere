from django.db import models
from django.contrib.auth.models import User  
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField


# Create your models here.

# Custom validator for alphabetic characters only
def validate_age(value):
    if value < 18 or value > 100:
        raise ValidationError('Age must be between 18 and 100.')

# Custom validator for alphabetic characters only
def validate_name(value):
    if not value.isalpha():
        raise ValidationError(f'{value} contains invalid characters. Only alphabetic characters are allowed.')

class Trainer(models.Model):
    # Foreign Key to User model 
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    featured_image = CloudinaryField('image', default='placeholder')
    # Fields with validation
    first_name = models.CharField(
        max_length=100,
        validators=[validate_name],  
        error_messages={
            'invalid': 'First name must only contain alphabetic characters.'
        }
    )
    last_name = models.CharField(
        max_length=100,
        validators=[validate_name],  
        error_messages={
            'invalid': 'Last name must only contain alphabetic characters.'
        }
    )
    age = models.IntegerField(validators=[validate_age])  # Custom age validation
    description = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class TrainerFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="feedbacks")
    rating = models.FloatField()
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Feedback from {self.user.username} for {self.trainer.first_name} {self.trainer.last_name}"