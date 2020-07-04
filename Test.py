#s= "Monkey flash pants pants dance"
#string = str(input())
#if string in s:
#    print("found")
#if "flash" in s:
#   print("found")

#name = input ('whats your phone number?')
#print('Thanks for letting us know your number '+name)
#job = input('please let us know your preffered language?')
#print('Thanks for informing '+job)
#num = input('Please let us know your roll number?')
#print('Thanks for informing me your number '+str(num))

#gender = input("Gender? ")
#if gender == "male" or gender == "Male":
#    print ("Your cat is male")
#else:
#    print ("Your cat is a bitch")

#age = int(input("Age of your cat? "))
#if age < 5:
#    print("Your cat is young")
#else:
#    print("Your cat is a scary one")

# age = int(input("Please type in your age "))
#if age <= 15:
#    print("you are a young twat")
#elif age <= 20:
#    print("You are a teen twat")
#elif age >= 20 and age <= 28:
#    print("you are a the real deal")
#else:
#    print("need to get yo head right")
#import getpass
#name = input(str())
#print ("Thanks " + name + " Please type in Password")
#getpass.getpass("Password: ")
#print ("Welcome to root")

#city = ['toki toki','moki moki','choki choki']
#print ('Cities loop:')
#for x in city:
#    print('City: ' + x)

#print('\n')

#num = [1,2,3,4,5,6,7,8]
#print('x^2 loop: ')
#for x in num:
#    y = x * x
#    print(str(x) + '*' + str(x) + '=' + str(y))

#clist = ['Canada', 'USA', 'Mexico','Australia']
#print('List of countries: ')
#for x in clist:
#    print('Country: ' + x)

#print('\n')

#print('Count till 100')
#for y in range(0, 101, 1):
#    print(y)

#print('\n')

#revcount = range(1,4)
#reversed_range = reversed (revcount)
#for r in reversed_range:
#    print(r)

#print('\n')

#print('Even Number')
#for e in range(0,12,2):
#    print(e)

#print('\n')

#b = 0
#for a in range(100,200):
#    b = b + a
#    print(b)

#print('\n')

#print('Table of Twenty Four')
#m = 24
#for t in range(1,11,1):
#    p = m * t
#    print(str(m) + ' x ' + str(t) + ' = ' + str(p))

#x = 1
#while x <10:
#    print(x)
#    x = x + 1

#def currentYear():
#    print('2018')

#currentYear()

#def f (x,y):
#    return x*y

#print(f(5,8))

#answer = f(5,6)
#print(answer)

#def sum(numbers):
#    total = 0
#    for x in numbers:
#        total += x
#    return total

#print(sum((5,5,5)))

#def print_msg(msg):
#    def printer():
#        print(msg)
#    printer()

#print_msg("Hello")

#def print_msg(msg):
#    def printer():
#        print(msg)
#    return printer
#another = print_msg("Hello")
#another()

#def make_multiplier_of(n):
#    def multiplier (x):
#        return x * n
#    return multiplier

#times3 = make_multiplier_of(3)
#times5 = make_multiplier_of(5)

#print(times3(9))
#print(times5(3))
#print(times5(times5(2)))

#ratings = ['test', 1,2,3,4,5,'a','b']
#print(ratings[0])

#import re
#states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
#print(states[0:2])
#mlist = re.search("^M",states)
#print(mlist)
#x = [3,4,5]
#print(x)
#x.append(6)
#print(x)
#x.append(7)
#print(x)
#x.pop()
#print(x)
#x.pop()
#print(x)
#print(x[0])
#print(x[1])
#print(x[-1])
#y = [6,4,2]
#y.append(12)
#y.append(8)
#y.append(4)
#print(y)
#for n, i in enumerate(y):
#    if i == 4:
#        y[n] = 3
#print(y)

#x = [3,40,5,6,7,98,9,112,34,49,798]
#x.sort()
#print(x)

#xord = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
#xord.sort()
#xord = list(reversed(xord))
#print(xord)
#xord = xord[::-1]
#print(xord)
#t = [(3,6),(4,7),(5,9),(8,4),(3,1)]
#t.sort()
#print(t)
#t = list(reversed(t))
#print(t)

#x = list(range(11))
#print(x)
#x = list(range(1,101))
#print(x)
#for i in range(1,11):
#    print(i)

#for i in range(0,25,5):
#    print(i)

#for i in range(0,100,10):
#    print(i)

for l in range(1,1001):
    print(l)