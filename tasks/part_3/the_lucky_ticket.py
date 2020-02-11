def check_ticket(ticket_number):
    first_part = ticket_number[0:3]
    second_part = ticket_number[3:7]
    first_part_sum = int(first_part[0]) + int(first_part[1]) + int(first_part[2])
    second_part_sum = int(second_part[0]) + int(second_part[1]) + int(second_part[2])

    if first_part_sum == second_part_sum:
        print('Lucky')
    else:
        print('Regular')


if __name__ == '__main__':
    ticket = input()
    check_ticket(ticket)
