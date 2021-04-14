signs = ['+', '-', '*', '/', '**', '%']
result = input()
if result.isdigit():
    result = float(result)
    line = input().split(' ')
    while line[0] != '=':
        if len(line) == 2:
            if line[0] in signs:
                if line[1].isdigit():
                    if line[0] == '+':
                        result += float(line[1])
                    elif line[0] == '-':
                        result -= float(line[1])
                    elif line[0] == '*':
                        result *= float(line[1])
                    elif line[0] == '/':
                        if float(line[1]) != 0:
                            result /= float(line[1])
                        else:
                            print('Деление на 0 запрещено!')
                    elif line[0] == '**':
                        result **= float(line[1])
                    elif line[0] == '%':
                        result %= float(line[1])
                else:
                    print('Введите строку формата: [Знак мат. операции] [число]')
            else:
                print('Введите строку формата: [Знак мат. операции] [число]')
        else:
            print('Введите строку формата: [Знак мат. операции] [число]')
        line = input().split(' ')
    print(result)
else:
    print('Введите число')
