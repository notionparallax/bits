import itertools


def erat2():
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x & 1):
                x += p
            D[x] = p


def get_primes_erat(n):
    return list(itertools.takewhile(lambda p: p < n, erat2()))


def get_prime_string(n):
    prime_list = get_primes_erat(n)
    return "".join([str(s) for s in prime_list])


primes = get_prime_string(20000)
ids = []


def answer(n):
    newID = primes[n:n+5]
    if newID not in ids:
        ids.append(newID)
        return newID
    else:
        return False


for i in range(10000):
    ids.append(answer(i))

print len(ids)
print len(set(ids))

print "a", answer(10000)
