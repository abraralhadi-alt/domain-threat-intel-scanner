# Domain Threat Intel Scanner

A Python-based cybersecurity tool that detects potential phishing and brand impersonation domains using domain permutation generation and DNS resolution analysis.

## Overview

This project identifies suspicious lookalike domains that may be used in phishing attacks or brand impersonation. It generates domain variations based on common typing mistakes and checks whether they are actively resolving on the internet.

## Features

- Generates typo-squatting domain variations:
  - Character omission
  - Character substitution
  - Adjacent key swaps
  - Homoglyph replacements
- Performs DNS resolution checks using Python's socket library
- Identifies actively registered suspicious domains
- Lightweight implementation with no external dependencies

## How It Works

1. The user inputs a target domain (e.g., google.com)
2. The tool generates multiple domain permutations
3. Each variant is checked using DNS resolution
4. Active domains are flagged for review

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

### Requirements
- Python 3

This project uses only Python standard libraries, so no external dependencies are required.

### Clone the repository

```bash
git clone https://github.com/abraralhadi-alt/domain-threat-intel-scanner.git
cd domain-threat-intel-scanner
```

### Run the tool

```bash
python scanner.py
```

## Usage

Enter a domain name without the TLD when prompted:

```
Enter domain (without TLD): google
```

The tool will:
- Use `.com` as the default TLD
- Generate domain permutations
- Scan DNS availability for the first 15 results

## Example Output

```
g0ogle.com    | ACTIVE (IP: 142.250.x.x)
ggoogle.com   | ACTIVE (IP: 142.250.x.x)
giogle.com    | INACTIVE
```

## Purpose

This project is intended for educational and defensive cybersecurity use only, focusing on phishing detection and domain intelligence techniques.

## Limitations

- Does not analyze website content or detect phishing behavior
- Only performs DNS resolution checks
- “ACTIVE” means the domain resolves to an IP address, not that it is malicious

## License

This project is licensed under the MIT License.
