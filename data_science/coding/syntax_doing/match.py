number=-100
#number=int(input("enter the number:"))
def checknumber(number):
    match number:
        case 0:
            return "Zero"
        case number if number>0:
            return "Positive"
        case number if number<0:
            return "Negitive"
print(checknumber(number))