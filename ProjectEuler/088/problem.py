limit = 12000

minimal = [999999999] * (limit + 1)

def generate(product, total, count, start):
    #product: product of the factors >= 2
    #total: sum of those factors
    #count: number of factors >= 2

    num_ones = product - total
    k = count + num_ones

    if k <= limit:
        minimal[k] = min(minimal[k], product)

    for factor in range(start, limit + 1):
        new_product = product * factor

        # check if we are above our limit
        if new_product > limit * 2:
            break

        new_total = total + factor
        new_count = count + 1
        new_num_ones = new_product - new_total
        new_k = new_count + new_num_ones

        if new_k > limit:
            break

        generate(new_product, new_total, new_count, factor)


generate(1, 0, 0, 2)

result = sum(set(minimal[2:]))

print(result)
