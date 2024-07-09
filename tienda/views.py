# Django Imports
from django.shortcuts import render
from django.contrib.auth.models import User
import decimal

# Proyect Imports
from productos.models import Producto
from tienda.models import Venta, Detalle_Venta
from tienda.forms import RealizarPedido, DatosInvitado

def tienda(request, param_int=0, param_str=None):
    # View de la tienda de producto
    def obtener_carrito(id_usuario):
        """ Función que obtiene el carrito de compras, acumula los productos agregados y los muestra
        en una tabla, con el precio, cantidad comprada y precio total.
        El if principal de la función divide a los usuarios registrados y no registrados"""
        if request.user.is_authenticated:
            venta = Venta.objects.filter(id_usuario = id_usuario, venta_finalizada = False).last()
            detalle_venta = Detalle_Venta.objects.filter(id_venta = venta)
            lista_prd = []
            for x in detalle_venta:
                lista_1 = [
                    str(x.id_producto),
                    x.cant_vendida,
                    str(x.precio_unitario),
                    int(venta.id),
                    str(venta.precio_total),
                ]
                lista_prd.append(lista_1)

            return lista_prd
        else:
            venta = Venta.objects.filter(id_usuario = id_usuario, venta_finalizada = False).last()
            detalle_venta = Detalle_Venta.objects.filter(id_venta = venta)
            lista_prd = []
            for x in detalle_venta:
                lista_1 = [
                    str(x.id_producto),
                    x.cant_vendida,
                    str(x.precio_unitario),
                    int(venta.id),
                    str(venta.precio_total),
                ]
                lista_prd.append(lista_1)

            return lista_prd
    def realizar_compra(id_usuario, precio_final, datos_formulaio_venta):
        # Obtengo el estado de la ultima venta registrada (si existe)
        crear_venta = Venta.objects.filter(id_usuario = id_usuario).last()
        if crear_venta != None:
            try:
                # Primer caso, que crea una venta, 
                # cuando venta finalizada o procesada están True.
                if (crear_venta.venta_finalizada == True) and (crear_venta.venta_procesada == True):
                    # Agrego el dato del usuario para que se cree
                    # una nueva venta.
                    venta = Venta(
                        id_usuario = id_usuario,
                    )
                    venta.save()
                    # Busco la venta recien creada.
                    info_venta = Venta.objects.filter(
                            id_usuario = id_usuario, 
                            venta_finalizada = False, 
                            venta_procesada = False,
                    ).last()
                    # Luego guardo la compra en la nueva venta.
                    detall_venta = Detalle_Venta(
                        id_venta = info_venta, 
                        id_producto = datos_formulaio_venta['producto'], 
                        cant_vendida = datos_formulaio_venta['cantidad'],
                        precio_unitario = precio_final
                    )
                    detall_venta.save()
                    # Agrego el precio a la venta.
                    venta.precio_total += precio_final
                    venta.save()
                elif (crear_venta.venta_finalizada == False) and (crear_venta.venta_procesada == False):
                    # Guardola compra en la venta.
                    detall_venta = Detalle_Venta(
                        id_venta = crear_venta, 
                        id_producto = datos_formulaio_venta['producto'], 
                        cant_vendida = datos_formulaio_venta['cantidad'],
                        precio_unitario = precio_final
                    )
                    detall_venta.save()
                    # Agrego el precio a la venta.
                    crear_venta.precio_total += decimal.Decimal(precio_final)
                    crear_venta.save()
                elif (crear_venta.venta_finalizada == True) and (crear_venta.venta_procesada == False):
                    # Busco si el usuario tiene 
                    # venta finalizada pero no procesada.
                    # Y la cambio a False
                    crear_venta.venta_finalizada = False
                    crear_venta.save()
                    # Agrego el nuevo producto
                    detall_venta = Detalle_Venta(
                        id_venta = crear_venta, 
                        id_producto = datos_formulaio_venta['producto'], 
                        cant_vendida = datos_formulaio_venta['cantidad'],
                        precio_unitario = precio_final
                    )
                    detall_venta.save()
                    # Agrego el precio a la venta.
                    crear_venta.precio_total += decimal.Decimal(precio_final)
                    crear_venta.save()
                else:
                    print('Error de indice 1')
            except:
                print('Error de indice 2')
        else:
            venta = Venta(
                id_usuario = id_usuario,
            )
            venta.save()
            # Busco la venta recien creada.
            info_venta = Venta.objects.filter(
                    id_usuario = id_usuario,
                    venta_finalizada = False,
                    venta_procesada = False,
            ).last()
            # Luego guardo la compra en la nueva venta.
            detall_venta = Detalle_Venta(
                id_venta = info_venta,
                id_producto = Producto.objects.get(id=datos_formulaio_venta['producto']),
                cant_vendida = datos_formulaio_venta['cantidad'],
                precio_unitario = precio_final
            )
            detall_venta.save()
            # Agrego el precio a la venta.
            venta.precio_total += precio_final
            venta.save()
    def realizar_compra_invitado(id_usuario, precio_final, datos_formulaio_venta):
        # Paso el usuario como session para que se genere la session_key
        request.session['usuario'] = str(User.objects.get(username= 'invitado'))
        # Obtengo el estado de la ultima venta registrada (si existe)
        crear_venta = Venta.objects.filter(id_usuario = id_usuario, nombre_inv = request.session.session_key).last()
        if crear_venta != None:
            try:
                # Primer caso, que crea una venta, 
                # cuando venta finalizada o procesada están True.
                if (crear_venta.venta_finalizada == True) and (crear_venta.venta_procesada == True):
                    # Agrego el dato del usuario para que se cree
                    # una nueva venta.
                    venta = Venta(
                        id_usuario = id_usuario,
                        nombre_inv = request.session.session_key,
                    )
                    venta.save()
                    # Busco la venta recien creada.
                    info_venta = Venta.objects.filter(
                            id_usuario = id_usuario, 
                            nombre_inv = request.session.session_key,
                            venta_finalizada = False, 
                            venta_procesada = False,
                    ).last()
                    # Luego guardo la compra en la nueva venta.
                    detall_venta = Detalle_Venta(
                        id_venta = info_venta, 
                        id_producto = datos_formulaio_venta['producto'], 
                        cant_vendida = datos_formulaio_venta['cantidad'],
                        precio_unitario = precio_final
                    )
                    detall_venta.save()
                    # Agrego el precio a la venta.
                    venta.precio_total += precio_final
                    venta.save()
                elif (crear_venta.venta_finalizada == False) and (crear_venta.venta_procesada == False):
                    # Guardola compra en la venta.
                    detall_venta = Detalle_Venta(
                        id_venta = crear_venta, 
                        id_producto = datos_formulaio_venta['producto'], 
                        cant_vendida = datos_formulaio_venta['cantidad'],
                        precio_unitario = precio_final
                    )
                    detall_venta.save()
                    # Agrego el precio a la venta.
                    crear_venta.precio_total += decimal.Decimal(precio_final)
                    crear_venta.save()
                elif (crear_venta.venta_finalizada == True) and (crear_venta.venta_procesada == False):
                    # Busco si el usuario tiene 
                    # venta finalizada pero no procesada.
                    # Y la cambio a False
                    crear_venta.venta_finalizada = False
                    crear_venta.save()
                    # Agrego el nuevo producto
                    detall_venta = Detalle_Venta(
                        id_venta = crear_venta, 
                        id_producto = datos_formulaio_venta['producto'], 
                        cant_vendida = datos_formulaio_venta['cantidad'],
                        precio_unitario = precio_final
                    )
                    detall_venta.save()
                    # Agrego el precio a la venta.
                    crear_venta.precio_total += decimal.Decimal(precio_final)
                    crear_venta.save()
            except:
                print('Error de indice 2')
        else:
            venta = Venta(
                id_usuario = id_usuario,
                nombre_inv = request.session.session_key,
            )
            venta.save()
            # Busco la venta recien creada.
            info_venta = Venta.objects.filter(
                    id_usuario = id_usuario, 
                    nombre_inv = request.session.session_key,
                    venta_finalizada = False, 
                    venta_procesada = False,
            ).last()
            # Luego guardo la compra en la nueva venta.
            detall_venta = Detalle_Venta(
                id_venta = info_venta, 
                id_producto = datos_formulaio_venta['producto'], 
                cant_vendida = datos_formulaio_venta['cantidad'],
                precio_unitario = precio_final
            )
            detall_venta.save()
            # Agrego el precio a la venta.
            venta.precio_total += precio_final
            venta.save()
    def finalizar_pedido(parametro_int, parametro_str):
        if parametro_int == 1 and parametro_str == 'safe':
            finalizar_pedido = Venta.objects.filter(
                id_usuario = dato_usuario,
            ).last()
            if (finalizar_pedido.venta_procesada == False) and (finalizar_pedido.venta_finalizada == False):
                finalizar_pedido.venta_finalizada = True
                finalizar_pedido.save() 
    def eliminar_producto(parametro_int, parametro_str):
        if parametro_str != 'safe':
            # Condicion para borrar items de el "carrito"
            # En caso de que el request se esté refiriendo 
            # a otro pedido pongo la palabra safe como seguridad

            # Traigo el N° Venta de
            venta_a_borrar = Venta.objects.filter(id=parametro_int).last()
            producto = Producto.objects.filter(
                nombre_prd=parametro_str,
                ).last()
            borrar_art = ''
            try:
                borrar_art = Detalle_Venta.objects.filter(
                    id_venta=venta_a_borrar, 
                    id_producto=producto.id,
                    ).last()
                # Antes de borrar el producto, resto
                # el valor del producto al valor total de la compra.
                venta_a_borrar.precio_total -= borrar_art.precio_unitario
                venta_a_borrar.save()
                borrar_art.delete()
            except:
                print('clase nontype')
    
    # Cuando la pagina pide un POST entra al if.
    if request.method == "POST":
        if request.user.is_authenticated:
            # Traigo el usuario que esté logueado
            dato_usuario = User.objects.get(username= request.user.username)
            formularioVenta = RealizarPedido(request.POST)
            # Si se llenaron todos los casilleros del formulario entra al if.
            if formularioVenta.is_valid():
                # Paso los datos del formulario a una variable.
                infoFormulario = formularioVenta.cleaned_data
                # Divido en una lista para obtener los datos del prod.
                # Obtengo elprecio del producto        
                prd_elegido = Producto.objects.filter(nombre_prd= str(infoFormulario['producto']))
                # Calculo el precio de lo que compro el usuario.
                precio_final = (infoFormulario['cantidad'])*float(prd_elegido[0].precio)*0.9
                
                # llama a la funcion que agrega los productos a la DB
                realizar_compra(dato_usuario,precio_final,infoFormulario)
                    
                formularioVenta = RealizarPedido()

                context = {
                    'formularioVenta': formularioVenta,
                    'lista_ventas': obtener_carrito(dato_usuario),
                }

                return render(request, "tienda/tienda.html", context)
            else:
                formularioVenta = RealizarPedido()
                
                context = {
                    'formularioVenta': formularioVenta,
                    'lista_ventas': obtener_carrito(dato_usuario),
                }

                return render(request, "tienda/tienda.html", context)
        else:
            # Traigo el usuario invitado.
            dato_usuario = User.objects.get(username= 'invitado')
            formularioVenta = RealizarPedido(request.POST)
            # Si se llenaron todos los casilleros del formulario entra al if.
            if formularioVenta.is_valid():
                # Paso los datos del formulario a una variable.
                infoFormulario = formularioVenta.cleaned_data
                # Divido en una lista para obtener los datos del prod.
                # Obtengo elprecio del producto        
                prd_elegido = Producto.objects.filter(nombre_prd= str(infoFormulario['producto']))
                # Calculo el precio de lo que compro el usuario.
                precio_final = (infoFormulario['cantidad'])*float(prd_elegido[0].precio)*0.9
                
                # llama a la funcion que agrega los productos a la DB
                realizar_compra_invitado(dato_usuario, precio_final, infoFormulario)

            formularioInvitado = DatosInvitado(request.POST)
            if formularioInvitado.is_valid():
                infoFormulario = formularioInvitado.cleaned_data
                print(type(infoFormulario['nombre']))
                actualizar_venta = Venta.objects.filter(
                    id_usuario = dato_usuario, 
                    nombre_inv = request.session.session_key,
                    ).last()
                actualizar_venta.nombre_inv = infoFormulario['nombre']
                actualizar_venta.apellido_inv = infoFormulario['apellido']
                actualizar_venta.telefono_inv = infoFormulario['teléfono']
                actualizar_venta.save()

                del request.session['usuario']

                # funcion para finalizar el pedido con el boton "Finalizar Pedido"
                finalizar_pedido(param_int, param_str)

            formularioVenta = RealizarPedido()
            formularioInvitado = DatosInvitado()
                
            context = {
                'formularioVenta': formularioVenta,
                'lista_ventas': obtener_carrito(dato_usuario),
                'formularioInvitado': formularioInvitado,
            }

            return render(request, "tienda/tienda.html", context)
    else:
        if request.user.is_authenticated:
            # Traigo el usuario que esté logueado
            dato_usuario = User.objects.get(username= request.user.username)
            # funcion para eliminar un producto de la lista de comprados.
            eliminar_producto(param_int, param_str)
            finalizar_pedido(param_int, param_str)
           
            formularioVenta = RealizarPedido()
            
            context = {
                'formularioVenta': formularioVenta,
                'lista_ventas': obtener_carrito(dato_usuario),
            }

            return render(request, "tienda/tienda.html", context)
        else:
            # usuario invitado por defecto
            dato_usuario = User.objects.get(username= 'invitado')
            # funcion para eliminar un producto de la lista de comprados.
            eliminar_producto(param_int, param_str)

            formularioVenta = RealizarPedido()
            formularioInvitado = DatosInvitado()
            
            context = {
                'formularioVenta': formularioVenta,
                'lista_ventas': obtener_carrito(dato_usuario),
                'formularioInvitado': formularioInvitado,
            }

            return render(request, "tienda/tienda.html", context)
        

from .models import Producto

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages
from .models import Venta, Detalle_Venta
from .forms import AgregarProductoForm

class AgregarProductoCarritoView(View):
    def post(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        cantidad = request.POST.get('cantidad', 1)  # Obtener cantidad del formulario
        carrito = self.request.session.get('carrito', {})
        
        # Agregar producto al carrito o actualizar cantidad
        if producto_id in carrito:
            carrito[producto_id]['cantidad'] += int(cantidad)
        else:
            carrito[producto_id] = {
                'id_producto': producto_id,
                'nombre': producto.nombre,
                'precio_unitario': float(producto.precio),
                'cantidad': int(cantidad),
            }
        
        self.request.session['carrito'] = carrito
        messages.success(request, f'{producto.nombre} fue agregado al carrito.')
        return redirect('ver_carrito')  # Redirigir a la vista del carrito

from django.shortcuts import render
from django.views import View
from .models import Detalle_Venta

class VerCarritoView(View):
    def get(self, request):
        # Obtener los detalles de venta del carrito para el usuario actual
        items_carrito = Detalle_Venta.objects.filter(id_venta__id_usuario=request.user)

        # Calcular el precio total por cada ítem en el carrito
        for item in items_carrito:
            item.precio_total_item = item.precio_unitario * item.cant_vendida

        # Calcular el precio total del carrito sumando todos los precios totales de los ítems
        total_carrito = sum(item.precio_total_item for item in items_carrito)

        context = {
            'items_carrito': items_carrito,
            'total_carrito': total_carrito,
        }

        return render(request, 'tienda/ver_carrito.html', context)


class ActualizarCantidadProductoView(View):
    def post(self, request, producto_id):
        carrito = self.request.session.get('carrito', {})
        nueva_cantidad = int(request.POST.get('cantidad'))
        
        if producto_id in carrito:
            carrito[producto_id]['cantidad'] = nueva_cantidad
            self.request.session['carrito'] = carrito
            messages.success(request, f'Cantidad actualizada para {carrito[producto_id]["nombre"]}.')
        else:
            messages.error(request, 'El producto no existe en el carrito.')
        
        return redirect('ver_carrito')

class ProcesarCompraView(View):
    def post(self, request):
        carrito = self.request.session.get('carrito', {})
        
        if not carrito:
            messages.error(request, 'No hay productos en el carrito.')
            return redirect('ver_carrito')
        
        # Crear la venta
        venta = Venta.objects.create(
            id_usuario=request.user,  # Aquí debes ajustar cómo obtienes el usuario actual
            precio_total=sum(item['precio_unitario'] * item['cantidad'] for item in carrito.values()),
            venta_procesada=False,
            venta_finalizada=False
        )
        
        # Agregar detalles de la venta
        for item in carrito.values():
            detalle_venta = Detalle_Venta.objects.create(
                id_venta=venta,
                id_producto=item['id_producto'],
                cant_vendida=item['cantidad'],
                precio_unitario=item['precio_unitario']
            )
        
        # Limpiar carrito después de procesar la compra
        del request.session['carrito']
        messages.success(request, 'Compra procesada correctamente.')
        return redirect('pagina_de_inicio')  # Redirigir a la página de inicio o a una confirmación de compra
    
# tienda/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta
from .forms import RealizarPedidoForm, ModificarVentaForm

def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'tienda/listar_ventas.html', {'ventas': ventas})

def modificar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        form = ModificarVentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('listar_ventas')
    else:
        form = ModificarVentaForm(instance=venta)
    return render(request, 'tienda/modificar_venta.html', {'form': form})

def eliminar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        venta.delete()
        return redirect('listar_ventas')
    return render(request, 'tienda/confirmar_eliminar_venta.html', {'venta': venta})

from django.shortcuts import render
from django.http import HttpResponse
from .forms import RealizarPedidoForm

def nueva_venta(request):
    if request.method == 'POST':
        form = RealizarPedidoForm(request.POST)
        if form.is_valid():
            # Procesar el formulario aquí
            form.save()
            return HttpResponse('Venta realizada correctamente.')
    else:
        form = RealizarPedidoForm()
    
    return render(request, 'nueva_venta.html', {'form': form})































