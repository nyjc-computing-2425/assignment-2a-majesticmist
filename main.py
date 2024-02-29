num = input('Enter a number (decimal or integer): ')
# type your code here

new_num = num.strip()
new_num = new_num.replace('.', '')
new_num = new_num.lstrip('0')


sf = len(new_num)


# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
