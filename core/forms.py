from django import forms
from .models import FacebookStatus
from datetimepicker.widgets import DateTimePicker


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class UserPostSubmit(forms.ModelForm):
    publish_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = FacebookStatus
        fields = ['status', 'publish_date', 'publish_time', 'message', 'link']
        widgets = {
            'publish_date': forms.SelectDateWidget(),
        }
