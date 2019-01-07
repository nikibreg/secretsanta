
import smtplib
 
def send(msg, to):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("saidumlosantaclaus@gmail.com", "usaidumloesi")
    
    message = """Subject:Your Secret Santa Addressee\nFrom:Saidumlo Santa\n""" + msg
    server.sendmail("saidumlosantaclaus@gmail.com", to, message)
    server.quit()