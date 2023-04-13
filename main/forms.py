from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import CharField, TextInput, PasswordInput, EmailField, EmailInput


class SignUpUserForm(UserCreationForm):

    username = CharField(max_length=100,
                               required=True,
                               widget=TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = EmailField(required=True,
                             widget=TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = CharField(max_length=50,
                                required=True,
                                widget=PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = CharField(max_length=50,
                                required=True,
                                widget=PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(AuthenticationForm):
        username = CharField(max_length=100,
                             required=True,
                             widget=TextInput(attrs={'placeholder': 'Username',
                                                     'class': 'form-control',
                                                     }))

        password = CharField(max_length=50,
                              required=True,
                              widget=PasswordInput(attrs={'placeholder': 'Password',
                                                          'class': 'form-control',
                                                          'data-toggle': 'password',
                                                          'id': 'password',
                                                          }))

