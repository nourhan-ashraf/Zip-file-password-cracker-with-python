from zipfile import ZipFile
import pathlib
zip = input("Enter zip file name: ")
passlist = input("Enter password list file name: ")

FoundListFile = 0
FoundPass = ""

if pathlib.Path(passlist).exists() == True:
    FoundListFile += 1

try:
    ZipFile(zip)
except FileNotFoundError:
    print("ERROR! Wrong file type")
except RuntimeError:
    print("ERROR! Wrong file type")
else:
    zip = ZipFile(zip)
    try:
        zip.extractall()
    except RuntimeError as e:
        if 'encrypted' in str(e):
            if FoundListFile > 0:
                print("zip file has a password")
                print("finding the password...")
                with open(passlist, "r") as f:
                    for line in f:
                        password = line.strip()
                        password = password.encode('utf-8')
                        try:
                            FoundPass = zip.extractall(pwd=password)

                        except RuntimeError:
                            pass
                        except:
                            pass
                        else:
                            print("password is: ", password.decode())
                            print("extracting files...")
                            print("done")
            else:
                print("ERROR! Wrong file type")

                if FoundPass == "" and FoundListFile > 0:
                    print("not found, try another list.")
    else:
        print("zip file does not have a password")
        print("extracting files...")
        print("done")
