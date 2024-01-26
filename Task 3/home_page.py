import add_user
import log_in
import remove_user
import change_password

running = True
while running:
      print('''Please choose from the following options:-
            1) Log in 
            2) Add user
            3) Remove user
            4) Change password
            5) Exit ''')

      option = None
      option = input("Enter your option: ").lower()

      if option == 'log in':
            log_in.log()

      elif option == 'add user':
            add_user.add_profile()

      elif option == 'remove user':
            remove_user.remove_profile()

      elif option == 'change password':
            change_password.change_pwd()

      elif option == 'exit':
            print("Exiting....")
            running = False

      else:
            print("\nInvalid option. Please try again.")

print("Done")