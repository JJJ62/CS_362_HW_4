def get_average(list):
    i = 0
    total = 0
    while (i < len(list)):
        total += int(list[i])
        i += 1
    average = int(total) / int(i)
    return int(average)


def get_input():
    thislist = list()
    print("Please input the number of elements you would like to find the average of\n")
    exit = 0
    while (exit != 1):
        num_elem = input("Number of elements: ")
        if (num_elem != '' and num_elem != None):
            exit = 1
        else:
            print("Input == None. Please try again\n")
    i = 0
    print("Please input each of the elements of the list to find the average of. ")
    print("Input one element at a time")
    while (int(i) < int(num_elem)):
        exit = 0
        while (exit != 1):
            elem_value = input("list element [" + str(i) + "] :")
            if (elem_value != '' and elem_value != None):
                thislist.append(elem_value)
                i += 1
                exit = 1
            else:
                print("Input == None. Please try again\n")
    return thislist


def main():
    thislist = get_input()
    average = get_average(thislist)
    print("the average of your list is: " + str(average))


if __name__ == '__main__':
    main()
