name = 'Denis'
years_old = 18
billion_number = 1000000000

if __name__ == '__main__':
    print(f'My name is {name}. I\'m {years_old} years old.')
    print(f'My name is {name.upper()}. I\'m {years_old * 2} years old.')
    print(f'{years_old = }')
    print(f'{years_old:b}')
    print(f'{years_old:.10f}')
    print(f'{years_old:10}')
    print(f'{years_old:010}')
    print(f'{years_old:^10}')
    print(f'{years_old:>10}')
    print(f'{years_old:<10}')
    print(f'{years_old:=^10}')
    print(f'{years_old:0<10}')
    print(f'{years_old:0<10}')
    print(f'{billion_number:,}')
    print(f'Result = {min(billion_number, years_old)}')
    print(f'{years_old / billion_number:.10%}')
