import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\Third\djinni-scraping-and-analysis\scrape_djinny\vacancies.csv"
df = pd.read_csv(file_path)

df_technologies = (
    df["technologies"]
    .str.split(",\s*", expand=True)
    .stack()
    .reset_index(level=1, drop=True)
    .rename("technology")
)
df_split = df.drop("technologies", axis=1).join(df_technologies)

technology_counts = df_split["technology"].value_counts()

plt.figure(figsize=(10, 6))
technology_counts.head(30).plot(kind="bar", color="skyblue")
plt.title("Top 10 Popular Technologies in Job Vacancies")
plt.xlabel("Technology")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
