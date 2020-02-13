import string
import random


user_choice = None
while user_choice == None:
    try:
       user_choice = int(input('How many characters you want to have in your password:'))
       if user_choice < 6:
           print('Password must be with 6 characters at least')
           user_choice = None
    except ValueError:
        user_choice = None

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(1,user_choice+1))
print('Your password is {}'.format(password))
