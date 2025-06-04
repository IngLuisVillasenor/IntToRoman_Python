###########################################
#Description: Program to convert an integer number between 1 and 3999 into a Roman number
#Author: Luis Villaseñor
#Date: 04 - june -2025
###########################################

#Definition of a dictionary 
roman_d = {1 : 'I',
           5 : 'V',
           10 : 'X',
           50 : 'L',
           100 : 'C',
           500 : 'D',
           1000 : 'M'}

#Function to translate the numbers accoding to their position
def intToRoman10(t,l):
    roman_n = ''
    X = None
    Y = None
    Z = None
    
    match l:
        case 1:
            X = 1
            Y = 5
            Z = 10
        case 2:
            X = 10
            Y = 50
            Z = 100
        case 3:
            X=100
            Y=500
            Z=1000
        case 4:
            X=1000
            Y=5000
            Z=10000
        
    if roman_d.get(t) == None:
        if t == 4:
            roman_n = roman_d.get(X) + roman_d.get(Y)
        elif t == 9:
            roman_n = roman_d.get(X) + roman_d.get(Z) 
        elif t <= 3:
            for i in range(t):
                roman_n = roman_n + roman_d.get(X)
        elif t <=8:
            roman_n = roman_d.get(Y)
            for i in range(t-5):
                roman_n = roman_n + roman_d.get(X)
    else:
        roman_n = roman_d.get(t) 

    return(roman_n)   


#Main function that uses intToRoman10 function and creates the Roman number
def main(s):    
    if 1 <= s <=3999:
        cadena = str(s)
        size = len(cadena)
        romano_n = intToRoman10(s,1)
        part1=None
        part2=None
        part3=None
        part4=None
        
        if romano_n == '':
            match size:
                case 2: 
                    p1 = int(cadena[0])
                    p2 = int(cadena[-1])
                    
                    if p1 == 1 or p1 == 5:
                        p1= p1*10
                                        
                    part1 = intToRoman10(p1,2)
                    part2 = intToRoman10(p2,1)
                    romano_n = part1+part2    
                case 3:
                    p1 = int(cadena[0])
                    p2 = int(cadena[1])
                    p3 = int(cadena[-1])
                    
                    if p1 == 1 or p1 ==5:
                        p1=p1*100      
                    if p2 == 1 or p2 == 5:
                        p2= p2*10
                    
                    part1 = intToRoman10(p1,3)
                    part2 = intToRoman10(p2,2)
                    part3 = intToRoman10(p3,1)               
                    romano_n = part1+part2+part3
                case 4:
                    p1 = int(cadena[0])
                    p2 = int(cadena[1])
                    p3 = int(cadena[2])
                    p4 = int(cadena[-1])
                    
                    if p1 == 1 or p1 ==5:
                        p1=p1*1000
                    if p2 == 1 or p2 == 5:
                        p2= p2*100
                    if p3 == 1 or p3 == 5:
                        p3=p3*10
                    
                    part1 = intToRoman10(p1,4)
                    part2 = intToRoman10(p2,3)
                    part3 = intToRoman10(p3,2)
                    part4 = intToRoman10(p4,1)               
                    romano_n = part1+part2+part3+part4
                    
            print(romano_n)
            return(romano_n)    
        else:
            print(romano_n)
            return(romano_n)  
    else:
        print("Please enter a valid number between 1 and 3999")
        return False

if __name__ == '__main__':
    entrada = input("Enter an integer number between 1 and 3999: ")
    entero = int(entrada)
    main(entero)

