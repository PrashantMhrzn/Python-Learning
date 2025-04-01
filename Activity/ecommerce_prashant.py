# ecommerce
# Register or Login
# choice - login, register
# if register,get username, password and usertype(buyer, seller), store the username in a file
# if login, get username and password, check if it exist in the file, login success if not invalid
# if user is a buyer: show them option: 1.View product, 2. buy product(billing option)
# if user is a seller: show them option: 1.View their product, 2.Add product(name, description, price) store it in a file 
# {
#   "name":"product1",
#   "description":"descrioion1",
#   "price":20,
#   "seller":"ram"
# },
# {
#   "name":"product2",
#   "description":"descrioion2",
#   "price":20,
#   "seller":"hari"
# }

def register():
    # when registering, we create two files one for username and other for money with the same username
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    f = open('ecommerce_users.txt', 'a')
    f.write(f"{username}:{password},")
    f.close()
    type = input('What type of user are you?(buyer/seller): ').lower()
    m = open('user_type.txt', 'a')
    m.write(f"{username}:{type},")
    m.close()

def add_product(**kwargs):
    f = open('products.txt', 'a')
    data = kwargs
    f.write(f'{str(data)},')
    f.close()

def view_products():
    f = open('products.txt', 'r')
    r = f.read()
    print(r)
    f.close()

def buy_product(product_name):
    f = open('products.txt', 'r')
    r = f.read()
    products = r.split(',')
    for i in products:
        s = i.strip('{}')
        product = s.split(',')
        for j in product:
            if j[1] == product_name:
                pass
    pass

def login():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    f = open('ecommerce_users.txt', 'r')
    data = f.read()
    unit = data.split(',')
    is_logged = False
    for i in unit:
        uname = i.split(':')
        if uname[0] == username and uname[1] == password:
            # if uname and pw is not what we entered, then skip to the next value cause is_logged is False
            is_logged = True

    if is_logged:
        print('Logged in')
        f = open('user_type.txt', 'r')
        data = f.read()
        unit = data.split(',')
        for i in unit:
            uname = i.split(':')
            if uname[0] == username:
                if uname[1] == 'seller':
                    print('You are a SELLER')
                    option = input('1.View Your Products\n2.Add Product\n>')
                    if option == '1':
                        view_products()
                    elif option == '2':
                        product_name = input('Enter product name: ')
                        product_description = input('Enter product description: ')
                        product_price = input('Enter product price: ')
                        add_product(product_name=product_name, product_description=product_description, product_price=product_price)
                elif uname[1] == 'buyer':
                    print('You are a BUYER')
                    option = input('1.View Products\n2.Buy Product\n>')
                    if option == '1':
                        view_products()
                    elif option == '2':
                        buy_product()
            # if uname and pw is not what we entered, then skip to the next value cause is_logged is False
        
    else:
        print('Invalid Credentails!')


print('***WELCOME TO OUR BUSINESS***')
choice = input('1.Register\n2.Login\n>')
if choice == '1':
    register()
elif choice == '2':
    login()
else:
    print('Not a valid choice!')