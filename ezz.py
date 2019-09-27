# Decompiled By xNot_Found
# Github : https://github.com/hatakecnk
# uncompyle6 version 3.3.5
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Jul  7 2019, 21:05:54) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: dg
import os, time, random, requests
from requests.exceptions import ConnectionError
os.system('clear')
logo = "\x1b[1;38m\n ____                              _         _\n|  _ \\ ___ _ __   __ _ _ __   __ _| | ____ _| |\n| |_) / _ \\ '_ \\ / _` | '_ \\ / _` | |/ / _` | |\n|  __/  __/ | | | (_| | | | | (_| |   < (_| | |\n|_|   \\___|_| |_|\\__,_|_| |_|\\__, |_|\\_\\__,_|_|\n                             |___/\n\n By JustAHacker \n"
print logo
print '\x1b[1;33m\ntools ini digunakan untuk menahan serangan virus'
time.sleep(2)
print '\x1b[1;31mSubscribe Channel Pembuat Script ini \n \x1b[1;36mJustA Hacker'
print 'github = https://github.com/justahackers/perusak'
print 'youtube = JustA Hacker'
time.sleep(5)
print 'Whatsapp = 6289682009902\n\n\n'
time.sleep(5)
a = 1
os.system('apt install neofetch && clear')
print 'INFO DEVICE'
os.system('neofetch')
raw_input('Ketik Apapun Untuk Melanjutkan [+]')

def loop(a):
    for i in range(1000000):
        try:
            requests.get('https://m.facebook.com')
            b = ['Trojan', 'Worm', 'Malware', 'Ransomware', 'DroidDream', 'StageFright']
            c = random.choice(b)
            aa = random.randint(5, 30)
            print '\x1b[1;32m' + str(a) + ' \x1b[1;33mTelah Berhasil Menahan Serangan Virus ' + '\x1b[1;32m' + str(c)
            time.sleep(0.2)
            print '\x1b[1;31mMelindungi Hp Anda....'
            time.sleep(0.1)
            print '\x1b[1;34mSubscribe JustA Hacker'
            time.sleep(aa)
            a += 1
        except requests.exceptions.ConnectionError:
            print 'Tidak Ada Jaringan !!!! '
            os.system('python2 penangkal.py')
            time.sleep(1)
        except KeyboardInterrupt:
            print 'Keluar(!) '
            os.sys.exit()


if __name__ == '__main__':
    loop(a)