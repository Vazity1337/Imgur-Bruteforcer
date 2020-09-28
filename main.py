import requests
import random
import string
import urllib
import threading
from colors import *

lock = threading.Lock()
    
def main():
    code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for k in range(7))
    link = f'https://i.imgur.com/{code}.png'
    r = requests.get(link, allow_redirects=False)

    if r.status_code == 200:
        lock.acquire()
        print(f'{green()}[VALID] {link}')
        lock.release()
        with open('Image Links.txt', 'a') as f: 
            f.write(f'{link}\n')
        contents = urllib.request.urlopen(link)
        i = open(f"Results/{code}.png","wb")
        i.write(contents.read())
        i.close()
    else:
        lock.acquire()
        print(f'{red()}[INVALID] {link}')
        lock.release()

threads = int(input(f'Threads: '))

while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = main).start()
        except:
            pass