#Sending Mail using Python
#!/usr/bin/python3
import smtplib
#starting smtp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
#Loggging in to ur account
s.login("kiranrocks5005@gmail.com", "STSAPOKIVA") 
message = "hi"
s.sendmail("kiranrocks5005@gmail.com", "kiranrocks5005@gmail.com",message)
s.quit()
