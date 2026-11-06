from pipeline import load, clean, add_features


def test_pipeline():
    # Step 1: load the real messy file.
    df = load("students_messy.csv")

    # Step 2: clean the data.
    df = clean(df)

    # Step 3: add the new columns.
    df = add_features(df)

    # 7 rows in the file; duplicate, missing score and missing name are removed.
    assert len(df) == 4

    # Names left are Ali, Sara, Hina, Bilal.
    assert list(df["name"]) == ["Ali", "Sara", "Hina", "Bilal"]

    # City names are clean.
    assert list(df["city"]) == ["Karachi", "Karachi", "Lahore", "Lahore"]

    # Score as a value out of 1.
    assert list(df["score_pct"]) == [0.80, 0.92, 0.72, 0.38]

    # Ali and Sara are from Karachi, so they get 1.
    assert list(df["is_karachi"]) == [1, 1, 0, 0]

    # Hina, Ali and Sara have 50 or more, so passed is 1. Bilal has 38, so 0.
    assert list(df["passed"]) == [1, 1, 1, 0]

    # Age has no missing values.
    assert df["age"].isna().sum() == 0
