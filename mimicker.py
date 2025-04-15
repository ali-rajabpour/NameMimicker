#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# By Ali Rajabpour Sanati | Rajabpour.com
"""
Mimicker - Character Set Mimicking Tool
Created for CEH certified research purposes
"""

import random
import sys
import argparse
import json
import re
from typing import Dict, List, Tuple, Any, Optional

# Character mapping dictionaries for various lookalike characters
LOOKALIKE_CHARS = {
    # Latin to Cyrillic
    'a': ['а'],  # Cyrillic 'а'
    'c': ['с'],  # Cyrillic 'с'
    'e': ['е'],  # Cyrillic 'е'
    'o': ['о'],  # Cyrillic 'о'
    'p': ['р'],  # Cyrillic 'р'
    'x': ['х'],  # Cyrillic 'х'
    'y': ['у'],  # Cyrillic 'у'
    'A': ['А'],  # Cyrillic 'А'
    'B': ['В'],  # Cyrillic 'В'
    'C': ['С'],  # Cyrillic 'С'
    'E': ['Е'],  # Cyrillic 'Е'
    'H': ['Н'],  # Cyrillic 'Н'
    'K': ['К'],  # Cyrillic 'К'
    'M': ['М'],  # Cyrillic 'М'
    'O': ['О'],  # Cyrillic 'О'
    'P': ['Р'],  # Cyrillic 'Р'
    'T': ['Т'],  # Cyrillic 'Т'
    'X': ['Х'],  # Cyrillic 'Х'
    'Y': ['У'],  # Cyrillic 'У'
    
    # Latin to Greek
    'A': ['Α'],  # Greek Alpha
    'B': ['Β'],  # Greek Beta
    'E': ['Ε'],  # Greek Epsilon
    'H': ['Η'],  # Greek Eta
    'I': ['Ι'],  # Greek Iota
    'K': ['Κ'],  # Greek Kappa
    'M': ['Μ'],  # Greek Mu
    'N': ['Ν'],  # Greek Nu
    'O': ['Ο'],  # Greek Omicron
    'P': ['Ρ'],  # Greek Rho
    'T': ['Τ'],  # Greek Tau
    'X': ['Χ'],  # Greek Chi
    'Y': ['Υ'],  # Greek Upsilon
    'Z': ['Ζ'],  # Greek Zeta
    'o': ['ο'],  # Greek omicron
    'v': ['ν'],  # Greek nu
    
    # Latin to Mathematical Alphanumeric Symbols
    'A': ['𝐀', '𝐴', '𝑨', '𝒜', '𝓐', '𝔄', '𝕬'],
    'B': ['𝐁', '𝐵', '𝑩', '𝓑', '𝔅', '𝕭'],
    'C': ['𝐂', '𝐶', '𝑪', '𝒞', '𝓒', '𝔆', '𝕮'],
    'D': ['𝐃', '𝐷', '𝑫', '𝒟', '𝓓', '𝔇', '𝕯'],
    'E': ['𝐄', '𝐸', '𝑬', '𝓔', '𝔈', '𝕰'],
    'F': ['𝐅', '𝐹', '𝑭', '𝓕', '𝔉', '𝕱'],
    'G': ['𝐆', '𝐺', '𝑮', '𝒢', '𝓖', '𝔊', '𝕲'],
    'H': ['𝐇', '𝐻', '𝑯', '𝓗', '𝔍', '𝕳'],
    'I': ['𝐈', '𝐼', '𝑰', '𝓘', '𝔎', '𝕴'],
    'J': ['𝐉', '𝐽', '𝑱', '𝒥', '𝓙', '𝔏', '𝕵'],
    'K': ['𝐊', '𝐾', '𝑲', '𝓚', '𝔐', '𝕶'],
    'L': ['𝐋', '𝐿', '𝑳', '𝓛', '𝔑', '𝕷'],
    'M': ['𝐌', '𝑀', '𝑴', '𝓜', '𝔒', '𝕸'],
    'N': ['𝐍', '𝑁', '𝑵', '𝓝', '𝔓', '𝕹'],
    'O': ['𝐎', '𝑂', '𝑶', '𝒪', '𝓞', '𝔔', '𝕺'],
    'P': ['𝐏', '𝑃', '𝑷', '𝓟', '𝔕', '𝕻'],
    'Q': ['𝐐', '𝑄', '𝑸', '𝒬', '𝓠', '𝔖', '𝕼'],
    'R': ['𝐑', '𝑅', '𝑹', '𝓡', '𝔗', '𝕽'],
    'S': ['𝐒', '𝑆', '𝑺', '𝒮', '𝓢', '𝔘', '𝕾'],
    'T': ['𝐓', '𝑇', '𝑻', '𝒯', '𝓣', '𝔙', '𝕿'],
    'U': ['𝐔', '𝑈', '𝑼', '𝒰', '𝓤', '𝔚', '𝖀'],
    'V': ['𝐕', '𝑉', '𝑽', '𝒱', '𝓥', '𝔛', '𝖁'],
    'W': ['𝐖', '𝑊', '𝑾', '𝒲', '𝓦', '𝔜', '𝖂'],
    'X': ['𝐗', '𝑋', '𝑿', '𝒳', '𝓧', '𝔝', '𝖃'],
    'Y': ['𝐘', '𝑌', '𝒀', '𝒴', '𝓨', '𝔞', '𝖄'],
    'Z': ['𝐙', '𝑍', '𝒁', '𝒵', '𝓩', '𝔟', '𝖅'],
    'a': ['𝐚', '𝑎', '𝒂', '𝒶', '𝓪', '𝔠', '𝖆'],
    'b': ['𝐛', '𝑏', '𝒃', '𝒷', '𝓫', '𝔡', '𝖇'],
    'c': ['𝐜', '𝑐', '𝒄', '𝒸', '𝓬', '𝔢', '𝖈'],
    'd': ['𝐝', '𝑑', '𝒅', '𝒹', '𝓭', '𝔣', '𝖉'],
    'e': ['𝐞', '𝑒', '𝒆', '𝓮', '𝔤', '𝖊'],
    'f': ['𝐟', '𝑓', '𝒇', '𝒻', '𝓯', '𝔥', '𝖋'],
    'g': ['𝐠', '𝑔', '𝒈', '𝓰', '𝔦', '𝖌'],
    'h': ['𝐡', '𝒉', '𝒽', '𝓱', '𝔧', '𝖍'],
    'i': ['𝐢', '𝑖', '𝒊', '𝒾', '𝓲', '𝔨', '𝖎'],
    'j': ['𝐣', '𝑗', '𝒋', '𝒿', '𝓳', '𝔩', '𝖏'],
    'k': ['𝐤', '𝑘', '𝒌', '𝓀', '𝓴', '𝔪', '𝖐'],
    'l': ['𝐥', '𝑙', '𝒍', '𝓁', '𝓵', '𝔫', '𝖑'],
    'm': ['𝐦', '𝑚', '𝒎', '𝓂', '𝓶', '𝔬', '𝖒'],
    'n': ['𝐧', '𝑛', '𝒏', '𝓃', '𝓷', '𝔭', '𝖓'],
    'o': ['𝐨', '𝑜', '𝒐', '𝓸', '𝔮', '𝖔'],
    'p': ['𝐩', '𝑝', '𝒑', '𝓅', '𝓹', '𝔯', '𝖕'],
    'q': ['𝐪', '𝑞', '𝒒', '𝓆', '𝓺', '𝔰', '𝖖'],
    'r': ['𝐫', '𝑟', '𝒓', '𝓇', '𝓻', '𝔱', '𝖗'],
    's': ['𝐬', '𝑠', '𝒔', '𝓈', '𝓼', '𝔲', '𝖘'],
    't': ['𝐭', '𝑡', '𝒕', '𝓉', '𝓽', '𝔳', '𝖙'],
    'u': ['𝐮', '𝑢', '𝒖', '𝓊', '𝓾', '𝔴', '𝖚'],
    'v': ['𝐯', '𝑣', '𝒗', '𝓋', '𝓿', '𝔵', '𝖛'],
    'w': ['𝐰', '𝑤', '𝒘', '𝓌', '𝔀', '𝔶', '𝖜'],
    'x': ['𝐱', '𝑥', '𝒙', '𝓍', '𝔁', '𝔷', '𝖝'],
    'y': ['𝐲', '𝑦', '𝒚', '𝓎', '𝔂', '𝖞'],
    'z': ['𝐳', '𝑧', '𝒛', '𝓏', '𝔃', '𝖟'],
    
    # Numbers
    '0': ['𝟎', '𝟖', '𝟢', '𝟬', '𝟶', '０'],
    '1': ['𝟏', '𝟙', '𝟣', '𝟭', '𝟷', '１'],
    '2': ['𝟐', '𝟚', '𝟤', '𝟮', '𝟸', '２'],
    '3': ['𝟑', '𝟛', '𝟥', '𝟯', '𝟹', '３'],
    '4': ['𝟒', '𝟜', '𝟦', '𝟰', '𝟺', '４'],
    '5': ['𝟓', '𝟝', '𝟧', '𝟱', '𝟻', '５'],
    '6': ['𝟔', '𝟞', '𝟨', '𝟲', '𝟼', '６'],
    '7': ['𝟕', '𝟟', '𝟩', '𝟳', '𝟽', '７'],
    '8': ['𝟖', '𝟠', '𝟪', '𝟴', '𝟾', '８'],
    '9': ['𝟗', '𝟡', '𝟫', '𝟵', '𝟿', '９'],
    
    # Additional homoglyphs
    'l': ['1', 'I', '|', 'ⅼ', 'ｌ'],
    'I': ['l', '1', '|', 'ⅼ', 'ｌ'],
    '1': ['l', 'I', '|', 'ⅼ'],
    'O': ['0', 'Ο', 'ο', '𝟎', '𝟖', '𝟢', '𝟬', '𝟶'],
    '0': ['O', 'Ο', 'ο', '𝟎', '𝟖', '𝟢', '𝟬', '𝟶'],
    
    # NEW: Additional Latin letters homoglyphs
    'd': ['ⅾ', 'ḍ', 'ᑯ', 'ᗞ', 'ԁ'],  # More 'd' lookalikes
    'g': ['ɡ', 'ƍ', 'ǵ', 'ց'],  # More 'g' lookalikes
    'n': ['ո', 'ղ', 'ӊ', 'ռ'],  # Armenian letters that look like 'n'
    'w': ['ԝ', 'ա', 'ɯ', 'ѡ'],  # More 'w' lookalikes
    'S': ['Ѕ', 'Տ', 'Ꭶ'],  # More 'S' lookalikes
    'Z': ['Ꮓ', 'Ζ', '乙'],  # More 'Z' lookalikes
    
    # NEW: Hebrew lookalikes
    'o': ['ס', 'օ'],  # Hebrew samekh looks like 'o'
    'i': ['ו', 'ׁ', 'ז', 'ן'],  # Some Hebrew chars look like 'i'
    'n': ['ח', 'ת'],  # Some Hebrew chars can look like 'n'
    
    # NEW: Armenian lookalikes
    'U': ['Ս', 'Ա'],  # Armenian capital letter se/ayb
    'h': ['հ', 'հ'],  # Armenian small letter ho
    'q': ['զ', 'գ'],  # Armenian small letter za/gen
    
    # NEW: Special punctuation lookalikes
    '.': ['․', '。', '･'],  # Various dot-like characters
    ',': ['،', '؍', '⸲'],  # Various comma-like characters
    '-': ['‐', '۔', '⁃', '˗'],  # Various hyphen-like characters
    "'": ['´', '\u2019', '\u02BC', '\u02BB', '`'],  # Various apostrophe-like characters
    '"': ['\u201C', '\u201D', '״', '˝'],  # Various quote-like characters
}

# NEW: Zero-width characters for insertion
ZERO_WIDTH_CHARS = [
    '\u200B',  # Zero-width space
    '\u200C',  # Zero-width non-joiner
    '\u200D',  # Zero-width joiner
    '\u2060',  # Word joiner
    '\u200E',  # Left-to-right mark
    '\u200F',  # Right-to-left mark
    '\u061C',  # Arabic letter mark
    '\uFEFF',  # Zero-width no-break space
]

# NEW: Combining marks that can be stacked on characters
COMBINING_MARKS = [
    '\u0305',  # Combining overline
    '\u0306',  # Combining breve
    '\u0307',  # Combining dot above
    '\u0308',  # Combining diaeresis
    '\u030A',  # Combining ring above
    '\u0323',  # Combining dot below
    '\u0324',  # Combining diaeresis below
    '\u0325',  # Combining ring below
    '\u0330',  # Combining tilde below
    '\u0331',  # Combining macron below
    '\u0332',  # Combining low line
    '\u034F',  # Combining grapheme joiner
    '\u035F',  # Combining double macron below
]

# NEW: Bidirectional control characters
BIDI_CONTROLS = [
    '\u202A',  # Left-to-right embedding
    '\u202B',  # Right-to-left embedding
    '\u202C',  # Pop directional formatting
    '\u202D',  # Left-to-right override
    '\u202E',  # Right-to-left override
    '\u2066',  # Left-to-right isolate
    '\u2067',  # Right-to-left isolate
    '\u2068',  # First strong isolate
    '\u2069',  # Pop directional isolate
]

# NEW: Common detection patterns to test against
DETECTION_PATTERNS = [
    r'[^\x00-\x7F]+',  # Non-ASCII characters
    r'[\u0400-\u04FF]+',  # Cyrillic characters
    r'[\u0370-\u03FF]+',  # Greek characters
    r'[\u0590-\u05FF]+',  # Hebrew characters
    r'[\u0530-\u058F]+',  # Armenian characters
    r'[\u200B-\u200F\u2060-\u206F]+',  # Invisible characters
    r'[\u0300-\u036F]+',  # Combining diacritical marks
    r'[\u202A-\u202E\u2066-\u2069]+',  # Bidirectional control characters
]

def generate_single_charset_mimic(input_string: str, charset_index: int = 0) -> str:
    """
    Generate a mimicked string using a single character set.
    
    Args:
        input_string: The original string to mimic
        charset_index: Index of the character set to use (0 for first alternative)
        
    Returns:
        A string that looks like the input but uses characters from the specified charset
    """
    result = ""
    for char in input_string:
        if char in LOOKALIKE_CHARS and len(LOOKALIKE_CHARS[char]) > charset_index:
            result += LOOKALIKE_CHARS[char][charset_index]
        else:
            result += char
    return result

def generate_mixed_charset_mimic(input_string: str) -> str:
    """
    Generate a mimicked string using a mix of character sets.
    
    Args:
        input_string: The original string to mimic
        
    Returns:
        A string that looks like the input but uses characters from mixed charsets
    """
    result = ""
    for char in input_string:
        if char in LOOKALIKE_CHARS and LOOKALIKE_CHARS[char]:
            result += random.choice(LOOKALIKE_CHARS[char])
        else:
            result += char
    return result

# NEW: Function to insert zero-width characters
def insert_zero_width_chars(input_string: str, frequency: float = 0.3) -> str:
    """
    Insert zero-width characters into a string.
    
    Args:
        input_string: The original string
        frequency: Probability of inserting after each character (0.0-1.0)
        
    Returns:
        String with zero-width characters inserted
    """
    result = ""
    for char in input_string:
        result += char
        if random.random() < frequency:
            result += random.choice(ZERO_WIDTH_CHARS)
    return result

# NEW: Function to add combining marks
def add_combining_marks(input_string: str, frequency: float = 0.2, max_marks: int = 2) -> str:
    """
    Add combining marks to characters in a string.
    
    Args:
        input_string: The original string
        frequency: Probability of adding marks to each character (0.0-1.0)
        max_marks: Maximum number of marks to add per character
        
    Returns:
        String with combining marks added
    """
    result = ""
    for char in input_string:
        result += char
        if random.random() < frequency:
            marks_count = random.randint(1, max_marks)
            for _ in range(marks_count):
                result += random.choice(COMBINING_MARKS)
    return result

# NEW: Function to apply bidirectional text manipulation
def apply_bidi_manipulation(input_string: str, technique: str = "random") -> str:
    """
    Apply bidirectional text manipulation to a string.
    
    Args:
        input_string: The original string
        technique: Type of BIDI manipulation ("rtl_override", "embed", "isolate", or "random")
        
    Returns:
        String with bidirectional manipulation applied
    """
    if technique == "random":
        technique = random.choice(["rtl_override", "embed", "isolate"])
    
    if technique == "rtl_override":
        # Right-to-left override
        return "\u202E" + input_string + "\u202C"
    elif technique == "embed":
        # Right-to-left embedding
        return "\u202B" + input_string + "\u202C"
    elif technique == "isolate":
        # Right-to-left isolate
        return "\u2067" + input_string + "\u2069"
    else:
        return input_string

# NEW: Function to calculate stealth score for a string
def calculate_stealth_score(input_string: str) -> float:
    """
    Calculate a "stealth score" indicating how likely a string is to evade detection.
    
    Args:
        input_string: The string to evaluate
        
    Returns:
        A score from 0.0 (easily detectable) to 1.0 (highly stealthy)
    """
    # Base score
    score = 1.0
    
    # Check against detection patterns
    for pattern in DETECTION_PATTERNS:
        matches = re.findall(pattern, input_string)
        if matches:
            # Reduce score based on number of matches and their length
            match_ratio = sum(len(m) for m in matches) / len(input_string)
            score -= match_ratio * 0.2
    
    # Check character diversity - more diverse character sets are more detectable
    charset_count = len(set(input_string))
    diversity_score = min(1.0, charset_count / 10)
    score -= diversity_score * 0.1
    
    # Check for overuse of special techniques
    zero_width_count = sum(input_string.count(zw) for zw in ZERO_WIDTH_CHARS)
    combining_count = sum(input_string.count(cm) for cm in COMBINING_MARKS)
    bidi_count = sum(input_string.count(bc) for bc in BIDI_CONTROLS)
    
    special_char_ratio = (zero_width_count + combining_count + bidi_count) / (len(input_string) + 0.001)
    if special_char_ratio > 0.5:
        score -= (special_char_ratio - 0.5) * 0.4
    
    # Ensure score is between 0 and 1
    return max(0.0, min(1.0, score))

def generate_all_mimics(input_string: str, advanced: bool = False) -> Dict[str, Any]:
    """
    Generate all possible mimicked strings.
    
    Args:
        input_string: The original string to mimic
        advanced: Whether to use advanced techniques
        
    Returns:
        A dictionary containing all mimicked versions and metadata
    """
    results = {
        "original": input_string,
        "mixed_charset": generate_mixed_charset_mimic(input_string)
    }
    
    # Find the maximum number of alternatives for any character
    max_alternatives = 0
    for char in input_string:
        if char in LOOKALIKE_CHARS:
            max_alternatives = max(max_alternatives, len(LOOKALIKE_CHARS[char]))
    
    # Generate mimics for each possible charset index
    for i in range(max_alternatives):
        charset_name = f"charset_{i+1}"
        results[charset_name] = generate_single_charset_mimic(input_string, i)
    
    if advanced:
        # Add advanced techniques
        zero_width_result = insert_zero_width_chars(results["mixed_charset"])
        results["zero_width"] = zero_width_result
        
        combining_result = add_combining_marks(results["mixed_charset"])
        results["combining_marks"] = combining_result
        
        bidi_result = apply_bidi_manipulation(results["mixed_charset"])
        results["bidirectional"] = bidi_result
        
        # Extreme obfuscation - apply all techniques together
        extreme = insert_zero_width_chars(results["mixed_charset"], 0.2)
        extreme = add_combining_marks(extreme, 0.15)
        extreme = apply_bidi_manipulation(extreme)
        results["extreme_obfuscation"] = extreme
        
        # Add stealth scores for each variant
        scores = {}
        for name, value in results.items():
            if name != "original":
                decimal_score = calculate_stealth_score(value)
                percentage_score = int(decimal_score * 100)
                scores[name] = {
                    "decimal": decimal_score,
                    "percentage": percentage_score
                }
        results["stealth_scores"] = scores
        
        # Add representation data for the mixed_charset
        mixed = results["mixed_charset"]
        hex_repr = " ".join(f"0x{ord(c):04X}" for c in mixed)
        results["representations"] = {
            "hex": hex_repr,
            "unicode_names": [f"U+{ord(c):04X} ({unicodedata.name(c, 'UNKNOWN')})" for c in mixed]
        }
    
    return results

def print_results(results: Dict[str, Any], show_scores: bool = False) -> None:
    """
    Print the results in a formatted way.
    
    Args:
        results: Dictionary containing the mimicked strings
        show_scores: Whether to show stealth scores
    """
    print("\n" + "="*50)
    print(f"MIMICKER RESULTS")
    print("="*50)
    
    for name, value in results.items():
        if name == "original":
            print(f"Original:      {value}")
        elif name == "mixed_charset":
            print(f"Mixed charset: {value}")
        elif name == "stealth_scores" and show_scores:
            print("\nStealth Scores (0-100%, higher = more stealthy):")
            for variant, score_data in value.items():
                percentage = score_data["percentage"]
                print(f"  {variant.replace('_', ' ').title()}: {percentage}%")
        elif name == "representations":
            # Skip this in console output as it can be verbose
            pass
        elif isinstance(value, str):
            print(f"{name.replace('_', ' ').title()}: {value}")
    
    print("="*50)

def export_to_json(results: Dict[str, Any], filename: str) -> None:
    """
    Export results to a JSON file.
    
    Args:
        results: Dictionary containing the mimicked strings
        filename: Name of the file to save to
    """
    # Prepare export data
    export_data = {k: v for k, v in results.items()}
    
    # Ensure custom combination is included if it exists
    if "custom_combination" in results:
        # Calculate stealth score for custom combination if not already done
        if "stealth_scores" in results and "custom_combination" not in results["stealth_scores"]:
            decimal_score = calculate_stealth_score(results["custom_combination"])
            percentage_score = int(decimal_score * 100)
            
            if "stealth_scores" not in export_data:
                export_data["stealth_scores"] = {}
                
            export_data["stealth_scores"]["custom_combination"] = {
                "decimal": decimal_score,
                "percentage": percentage_score
            }
    
    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, ensure_ascii=False, indent=2)
    print(f"\nResults exported to {filename}")
    
    # Print a summary of what was exported
    print("\nExported data includes:")
    for key in export_data:
        if key == "stealth_scores" or key == "representations" or key == "custom_combination_details":
            print(f"- {key.replace('_', ' ').title()}")
        elif isinstance(export_data[key], str):
            print(f"- {key.replace('_', ' ').title()}: {export_data[key][:20]}{'...' if len(export_data[key]) > 20 else ''}")
    
    # If custom combination was included, highlight this
    if "custom_combination" in export_data:
        print("\nYour custom combination has been included in the export.")

def load_unicodedata():
    """Load the unicodedata module if available, otherwise provide a stub."""
    try:
        import unicodedata
        return unicodedata
    except ImportError:
        # Stub implementation if unicodedata is not available
        class UnicodeDataStub:
            def name(self, char, default=None):
                return default
        return UnicodeDataStub()

# Load unicodedata once to avoid repeated import attempts
unicodedata = load_unicodedata()

def create_custom_combination(input_string: str, results: Dict[str, Any]) -> str:
    """
    Create a custom combination of character sets based on user input.
    
    Args:
        input_string: The original string to mimic
        results: Dictionary containing all the generated mimicked versions
        
    Returns:
        A custom combined string based on user selections
    """
    print("\n" + "="*50)
    print("CUSTOM COMBINATION CREATOR")
    print("="*50)
    print("For each character, select which variant you want to use.")
    
    # Create a list of available variants
    variant_names = []
    for name in results:
        if isinstance(results[name], str) and name not in ["original", "representations", "custom_combination"]:
            variant_names.append(name)
    
    # Print available variants with numbers
    print("\nAvailable variants:")
    for i, name in enumerate(variant_names):
        print(f"{i+1}. {name.replace('_', ' ').title()}")
    
    print(f"{len(variant_names)+1}. Original (unchanged)")
    print("="*50)
    
    # Ask if user wants to use quick selection
    quick_selection = input("\nDo you want to use quick selection mode? (y/n): ").lower().startswith('y')
    
    # Track user selections for display at the end
    selections = []
    
    if quick_selection:
        # Quick selection mode - select one variant for each character position
        custom_result = ""
        for i, char in enumerate(input_string):
            print(f"\nCharacter {i+1}: '{char}'")
            
            # Display a compact view of all variants for this character
            print("Variants: ", end="")
            for j, variant in enumerate(variant_names):
                if i < len(results[variant]):
                    variant_char = results[variant][i]
                    print(f"{j+1}:{variant_char} ", end="")
            print(f"{len(variant_names)+1}:{char} (original)")
            
            # Get user choice
            while True:
                try:
                    choice = input(f"Select variant (1-{len(variant_names)+1}): ")
                    choice_num = int(choice)
                    
                    if 1 <= choice_num <= len(variant_names):
                        # Add the character from the selected variant
                        selected_variant = variant_names[choice_num-1]
                        if i < len(results[selected_variant]):
                            variant_char = results[selected_variant][i]
                            custom_result += variant_char
                            selections.append((char, variant_char, selected_variant))
                        else:
                            custom_result += char
                            selections.append((char, char, "original"))
                        break
                    elif choice_num == len(variant_names)+1:
                        # Use original character
                        custom_result += char
                        selections.append((char, char, "original"))
                        break
                    else:
                        print(f"Please enter a number between 1 and {len(variant_names)+1}")
                except ValueError:
                    print("Please enter a valid number")
    else:
        # Detailed selection mode - show each variant in detail
        custom_result = ""
        for i, char in enumerate(input_string):
            print(f"\nCharacter {i+1}: '{char}'")
            
            # Show how this character looks in each variant
            for j, variant in enumerate(variant_names):
                if i < len(results[variant]):
                    variant_char = results[variant][i]
                    print(f"{j+1}. {variant.replace('_', ' ').title()}: '{variant_char}'")
            
            print(f"{len(variant_names)+1}. Original: '{char}'")
            
            # Get user choice
            while True:
                try:
                    choice = input(f"Select variant for '{char}' (1-{len(variant_names)+1}): ")
                    choice_num = int(choice)
                    
                    if 1 <= choice_num <= len(variant_names):
                        # Add the character from the selected variant
                        selected_variant = variant_names[choice_num-1]
                        if i < len(results[selected_variant]):
                            variant_char = results[selected_variant][i]
                            custom_result += variant_char
                            selections.append((char, variant_char, selected_variant))
                        else:
                            custom_result += char
                            selections.append((char, char, "original"))
                        break
                    elif choice_num == len(variant_names)+1:
                        # Use original character
                        custom_result += char
                        selections.append((char, char, "original"))
                        break
                    else:
                        print(f"Please enter a number between 1 and {len(variant_names)+1}")
                except ValueError:
                    print("Please enter a valid number")
    
    # Display a summary of the selections
    print("\n" + "="*50)
    print("SELECTION SUMMARY")
    print("="*50)
    print(f"Original string: {input_string}")
    print(f"Custom result:   {custom_result}")
    print("\nCharacter by character:")
    
    for i, (orig_char, selected_char, variant) in enumerate(selections):
        variant_display = variant.replace('_', ' ').title() if variant != "original" else "Original"
        print(f"Position {i+1}: '{orig_char}' → '{selected_char}' ({variant_display})")
    
    # Store the selections in the results dictionary for potential JSON export
    results["custom_combination_details"] = {
        "selections": [
            {
                "position": i+1,
                "original": orig_char,
                "selected": selected_char,
                "variant": variant
            } for i, (orig_char, selected_char, variant) in enumerate(selections)
        ]
    }
    
    return custom_result

def print_help() -> None:
    """Print detailed help information about the tool."""
    print("\n" + "="*50)
    print("MIMICKER HELP")
    print("="*50)
    print("Mimicker is a tool for creating lookalike strings using different character sets.")
    print("This can be used for research purposes to understand homoglyph attacks.")
    print("\nAvailable character sets and techniques:")
    print("  - Mixed charset: Random selection from all available lookalikes")
    print("  - Charset 1-7: Specific character sets (Cyrillic, Greek, Mathematical, etc.)")
    print("  - Zero Width: Inserts invisible zero-width characters between visible ones")
    print("  - Combining Marks: Adds combining diacritical marks to characters")
    print("  - Bidirectional: Uses bidirectional text control characters")
    print("  - Extreme Obfuscation: Combines multiple techniques for maximum obfuscation")
    print("\nUsage examples:")
    print("  python mimicker.py                             # Run in interactive mode")
    print("  python mimicker.py -i                          # Run in interactive mode")
    print("  python mimicker.py -s 'Apple'                  # Basic usage")
    print("  python mimicker.py -s 'Apple' -a               # Use advanced techniques")
    print("  python mimicker.py -s 'Apple' -a -c            # Create custom combination")
    print("  python mimicker.py -s 'Apple' -a --scores      # Show stealth scores")
    print("  python mimicker.py -s 'Apple' -p '1,2,3,4,5'   # Use preset combination")
    print("  python mimicker.py -s 'Apple' -e results.json  # Export results to JSON")
    print("  python mimicker.py --help                      # Show command-line help")
    print("\nInteractive Mode:")
    print("  The interactive mode (-i) provides a menu-driven interface that guides you")
    print("  through the process of creating custom character combinations. It will:")
    print("  1. Ask for the input string to mimic")
    print("  2. Let you choose whether to use advanced techniques")
    print("  3. Show all available mimicked versions")
    print("  4. Guide you through creating a custom combination")
    print("  5. Include your custom combination in the JSON export")
    print("="*50)

def main() -> None:
    """Main function to run the mimicker tool."""
    parser = argparse.ArgumentParser(description="Mimicker - Generate lookalike strings using different character sets")
    parser.add_argument("--string", "-s", type=str, help="String to mimic")
    parser.add_argument("--advanced", "-a", action="store_true", help="Use advanced techniques")
    parser.add_argument("--export", "-e", type=str, help="Export results to a JSON file")
    parser.add_argument("--scores", action="store_true", help="Show stealth scores")
    parser.add_argument("--custom", "-c", action="store_true", help="Create custom combination after showing results")
    parser.add_argument("--preset", "-p", type=str, help="Preset for custom combination (format: '1,3,2,1' for character positions)")
    parser.add_argument("--help-mimicker", action="store_true", help="Show detailed help about mimicker")
    parser.add_argument("--interactive", "-i", action="store_true", help="Run in fully interactive mode")
    args = parser.parse_args()
    
    if args.help_mimicker:
        print_help()
        return
    
    # Interactive mode overrides other flags
    if args.interactive or not any([args.string, args.advanced, args.export, args.scores, args.custom, args.preset]):
        run_interactive_mode()
        return
    
    if args.string:
        input_string = args.string
    else:
        print("Enter the string you want to mimic (e.g., 'Apple'): ", end="")
        input_string = input().strip()
    
    if not input_string:
        print("Error: Empty string provided.")
        sys.exit(1)
    
    # Always use advanced features to have more options for custom combinations
    results = generate_all_mimics(input_string, args.advanced or args.custom or args.preset)
    print_results(results, args.scores)
    
    # Handle preset custom combination
    if args.preset:
        try:
            # Parse the preset string (e.g., "1,3,2,1" for character positions)
            preset_choices = [int(x.strip()) for x in args.preset.split(',')]
            
            # Create a list of available variants
            variant_names = []
            for name in results:
                if isinstance(results[name], str) and name not in ["original", "representations", "custom_combination"]:
                    variant_names.append(name)
            
            # Create custom result based on preset
            custom_result = ""
            for i, char in enumerate(input_string):
                if i < len(preset_choices):
                    choice = preset_choices[i]
                    if 1 <= choice <= len(variant_names):
                        selected_variant = variant_names[choice-1]
                        if i < len(results[selected_variant]):
                            custom_result += results[selected_variant][i]
                        else:
                            custom_result += char
                    else:
                        # Use original for out of range choices
                        custom_result += char
                else:
                    # Use original for remaining characters
                    custom_result += char
            
            print("\n" + "="*50)
            print("PRESET CUSTOM COMBINATION RESULT")
            print("="*50)
            print(f"Original:  {input_string}")
            print(f"Custom:    {custom_result}")
            
            # Calculate stealth score for custom result
            if args.scores:
                decimal_score = calculate_stealth_score(custom_result)
                percentage_score = int(decimal_score * 100)
                print(f"Stealth Score: {percentage_score}%")
            
            print("="*50)
            
            # Add custom result to results dictionary
            results["custom_combination"] = custom_result
            
            # Export if requested
            if args.export:
                export_to_json(results, args.export)
            
            return
        except (ValueError, IndexError) as e:
            print(f"Error with preset format: {e}")
            print("Expected format: --preset '1,3,2,1' (numbers correspond to variant choices)")
            sys.exit(1)
    
    # Ask for custom combination
    create_custom = args.custom
    if not create_custom and not args.string:
        create_custom = input("\nWould you like to create a custom combination? (y/n): ").lower().startswith('y')
    
    if create_custom:
        custom_result = create_custom_combination(input_string, results)
        
        print("\n" + "="*50)
        print("CUSTOM COMBINATION RESULT")
        print("="*50)
        print(f"Original:  {input_string}")
        print(f"Custom:    {custom_result}")
        
        # Calculate stealth score for custom result
        if args.scores:
            decimal_score = calculate_stealth_score(custom_result)
            percentage_score = int(decimal_score * 100)
            print(f"Stealth Score: {percentage_score}%")
        
        print("="*50)
        
        # Add custom result to results dictionary
        results["custom_combination"] = custom_result
        
        # Ask if user wants to save the custom result to clipboard
        try:
            import pyperclip
            if input("Copy custom result to clipboard? (y/n): ").lower().startswith('y'):
                pyperclip.copy(custom_result)
                print("Custom result copied to clipboard!")
        except ImportError:
            print("Note: Install 'pyperclip' package to enable clipboard functionality")
    
    # Export results to JSON
    if args.export:
        export_to_json(results, args.export)
    elif create_custom and input("Export results to JSON file? (y/n): ").lower().startswith('y'):
        filename = input("Enter filename (default: mimicker_results.json): ").strip() or "mimicker_results.json"
        export_to_json(results, filename)

def run_interactive_mode() -> None:
    """Run the tool in fully interactive mode with a menu-based interface."""
    print("\n" + "="*50)
    print("MIMICKER - INTERACTIVE MODE")
    print("="*50)
    print("Welcome to the Mimicker interactive mode!")
    
    # Get input string
    print("\nEnter the string you want to mimic (e.g., 'Apple'): ", end="")
    input_string = input().strip()
    
    if not input_string:
        print("Error: Empty string provided.")
        sys.exit(1)
    
    # Ask about advanced features
    use_advanced = input("\nUse advanced techniques? (y/n): ").lower().startswith('y')
    show_scores = input("Show stealth scores? (y/n): ").lower().startswith('y')
    
    # Generate all mimics
    results = generate_all_mimics(input_string, use_advanced)
    print_results(results, show_scores)
    
    # Always create custom combination in interactive mode
    custom_result = create_custom_combination(input_string, results)
    
    print("\n" + "="*50)
    print("CUSTOM COMBINATION RESULT")
    print("="*50)
    print(f"Original:  {input_string}")
    print(f"Custom:    {custom_result}")
    
    # Calculate stealth score for custom result
    if show_scores:
        decimal_score = calculate_stealth_score(custom_result)
        percentage_score = int(decimal_score * 100)
        print(f"Stealth Score: {percentage_score}%")
    
    print("="*50)
    
    # Add custom result to results dictionary
    results["custom_combination"] = custom_result
    
    # Ask if user wants to save the custom result to clipboard
    try:
        import pyperclip
        if input("Copy custom result to clipboard? (y/n): ").lower().startswith('y'):
            pyperclip.copy(custom_result)
            print("Custom result copied to clipboard!")
    except ImportError:
        print("Note: Install 'pyperclip' package to enable clipboard functionality")
    
    # Always ask about exporting to JSON in interactive mode
    if input("Export results to JSON file? (y/n): ").lower().startswith('y'):
        filename = input("Enter filename (default: mimicker_results.json): ").strip() or "mimicker_results.json"
        export_to_json(results, filename)

if __name__ == "__main__":
    main() 