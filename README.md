# et al. checks

Every check of [et al.](https://etal.example) lives here: `checks/<n>-<attempt>/plan.json` (the claim, the source,
the assumptions, the claimed number) and `checks/<n>-<attempt>/sim.py` (the code). The workflow `check` runs the
code in a container with no network, one CPU, 2 GB of memory and a 10 minute kill, and prints `RESULT=`.
The keeper reads that line from the run log and compares it with the claimed number by a fixed rule.

Nothing here runs on the keeper's machine. Pull requests do not trigger anything.
