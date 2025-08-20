# 🌦️ Quadratic Weather Modeling

This project models temperature variation over time using a quadratic equation of the form:

<div align="center">
$$
T(t) = at^2 + bt + c
$$
</div>

where:
- **t** is the time (in days, hours, etc.)
- **a, b, c** are coefficients

---

## ✅ Stage-wise Implementation
We’ll write 4 versions of the program:
1. **Hard-coded values**
2. **Keyboard input**
3. **Read from file (one set of inputs)**
4. **Read from file (multiple sets of inputs)**

---

## 📂 Files

```text
weather_model_quadratic/
│
├── version1_hardcoded.py           # Uses hardcoded coefficients
├── version2_keyboard_input.py      # Takes coefficients from keyboard input
├── version3_file_input_single.py   # Reads coefficients from inputs_single.txt
├── version4_file_input_multiple.py # Reads multiple sets of coefficients from inputs_multiple.txt
├── inputs_single.txt               # Contains one set of a, b, c values
├── inputs_multiple.txt             # Contains multiple sets of a, b, c values
└── README.md                       # Project documentation
```

---

📊 Output
The program will display line plots:
X-axis → Time (0–10)
Y-axis → Calculated Temperature
Each curve represents one set of (a, b, c) coefficients

✨ Example:
Version 1 → 1 curve (hardcoded)
Version 2 → 1 curve (user input)
Version 3 → 1 curve (from file)
Version 4 → Multiple curves with legends
