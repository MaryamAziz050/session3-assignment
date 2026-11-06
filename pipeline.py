import pandas as pd


def load(path="students_messy.csv"):
    # Read the CSV file into a DataFrame.
    return pd.read_csv(path)


def clean(df):
    # Make a copy so the original data is not changed.
    df = df.copy()

    # Remove extra spaces from column names and make them lowercase.
    df.columns = df.columns.str.strip().str.lower()

    # Fix city text: remove spaces and use Title Case.
    df["city"] = df["city"].str.strip().str.title()

    # Fix name text: remove spaces and use Title Case.
    df["name"] = df["name"].str.strip().str.title()

    # Change age and score to numbers; bad values like "twenty" become NaN.
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["score"] = pd.to_numeric(df["score"], errors="coerce")

    # Remove duplicate rows.
    df = df.drop_duplicates()

    # Remove rows where name or score is missing.
    df = df.dropna(subset=["name", "score"])

    # Keep only scores between 0 and 100.
    df = df[(df["score"] >= 0) & (df["score"] <= 100)]

    # Fill any missing age with the median age.
    df["age"] = df["age"].fillna(df["age"].median())

    # Reset the row numbers to 0, 1, 2, ...
    return df.reset_index(drop=True)


def add_features(df):
    # Make a copy so the input data is not changed.
    df = df.copy()

    # New column: score as a value out of 1.
    df["score_pct"] = df["score"] / 100

    # New column: 1 if city is Karachi, otherwise 0.
    df["is_karachi"] = (df["city"] == "Karachi").astype(int)

    # New column: 1 if score is 50 or more, otherwise 0.
    df["passed"] = (df["score"] >= 50).astype(int)
    return df


# Run the pipeline: load, clean, add features.
df = load()
df = clean(df)
df = add_features(df)

# Save the final data to a new CSV file.
df.to_csv("students_clean.csv", index=False)

# Show the result on screen.
print(df)
print("Saved students_clean.csv with", len(df), "rows")
