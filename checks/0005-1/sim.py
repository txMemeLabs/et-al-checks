# Bitcoin whitepaper, section 11: attacker with share q, merchant waits z blocks.
# The race counted exactly: while the honest chain finds z blocks, the attacker's block count k is negative
# binomial (each block is the attacker's with probability q). From k blocks the attacker then catches up from
# z - k behind with probability (q/p)^(z-k) (gambler's ruin); k >= z means he is already level or ahead.
import numpy as np
q = 0.3
z = 10
p = 1 - q
rng = np.random.default_rng(int(q * 1000) + z)
T = 20_000_000
def run(zz, trials):
    k = rng.negative_binomial(zz, p, size=trials)       # attacker blocks before zz honest blocks
    deficit = zz - k
    win = np.where(deficit <= 0, 1.0, (q / p) ** np.maximum(deficit, 0))
    return win.mean(), win.std(ddof=1) / np.sqrt(trials)
print("POINT=0,1.0")
for zz in range(1, z + 1):
    m, _ = run(zz, 1_000_000)
    print(f"POINT={zz},{m:.7f}")
m, se = run(z, T)
print(f"RESULT={m:.7f}")
print(f"SE={se:.7f}")
