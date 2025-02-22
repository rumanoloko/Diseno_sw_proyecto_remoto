from math import comb

n = 10
p = 0.05  # Probabilidad de fallo
q = 1 - p

prob = sum(comb(n, k) * (p**k) * (q**(n-k)) for k in range(3))
print(f"La probabilidad de fallar como máximo 2 veces es: {prob:.10f}")

from math import comb

n = 10
p = 0.95  # Probabilidad de fallo
q = 1 - p
w2 = 0
print("========")
for k in [8, 9, 10]:
    w = comb(n, k) * (p**k) * (q**(n-k))
    print(w)
    w2 += w
print(w2)
