#!/usr/bin/python3  # Update to python2 if using Python 2
# -*- coding: utf-8 -*-
# coded by kereh

import subprocess

try:
    import mechanize, requests, os, sys, time, random
    try:
        # Conditional import for Python 2 and 3 compatibility
        import cookielib
    except ImportError:
        import http.cookiejar as cookielib  # For Python 3
except ImportError:
    subprocess.call("pip3 install requests mechanize", shell=True)

subprocess.call("clear", shell=True)

# Colors and Symbols
green = "\033[1;32m"
normal = "\033[0m"
red = "\033[1;31m"
cyan = "\033[1;36m"
good = "\033[1;32m[\033[1;36m+\033[1;32m]\033[0m"
bad = "\033[1;32m[\033[1;31m!\033[1;32m]\033[0m"
success = "\033[1;32mSuccessful\033[0m"
failed = "\033[1;31mFailed\033[0m"

# Banners
banner_menu = """
 ▄▄▄▄    ▒█████  ▄▄▄█████▓
▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
▒░▒   ░   ░ ▒ ▒░     ░    
 ░    ░ ░ ░ ░ ▒    ░      
 ░          ░ ░           
      ░

Github : {}https://github.com/kereh{}
[+] Menu Bot [+]
[1] Generate Access Token
[2] Auto Like On Your Post 200
[3] Auto Commenter On Your Post
[4] Auto Friend Requests On Your Account
""".format(green, normal, green, normal)

banner = """
 ▄▄▄▄    ▒█████  ▄▄▄█████▓
▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▒██░█▀  ▒██   ██░░ ▓██▓ ░
░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░
░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░
▒░▒   ░   ░ ▒ ▒░     ░
 ░    ░ ░ ░ ░ ▒    ░
 ░          ░ ░
      ░

Github : {}https://github.com/kereh{}
""".format(green, normal, cyan, normal, green, normal)

# Initialize mechanize browser with cookie jar
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_cookiejar(cookielib.LWPCookieJar())
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
info = time.strftime("%S:%M:%H")

# Functions for each option
def generate_token():
    print(banner)
    username = input("[+] Username: ")
    password = input("[+] Password: ")
    print("[{}]{} Generating Access Token, please wait...".format(info, good))
    time.sleep(5)
    if not username:
        print("[{}]{} You must input your Username!".format(info, bad))
    elif not password:
        print("[{}]{} You must input your Password!".format(info, bad))
    else:
        token_url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password={}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
        token_parsing = br.open(token_url.format(username, password)).read()
        with open("token.txt", "w") as file_token_access:
            file_token_access.write(str(token_parsing))
        print("[{}]{} STATUS: {}".format(info, good, success))
        print("[{}]{} Token saved as token.txt".format(info, good))

def autolike():
    print(banner)
    token = open("token.txt", "r").read()
    br.open("https://yolikers.com/")
    br.select_form(nr=0)
    br.form["access_token"] = token
    br.submit()
    try:
        react = input("[+] Type reaction ['LIKE','LOVE','HAHA','WOW','SAD','ANGRY']: ")
        br.open("https://yolikers.com/like.php?type=status")
        br.select_form(nr=0)
        br.form["type"] = [react]
        br.submit()
        print("[{}][+] Successfully sent like.".format(info, good))
    except:
        print("[{}][+] Try again after 15 minutes.".format(info, bad))

def comment():
    print(banner)
    print("[{}]{} Sending comment on your latest post...".format(info, good))
    token = open("token.txt", "r").read()
    br.open("https://yolikers.com/commenter.php?type=status")
    br.select_form(nr=0)
    br.form["access_token"] = token
    br.submit()
    try:
        br.open("https://yolikers.com/commenter.php?type=status")
        br.select_form(nr=0)
        br.submit()
        print("[{}]{} Comment sent successfully.".format(info, good))
    except:
        print("[{}]{} Try again after 15 minutes.".format(info, bad))

def friend():
    print(banner)
    print("[{}]{} Sending 30 friend requests on your Facebook account...".format(info, good))
    token = open("token.txt", "r").read()
    br.open("https://yolikers.com/")
    br.select_form(nr=0)
    br.form["access_token"] = token
    try:
        br.open("https://yolikers.com/autorequest.php?type=profile")
        br.select_form(nr=0)
        br.submit()
        print("[{}]{} 30 friend requests sent successfully.".format(info, good))
    except:
        print("[{}]{} Try again after 15 minutes.".format(info, good))

# Main Menu
if __name__ == "__main__":
    while True:
        print(banner_menu)
        choice = input("[+] Enter Your Choice: ")
        if choice == "1":
            generate_token()
            time.sleep(5)
        elif choice == "2":
            autolike()
            time.sleep(5)
        elif choice == "3":
            comment()
            time.sleep(5)
        elif choice == "4":
            friend()
            time.sleep(5)
        else:
            print("{} Invalid choice. Please select a valid option.".format(bad))
