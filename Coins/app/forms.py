from django import forms
from .models import Attendance, CoinTransaction

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['status']

class CoinForm(forms.ModelForm):
    class Meta:
        model = CoinTransaction
        fields = ['coins']