# Refugium odds: n carriers and one hazard draw i.i.d. lifetimes; the line survives if a carrier outlasts the hazard.
import numpy as np
rng = np.random.default_rng(20261118)
T = 2_000_000
last = None
for n in range(1, 11):
    life = rng.exponential(size=(T, n + 1))          # column 0 = the hazard
    survived = life[:, 1:].max(axis=1) > life[:, 0]
    p = survived.mean() * 100
    se = survived.std(ddof=1) / np.sqrt(T) * 100
    print(f"POINT={n},{p:.4f}")
    last = (p, se)
print(f"RESULT={last[0]:.4f}")
print(f"SE={last[1]:.4f}")
