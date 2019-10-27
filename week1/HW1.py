project = "cake"
print (project)
difficulty = 3
int(difficulty)
ingredients = ["flour", "butter", "sugar", "eggs", "cocoa powder", "baking powder"] 
print (ingredients)
print ("apple" in ingredients)
print ("butter" in ingredients)
has_margarine_or_eggs   = ('margarine' in ingredients) or ('eggs' in ingredients)
has_margarine_and_eggs  = ('margarine' in ingredients) and ('eggs' in ingredients)
print(has_margarine_or_eggs)
print(has_margarine_and_eggs)
flour = 175
butter = 175
sugar = "100g"
eggs = 2
cocoa_powder = "1ts"
baking_powder = 0.5
print('Flour - ', flour)
print('Butter - ', butter)
print('Sugar - ', sugar)
print('Eggs - ', eggs)
print('Cocoa Powder - ', cocoa_powder)
print('Baking Powder - ', baking_powder)
a = 15
b = 8
c = 2
d = 5*a**2 - a*b + (a%2) - a/5
print (d)
e = (b**3 + 3*a*b - 10*c)
print (e)
num = int(input('Number: '))
is_even = num % 2 == 0
print('Number is', (is_even is True and 'even') or 'odd')
