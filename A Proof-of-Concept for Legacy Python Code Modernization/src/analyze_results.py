import pandas as pd

df = pd.read_csv("experiments/results.csv")

print("\n=== Average Metrics by Level ===")
print(df.groupby("Level")[["Lines", "Complexity", "Pylint"]].mean())

print("\n=== Pylint Improvement Over Baseline ===")

baseline = df[df["Level"] == "Baseline"].set_index("Module")
medium = df[df["Level"] == "Medium"].set_index("Module")
high = df[df["Level"] == "High"].set_index("Module")

print("\nMedium Improvement:")
print((medium["Pylint"] - baseline["Pylint"]).mean())

print("\nHigh Improvement:")
print((high["Pylint"] - baseline["Pylint"]).mean())