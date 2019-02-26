# Counting the number of bases
def count_let(seq):
    """Computing the number of As in the sequence"""
    result_a = 0
    result_c = 0
    result_g = 0
    result_t = 0

    for b in seq:
        if b == 'A':
            result_a += 1
        elif b == 'C':
            result_c += 1
        elif b == 'G':
            result_g += 1
        elif b == 'T':
            result_t += 1

    return {"As": result_a, "Cs": result_c, "Gs": result_g, "Ts": result_t}
