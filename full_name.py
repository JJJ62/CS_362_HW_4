

def str_cat(first, last):
    full = str(first) + " " + str(last)
    return str(full)

def get_input_first():
    print("Please provide your first name and last name")
    first = input("First Name: ")
    return first

def get_input_last():
    last = input("Last Name: ")
    return last

def main():
    first = get_input_first()
    last = get_input_last()
    full = str_cat(first, last)
    print("Your full name is: " + str(full))

if __name__ == '__main__':
    main()
