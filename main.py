from project.webdata import return_data
from project.mail import send_email

data = return_data()
print(data)
send_email(data['product_name'], data['price'])