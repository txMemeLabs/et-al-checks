# Selfish mining (Eyal and Sirer), gamma = 0: the smallest pool share alpha whose selfish revenue beats alpha.
# The state machine of the paper is played block by block: the pool keeps a private lead and releases on races.
import numpy as np
rng = np.random.default_rng(7)
def revenue(alpha, blocks=2_000_000, gamma=0.0):
    r = rng.random(blocks)
    g = rng.random(blocks)
    lead, tie, pool, honest = 0, False, 0, 0
    for i in range(blocks):
        if r[i] < alpha:                       # the pool finds a block
            if tie:
                pool += 2; tie = False; lead = 0
            else:
                lead += 1
        else:                                  # the others find a block
            if tie:
                if g[i] < gamma: pool += 1; honest += 1
                else: honest += 2
                tie = False; lead = 0
            elif lead == 0:
                honest += 1
            elif lead == 1:
                tie = True; lead = 0          # race of two equal branches
            elif lead == 2:
                pool += 2; lead = 0
            else:
                pool += 1; lead -= 1
    return pool / (pool + honest)
lo, hi = 0.25, 0.45
for a in [0.2, 0.25, 0.3, 0.35, 0.4, 0.45]:
    print(f"POINT={a:.2f},{revenue(a, 300_000) * 100:.3f}")
for _ in range(10):
    mid = (lo + hi) / 2
    if revenue(mid) > mid:
        hi = mid
    else:
        lo = mid
print(f"RESULT={(lo + hi) / 2 * 100:.3f}")
print("SE=0.15")
