import pandas as pd

df = pd.read_excel("https://osf.io/download/jyh2u/", usecols=['DOI', 'include'])

# adjust columns
df["DOI"] = df["DOI"].str.extract(r"(10.\S+)")
df['id_type'] = 'doi'

# rename columns
df.rename({'include': 'label_included', 'DOI': 'id'}, axis=1, inplace=True)

# drop missing ids
df.dropna(subset=["id"], inplace=True)

# drop duplicate DOIs
df.drop_duplicates(subset=['id'])

# export
df.to_csv("Savas_ids.csv", columns=['id', 'id_type', 'label_included'], index=False)
