while True:
    try:
        string =input()
        string = string.replace('{','(')
        string = string.replace('[','(')
        string = string.replace(']',')')
        string = string.replace('}',')')
        print(int(eval(string)))
    except:
        break
