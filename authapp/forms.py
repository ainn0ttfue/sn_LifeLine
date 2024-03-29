from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm

from authapp.models import Person


class RegisterForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'b-form__input b-auth-form__input'

            if not 'password' in field_name:
                field.widget.attrs['placeholder'] = self.Meta.model._meta.get_field(field_name).verbose_name.capitalize
            else:
                field.widget.attrs['placeholder'] = 'Пароль'
                if field_name == 'password2':
                    field.widget.attrs['placeholder'] = 'Повторите пароль'
            field.help_text = ''
            field.label = ''


class LoginForm(AuthenticationForm):
    class Meta:
        model = Person
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'b-form__input b-auth-form__input'

            if not 'password' in field_name:
                field.widget.attrs['placeholder'] = self.Meta.model._meta.get_field(field_name).verbose_name.capitalize
            else:
                field.widget.attrs['placeholder'] = 'Пароль'

            field.help_text = ''
            field.label = ''


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'b-form__input b-auth-form__input'

            if 'email' in field_name:
                field.widget.attrs['placeholder'] = 'Электронная почта'

            field.help_text = ''
            field.label = ''


class UpdatePasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UpdatePasswordForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'b-form__input b-auth-form__input mb-2'
            field.widget.attrs['placeholder'] = 'Пароль'

            if field_name == 'new_password2':
                field.widget.attrs['placeholder'] = 'Повторите пароль'

            field.label = ''
