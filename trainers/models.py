from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField
from django.db.models import Avg


# Create your models here.

# Custom validator for alphabetic characters only
def validate_age(value):
    if value < 18 or value > 100:
        raise ValidationError('Age must be between 18 and 100.')


# Custom validator for alphabetic characters only
def validate_name(value):
    if not value.isalpha():
        raise ValidationError(
            f'{value} contains invalid characters. Only alphabetic characters '
            'are allowed.'
        )


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

    # Custom age validation
    age = models.IntegerField(validators=[validate_age])
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trainer: {self.first_name} {self.last_name}"

    def get_average_rating(self):
        """Get the average rating of the
        trainer based on the related feedbacks."""
        avg_rating = self.feedbacks.aggregate(Avg('rating'))
        return avg_rating['rating__avg'] if avg_rating['rating__avg'] else 0.0

    class Meta:
        ordering = ['first_name', 'last_name', 'created_at']


class TrainerFeedback(models.Model):
    """Comments and rating system for trainers"""
    STARS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE,
        related_name="feedbacks"
    )
    rating = models.IntegerField(choices=STARS)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"Feedback from {self.user.username} for {self.trainer.first_name}"
            f"{self.trainer.last_name}"
        )

    class Meta:
        ordering = ['-created_at']  # Ordering feedback
        indexes = [
            models.Index(fields=['trainer', 'created_at'])
        ]
