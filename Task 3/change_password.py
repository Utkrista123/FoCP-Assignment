def change_pwd():
    import getpass
    import codecs
    def get_user_name(): # Prompts user for username
        '''Taking input the for username.'''
        while True:
            user = input("Enter your user name: ")
            if check_user_name(user) == True:
                break
            else:
                pass
        
        return user # Return user details

    def check_user_name(user, file_content = "passwd.txt"): # Check if user exists in passwd file
        '''Checks to see if the entered username is valid.'''
        with open(file_content,"r") as file:
            content_list = [line.strip().split(":") for line in file]
            for i in content_list:
                if i[0] == user:
                    return True
                
            else: # User does not exist
                print("The user doesn't exist. Nothing was changed!!!")
                return False
            
    def decode_password(user_name, file_content = "passwd.txt"):
        '''Decode the password.'''
        with open(file_content,"r") as file:
            content_list = [line.strip().split(":") for line in file]
            for i in content_list:
                if i[0] == user_name:
                    decrypted_password = codecs.decode(i[2], "rot_13")
        return decrypted_password
            
    def get_password(d_password):
        '''Prompting user to enter a new password and confirm it.'''
        while True:
            current_password = getpass.getpass("Enter you current password: ")
            if current_password == d_password:
                break
            else:
                print("Invalid password!!! Please try again.")
                pass 
        
        while True:
            new_password1 = getpass.getpass("Enter a new password: ")
            new_password1 = encode_password(new_password1)
            new_password2 = getpass.getpass("Confirm the new password: ")
            new_password2 = encode_password(new_password2)
            if new_password1 != new_password2:
                print("\nPasswords do not match.")
                continue
            else:
                break
        return new_password1, new_password2

    def encode_password(pwd): 
        '''Encrypting the password.'''
        encrypted_password = codecs.encode(pwd, "rot_13") # Encrypt password using rot13
        return(encrypted_password)
            
    def change_password(user_name, n1_password,file_content = "passwd.txt"):
        '''Changes the users password.'''
        with open(file_content,"r") as file:
            content_list = [line.strip().split(":") for line in file]
            new_list = []
            for i in content_list:
                if i[0] == user_name:
                    i.remove(i[2]) # remove third element from the list
                    i.insert(2, n1_password) # insert new value in third element
                new_line = ":".join(i)
                new_list.append(new_line)

        with open(file_content,"w") as file:
            for line in new_list:
                file.write(line + "\n")

    # Main part of the program
    if __name__ != "__main__":
        user_name = get_user_name()
        d_password = decode_password(user_name)
        n1_password, n2_password = get_password(d_password)
        change_password(user_name, n1_password,file_content = "passwd.txt")