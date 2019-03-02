# _*_ coding: UTF-8 _*_

import os
import sys
import time
import json
import requests
import mechanize
import subprocess

bi='\033[34;1m' #biru
i='\033[32;1m' #ijo
pur='\033[35;1m' #purple
cy='\033[36;1m' #cyan
me='\033[31;1m' #merah
pu='\033[37;1m' #putih
ku='\033[33;1m' #kuning

def ketik(s):
                for c in s + '\n':
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(10. / 50)

def load():
    ketik(ku+"LOADING "+cy+"...............")
    os.system ('clear')
    awalan()

def awalan():
    print " "
    print " "
    print " "
    print " "
    print cy+"-@-@-@-@-@-@-@-@-@-@-@-@-@-@-"
    print cy+"|"+i+" PENYUSUN :"+pu+" RISKI DARMAWAN"+cy+" |"
    print cy+"|"+pur+"  KUMPULAN BRUTEFORCE"+bi+" FB"+cy+"   |"
    print cy+"-@-@-@-@-@-@-@-@-@-@-@-@-@-@-"+pu
    os.system ('date')
    print " "
    menu()

def menu():
    print pur+"()===||================>>"
    print cy+"["+me+"1"+cy+"]"+i+" BRUTE FB NEW"
    print cy+"["+me+"2"+cy+"]"+i+" BRUTE FB BRF"
    print cy+"["+me+"3"+cy+"]"+i+" BRUTE FB MBF"
    print cy+"["+me+"4"+cy+"]"+i+" BRUTE FB CRK"
    print cy+"["+me+"5"+cy+"]"+i+" BRUTE FB T&G"
    print cy+"["+me+"6"+cy+"]"+i+" BRUTE FB CNK"
    print cy+"["+me+"7"+cy+"]"+i+" BRUTE FB A27"
    print cy+"["+me+"8"+cy+"]"+me+" EXIT PROGRAM"
    print pur+"()===||================>>"
    mau = raw_input(ku+"   ["+me+"?"+ku+"]"+cy+" PILIH NO : "+pu)

    if mau == '1':
       os.system ('cd brute;python2 new.py')
    if mau == '2':
       os.system ('cd brute;python2 brute.py')
    if mau == '3':
       os.system ('cd brute;python2 mbf.py')
    if mau == '4':
       os.system ('cd brute;python2 CRK.py')
    if mau == '5':
       os.system ('cd brute;python2 TG.py')
    if mau == '6':
       os.system ('cd brute;python2 cnk-mbf.py')
    if mau == '7':
       os.system ('cd brute;python2 MRA27.py')
    if mau == '8':
       os.system ('exit')


if __name__ == '__main__':
     os.system ('clear')
     load()
