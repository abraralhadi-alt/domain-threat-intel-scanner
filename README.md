# Domain Threat Intel Scanner

A Python-based cybersecurity tool that detects potential phishing and brand impersonation domains using domain permutation generation and DNS resolution analysis.

## Overview

This project identifies suspicious lookalike domains that may be used in phishing attacks or brand impersonation. It generates domain variations based on common typing mistakes and checks whether they are actively resolving on the internet.

## Features

- Generates typo-squatting domain variations
  - Character omission
  - Character substitution
  - Adjacent key swaps
  - Homoglyph replacements
- Performs DNS resolution checks using Python's socket library
- Identifies actively registered suspicious domains
- Lightweight implementation with no external dependencies

## How It Works

1. The user inputs a target domain (for example, google.com)
2. The tool generates multiple domain permutations
3. Each variant is checked using DNS resolution
4. Domains that resolve successfully are flagged for review

## Example

Input:
```
google.com
```

Generated variants:
```
gogle.com
gooogle.com
googel.com
goog1e.com
```

Output:
```
Active domain detected: googel.com -> 93.184.216.34
```

## Technologies Used

- Python 3
- socket library
- string handling

## Project Structure

```
domain-threat-intel-scanner/
├── scanner.py
├── README.md
├── .gitignore
├── LICENSE
```

## Getting Started

### Clone the repository
```bash
git clone https://github.com/abraralhadi-alt/domain-threat-intel-scanner.git
cd domain-threat-intel-scanner
```

### Run the tool
```bash
python scanner.py
```

## Purpose

This project is intended for educational and defensive cybersecurity use only, focusing on phishing detection and domain intelligence techniques.

## License

This project is licensed under the MIT License.
