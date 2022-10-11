def run_timing()->None:
    """Asks the user repeatedly for numeric input. Prints the average time and
    number of runs."""
    
    numbers_of_runs = 0
    total_time = 0
    
    while True:
        one_run = input('Enter 10 km run time: ')
        
        if not one_run:
            break
        
        numbers_of_runs += 1
        total_time += float(one_run)
        
    average_time = total_time / numbers_of_runs
    
    print(f'Average of {average_time}, over {numbers_of_runs} runs')
    
    
def crop_float(number: float, before: int=0, after: int=None)->float:
    
    number %= 10 ** before
    number = round(number, after)
    print(number)


def sum_decimal()->None:
    import decimal
    float1 = decimal.Decimal(input('Input numbers 1: '))
    float2 = decimal.Decimal(input('Input numbers 2: '))
    print(float1 + float2)
    

if __name__ == '__main__':
    # run_timing()
    # crop_float(1234.5678, 2, 3)
    sum_decimal()
    print(0.1 + 0.2)
    