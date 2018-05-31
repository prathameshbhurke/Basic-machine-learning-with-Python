def capitalize(string):
    str = string.split()
    refined_list = []
    #print(str)
    for word in str:
        new_word = word[:1].upper() + word[1:]
        refined_list.append(new_word)
    return ' '.join(refined_list)

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)