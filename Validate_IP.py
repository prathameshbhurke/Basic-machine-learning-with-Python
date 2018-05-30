'''
Valdiate if its a true IP address:

- IP addresses are represented in dot decimal notations.
- consists of 4 decimal numbers ranging from  0 to 255
- ex: 172.15.215.18
pseudo_code:
-- First split the given string by split() on '.'
-- check the split string's len if its = 4, if not return false.
-- check if all elements in split string are digits, if not return false.
-- convert all elements of split string into int and check if they are greater than 0 but less than 255, else return false.
'''


def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


if __name__ == '__main__':
    in_string = '142.23.36.AAA'
    result = validate_ip(in_string)
    print(result)
