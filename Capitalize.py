def capitalize(string):
    l=string.split(" ")
    a = [i.capitalize() for i in l]
    return ' '.join(a)


if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)