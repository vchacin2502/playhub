from django import forms
from .models import Juego, Resena

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = '__all__'

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        exclude = ['usuario_username', 'fecha']

    def clean_comentario(self):
        comentario = self.cleaned_data.get('comentario')
        if comentario and len(comentario) < 10:
            raise forms.ValidationError(
                "El comentario debe tener al menos 10 caracteres"
            )
        return comentario
