def fun_calc(num1,num2,operator):
    if operator == '*':
        result = num1 * num2
        print(f"fun_calc({num1},{num2},'{operator}') Product:")
        print(result)
        print(f'Process: {num1}{operator}{num2}={result}')
fun_calc(50,2,'*')

