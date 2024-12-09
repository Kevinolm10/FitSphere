from django import forms
from .models import TrainerFeedback


class TrainerFeedbackForm(forms.ModelForm):
    class Meta:
        model = TrainerFeedback
        fields = ['rating', 'comment']


def clean_comment(self):
    comment = self.cleaned_data.get('comment')
# You can add extra validations here if needed
    if not comment:
        raise forms.ValidationError('Comment cannot be empty.')
        return comment
