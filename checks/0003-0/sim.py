# Birthday problem: 23 people, 365 equally likely birthdays; share of groups with at least one shared birthday.
import numpy as np
rng = np.random.default_rng(23)
T = 2_000_000
for k in range(5, 41, 5):
    g = np.sort(rng.integers(0, 365, size=(200_000, k)), axis=1)
    print(f"POINT={k},{(np.diff(g, axis=1) == 0).any(axis=1).mean() * 100:.3f}")
hits = 0
for _ in range(T // 200_000):
    g = np.sort(rng.integers(0, 365, size=(200_000, 23)), axis=1)
    hits += int((np.diff(g, axis=1) == 0).any(axis=1).sum())
p = hits / T
print(f"RESULT={p * 100:.4f}")
print(f"SE={np.sqrt(p * (1 - p) / T) * 100:.4f}")
