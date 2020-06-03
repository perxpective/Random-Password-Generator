import random
password = ''
print('===========================================================')
print('--[][][]---[][][]]-[]---[]--[][]---[][][]--[]----[]--[][][]')
print('--[]----[]-[]---[]-[][]-[]--[]--[]---[]----[][]--[]----[]--')
print('--[][][]---[][][]]-[]-[][]--[]--[]---[]----[]-[]-[]----[]--')
print('--[]--[]---[]---[]-[]--[]]--[]--[]---[]----[]--[][]----[]--')
print('--[]---[]--[]---[]-[]---[]--[][]---[][][]--[]---[[]----[]--')
print('===========================================================')
print('GENERATOR \t\t\t\t\t\t\t\t @perxpective.jpeg')
print()
print()
print('[1] alphanumeric only')
print('[2] with special characters')
imput = input('select option: ')
num  = int(input('enter number of characters for password [must be more than 8 char]: ' ))
while num < 8:
    print('password length must be more than 8 char')
    num  = int(input('enter number of characters for password [must be more than 8 char]: ' ))

if imput == '2':
    for i in range(num):
        char_num = random.randint(33,126)
        password += chr(char_num)
elif imput == '1':
    for i in range(num):
        numbers = random.randint(48,57)
        upper_case = random.randint(65,90)
        lower_case = random.randint(97,122)
        char_list = [numbers, upper_case, lower_case]
        password += chr(char_list[random.randint(0,2)])
        
print('Password:')
print(password)

    


