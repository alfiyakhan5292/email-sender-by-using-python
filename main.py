import smtplib as s 

ob =s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('your email','your password')
subject="test python"
body="this is a test mail sent from python"
massage="Subject: {}\n\n{}".format(subject,body)
listadd=["receiver email address" ]
ob.sendmail('your email',listadd,massage)
print("send mail")
ob.quit()

