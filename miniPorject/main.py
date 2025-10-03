def login():
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        with open("data.txt", "r") as file:
            data = file.readlines()
            for line in data:
                user, pwd = line.strip().split(",")
                if username == user and password == pwd:
                    print("Login successful!")
                    return True
            print("Invalid username or password.")
            return False
        
def register():
        username = input("Enter your desired username: ")
        password = input("Enter your desired password: ")
        with open("data.txt", "a") as file:
            file.write(f"{username},{password}\n")
        print("Registration successful!")
        return True
while True:
    log = input("Enter wether you want to login or register: ").lower()
    if log == "login":
        login()
        break
    elif log == "register":
        register()
        break
    else:
        print("Invalid option. Please enter 'login' or 'register'.")

   


    