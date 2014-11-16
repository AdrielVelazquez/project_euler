def get_abundant_numbers(limit):
    '''
    abundant limits only increment by 2, 4, or 6
    This function increments by 2
    '''
    all_nums = {x for x in range(281240)}
    abundant = []
    for num in range(12, limit, 2):
        total = 0
        for divisor in range(1, num):
            if num%divisor == 0:
                total += divisor
            if total > num:
                for value in abundant:
                    all_nums.discard(value + num)
                abundant.append(num)
                break
    sum = 0
    for item in all_nums:
        sum += item

    return sum


print get_abundant_numbers(281240)