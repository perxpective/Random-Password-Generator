# Random-Password-Generator
Generate a random secure password. 

I import the `random` module so I can use it to generate random characters in the character. I also begin to declare the `password` variable, which will be used to consolidate all generated characters into a string.

```python
import random
password = ''
```

I print out the user prompt and menu to ask the user whether he/she wants only an alphanumberic password or a password with special characters inclusive.

```python
print('[1] alphanumeric only')
print('[2] with special characters')
imput = input('select option: ')
```

Users can decide how long their password can be. However, they must have a password with more than 8 characters.

```python
num  = int(input('enter number of characters for password [must be more than 8 char]: ' ))
while num < 8:
    print('password length must be more than 8 char')
    num  = int(input('enter number of characters for password [must be more than 8 char]: ' ))
```

A `while` loop is initiated to ensure input validation.

### Generating the password
If the user chooses the second option (random password with special characters), a `for` loop is initiated for a character is in the range of the `num` (the inputted length of password). Each iteration, a new random value is generated.

> A random number is generated using the `random.randint()` function within the range of ASCII values of all characters found in the keyboard. After which, these numbers will be converted into ASCII characters using the `chr()` function. Characters are stitched together in the `password` variable.

```python
if imput == '2':
    for i in range(num):
        char_num = random.randint(33,126)
        password += chr(char_num)
```

If the user chooses the first option (alphanumeric), a `for` loop is initated for a character is in the range of the `num`. Each iteration, a new random value is generated. However, we only want uppercase, lowercase letters and numbers. As such, we have a `random.randint()` function each with a range of numerical values in the ASCII table where only uppercasse letters, lowercase letters and numbers are retrieved. Then I put them into a list with a random index retieving a random type of uppercase letter/lowercase letter/number from the list.

```python
elif imput == '1':
    for i in range(num):
        numbers = random.randint(48,57)
        upper_case = random.randint(65,90)
        lower_case = random.randint(97,122)
        char_list = [numbers, upper_case, lower_case]
        password += chr(char_list[random.randint(0,2)])
```
Now, I can output the final password:
```python
print('Password:')
print(password)
```

## Dry Runs
```
[1] alphanumeric only
[2] with special characters
select option: 1
enter number of characters for password [must be more than 8 char]: 10
Password:
RQA83QLpIK
```

```
[1] alphanumeric only
[2] with special characters
select option: 2
enter number of characters for password [must be more than 8 char]: 20
Password:
*nT,-|cAkiq:$KN;}-2n
```


```
[1] alphanumeric only
[2] with special characters
select option: 1
enter number of characters for password [must be more than 8 char]: 30
Password:
tSaTx9p445pVamZjkx8OwhGYt435Au
```
