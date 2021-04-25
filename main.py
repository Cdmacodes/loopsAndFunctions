


database = {} # A database for dictionary


# initializing the system
import random # to generate account numbers at random
import time

def init():

    print("************")
    time.sleep(1)
    print("Welcome to bankJMS")
    time.sleep(1)



    confirm_account_status = int(input("Do you have an account with us?: 1 (yes) 2(no) \n"))

    if confirm_account_status == 1:

            login()

    elif confirm_account_status == 2:

            register()
    else:
            print("You have selected an invalid option.")
            init()


def login():

    print("Please login to your account")


    request_account_number_from_user = int(input("Now log in with  your account number? \n"))
    time.sleep(1)
    print("Please wait")
    time.sleep(1)
    password = input("Enter your password \n")

    for accountNumber,userDetails in database.items():
            if accountNumber == request_account_number_from_user:
                if userDetails[3] == password:
                    bankOperation(userDetails)


    print("Invalid account or password")
    login()



def register():
    print("Please register here")
    time.sleep(1)

    email = input("Input your email address here: \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your surname?\n")
    password = input("Enter your password here\n")

    account_number = generateAccountNumber()

    database[account_number] = [ first_name, last_name, email, password ]


    print("Your account number has been created")
    time.sleep(1)
    print("*************")
    time.sleep(1)
    print("Your account number is:  %d" % account_number)
    time.sleep(1)
    print("Your account number is personal to you only, please keep it safe")
    time.sleep(1)
    print("*****************")

    login()

def bankOperation(user):

    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do today? (1) deposit (2) withdrawal (3) logout (4) Exit \n"))

    if selected_option == 1:

        depositOperation()
    elif selected_option == 2:

        withdrawalOperation()
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")
        bankOperation(user)




def withdrawalOperation():
    print("Withdrawal")

def depositOperation():
    print("Deposit")

def generateAccountNumber():

    return random.randrange(1111111111,9999999999)

def logout():
    login()



init()