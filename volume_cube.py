def take_input():
    exit = 0
    while (exit != 1):
        a = input("length of a side/edge: ")
        try:
            int(a)
            is_int = True
        except:
            is_int = False
        if (is_int):
            if (int(a) > 0):
                exit = 1
            else:
                print("The value you entered was 0 or less than 0 ")
                print("please enter a positive integer to find the volume\n")
        else:
            print("The value you entered was not an integer. Please try again\n")
    return a


def get_volume(edge):
    volume = int(edge) * int(edge) * int(edge)
    return volume


def main():
    print("This program will calculate the volume of a cube for you\n")
    print("Please enter the length of a side or edge of the cube")
    print(" you would like the volume of\n")

    edge = take_input()
    volume = get_volume(edge)
    print("The volume of your cube is: " + str(volume))


if __name__ == '__main__':
    main()
