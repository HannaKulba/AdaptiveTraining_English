inputTime = int(input())

hours = int((inputTime / 3600) % 24)
minutes = int((inputTime / 60) % 60)
seconds = int((inputTime % 60) % 60)

if minutes < 10:
    minutes = "0" + str(minutes)

if seconds < 10:
    seconds = "0" + str(seconds)

print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
