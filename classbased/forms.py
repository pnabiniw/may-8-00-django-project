from django import forms


class ClassRoomForm(forms.Form):
    name = forms.CharField(max_length=20)