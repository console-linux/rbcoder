import json
import argparse
import sys
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def encode_text(input_file, output_file, dict_file):
    with open(dict_file, 'r', encoding='utf-8') as f:
        dictionary = json.load(f)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    
    binary_string = ''
    missing_words = set()
    original_missing = set()
    
    for word in words:
        if word in dictionary:
            binary_string += dictionary[word]
        else:
            missing_words.add(word)
            original_missing.add(word)
    
    if missing_words:
        print("Warning: The following words are not in the dictionary and will be skipped:")
        for word in missing_words:
            print(f"  - {word}")
    
    byte_array = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        if len(byte) < 8:
            byte = byte.ljust(8, '0')
        byte_array.append(int(byte, 2))
    
    with open(output_file, 'wb') as f:
        f.write(byte_array)
    
    print(f"Encoded {len(words) - len(missing_words)} words to {output_file}")

def decode_binary(input_file, output_file, dict_file):
    with open(dict_file, 'r', encoding='utf-8') as f:
        dictionary = json.load(f)
    
    reverse_dict = {code: word for word, code in dictionary.items()}
    
    with open(input_file, 'rb') as f:
        byte_data = f.read()
    
    binary_string = ''.join(f'{byte:08b}' for byte in byte_data)
    
    word_length = 15
    words = []
    missing_codes = set()
    
    for i in range(0, len(binary_string), word_length):
        chunk = binary_string[i:i+word_length]
        if len(chunk) < word_length:
            continue
        if chunk in reverse_dict:
            words.append(reverse_dict[chunk])
        else:
            missing_codes.add(chunk)
    
    if missing_codes:
        print("Warning: The following binary codes are not in the dictionary and will be skipped:")
        for code in missing_codes:
            print(f"  - {code}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(' '.join(words))
    
    print(f"Decoded {len(words)} words to {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Encode and decode text using a binary dictionary')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    encode_parser = subparsers.add_parser('encode', help='Encode text to binary')
    encode_parser.add_argument('-i', '--input', required=True, help='Input text file')
    encode_parser.add_argument('-o', '--output', required=True, help='Output binary file')
    
    decode_parser = subparsers.add_parser('decode', help='Decode binary to text')
    decode_parser.add_argument('-i', '--input', required=True, help='Input binary file')
    decode_parser.add_argument('-o', '--output', required=True, help='Output text file')
    
    args = parser.parse_args()
    
    if args.command == 'encode':
        encode_text(args.input, args.output, 'dict.json')
    elif args.command == 'decode':
        decode_binary(args.input, args.output, 'dict.json')
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
