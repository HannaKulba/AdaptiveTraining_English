lp = [int(i) for i in input().split()]

login = 100500
password = 424242

if login == lp[0] and password == lp[1]:
    print("Login success")
elif login == lp[0] and password != lp[1]:
    print("Wrong password")
elif login != lp[0]:
    print("No user with login " + str(lp[0]) + " found")
