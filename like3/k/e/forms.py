from django import forms

class ExampleForm(forms.Form):
    CHOICES = [('option1', 'like'), ('option2', 'dislike')]
    select_field = forms.ChoiceField(choices=CHOICES, widget=forms.Select())
