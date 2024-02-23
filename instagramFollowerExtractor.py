import instaloader
import random
import time
from time import sleep
from threading import Thread
from os.path import exists

# Global variables
terminationPoint = False
running = True
amount = 0
totalusers = 1

# Function to iterate over followers and write them to a file
def iterate():
    global running
    
    # Initialize Instaloader
    L = instaloader.Instaloader()
    
    # Load session from file
    L.load_session_from_file('youraccname')  # Replace 'youraccname' with your Instagram profile name
    
    # Username of the person to extract followers from
    user = 'username'  # Replace 'username' with the person's IG profile
    
    # Open file to write followers' usernames
    f = open('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Data\\instagram_users\\' + user + '.txt', 'a')
    
    # Get profile object
    profile = instaloader.Profile.from_username(L.context, user)
    
    # Get iterator for followers
    user_iterator = profile.get_followers()
    
    # Thaw iterator from file if exists
    if exists(user + "_iterator.json"):
        print("Existing iterator was found, loading previous state\n")
        user_iterator.thaw(instaloader.load_structure_from_file(L,user + "_iterator.json"))
    
    global totalusers # Assume global variables
    global amount
    amount = user_iterator.total_index
    totalusers = profile.followers
    
    # Start time
    start = time.time()
    PERIOD_OF_TIME = 12600 # Need to pause every 3.5 hours to avoid rate limiting, currently unused in favor of random sleeping
    
    # Iterate over followers
    for followers in user_iterator:
        amount += 1
        f.write(followers.username + '\n')
        
        # Save iterator to file every 60 followers
        instaloader.save_structure_to_file(user_iterator.freeze(), user + "_iterator.json")
        
        # Random sleep to avoid rate limiting
        sleep(random.uniform(0, 3))
    
    # Close file
    f.close()
    
    # Check if all usernames retrieved
    if (amount / totalusers) >= 0.99:
        print("Completed - all usernames retrieved. Margin of error - 1%")

# Function to display progress
def progress():
    prev = 0
    print ("Initializing: Logging in, retrieving profile, retrieving iterator...\n")
    while running:
        sleep(1)
        if (amount/totalusers)*100 != prev:
            prev = ((amount/totalusers)*100)
            print (str((amount/totalusers)*100) +'%')

# Create threads
t1 = Thread(target=iterate)
t2 = Thread(target=progress)

# Start the threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print ("Threads successfully closed")
