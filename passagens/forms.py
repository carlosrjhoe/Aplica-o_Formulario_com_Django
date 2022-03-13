from datetime import datetime
from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classes

class PassagensForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    classe_viagem = forms.ChoiceField(label='Classe do vôs', choices=tipos_de_classes)
    informacoes = forms.CharField(
        label='Informações extras',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='Email', max_length=150)
    
    def clean_origem(self):
        origem = self.cleaned_data.get('origem',)
        if any(char.isdigit() for char in origem):
            raise forms.ValidationError('Origem invalida: Não inclua números')
        else:
            return origem
        
    def clean_destino(self):
        destino = self.cleaned_data.get('destino',)
        if any(char.isdigit() for char in destino):
            raise forms.ValidationError('destino invalida: Não inclua números')
        else:
            return destino
        