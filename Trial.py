#firstName = "shashikant"
#lastName = "vishwakarma"
#nerds = ["her","fur","pur"]
#sequence = (firstName,lastName)
#name = "_".join(nerds)
#print(name)
#s = "its,a,swan,song"
#words = s.split()
#print(words)
#print(len(words))
#print(len(s))
#word = "Easy"
#x = list(word)
#print(x)
#print(list(s))
import random
from collections import Counter
#print(random.random())
#print(random.randrange(0,10))
#print(random.uniform(8,12))
#print (random.random(), random.random(),random.random())
for _ in range(100):
    value = random.random()
 #   print(value)
    
ctr = Counter(value)
print("list: ",ctr)