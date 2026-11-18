# Birthday attack on a 32-bit hash: values drawn uniformly from 2^32 until the first repeat; the 50% point is
# the median of that count.
import numpy as np
rng = np.random.default_rng(11)
N = 2 ** 32
trials = 4_000
firsts = []
for _ in range(trials):
    x = rng.integers(0, N, size=300_000, dtype=np.uint64)
    _, idx, inv = np.unique(x, return_index=True, return_inverse=True)
    dup = np.flatnonzero(idx[inv] != np.arange(x.size))
    firsts.append(dup[0] + 1 if dup.size else x.size)
firsts = np.sort(np.array(firsts, dtype=float))
for q in range(5, 100, 5):
    print(f"POINT={firsts[int(q / 100 * trials)]:.0f},{q}")
med = np.median(firsts)
se = 1.2533 * firsts.std(ddof=1) / np.sqrt(trials)
print(f"RESULT={med:.1f}")
print(f"SE={se:.1f}")
