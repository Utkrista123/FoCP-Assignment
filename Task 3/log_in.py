def log():    
    import codecs
    import getpass

    def get_user_name_and_password(): # Prompts user for username
        '''Taking input the for username.'''
        while True:
            user = input("Enter your user name: ")
            if check_user_name(user) == True:
                break
            else:
                pass
        password = getpass.getpass("Enter your password: ")
        
        return user, password # Return user details

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
                        decrypted_password = codecs.decode(i[2], "rot_13") # Decode the encrypted password using rot13
            return decrypted_password

    def check_info(d_pwd, passwd):  
        '''Compares decrypted password to entered password.'''  
        if d_pwd == passwd:
            print("You have sucessfully logged in.")
        else:
            print("Wrong password. Please try again.")
            user_name, passwd = get_user_name_and_password()
            d_pwd = decode_password(user_name)
            check_info(d_pwd, passwd)

    # Main part of the program
    if __name__ != "__main__": 
        user_name, passwd = get_user_name_and_password()
        d_pwd = decode_password(user_name)
        check_info(d_pwd, passwd)

