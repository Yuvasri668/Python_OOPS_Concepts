def login(login_page):
    def wrapper(user,password):
        if user=="admin" and password=="1234":
            print("Login Successfull")
            login_page(user,password)

        else:
            print("Login Failed")

    return wrapper
@login
def login_page(user,password):
    print("Welcome to the dashboard")

login_page("admin","1234")