import sys # Using sys module

def read_the_file(f_path):
    '''make list and sub list using the files and check for file error'''
    try:
        with open(f_path, 'r') as file:
            # Create a list of lists using file content
            content_list = [line.strip().split(',') for line in file]
            return content_list
        
    except FileNotFoundError:
        print(f"Could not open the file '{f_path}'")
        sys.exit(1)

def our_cat(content):
    '''The total number of times the correct cat has entered the house.'''
    num_our = 0
    # Calculate total time spent at home
    for i in content:
        if i[0] == "OURS":
            num_our += 1

        else:
            continue 
    return num_our

def their_cat(content):
    '''The number of times intruding cats have been doused with water.'''
    num_theirs = 0
    for i in content:
        if i[0] == "THEIRS":
            arrival_number = int(i[1])
            left_number = int(i[2])
            time_spend = left_number - arrival_number
            if time_spend == 1:
                num_theirs += 1
        else:
            continue
    return num_theirs
        
def spend_home(content):
    '''The total time spent in the house by the correct cat.'''
    hour = 0
    minute = 0
    
    for i in content:
        if i[0] == "OURS":
            arrived = int(i[1])
            time_hour_a= arrived // 60
            time_minute_a = arrived % 60
            left = int(i[2])
            time_hour_l = left // 60
            time_minute_l = left % 60
            hour += time_hour_l - time_hour_a 
            minute += time_minute_l - time_minute_a
            if minute >= 60: # Converting minutes to hours
                hour += 1
                minute -= 60 
    return hour, minute


def average_time(hr,min,content):
    '''Average time the cat stayed at home.'''
    count = 0
    for i in content:
        if i[0] == "OURS":
            count += 1

    hour_in_min = hr * 60
    total_time = hour_in_min + min
    average = total_time // count

    return average

def longest_shortest_time(content):
    '''longest and shortest time cat stayed at home.'''
    new_list = []
    for i in content:
        if i[0]=="OURS":
            arrived = i[1]
            left = i[2]
            time_spent = int(left) - int(arrived)
            new_list.append(time_spent)
    longest = shortest = new_list[0]

    # Keeping track of longest and shortest visit 
    for j in new_list:
        if j > longest:
            longest = j

        if j < shortest:
            shortest = j

    return longest, shortest

def display(o_cat, t_cat, hr, min, avg, long, short):
    '''print output'''
    print("\t \t \t Log File Analysis")
    print("\t \t \t ==================\n")
    print(f"Our Cat enterd the house for {o_cat} times.\n")
    print(f"Intruding cats have been doused with water for {t_cat} times.\n")        
    print(f"Our Cat spent {hr} hour and {min} minute in house.\n")
    print(f"Average Vist length is: \t{avg} minute\n")
    print(f"Longest Vist is: \t\t{long} minute\n")
    print(f"Shortest Vist is: \t\t{short} minute\n")

# Main part of the program
if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Missing command line argument")
        sys.exit(1)
    else:
        file_path=sys.argv[1]
        content = read_the_file(file_path)

    o_cat = our_cat(content)
    t_cat = their_cat(content)
    hr, min = spend_home(content)
    avg = average_time(hr,min,content)
    long, short = longest_shortest_time(content)
    display(o_cat, t_cat, hr, min, avg,long, short)