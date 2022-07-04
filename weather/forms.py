from django import forms

cities = [
    ('1', 'Prague'),
    ('2', 'Seattle'),
    ('3', 'Istanbul'),
    ('4', 'Lima'),
    ('5', 'Athenos')
    ]

class UserForm(forms.Form):

    cities_list = forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=cities))