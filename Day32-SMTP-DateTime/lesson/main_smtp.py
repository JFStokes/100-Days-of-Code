import smtplib


my_email = 'joshua.f.stokes.mil@gmail.com'
password = 'cgfhzcjcgcazjvoo'
to_email = 'joshua.stokes1617@yahoo.com'


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_email,
        msg='Subject:Hello\n\nThis is the body of my email.'
    )