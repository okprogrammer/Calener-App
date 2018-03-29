from django import forms

class EntryForm(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Event Name'}))
    date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'Date'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Plese Enter the description'}))