# 🇺🇸 NATO Phonetic Alphabet Converter

A Python script that converts each letter in a name into its corresponding NATO phonetic alphabet code. Built with robust error handling, input validation, and user-friendly feedback to ensure reliability in real-world usage.

## 🚀 Features

- ✅ Converts each letter in a name to its NATO phonetic equivalent (e.g., "A" → "Alpha")
- 🛡️ Handles edge cases including:
  - Empty or whitespace-only input
  - Non-alphabetic characters (numbers, symbols)
  - Invalid letters (e.g., "1", "!", "ö")
- 📂 Loads phonetic data from a CSV file (`nato_phonetic_alphabet.csv`)
- 📝 Includes clear warnings and user feedback for skipped characters
- 🧪 Graceful error handling for missing files or unexpected input

## 📂 Project Structure

```
nato_phonetic_converter/
│
├── nato_phonetic_alphabet.csv        # Source data file (standard NATO phonetic alphabet)
├── main.py                           # The core script (this file)
└── README.md                        # Project documentation
```

## 📝 How to Use

1. Ensure you have the `nato_phonetic_alphabet.csv` file in the same directory as `main.py`.
2. Run the script:
   ```bash
   python main.py
   ```
3. Enter your name when prompted (e.g., `John Smith`).
4. The script will output the NATO phonetic codes for each valid letter.

> Example Output:
> ```
> Enter your name: John Smith
> NATO phonetic codes: ['Juliet', 'Oscar', 'Hotel', 'India', 'Sierra', 'Tango', 'Mike']
> ```

## ⚠️ Edge Case Behavior

| Input | Behavior |
|------|---------|
| `""` or `"   "` | Empty input → "No name entered. Exiting." |
| `"John123"` | Skips `1`, `2`, `3` with a warning; processes `J`, `o`, `h`, `n` |
| `"Zzz!"` | Skips `!`, processes `Z` (if valid), warns about non-letters |
| Missing CSV file | Prints error and exits gracefully |

## 🛠️ Requirements

- Python 3.7+
- `pandas` library (install via `pip install pandas`)

## 💡 Why This Matters

This tool demonstrates practical programming principles:
- Input validation and user experience (UX)
- Error resilience in real-world data
- Clean, modular code with clear feedback
- Use of real-world data (NATO phonetic alphabet)

Ideal for beginners learning data processing, input handling, and exception management in Python.

## 📚 License

MIT License — Feel free to use, modify, and distribute.

## 🚀 Contributing

Contributions are welcome! Please open an issue or submit a pull request for:
- Bug fixes
- New features (e.g., support for international characters)
- Improved UX (e.g., CLI interface, GUI, or JSON output)

## 📣 Contact

For questions or feedback, reach out via GitHub issues or email [me](mailto:whoknows.camping830@passinbox.com).

---

> 🎯 Built with care. Simple. Reliable. Real-world ready.