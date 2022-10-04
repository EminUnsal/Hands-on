from ast import And
import time

contact = {}
def menu():
    time.sleep(1)
    print(""" Welcome to the phonebook application
    1. Find phone number
    2. Insert a phone number
    3. Delete a person from the phonebook
    4. Terminate""")
    giris = input("Select operation on Phonebook App (1/2/3/4) :  ")


    return giris

def phonebook():

    while True:
        giris=menu()
        if giris == '1':
            find_name = input('Find the phone number of : ')
            if find_name not in contact.keys():
                print("Couldn't find phone number of ",find_name )
            else:
                print(contact[find_name])
            time.sleep(1)
            print(" ")
        elif giris == '2':
            name = input('Insert name of the person : ')
            number =input('Insert phone number of the person : ')
            if number not in contact.values() and number.isnumeric() == True :
                contact.update({name:number})
                print ('Phone number of', name, 'is inserted into the phonebook')
            else:
                print('Invalid input format, cancelling operation ...')
            
            time.sleep(1)
            print(" ")
        elif giris == '3':
            delete_name = input("Whom to delete from phonebook :")
            if delete_name in contact.keys():
                contact.pop(delete_name)
                print(delete_name,' is deleted from the phonebook')
            else:
                print("Couldn't find phone number of ",delete_name)
            time.sleep(1)
        elif giris == '4':
            print('Exiting Phonebook')
            break
            time.sleep(1)
        else:
            print("Gecersiz giris!!")
    
print(phonebook())
print(contact)   

