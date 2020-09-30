#functions
def udl_whole():
    w = int(input("Enter the value of udl: "))
    l = int(input("Enter the length of span: "))
    m = w*l**2 / 12
    print("Fixed moment at both side of applying udl are  -",m ,"and" ,m)
def point_load():
    p = int(input("Enter the value of point load: "))
    l = int(input("Enter the length of span: "))
    m = p*l /8
    print("Fixed end moment at both side of applying point load are - ", m ,"and ", m)
def point_load_any_place():
    p = int(input("Enter the value of point load: "))
    l = int(input("Enter the length of span: "))
    print("a is left side distance from fixed end to point load and b in right side from fixed and to point load")
    a = int(input("a = "))
    b = int(input("b = "))
    m1 = p * a * b**2 / l**2
    m2 = p * a**2 * b / l**2
    print("Fixed end moments at both side of applying point load at random point are -", m1 ,"and ", m2)
def trang_whole():
    w = int(input("Enter the value of highest load: "))
    l = int(input("Enter the length of span: "))
    m1 = w*l**2 / 30
    m2 = w * l**2 / 20
    print("Fixed end moments at both side of applying trangular load at whole span are -", m1 ,"(0 load side) and ", m2)
def trang_equi_whole():
    w = int(input("Enter the value of highest load at middle: "))
    l = int(input("Enter the length of span: "))
    m = 5 * w * l**2 / 96
    print("Fixed end moments at both side of applying equi trangular load at random point are -", m ,"and ", m)
def udl_half_span():
    w = int(input("Enter the value of udl: "))
    l = int(input("Enter the length of span: "))
    m1 = 11 * w * l**2 / 192
    m2 = 5 * w * l**2 / 192
    print("Fixed end moments at both side of applying udl at half span are -", m1 ,"(loaded side) and ", m2)
def moment():

    a = int(input("a = "))
    b = int(input("b = "))
    l = int(input("Enter the span of length: "))
    m0 = int(input("enter the value of moment: "))
    m1 = m0 * b * ((3 * a) - l) / (l**2)
    m2 = m0 * a * ((3 * b) - l) / (l**2)
    print("Fixed end moments at both side of applying moment at random point are -", m1 ,"and ", m2)
#calling function
if __name__ == "__main__":
    fg = 1
    while fg == 1 : 
        print("welcome")
        print("Enter the type of load ")
        print("For point load press p \nFor udl press u\nFor triangular load press t\nFor moment only prass m")
        type = input("p/u/t/m : ")
        if type == "u":
            print("Input taken successfully")
            print("full span or half span?")
            s1 = input("full span press f and half span press h :")
            if s1 == "h":
                udl_half_span()
            else:
                udl_whole()

        elif type == "p":
            print("Input taken successfully")
            print("middle of the span or specific distance?")
            s2 = input("For middle span press m and for specific point press s :")
            if s2 == "m":
                point_load()
            else :
                point_load_any_place()

        elif  type == "t" :
            print("Input taken successfully")
            print("For normal triangular load (o to w) press t and for equilateral triangle load press e.")
            s2 = input("t or e :")
            if s2 == "e":
                trang_equi_whole()
            else:
                trang_whole()

        elif  type == "m" :
            print("Input taken successfully")
            print("a is left side distance from fixed end to moment and b in right side from fixed and to moment")
            moment()

        else :
            print("please enter p/u/t/m.")
        
        fg = input()

        break;
        
        


#for_holding_comand_prompt = input()



