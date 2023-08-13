def swap_case(name):
    name1=""
    for i in name:
       if(i.isupper()):
           name1=name1+(i.lower())
       elif(i.islower()):
           name1=name1+(i.upper())
       else:
           name1=name1+i
    return name1
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
