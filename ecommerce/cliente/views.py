from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Variante_p, producto
from django.contrib import messages as alerts
from .forms import Registro, loginn, Varianteform, formProducto
#from django.contrib.auth import get_user_model
# Create your views here.
def home(request):
    variantes= Variante_p.objects.all()
    return render(request, 'paginas/index.html',{'variantes':variantes})

def base(request):
    return render(request, 'base.html')

def base_login(request):
    return render(request, 'base_login.html')





def home_vendedor(request):
    usuario= request.session.get('usuario')
    request.session['usuario']= usuario
    variantes= Variante_p.objects.filter(
        producto_id__usuario_id__correo= usuario
    ).select_related('producto')
   
    return render(request, 'paginas/home_vendedor.html',{
        'usuario':usuario,
        'variantes':variantes
        })




# def login(request):
#     return render(request, 'paginas/login.html')

# def actualizarProducto(request):
#     return render(request, 'paginas/actualizarProducto.html')




    # if request.method=='POST':
    #     formulario= Registro(request.POST)
    #     if formulario.is_valid():
    #         usuario= formulario.save(commit=False)
    #         usuario.username= formulario.cleaned_data['correo']
    #         usuario.save()
    #         login(request, usuario)
    #         return redirect('home_vendedor')
    # else:
    #     formulario= Registro()
    # return render(request, 'paginas/registro.html',{'formulario':formulario})
def registro(request):
    if request.method == 'POST':

        form= Registro(request.POST)
        if form.is_valid():
            usuario= Usuario(
                correo=form.cleaned_data['correo'],
                contrasenia=form.cleaned_data['contrasenia'],
                
                # es_vendedor=form.cleaned_data['es_vendedor']
            )
            request.session['usuario']= usuario.correo
            usuario.save()
            # return redirect('paginas/index.html')
            return redirect('home_vendedor')
            #return render(request, 'paginas/index.html', {'form': form})
        else:
            form = Registro()

        return render(request, 'paginas/registro.html', {'form': form})
    
    else:
        form = Registro()
        return render(request, 'paginas/registro.html', {'form': form})
    #return render(request, 'paginas/registro.html')
    


def addProducto(request):
    usuarioo= request.session.get('usuario')
    if request.method=='POST':
        form_producto= formProducto(request.POST)
        variante_form= Varianteform(request.POST, request.FILES)

        if form_producto.is_valid() and variante_form.is_valid():
            #print("Forms validos")
            try:
                producto= form_producto.save(commit=False)
                usuario = Usuario.objects.get(correo=usuarioo)
                producto.usuario = usuario
                producto.save()
                
                variante= variante_form.save(commit=False)
                variante.producto=producto
                variante.save()
                alerts.success(request, 'Peoducto Agregado Correctamente')
                #return redirect('home_vendedor')
                return redirect('frontend_catalogoVendedor')
            except Exception as e:
                print(e)
                alerts.error(request, f'Error al guardar: {e}')
        else:
            alerts.error(request,'Fallo en los datos')
    else:
       
        form_producto= formProducto()
        variante_form= Varianteform()
        alerts.error(request,'Fallo al agregar' )
    return render(request, 'paginas/agregarProducto.html',{
        'usuario':usuarioo,
        'form_producto': form_producto,
        'variante_form': variante_form
    })


def login(request):
   
    if request.method == 'POST':
        formulario= loginn(request.POST)
        if formulario.is_valid():
            correo= formulario.cleaned_data['correo']
            contrasenia= formulario.cleaned_data['contrasenia']
            
            try:
                usuario= Usuario.objects.get(correo=correo)
                if(usuario.verificar(contrasenia)):
                    ##Login Exitoso
                    #return render(request,'paginas/home_vendedor.html', {'usuario': usuario})
                
                    request.session['usuario']= correo
                    return redirect('home_vendedor')
                
                  
                else:
                    alerts.error(request, 'Contraseña incorrecta')

            except Usuario.DoesNotExist:
                alerts.error(request, 'Usuario no encontrado')

    else:
        formulario= loginn()
    return render(request, 'paginas/login.html', {'formulario': formulario})


# @login_required(login_url='base_login')
def actualizarProducto(request, variante_id):
    variante= get_object_or_404(
        Variante_p,
        id= variante_id,
        producto_usuario= request.user
    )
    if request.method=='POST':
        form= Varianteform(request.POST, request.FILES, instance=variante)
        if form.is_valid():
            form.save()
            alerts.success(request('Detalle del producto', producto_id=variante.producto.id))
    else:
        form= Varianteform(instance=variante)

    return render(request, 'paginas/actualizarProducto.html',{
        'form': form,
        'variante': variante
    })


# Vistas para el frontend integrado
def frontend_home(request):
    """Vista para la página principal del frontend"""
    #return render(request, 'cliente/index.html')
    variantes= Variante_p.objects.order_by('?')[:5]
    #variantes= producto.objects.all()
    return render(request, 'cliente/index.html',{'variantes':variantes})


def frontend_catalogo(request):
    # """Vista para el catálogo de productos"""
    # return render(request, 'cliente/catalogo.html')
    productos= Variante_p.objects.all()
    return render(request,'cliente/catalogo.html',{
        'productos':productos
    })
    

def frontend_catalogo_vendedor(request):
    usuario= request.session.get('usuario')
    request.session['usuario']= usuario
    variantes= Variante_p.objects.filter(
        producto_id__usuario_id__correo= usuario
    ).select_related('producto')
    return render(request, 'cliente/catalogo_vendedor.html',{
        'usuario':usuario,
        'variantes':variantes
    })

def frontend_carrito(request):
    """Vista para el carrito de compras"""
    # producto= Variante_p.objects.get(id=producto_id)
    # return render(request, 'cliente/carrito.html',{'producto': producto})
    carrito= request.session.get('carrito',[])
    productos= Variante_p.objects.filter(id__in=carrito)
    if producto not in productos:
        alerts.error(request, 'Aún no hay productos en tu carrito')
    return render(request, 'cliente/carrito.html',{'productos': productos})

def agregarCarrito(request, producto_id):
    carrito= request.session.get('carrito',[])
    if producto_id not in carrito:
        carrito.append(producto_id)
    request.session['carrito']= carrito
    return redirect('frontend_carrito')

def eliminarCarrito(request, producto_id):
    carrito= request.session.get('carrito',[])
    if producto_id in carrito:
        carrito.remove(producto_id)
    request.session['carrito']= carrito
    return redirect('frontend_carrito')

def frontend_checkout(request):
    carrito = request.session.get('carrito', [])
    productos = Variante_p.objects.filter(id__in=carrito)
    total = sum([p.producto.precio_base for p in productos])
    return render(request, 'cliente/checkout.html', {'productos': productos, 'total': total})

def frontend_contacto(request):
    """Vista para la página de contacto"""
    return render(request, 'cliente/contacto.html')

def frontend_login(request):
    # """Vista para el login del frontend"""
    # return render(request, 'cliente/login.html')
    if request.method == 'POST':
        formulario= loginn(request.POST)
        if formulario.is_valid():
            correo= formulario.cleaned_data['correo']
            contrasenia= formulario.cleaned_data['contrasenia']
            try:
                usuario= Usuario.objects.get(correo=correo)
                if(usuario.verificar(contrasenia)):
                    ##Login Exitoso
                    #return render(request,'paginas/home_vendedor.html', {'usuario': usuario})
                    request.session['usuario']= correo
                    return redirect('frontend_catalogoVendedor')
                else:
                    alerts.error(request, 'Contraseña incorrecta')
            except Usuario.DoesNotExist:
                alerts.error(request, 'Usuario no encontrado')
    else:
        formulario= loginn()
    return render(request, 'cliente/login.html', {'formulario': formulario})






def frontend_perfil(request):
    """Vista para el perfil de usuario"""
    return render(request, 'cliente/perfil.html')

def frontend_personaliza(request):
    """Vista para personalización de productos"""
    return render(request, 'cliente/personaliza.html')

def frontend_signin(request):
    # """Vista para registro de usuarios"""
    # return render(request, 'cliente/signin.html')
    if request.method == 'POST':

        form= Registro(request.POST)
        if form.is_valid():
            usuario= Usuario(
                correo=form.cleaned_data['correo'],
                contrasenia=form.cleaned_data['contrasenia'],
                telefono= form.cleaned_data['telefono'],
            )
            request.session['usuario']= usuario.correo
            usuario.save()
            return redirect('frontend_catalogoVendedor')
        else:
            form = Registro()

        return render(request, 'paginas/registro.html', {'form': form})
    
    else:
        form = Registro()
        return render(request, 'cliente/signin.html', {'form': form})

def frontend_sobre(request):
    """Vista para la página sobre nosotros"""
    return render(request, 'cliente/sobre.html')
