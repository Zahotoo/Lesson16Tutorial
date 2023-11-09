name = input("What is your name?")
name = name.capitalize()

a = int(input("What is your a?"))
b = int(input("What is your b?"))
c = int(input("What is your c?"))
d = int(input("What is your d?"))

astr = str(a)
bstr = str(b)
cstr = str(c)
dstr = str(d)


def solvecubic(a,b,c,d):

    f1 = ((-(b**3))/(27*(a**3))) + ((b*c)/(6*(a**2))) - ((d)/(2*a))
    f2 = ((c)/(3*a)) - ((b**2) / (9*(a**2)))
    f3 = b / (3*a)
    x = (f1 + (((f1**2) + (f2**3))**0.5))**(1/3) + (f1-(((f1**2) + (f2**3))**0.5))**(1/3) - f3

    answer = astr+"x^3+"+bstr+"x^2+"+cstr+"x+"+dstr+"=0"

    answer = answer.replace("+-","-")
    answer = answer.replace("+1x","+x")
    answer = answer.replace("-1x","-x")
    answer = answer.replace("+0","")
    answer = answer.replace("-0","")
    answer = answer.replace("+1x^2","+x^2")
    answer = answer.replace("-1x^2","-x^2")
    answer = answer.replace("1x^3","x^3")
    answer = answer.replace("-1x^3", "-x^3")
    answer = answer.replace("x^2x", "")

    x = x.real

    print("Hello",name,", I will solve",answer)
    print("The root of the cubic is",x)


solvecubic(a,b,c,d)

quit()