# Ethereum: an epoch is 32 slots of 12 seconds. Its length in minutes, by adding the slots one by one.
slot_seconds = 12
slots = 32
t = 0
for s in range(1, slots + 1):
    t += slot_seconds
    if s % 4 == 0:
        print(f"POINT={s},{t / 60:.2f}")
print(f"RESULT={t / 60:.4f}")
