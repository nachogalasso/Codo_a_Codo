# Para hacerlo funcionar tengo que ir a una dirección de email y completar el doble factor de autenticación
# generar una password para app
# luego crear una function para enviar el email
# importamos el modulo del email, luego tenemos que ingrear las password que generamos para las app
from email.message import EmailMessage
from app_pass import password
import ssl
import smtplib

# Ahora tenemos que crear un par de variables para que funcione nuestro email sender
# en el email tenemos que poner el mail que vamos a utilizar
email_sender = 'backup.oficiales@gmail.com'
email_password = password

# especificar quien recibe el email
email_reciever = 'ignaciogalasso82@gmail.com'

# tenemos que especificar el título que va a tener nuestro email
subject = 'Designaciones fecha'
# creamos el body es donde irá el mensaje del mail
body = """

22/10 COR - BSAS	
	
R	Vasyl
U	ROS1
HL	COR1
LJ	Pela
SJ	ROS2
FJ	COR2
BJ	Herno

"""

# creamos una instancia del Email Message
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)


# Ahora tenemos que crear un contexto y para ello tendremos que importar SSL y SMTB library.
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())