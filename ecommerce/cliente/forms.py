from django import forms
from cliente.models import producto, Variante_p, Usuario

class Registro(forms.Form):
    correo= forms.EmailField(
        label='Correo',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    contrasenia= forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    telefono= forms.CharField(
        label='Teléfono', widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    # es_vendedor= True;



class loginn(forms.Form):
    correo= forms.EmailField(
        label='Correo',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    contrasenia= forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

# from models import Variante_p

class formProducto(forms.ModelForm):
    class Meta:
        model=producto
        fields=['nombre', 'descripcion', 'precio_base']
        widgets={
            'descripcion': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_base': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels={
            'precio_base': 'Precio Base (Mxn)'
            }

class Varianteform(forms.ModelForm):
    class Meta:
        model= Variante_p
        fields= ['color', 'imagen', 'stock', 'sku']
        labels= {
            'stock': 'Unidades Disponibles',
            'color': 'Colores disponibles'
        }
       
        widgets={
            'color': forms.Select(attrs={'class':'form-select'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'mn': 0}),
            'sku': forms.TextInput(attrs={'class': 'form-control'}),

        }

