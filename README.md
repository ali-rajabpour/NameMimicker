# Mimicker - Advanced Character Set Mimicking Tool

A powerful and sophisticated character set mimicking tool designed for CEH certified security research and homoglyph analysis.

## Overview

Mimicker is a Python-based tool designed for CEH certified researchers to generate advanced lookalike strings using different Unicode character sets. It transforms regular text into visually identical strings using alternative character sets (Cyrillic, Greek, Mathematical symbols, etc.) and implements various advanced obfuscation techniques to help researchers understand and test against homoglyph-based attacks.

## Features

### Basic Features
- Generate lookalike strings using different character sets
- Maintain the visual appearance of the original string, including capitalization
- Create mixed character set versions for more complex mimicking
- Easy-to-use command-line interface and interactive menu

### Advanced Features
- **Zero-Width Character Insertion**: Add invisible characters to break pattern matching
- **Combining Diacritical Marks**: Stack additional Unicode marks on characters
- **Bidirectional Text Manipulation**: Apply RTL override and other bidirectional text controls
- **Stealth Score Analysis**: Calculate detection evasion metrics
- **Export Capabilities**: Save results to JSON for further analysis
- **Unicode Representation**: View hex codes and Unicode character names
- **Extreme Obfuscation**: Combine multiple techniques for maximum evasion

## Requirements

- Miniconda or Anaconda
- Python 3.10 (automatically installed in the conda environment)

```bash
conda create -y -n mimicker python=3.10
conda activate mimicker
```

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Run the setup script:

```bash
cd mimicker
chmod +x mimicker.sh
./mimicker.sh setup
```

## Usage

### Using the Interactive Menu

The easiest way to use Mimicker is through its interactive menu:

```bash
./mimicker.sh menu
```

or simply:

```bash
./mimicker.sh
```

### Command Line Usage

```bash
# Basic usage
./mimicker.sh run "Apple"

# Advanced features (zero-width chars, combining marks, BIDI controls)
./mimicker.sh advanced "Apple"

# Export results to a JSON file
./mimicker.sh export "Apple" results.json

# Show help information
./mimicker.sh help

# Setup the environment
./mimicker.sh setup
```

### Python Script Direct Usage

If you prefer to use the Python script directly:

```bash
# Activate the conda environment
conda activate mimicker

# Basic usage
python mimicker.py --string "Apple"

# Advanced features
python mimicker.py --string "Apple" --advanced

# Show stealth scores
python mimicker.py --string "Apple" --advanced --scores

# Export to JSON
python mimicker.py --string "Apple" --advanced --export results.json

# Or run it interactively
python mimicker.py
```

## How It Works

### Character Set Mimicking
Mimicker uses a comprehensive database of lookalike characters from various Unicode character sets to replace Latin characters. The tool preserves the visual appearance of the text while changing the underlying character codes.

### Advanced Obfuscation Techniques

#### Zero-Width Characters
Zero-width characters are invisible but affect text processing. They can be used to insert characters into a string without visibly changing its appearance, making it difficult for pattern matching to detect the original string.

#### Combining Diacritical Marks
Unicode combining marks can be stacked on characters to slightly alter their appearance while keeping them recognizable. This technique can confuse character-level detection systems.

#### Bidirectional Text Controls
Bidirectional text control characters can change the display direction of text, creating strings that look normal but behave unexpectedly in different contexts.

#### Stealth Scoring
The tool includes an algorithm to evaluate how likely a generated string is to evade detection systems. This score considers factors like:
- Character diversity
- Usage of non-ASCII characters
- Presence of invisible characters
- Mix of different Unicode blocks

## Example Output

For the input string "Apple":

```
==================================================
MIMICKER RESULTS
==================================================
Original:      Apple
Mixed charset: Αpplе
Charset 1:     Αρρlе
Charset 2:     𝐀𝐩𝐩𝐥𝐞
Zero Width:    A‌p‌p‌l‌e
Combining Marks: A̲p̤p̥l̥e̤
Bidirectional: ‮Αpplе‬
Extreme Obfuscation: ‮A‌p̤‌p̥‌l̥‌e̤‬

Stealth Scores (higher = more stealthy):
  Mixed Charset: 0.85
  Zero Width: 0.72
  Combining Marks: 0.68
  Bidirectional: 0.61
  Extreme Obfuscation: 0.45
==================================================
```

## Security Research Applications

- Homoglyph attack simulation and detection
- Phishing URL detection testing
- Security filter bypass analysis
- Text-based security control assessment
- Unicode-based attack research
- Resilience testing for NLP systems
- Security awareness training
- Anti-phishing tool development
- Domain name security research

## Advanced Use Cases

- **Evasion Testing**: Test the effectiveness of security controls against homoglyph attacks
- **Filter Analysis**: Analyze how different text filters handle Unicode homoglyphs
- **Security Tool Development**: Use as a component in developing security tools for homoglyph detection
- **Awareness Training**: Demonstrate how easy it is to create visually identical strings with different character sets

## Disclaimer

This tool is intended for legitimate security research and educational purposes only. Use responsibly and ethically. The authors are not responsible for any misuse of this tool.

## License

This project is provided for educational and research purposes only. Use at your own risk. 

By: Ali Rajabpour Sanati | Rajabpour.com