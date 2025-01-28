def count_multiples(a, b, c):
    if c == 0:
        return 0 
    if a <= b:
        start = a
        end = b
    else:
        start = b
        end = a
    multiples_end = end // c
    multiples_start = (start - 1) // c
    count = multiples_end - multiples_start
    return count