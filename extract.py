from zipfile import ZipFile

zip = input("Enter zip file name: ")
passw = "passlist.txt"

try:
    r = ZipFile(zip)
except FileNotFoundError:
    print("That is not a zip file!")
else:
    zip = ZipFile(zip)
    found = ""
    try:
        zip.extractall()
    except RuntimeError as e:
        if 'encrypted' in str(e):
            print("zip file has a password")
            print("finding the password...")
            with open(passw, "r") as f:
                for line in f:
                    password = line.strip()
                    password = password.encode('utf-8')
                    try:
                        found = zip.extractall(pwd=password)

                    except RuntimeError:
                        pass
                    except:
                        pass
                    else:
                        print("password is: ", password.decode())
                        print("extracting files...")
                        print("done")


                if found == "":
                    print("not found, try another list.")
    else:
        print("zip file does not have a password")
        print("extracting files...")
        print("done")
