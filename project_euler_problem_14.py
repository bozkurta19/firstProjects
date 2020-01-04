from time import time


def longest_chain_under(num):
    chains = dict()
    record_num = None
    record_chain = 0

    for i in range(1,num):
        original = i
        chain = 1

        while i != 1:
            if i in chains:
                chain += chains[i] - 1
                break

            else:
                if i % 2 == 0:
                    i /= 2

                else:
                    i = i * 3 + 1

            chain += 1

        chains[original] = chain

        if chain > record_chain:
            record_chain = chain
            record_num = original


    return  record_num,record_chain


start = time()

records = longest_chain_under(1000000)

end = time()

print("""Number : {}
Chain : {}
Time : {:.3f} seconds""".format(records[0],records[1],end - start))