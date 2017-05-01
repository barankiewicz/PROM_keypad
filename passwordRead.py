def passwordRead(filename):
    try:
        f = open("password.txt", 'r')
        password = f.readline()
        f.close()
    except IOError:
        password = '1234'

    for i in range(len(password)-1):
        letter = str(keypadRead())
        if (password[i] != letter):
            print("Wrong password")
            print("should be", password[i])
            time.sleep(1)
