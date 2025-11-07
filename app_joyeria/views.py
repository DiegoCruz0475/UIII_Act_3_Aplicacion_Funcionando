from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Proveedor, Venta # Proveedor ahora solo se importa para fines de registro en admin

def inicio_joyeria(request):
    return render(request, 'inicio.html')

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        material = request.POST.get('material')
        precio = request.POST.get('precio')
        tipo = request.POST.get('tipo')
        stock = request.POST.get('stock')
        # id_proveedor eliminado

        producto = Producto(
            nombre=nombre,
            material=material,
            precio=precio,
            tipo=tipo,
            stock=stock,
            # id_proveedor ya no se asigna
        )
        producto.save()
        return redirect('ver_productos')
    # proveedores = Proveedor.objects.all() # Ya no se necesita
    return render(request, 'producto/agregar_producto.html') # Se eliminó el contexto 'proveedores'

def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/ver_productos.html', {'productos': productos})

def actualizar_producto(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.material = request.POST.get('material')
        producto.precio = request.POST.get('precio')
        producto.tipo = request.POST.get('tipo')
        producto.stock = request.POST.get('stock')
        # id_proveedor eliminado
        producto.save()
        return redirect('ver_productos')
    # proveedores = Proveedor.objects.all() # Ya no se necesita
    return render(request, 'producto/actualizar_producto.html', {'producto': producto}) # Se eliminó el contexto 'proveedores'

def borrar_producto(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})

# Vistas para Proveedor (PENDIENTE y sin relación con Producto)
def agregar_proveedor(request):
    pass
def ver_proveedores(request):
    pass
def actualizar_proveedor(request, id_proveedor):
    pass
def borrar_proveedor(request, id_proveedor):
    pass

# Vistas para Venta (PENDIENTE)
def agregar_venta(request):
    pass
def ver_ventas(request):
    pass
def actualizar_venta(request, id_venta):
    pass
def borrar_venta(request, id_venta):
    pass