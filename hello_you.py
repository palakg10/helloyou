#Ask user for name
name = input("what is your name?")
print(name)
#Ask user for city
city = input ("what city you live in?")
print(city)
#Ask user what color they like
color = input("what color do you like?")
print(color)
#Ask user what they enjoy
enjoy = input( "what do you most enjoy?")
print(enjoy)
#create output text
string ="Your name is {} and you live {} city. Color you like is {} and you love is {}"
output= string.format(name,city,color,enjoy)
#Print output to screen
print(output)
 
