from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        # 1. Capturamos los datos que viajan desde el formulario HTML
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        servicio = request.POST.get('servicio')
        detalles = request.POST.get('detalles')
        
        # 2. Armamos el diseño del correo que vas a recibir tú
        asunto = f"Nueva solicitud de {nombre} - {servicio}"
        mensaje = f"Nombre: {nombre}\nTeléfono: {telefono}\nEmail: {email}\nServicio: {servicio}\n\nDetalles:\n{detalles}"
        
        try:
            # 3. Intentamos enviar el correo usando la configuración de tu settings.py
            send_mail(
                asunto,
                mensaje,
                settings.EMAIL_HOST_USER,  # El remitente (tu cuenta de Gmail)
                ['novasolutionshvac@gmail.com'],    # El destinatario (a donde quieres que llegue)
                fail_silently=False,
            )
            # Creamos un aviso de éxito que leerá el bloque {% if messages %} en tu HTML
            messages.success(request, "¡Tu mensaje ha sido enviado con éxito!")
            return redirect('contact')  # Redireccionamos para limpiar el formulario
            
        except Exception as e:
            # Si Gmail rechaza la conexión o hay un error, te lo mostrará en la pantalla
            messages.error(request, f"Hubo un error al enviar el correo: {e}")
            
    # Si la petición es un GET normal (cuando entran a la página por primera vez), solo muestra la vista
    return render(request, 'contact.html')