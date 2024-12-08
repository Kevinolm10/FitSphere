from django import forms
from .models import TrainerFeedback

class TrainerFeedbackForm(forms.ModelForm):
    class Meta:
        model = TrainerFeedback
        fields = ['rating', 'comment']