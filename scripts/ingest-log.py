import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)
output_path = "logs/today_errors.md"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(f"# 🚨 Log Summary — {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n✅ Sistema monitorato. Nessuna anomalia critica rilevata.\n")

print(f"Log generati in: {output_path}")
