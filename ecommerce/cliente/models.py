from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import MinValueValidator

class Usuario(models.Model):
    correo= models.EmailField('correo',unique=True)
    contrasenia= models.CharField('contrasenia',max_length=128)
    telefono= models.CharField('telefono', max_length=15, null=False)
    def save(self, *args, **kwargs):
        self.contrasenia = make_password(self.contrasenia)
        super().save(*args, **kwargs)

    def verificar(self, contrasenia):
        return check_password(contrasenia, self.contrasenia)
   
    def __str__(self):
        return self.correo
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'



class producto(models.Model):
    nombre= models.CharField('nombre', max_length=100)
    descripcion= models.TextField('descripcion')
    precio_base= models.DecimalField('precio', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def cantidad_stock(self):
        return sum(variante.stock for variante in self.variantes.all())
    
    def __str__(self):
        return f"{self.nombre} (Stock: {self.cantidad_stock()})"

class Variante_p(models.Model):
    colores=[
        ('Negro', 'Negro'),
        ('Blanco', 'Blanco'),
        ('Verde', 'Verde'),
        ('Amarillo', 'Amarillo'),
        ('Rojo', 'Rojo'),
    ]
    
    categorias = [
        ('Niños', 'Niños'),
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
    ]
    producto= models.ForeignKey(producto, related_name='variantes', on_delete=models.CASCADE)
    color= models.CharField('Color', max_length=10, choices=colores)
    talla= models.IntegerField('Talla', null=False)
    categoria = models.CharField('Categoría', max_length=10, choices=categorias)
    imagen= models.ImageField('Imagen',upload_to='productos/')
    stock= models.PositiveIntegerField(
        'Cantidad en stock',
        default=0,
        validators=[MinValueValidator(0)]
        #verbose_name='Cantidad en Stock'
    )
    sku= models.CharField('Sku/código',max_length=50, unique=True)

    class Meta:
        unique_together= ('producto', 'color')
        verbose_name= 'Variante'
        verbose_name_plural= 'Variantes'

    def __str__(self):
        return f"{self.producto.nombre} - {self.get_color_display()} (Stock: {self.stock})"
    