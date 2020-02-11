def get_int(start_message, error_message, end_message):
    print(start_message)
    bool = True

    while bool:
        i = input()
        try:
            int(i)
            print(end_message)
            bool = False
            return int(i)
        except ValueError:
            print(error_message)



if __name__ == '__main__':
    x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')
