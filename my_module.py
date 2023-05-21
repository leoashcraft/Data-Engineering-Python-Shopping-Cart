from math import floor, pi

def sqft(l,w):
        a = 0
        a = a + (l * w)
        print("%.2f" % a)
        
def circ(r):
        a = 0
        a = a + (2 * pi * r)
        print("%.2f" % a)

def getspace():
    print("Enter S for square footage, C for circumference")
    usrchoice = input("Would you like the square footage or circumference of an object?")
    if usrchoice.lower() == "s":
        l = int(input("Enter the length value: "))
        w = int(input("Enter the width value: "))
        print("The square footage is:")
        sqft(l,w)
        
    elif usrchoice.lower() == "c":
        r = int(input("Enter the radius value: "))
        print('The Circumference is: ')
        circ(r)
    else:
        print("Please select a valid option.")