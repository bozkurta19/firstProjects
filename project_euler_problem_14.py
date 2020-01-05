"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved
yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from time import time


def longestChainUnder(num):
    chains = dict()
    record_num = None
    record_number_of_chains = 0

    for i in range(1, num):
        original_i = i

        # 1 is for the number itself
        number_of_chains = 1

        while i != 1:
            if i in chains:
                # subtracting the number itself
                number_of_chains += chains[i] - 1
                break

            else:
                if i % 2 == 0:
                    i /= 2

                else:
                    i = i * 3 + 1

                number_of_chains += 1

        chains[original_i] = number_of_chains

        if number_of_chains > record_number_of_chains:
            record_number_of_chains = number_of_chains
            record_num = original_i

    return record_num, record_number_of_chains


start = time()

record = longestChainUnder(1000000)

end = time()

print("""Number : {}
Chain : {}
Time : {:.3f} seconds""".format(record[0], record[1], end - start))
