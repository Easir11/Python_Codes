input_x=input('Enter Val: 1')
input_y=input('Enter Val: 2')

if(input_x!=input_y and input_y>=0 and input_x>=0):
    print(f'Addition: {input_x+input_y}')
    print(f'Subtraction: {input_x-input_y}')
    print(f'Multiplication: {input_x*input_y}')
    if(input_y!=0):
        print(f'Division: {input_x/input_y}')
    print(f'Power: {input_x**input_y}')

elif(input_x==0 or input_y==0):
    input_x+=input_x
    input_y+=input_y

    