import yagmail

user = ''
app_password = ""
to = ''

subject = 'New item price notification'


def send_email(product_name, product_price):
    content = f'This is a product price notification!\nProduct: {product_name}\nCurrent price: {product_price}'
    with yagmail.SMTP(user, app_password) as yag:
        yag.send(to, subject, content)
        print('Email send successfully')
