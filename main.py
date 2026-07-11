from config.loader import load_topics
from output.report import build_daily_report
from line.push import push_text

config = load_topics()

results = []

results.append("🩺 GMIA started successfully.")
results.append("")

results.append("Languages:")
for language in config["languages"]:
    results.append(f"• {language}")

results.append("")
results.append("Topics:")

for disease in config["diseases"]:
    results.append(f"• {disease}")

message = build_daily_report(results)

print(message)

push_text(message)
