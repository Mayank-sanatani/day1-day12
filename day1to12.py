print("hello my name is \"mayank sharma\"\nand i am from UP")

# and today i am here to start my coding journey
# moreover i know this may take some time
# but i beleive i can

a=568
b=True
c="mayank"
d=None
print(a)
print(b)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print("my full adress is")
print("chhutmalpur" ,"saharanpur",6,"up", sep="~")

print("my full adress is")
print("chhutmalpur","saharanpur", "6", "up",sep=",")

tuple1=(("parrot","sparrow"), ("lion" , "king"))
print(tuple1)
# # but if i close this with curly or big bracket then it become set and list respectively

dict1={"name":"mayank","age":18}
print(dict1)

a="1"
b="4"
print(int(a)+int(b))

name="mayank"
print(name[0])
print(name[1])
print(name[2])
# but this take much time so for this  we have a trick
# also for this we have to use this as it is also we have to leave a space before print
for character in name :
 print(character)

# if we want to get more than one number we can  use upcoming method but remember that first letter should be 0 and after semicolon just plus 1 to the digit you want to print also we have to count space and commas in numbers
names="mayank, sharma"
print(names[0:7])
# also for calculating their number of words just write it as
print(len(names))

name="mayank"
print(name[0:-3])
# for minus we simply subtract total number with that given digit number
print(name[0:len(name)-3])
# the line 50 and 51 is just same
print(name[-1:len(name) - 3])
print(name[-3:-1])

# Quick Quiz:
nm = "aditya"
print(nm[-4:-2])

# strings are immutable 
# means they dont resist changes
a = "!!!Harry!! !!!!!!!!"
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "mayank"))
print(a.replace("!", ""))