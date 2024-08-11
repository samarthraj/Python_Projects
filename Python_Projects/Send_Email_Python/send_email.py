#smtp is a protocol to send an email (simple mail transfer protocol)
import smtplib

#Server Address and Port Number will change for different services ex: gamil.  

#server object 
server = smtplib.SMTP('smtp.gamil.com', 587)


#befire logging in we need to create a connection and make sure its secure 
#tls - transfer layer security
server.starttls()

server.login('sampythonprojects@gmail.com', 'sam@123') 
server.sendmail('sampythonprojects@gmail.com', 'samraju@gmail.com', 'Hi, Sending you an email from python code') 
print('Mail Sent')

