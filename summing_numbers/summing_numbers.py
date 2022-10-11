
def mysum(*numbers, start:int=0) -> int:
    output = start
    
    for number in numbers:
        output += number
        
    return output


def average(*numbers):
    output = 0
    
    for number in numbers:
        output += number
    
    return output / len(numbers)


def lengths(*words):
    count = len(words)
    min_len = 20
    max_len = 0
    avg_len = 0
    
    for word in words:
        len_word = len(word)
        avg_len += len_word
        if len_word < min_len:
            min_len = len_word
        if len_word > max_len:
            max_len = len_word
        
    return min_len, max_len, int(avg_len/count)


def sum_objests(*args):
    pass


if __name__ == '__main__':
    print(mysum(1, 2, 3))
    print(average(1, 2, 3))
    print(lengths('hello', 'world', 'hi', 'there'))