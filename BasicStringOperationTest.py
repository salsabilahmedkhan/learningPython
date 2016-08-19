astring = "Hello World!"
astring2 = 'Hello World!'

print ("Single quotes are ''")
print(len(astring))

print(astring.index("o"))
print(astring.count("l"))

print (astring[3:7])
print(astring[3])
print(astring[:7])
print(astring[3:])
print(astring[3:7:2])
print(astring[3:7:1])
print(astring[::-1])
print(astring[-3])
print(astring[3:7:2])

print(astring.upper())
print(astring.lower())
print(astring.startswith("Hello"))
print(astring.endswith("ahjkdsfh"))

afewwords=astring.split(" ")
print(afewwords)
