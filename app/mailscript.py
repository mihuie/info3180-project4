import smtplib  

def sendcode(toaddr, code):
  fromname = 'Michael Huie'
  subject = 'Confirmation code'
#   url = 'michael-project-4.herokuapp.com/signup/confirm/'+code
  url = 'http://mihuieinfo3180-188841.use1.nitrousbox.com:8080/signup/confirm/'+code
  msg = 'Thank you for signing up. Please follow the link to validate email address. \n'+url 
  fromaddr = 'huie.michael@gmail.com'  

  header  = 'From: %s\n' % fromaddr
  header += 'To: %s\n' % toaddr
  header += 'Subject: %s\n\n' % subject
  messagetosend = header + msg


  # Credentials (if needed)  
  username = 'huie.michael@gmail.com'  
  password = 'aofbguskyevglfvx'

  # The actual mail send  
  server = smtplib.SMTP('smtp.gmail.com:587')  
  server.starttls()  
  server.login(username,password)  
  server.sendmail(fromaddr, toaddr, messagetosend)  
  server.quit()

