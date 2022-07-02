name = str(input('Input your name: '))
print(f'Enter your name: {name}')
display = int(input('Input number of times to display: '))
if name == '':
    print("No name entered")
else:
    for i in range(display):
        print(name)