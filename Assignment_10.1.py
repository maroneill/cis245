import os, csv

def get_user_info():
    global user_name, user_address, user_number
    """Gets the user's name address and number"""
    user_name = input("\t What is your name?: ")
    user_address = input("\t What is your address?: ")
    user_number = input("\t What is your phone number?: ")


def save_location():
    """Asks for absolute path to save file and handles windowserrors"""
    global filename
    filename = input("What would you like to name the file?: ")
    while True:
        absolute_path = input("Enter the absolute path to the folder you'd like to store this file in: ")
        try:
            os.listdir(absolute_path)
            return absolute_path
        except WindowsError:
            print("Oops! That's not a valid file path. Try again...")
    



print("Hello, let's save a file.")

get_user_info()

save_location()

files_to_write = [user_name, user_address, user_number]

filename_csv = str(filename + '.csv')

with open(filename_csv, 'w') as fileHandle:
    fileHandle.write(user_name)
    fileHandle.write(user_address)
    fileHandle.write(user_number)
