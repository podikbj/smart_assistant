from .models import *
from django.forms import ModelForm, TextInput, DateInput, TimeInput


class DatePickerInput(DateInput):
    input_type = 'date'


class TimePickerInput(TimeInput):
    input_type = 'time'


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['context', 'deadline_day', 'deadline_time']

        widgets = {
            "context": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'task context'
            }),

            "deadline_day": DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': 'deadline day'
            }),

            "deadline_time": TimePickerInput(attrs={
                'class': 'form-control',
                'placeholder': 'deadline time'
            }),

        }
