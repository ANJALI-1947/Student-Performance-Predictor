import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/StudentsPerformance.csv")

plt.scatter(df["reading score"], df["math score"])

plt.xlabel("Reading Score")
plt.ylabel("Math Score")
plt.title("Reading Score vs Math Score")

plt.show()