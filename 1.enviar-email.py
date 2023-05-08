import os
from email.message import EmailMessage
'''Se utiliza para crear mensajes de correo electronico con contenido
y encabezados personalizados.
Se envian utilizando un objeto SMTP o SMTP_SSL de smtplib'''
import ssl
'''proporciona acceso a funciones de seguridad de la capa de transporte
TLS y su predecesor, el protocolo de capa de sockets seguros SSL.
Se utiliza para agregar seguridad a las conexiones de red al crifrar 
los datos transmitidos entre dos puntos.'''
import smtplib
"""Este modulo define un objeto de sesion de cliente SMTP que se puede
utilizar para enviar correo a cualquier maquina de internet con un demonio
de escucha SMTP O ESMTP. Proporciona funciones para enviar correos
electronicos utilizando el protocolo simple de transferencia de correo
SMTP."""
import imghdr 
"""Este módulo determina el tipo de imagen de un archivo o secuencia 
de bytes. Proporciona una función llamada what() que puede tomar el 
nombre de un archivo o un objeto de archivo y devolver una cadena que 
describe el formato de la imagen."""







email_emisor = 'ejemplo@gmail.com'
email_contrasena = 'aqui va la contraseña de https://myaccount.google.com/apppasswords'

email_receptor = 'ejemplohotmail.es'

asunto = 'Asunto'
cuerpo = """
Texto plano
"""

em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)

# Adjuntar archivo
with open('varus.png', 'rb') as file: 
    file_data = file.read()
    file_tipo = imghdr.what(file.name)
    file_nombre = file.name
em.add_attachment(file_data, filename=file_nombre, subtype=file_tipo, maintype='image')

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    smtp.login(email_emisor, email_contrasena)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())