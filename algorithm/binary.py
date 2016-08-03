# import string
# def deci2bin(decimal):
# 	stack = []

# 	while decimal > 0 :
# 		stack.append(decimal%2)
# 		decimal = decimal //2

# 		print decimal

# 	binsatr = ''
# 	while stack:
# 		binsatr = binsatr +  str(stack.pop())
# 	return binsatr

# print deci2bin(233)

# def sum_list(list):
# 	if len(list) ==1 :
# 		return list[0]
# 	else :
# 		return list[0] + sum_list(list[1:])

# print sum_list([1,3,5,7,9])

# def factorial(n):
# 	if n <=1 :
# 		return 1
# 	else :
# 		return n * factorial(n-1)

# print factorial(0)

# def to_str(num, base):
# 	string='0123456789ABCDEF'
# 	if num < base:
# 		return string[num]
# 	else :
# 		return  to_str(num//base, base)+string[num%base]

# print to_str(10,2)

# def reverse_str(string):
# 	if len(string) <=1:
# 		return string
# 	else :
# 		return reverse_str(string[1:]) + string[0]

# print reverse_str('abc')

# myString = 'hi! there.'
# print myString.translate(string.maketrans("",""), string.punctuation) 


# def isPal(s):
#     if len(s) <=1:
#         return True
#     else:
#    		if s[0] != s[len(s)-1]:
#    			return False
#    		return isPal(s[1:len(s)-2])

# print isPal('abba')


# import turtle

# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()

# def drawSpiral(myTurtle, lineLen):
#     if lineLen > 0:
#         myTurtle.forward(lineLen)
#         myTurtle.right(90)
#         drawSpiral(myTurtle,lineLen-5)

# drawSpiral(myTurtle,200)
# myWin.exitonclick()

# import turtle

# def tree(branchLen,t):
#     if branchLen > 5:
#         t.forward(branchLen)
#         t.right(20)
#         tree(branchLen-15,t)
#         t.left(40)
#         tree(branchLen-10,t)
#         t.right(20)
#         t.backward(branchLen)

# def main():
#     t = turtle.Turtle()
#     myWin = turtle.Screen()
#     t.left(90)
#     t.up()
#     t.backward(100)
#     t.down()
#     t.color("green")
#     tree(75,t)
#     myWin.exitonclick()

# main()


# import turtle

# def drawTriangle(points,color,myTurtle):
#     myTurtle.fillcolor(color)
#     myTurtle.up()
#     myTurtle.goto(points[0][0],points[0][1])
#     myTurtle.down()
#     myTurtle.begin_fill()
#     myTurtle.goto(points[1][0],points[1][1])
#     myTurtle.goto(points[2][0],points[2][1])
#     myTurtle.goto(points[0][0],points[0][1])
#     myTurtle.end_fill()

# def getMid(p1,p2):
#     return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

# def sierpinski(points,degree,myTurtle):
#     colormap = ['blue','red','green','white','yellow',
#                 'violet','orange']
#     drawTriangle(points,colormap[degree],myTurtle)
#     if degree > 0:
#         sierpinski([points[0],
#                         getMid(points[0], points[1]),
#                         getMid(points[0], points[2])],
#                    degree-1, myTurtle)
#         sierpinski([points[1],
#                         getMid(points[0], points[1]),
#                         getMid(points[1], points[2])],
#                    degree-1, myTurtle)
#         sierpinski([points[2],
#                         getMid(points[2], points[1]),
#                         getMid(points[0], points[2])],
#                    degree-1, myTurtle)

# def main():
#    myTurtle = turtle.Turtle()
#    myWin = turtle.Screen()
#    myPoints = [[-100,-50],[0,100],[100,-50]]
#    sierpinski(myPoints,3,myTurtle)
#    myWin.exitonclick()

# main()

def recDC(coinValueList,change,knownResults):
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins

print(recDC([1,5,10,25],63,[0]*64))


def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
                
            else:
                first = midpoint+1
                print first, 'fri'

    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
# print(binarySearch(testlist, 18))



