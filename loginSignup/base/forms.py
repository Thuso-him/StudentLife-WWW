from django import forms
from .models import Reminder

class ReminderForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
        label="Due Date"
    )

    class Meta:
        model = Reminder
        fields = ['title', 'description', 'due_date'] 