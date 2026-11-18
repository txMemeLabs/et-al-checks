# Push gossip: each round every informed node tells one node picked uniformly at random. Rounds until all
# n = 10,000 nodes know, averaged over many runs.
import numpy as np
rng = np.random.default_rng(8)
n = 10_000
runs = 2_000
rounds = []
curve = None
for t in range(runs):
    known = np.zeros(n, dtype=bool); known[0] = True
    r = 0; trace = []
    while not known.all():
        senders = np.flatnonzero(known).size
        known[rng.integers(0, n, size=senders)] = True
        r += 1
        if t == 0: trace.append(known.sum())
    rounds.append(r)
    if t == 0: curve = trace
for i, k in enumerate(curve):
    print(f"POINT={i + 1},{k / n * 100:.2f}")
rounds = np.array(rounds, dtype=float)
print(f"RESULT={rounds.mean():.4f}")
print(f"SE={rounds.std(ddof=1) / np.sqrt(runs):.4f}")
