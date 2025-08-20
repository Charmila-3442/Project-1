# 🌦️ Quadratic Weather Modeling

This project models temperature variation over time using a quadratic equation of the form:

\[
T(t) = at^2 + bt + c
\]

where:
- **t** is the time (in days, hours, etc.)
- **a, b, c** are coefficients loaded from a CSV file

---

## 📂 Files
- **abc_values_20rows.csv** → Contains 20 rows of random `a`, `b`, `c` values (each below 10).
- **weather_model.py** → Python script that reads the CSV, computes temperature values, and plots the curves.
- **weather_modeling.ipynb** → Jupyter Notebook version of the same process.

---

## ⚙️ Requirements
Install dependencies:

```bash
pip install matplotlib pandas
