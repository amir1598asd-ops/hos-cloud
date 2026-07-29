
import json, time, random
from pathlib import Path

BEST = Path("best_target.py")
MEM = Path("memory.json")

score = random.randint(1, 100)
BEST.write_text(f'print("best score: {score}")\n', encoding="utf-8")
MEM.write_text(json.dumps({"best_score": score, "ts": time.time()}, indent=2), encoding="utf-8")

print(f"Done. Score = {score}")
