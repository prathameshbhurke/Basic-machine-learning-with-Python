'''
Problem:
In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
'''


if __name__ == '__main__':
    s = input()
    inp_list = list(s);
    # print(inp_list);
    a_flag = 0
    d_flag = 0
    l_flag = 0
    u_flag = 0
    an_flag = 0
    for i in range(0, len(inp_list)):
        if inp_list[i].isalpha():
            a_flag = 1

        if inp_list[i].isdigit():
            d_flag = 1

        if inp_list[i].islower():
            l_flag = 1

        if inp_list[i].isupper():
            u_flag = 1

        if inp_list[i].isalnum():
            an_flag = 1

    if (an_flag == 1):
        print('True')
    else:
        print('False')

    if (a_flag == 1):
        print('True')
    else:
        print('False')

    if (d_flag == 1):
        print('True')
    else:
        print('False')

    if (l_flag == 1):
        print('True')
    else:
        print('False')

    if (u_flag == 1):
        print('True')
    else:
        print('False')
