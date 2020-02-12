weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
leave = input()
d = int(input())
l = weekdays.index(leave)


# l is the numeric version of which day
# d is the number of days until return

# Enter your formula for calculating the return day
def index_day():
    res = d % 7 + l
    if res < 7:
        return res
    else:
        return res % 7


r = index_day()
print("If you leave on {} and return {} days later, you will return on {}.".format(leave, d, weekdays[r]))
