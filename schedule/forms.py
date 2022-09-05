from django import forms
from schedule.models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = "__all__"
