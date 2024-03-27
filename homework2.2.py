x = 38
print('здравствуйте')
if x < 0:
     print('меньше нуля')
print('до свидания')

a, b = 10, 5
if a > b:
     print('a > b')

if a > b and a > 0:
     print('OK')

if (a > b) and (a > 0 or b < 1000):
     print('OK')

if 5 < b and b < 10:
     print('OK')

if '34' > '123':
     print('OK')

if '123' > '12':
     print('OK')

if [1,2] > [1,1]:
     print('OK')

# что нельзя сравнивать - разные типы
#if '6' > 5:
    #print('OK')

#f [5,6] > 5:
     #print('OK')

# но
#if '6' != 5:
     #print(OK)