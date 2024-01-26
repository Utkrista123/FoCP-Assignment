def remove_profile(): 
    def get_user_name(): # Prompts user for username
        '''Taking input the for username'''
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

    def remove_user(user_name):
        '''Removes a user from file and returns the updated list of users.'''
        with open("passwd.txt", "r") as file:
            content_list = [line.strip().split(":") for line in file]

            # Build new list with user removed 
            new_list = []
            for i in content_list:
                if i[0] != user_name:
                    new_line = ":".join(i)
                    new_list.append(new_line)

            print("You have sucessfully deleted your account.")
            return new_list # Return updated data
        
    def newfile(file_list, file_content = "passwd.txt"): # Get updated list and save to file
        '''Writing updated list into the file'''
        with open(file_content, 'w') as file:
            for i in file_list:
                file.write(i + "\n")

    # Main part of the program
    if __name__ != "__main__":  
        user_name = get_user_name()
        file_list = remove_user(user_name)
        newfile(file_list)