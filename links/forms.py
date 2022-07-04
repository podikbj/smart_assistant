from .models import Links, Categories
from django.forms import ModelForm, TextInput, Textarea


class LinkForm(ModelForm):
    class Meta:
        model = Links
        fields = [ 'category', 'sub_category', 'title', 'url', 'context']
        # fields = '__all__'

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Link name'
            }),
            "sub_category": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'sub category'
            }),
            "url": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL address'
            }),
            "context": Textarea(attrs={
                'cols': 60, 'rows':10,
                'placeholder': 'context'
            })

        }

class CategoryForm(ModelForm):
    class Meta:
        model = Categories
        fields = ['title']

        # widgets = {
        #     "title": TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Category name'
        #     })
        #
        # }
