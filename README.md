# RBCoder - 15-bit Binary Text Encoder/Decoder

A lightweight command-line utility for encoding text files into 15-bit binary format and decoding them back using a custom dictionary mapping. Written in Python.

## Features

- **15-bit Encoding**: Efficient binary encoding using fixed 15-bit codes
- **Text Preprocessing**: Automatic lowercase conversion and special symbol removal
- **Bidirectional**: Encode text to binary and decode back to text
- **Dictionary-based**: Customizable word-to-binary mappings
- **CLI Interface**: Simple command-line interface with comprehensive help
- **UTF-8 Support**: Supports Russian words
- **Error Handling**: Clear warnings for missing dictionary entries

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd rbcoder
```

2. Ensure you have Python 3.6+ installed

3. No additional dependencies required - uses only Python standard library

## Quick Start

### Encoding Text to Binary
```bash
python rbcoder.py encode -i input.txt -o encoded.bin
```

### Decoding Binary to Text
```bash
python rbcoder.py decode -i encoded.bin -o decoded.txt
```

## Usage

### Command Line Options

#### Encode Command
```bash
python rbcoder.py encode -i INPUT -o OUTPUT
```
- `-i, --input`: Input text file to encode (required)
- `-o, --output`: Output binary file (required)

#### Decode Command
```bash
python rbcoder.py decode -i INPUT -o OUTPUT
```
- `-i, --input`: Input binary file to decode (required)
- `-o, --output`: Output text file (required)

### Help System
```bash
# General help
python rbcoder.py -h

# Encode-specific help
python rbcoder.py encode -h

# Decode-specific help
python rbcoder.py decode -h
```

## Text Preprocessing

During encoding, RBCoder automatically preprocesses text:

1. **Lowercasing**: All text converted to lowercase
2. **Special Symbol Removal**: Punctuation and special characters removed
3. **Whitespace Normalization**: Multiple spaces collapsed

**Example Transformation:**
```
Input:  "Hello, World! This is a TEST - with symbols."
Output: "hello world this is a test with symbols"
```
## Examples

### Basic Usage
```bash
# Create sample text
echo "Привет, мир! Как дела?" > test.txt

# Encode to binary
python rbcoder.py encode -i test.txt -o test.bin

# Decode back to text
python rbcoder.py decode -i test.bin -o decoded.txt 
```

### Handling Complex Text
```bash
# Text with mixed case and punctuation
echo "Сколько раз ты играл в LoL#1.0?" > complex.txt
python rbcoder.py encode -i complex.txt -o complex.bin 
```

**Output after preprocessing:**
```
сколько раз ты играл в
```

### Verbose Output Example
```
$ python rbcoder.py encode -i input.txt -o output.bin
Warning: The following words are not in the dictionary and will be skipped:
  - unknownword
  - anothermissing
Encoded 45 words to output.bin
```

## File Specifications

### Input Text File
- Format: Plain text, UTF-8 encoding
- Content: Can contain mixed case, punctuation, special symbols
- Word Separation: Whitespace (spaces, tabs, newlines)

### Output Binary File
- Format: Raw binary data
- Encoding: 15 bits per word, padded to complete bytes
- Size: Efficient storage using fixed-bit encoding

## Error Handling

RBCoder provides clear feedback for:
- Missing input/output files
- Words not found in dictionary (with warnings)
- File permission issues
- Invalid binary codes during decoding

## Performance

- **Encoding**: Linear time complexity O(n) based on word count
- **Decoding**: Linear time complexity O(n) based on binary chunks
- **Storage**: 15 bits per word, optimal for dictionary-based compression

## Use Cases

- **Text Compression**: Efficient storage of text
- **Language Processing**: Russian text encoding
- **Data Obfuscation**: Basic text obfuscation through binary conversion

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request
