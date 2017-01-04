def digital_root(n):
    # code to compute sum of digits in any given number
    sum = 0
    nString = str(n)
    for digit in nString:
        sum = sum + int(digit)
    
    print 'digital root:' + str(sum)


digital_root(123)
