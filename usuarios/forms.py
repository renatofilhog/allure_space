from django import forms


class LoginForms(forms.Form):
    login = forms.CharField(
        label='Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs= {
                'class': 'col-12 col-lg-12 form-control',
                'placeholder': 'Insira seu login',
                'style': 'margin-bottom: 5px;',
                'name':'login'
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs= {
                'class':'col-12 col-lg-12 form-control',
                'placeholder':'Insira sua senha',
                'style':'margin-bottom: 5px;',
                'name': 'senha'
            }
        )
    )


class RegistroForms(forms.Form):
    nome = forms.CharField(
        label='Nome completo',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs= {
                'class': 'col-12 col-lg-12 form-control',
                'placeholder': 'Ex.: Renato Filho',
                'style': 'margin-bottom: 5px;',
                'name':'nome'
            }
        )
    )
    email = forms.EmailField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs= {
                'class':'col-12 col-lg-12 form-control',
                'placeholder':'Ex.: renato@alluredev.com.br',
                'style':'margin-bottom: 5px;',
                'name': 'email'
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs= {
                'class': 'col-12 col-lg-12 form-control',
                'placeholder': 'Insira uma senha',
                'style': 'margin-bottom: 5px;',
                'name': 'senha'
            }
        )
    )
    confirmar_senha = forms.CharField(
        label='Confirmação de senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs= {
                'class': 'col-12 col-lg-12 form-control',
                'placeholder': 'Insira sua senha novamente',
                'style': 'margin-bottom: 5px;',
                'name': 'confirmasenha'
            }
        )
    )


