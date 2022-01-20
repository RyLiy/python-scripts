import instaloader, random, time
from time import sleep
from threading import Thread
from os.path import exists

terminationPoint = False
running = True
amount = 0
totalusers = 1

def iterate():
    global running 
    #L = instaloader.Instaloader(rate_controller=lambda ctx: MyRateController(ctx))
    L = instaloader.Instaloader()
    
    #youraccname = your instagram profile name
    L.load_session_from_file('youraccname')

    #Username of person we are going to extract all followers from
    user = ''
    
    profile = instaloader.Profile.from_username(L.context, user)
    f = open('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Data\\instagram_users\\' + user + '.txt', 'a')

    # Grab an iterator for list of followers
    user_iterator = profile.get_followers()
        
        
    if exists(user + "_iterator.json"):
        print("Existing iterator was found, loading previous state\n")
        user_iterator.thaw(instaloader.load_structure_from_file(L,user + "_iterator.json"))
    
    global totalusers
    global amount
    amount = user_iterator.total_index
    totalusers = profile.followers
    start = time.time()
    PERIOD_OF_TIME = 12600 #3.5 hours
    
    for followers in user_iterator:
        # if time.time() > start + PERIOD_OF_TIME:
            # bad_shutdown(3,user_iterator,user)
            # break
        amount += 1
        f.write(followers.username + '\n')
        
        #if amount % 60 == 0:
        instaloader.save_structure_to_file(user_iterator.freeze(), user + "_iterator.json")
        sleep(random.uniform(0, 3))

    f.close()
    if (amount / totalusers) >= 0.99:
        print("Completed - all usernames retrieved. margin of error - 1%")
    

def progress():
    prev = 0
    print ("Initializing: Logging in, retrieving profile, retrieving iterator...\n")
    while running:
        sleep(1)
        if (amount/totalusers)*100 != prev:
            prev = ((amount/totalusers)*100)
            print (str((amount/totalusers)*100) +'%')

t1 = Thread(target=iterate)
t2 = Thread(target=progress)
# start the threads
t1.start()
t2.start()


    


t1.join()
t2.join()
print ("threads successfully closed")

