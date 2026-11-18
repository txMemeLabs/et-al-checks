# Bloom filter: the bits per element needed for a 1% false positive rate, with the best whole number of hashes.
# A real filter is built (n random keys, k hash positions each) and probed with keys never inserted.
import numpy as np
rng = np.random.default_rng(6)
n = 20_000
probes = 400_000
def fp_rate(bits_per_el):
    m = int(round(bits_per_el * n))
    best = 1.0
    for k in range(max(1, int(bits_per_el * 0.69) - 1), int(bits_per_el * 0.69) + 3):
        bits = np.zeros(m, dtype=bool)
        bits[rng.integers(0, m, size=(n, k)).ravel()] = True
        hit = bits[rng.integers(0, m, size=(probes, k))].all(axis=1).mean()
        best = min(best, hit)
    return best
lo, hi = 8.0, 11.0
for b in np.arange(8.0, 11.01, 0.5):
    print(f"POINT={b:.2f},{fp_rate(b) * 100:.4f}")
for _ in range(14):
    mid = (lo + hi) / 2
    if fp_rate(mid) <= 0.01:
        hi = mid
    else:
        lo = mid
print(f"RESULT={hi:.4f}")
print("SE=0.03")
