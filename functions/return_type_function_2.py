def multi_input():
    """this function allows users to add multiple lines of data in one go"""
    data = ''
    while True:
        line = input('#')
        if not line:
            break
        data += line + '\n'
    return data

if __name__ =="__main__":
    story1 = multi_input()
    print(story1)