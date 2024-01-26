def add_profile():
   import codecs
   import getpass

   def Add_user(): # Prompts user for username, real name, password and validates if the username is unique   
      '''Taking input the for username, realname and password.'''
      while True:
         user_name = input("Enter a username: ")
         if check_user_name(user_name) == True:
            break
         else:
            pass

      real_name = input("Enter your real name: ")
      password = getpass.getpass("Enter a password: ")
      print("Your profile has been sucessfully been saved.")
      return user_name, real_name, password # Return user details

   def check_user_name(user_name, file_name = 'passwd.txt'): # Check if user exists in passwd file
      '''Checks to see if the entered username is valid.'''
      with open(file_name, 'r') as file:
         file_content = [line.strip().split(":") for line in file]
         
         for i in file_content:
            if i[0] == user_name:
                  print("The user already exist. Please choose another one.")
                  return False
         return True # User does not exist

   def encode_password(pwd): 
      '''Encrypting the password'''
      encrypted_password = codecs.encode(pwd, "rot_13") # Encrypt password using rot13
      return(encrypted_password)

   def save_to_file(u_name, r_name, encoded_pwd): # Append user details to file
      '''Saving information into file.'''
      with open('passwd.txt', 'a') as file:
         file.write(f'{u_name}:{r_name}:{encoded_pwd}\n')

   # Main part of the program
   if __name__ != "__main__": 
      u_name, r_name, pwd = Add_user()
      encoded_pwd = encode_password(pwd)
      save_to_file(u_name, r_name, encoded_pwd)