# Assignment 3: Data Processing Pipeline

This project cleans a messy student CSV file and adds new columns to it.

## Files

- `pipeline.py` - the main code.
- `test_pipeline.py` - a pytest test for the pipeline.
- `students_messy.csv` - the input file (messy data).
- `students_clean.csv` - the output file (clean data).

## What the code does

1. `load()` reads `students_messy.csv`.
2. `clean()` fixes the data:
   - Removes extra spaces from names and cities.
   - Makes names and cities Title Case (for example, `" karachi"` becomes `Karachi`).
   - Changes age and score to numbers (bad values like `twenty` become missing).
   - Removes duplicate rows.
   - Removes rows with a missing name or score.
   - Keeps only scores from 0 to 100.
3. `add_features()` adds new columns:
   - `score_pct` - score out of 1 (80 becomes 0.80).
   - `is_karachi` - 1 if the city is Karachi, otherwise 0.
   - `passed` - 1 if the score is 50 or more, otherwise 0.
4. The result is saved as `students_clean.csv`.
