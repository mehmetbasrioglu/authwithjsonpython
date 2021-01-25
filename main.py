#Framework

import base64
import json
import time
from termcolor import colored
import os
import webbrowser


global authCheck

authCheck = False

def Encode(var):
    return base64.b85encode(var.encode("utf-8"))
def Decode(var):
    return base64.b85decode(var.decode("utf-8"))

jsondb = open("dbs.json",encoding="utf8")

data = json.load(jsondb)



def kullaniciKontrol(kullaniciadi, email, sifre):
    for database in data:
        if database["kullaniciadi"] == kullaniciadi and database["email"] == email and database["password"] == sifre:
            print("E-mail:",database["email"],"Password:",database["password"]) 
            kullaniciyaHosgeldinYazdir("Hoşgeldin ",database["kullaniciadi"],database["admin"],database["adminlevel"])
            if database["admin"]:
                islemleriListele(database["admin"])
                Admin()

            else:
                islemleriListele(database["admin"])
                Uye()


def kullaniciyaHosgeldinYazdir(string,kullanici,isAdmin,level):
    if string == "":
        print("%s"%colored("Kullanıcıya Girilecek Mesajı Boş Bırakamazsınız","red"))
    elif len(string) > 1:
        clearterm()
        if isAdmin and level > 4:
            print("%s" %colored(string+" "+kullanici+" ( ☆ ☆ ☆ ☆ ☆  ) ","green"))
        elif isAdmin and level == 4:
            print("%s" %colored(string+" "+kullanici+" ( ☆ ☆ ☆ ☆  ) ","green"))
        elif isAdmin and level == 3:
            print("%s" %colored(string+" "+kullanici+" ( ☆ ☆ ☆  ) ","green"))
        elif isAdmin and level == 2:
            print("%s" %colored(string+" "+kullanici+" ( ☆ ☆  ) ","green"))
        elif isAdmin and level == 1:
            print("%s" %colored(string+" "+kullanici+" ( ☆  ) ","green"))
        else:
            print("%s" %colored(string+" "+kullanici,"green"))

def clearterm():
    os.system('cls' if os.name=='nt' else 'clear')


def BrowserAc(browser):
    if browser == 1:
        webbrowser.open_new_tab("www.google.com")
    elif browser == 2:
        webbrowser.open_new_tab("www.youtube.com")

def Admin():
    authCheck = True
    while authCheck == True:
        clearterm()
        islemleriListele(True)
        islem = input("Ne Yapmak Istiyorsunuz ?:")
        if islem == "Kullanıcı Ekle":
            kullaniciadi = input("Kullanıcı Adı:")
            email = input("Email:")
            password = input("Şifre:")
            admin = input("Admin Yetkisi Vermek Istiyormusunuz ?:")
            if admin.__contains__("Evet"):
                level = input("Admin Yetkisi Level Kaç Olsun ? ( Yetki Vermediyseniz 0 Yazın ):")
                Ekle(kullaniciadi,email,password,True,int(level))
            else:  
                Ekle(kullaniciadi,email,password,False,0)
            databaseUpdate('dbs.json',data)
        elif islem == "Kullanıcı Sil":
            id = input("Silinecek Kullanıcının ID Giriniz:")
            del data[int(id)]
            databaseUpdate('dbs.json',data)
        elif islem == "Kullanıcı Güncelle":
            kullaniciadi = input("Kullanıcı Adı:")
            for database in data:
                if kullaniciadi == database["kullaniciadi"]:
                    id = input(" ID Giriniz:")
                    kullaniciadi = input("Yeni Kullanıcı Adı:")
                    email = input("Yeni Email:")
                    password = input("Yeni Şifre:")
                    admin = input("Admin Yetkisi Vermek Istiyormusunuz ?:")
                    if admin.__contains__("Evet"):
                        level = input("Admin Yetkisi Level Kaç Olsun ? ( Yetki Vermediyseniz 0 Yazın ):")
                        #Ekle(kullaniciadi,email,password,True,int(level))
                        veri = {
                            "kullaniciadi": kullaniciadi,
                            "email": email,
                            "password": password,
                            "admin": admin,
                            "adminlevel": int(level)
                            }
                        data[int(id)] = veri

                    else: 
                        print(" ") 
                        #Ekle(kullaniciadi,email,password,False,0)
            databaseUpdate('dbs.json',data)
            time.sleep(1)
        elif islem == "Çıkış Yap":
            authCheck = False
            asama1()

def Uye():
    authCheck = True
    while authCheck == True:
        islem = input("Ne Yapmak Istiyorsunuz ?:")
        if islem == "Google Aç":
            BrowserAc(1)
        elif islem == "YouTube Aç":
            BrowserAc(2)
        elif islem == "Çıkış Yap":
            authCheck = False
            asama1()
            

def islemleriListele(isAdmin):
    if isAdmin:
        print("""
    1- Kullanıcı Ekle
    2- Kullanıcı Sil
    3- Kullanıcı Güncelle
    4- Çıkış Yap
    """)
    else:
        print("""
    1- Google Aç
    2- YouTube Aç
    3- Çıkış Yap
    """)
    

def asama2():
    clearterm()
    authuser = input("Kullanıcı Adı:")
    authmail = input("Email:")
    authuserpass = input("Şifre:")
    time.sleep(1)
    kullaniciKontrol(authuser,authmail,authuserpass)



def asama1():
    clearterm()
    print("""
    1- Giriş Yap
    2- Kayıt Ol
    """)
    authCheck = False
    while authCheck == False:
        secenek = input("Ne Yapmak Istiyorsunuz ? :")
        if secenek == "Giriş Yap" or secenek == "Giriş":
            asama2()
            authCheck = True
        elif secenek == "Kayıt Ol":
            KayitOlBilgileriIste()
            

jsondbw = open("dbs.json","a",encoding="utf8")


def KayitOlBilgileriIste():
    kullaniciadi = input("Yeni Kullanıcı Adı:")
    email = input("Yeni Email:")
    password = input("Yeni Şifre:")
    Ekle(kullaniciadi,email,password,False,0)
    databaseUpdate('dbs.json',data)


def databaseUpdate(fileName, data):
    with open(fileName, 'w') as fp:
        json.dump(data, fp, indent=4)

def Ekle(kullaniciadi,email,password,admin,level):
    veri = {
                "kullaniciadi": kullaniciadi,
                "email": email,
                "password": password,
                "admin": admin,
                "adminlevel": level
                }
    data.append(veri)  

asama1()


    
