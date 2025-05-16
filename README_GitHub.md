# CSV to JSON Converter

A comprehensive Python tool that converts CSV files to JSON format with support for various CSV configurations and output options.

## Features

- Convert CSV files to JSON with a single command
- Support for various CSV formats (including comma and tab-separated files)
- Automatic type detection (numbers, booleans, nulls)
- Custom CSV delimiters and quote characters
- Option to output as array of objects or array of arrays
- Pretty-printing with configurable indentation
- Support for different character encodings
- Comprehensive error handling and logging
- No external dependencies (uses Python standard library)

## Installation

No installation is required. Simply clone this repository to get started:

```bash
git clone https://github.com/earlution/csv-to-json-converter.git
cd csv-to-json-converter
```

## Requirements

- Python 3.6 or higher

## Basic Usage

To convert a CSV file to JSON format:

```bash
python csv_to_json.py input.csv
```

This will convert your CSV file to JSON and display the result in the console.

To save the output to a file:

```bash
python csv_to_json.py input.csv -o output.json
```

## Examples

### Simple CSV Conversion

```bash
python csv_to_json.py simple.csv -o simple.json
```

### Tab-Separated Values (TSV)

```bash
python csv_to_json.py sample.tsv -d $'\t' -o sample.json
```

### Disable Automatic Type Detection

```bash
python csv_to_json.py data.csv --no-auto-types -o data_strings.json
```

### Output as Array of Arrays

```bash
python csv_to_json.py data.csv -r -o data_records.json
```

## Command-Line Options

```
Options:
    -o, --output          Output file (default: stdout)
    -d, --delimiter       CSV delimiter (default: ',')
    -q, --quotechar       CSV quote character (default: '"')
    -n, --quoting         CSV quoting mode (default: minimal)
                          Options: minimal, all, nonnumeric, none
    -s, --skipinitialspace Skip initial space in CSV fields (default: False)
    -i, --indent          JSON indentation level (default: 4)
    -p, --pretty          Pretty print JSON output (default: True)
    -r, --records         Output as array of records instead of array of objects
                          (default: False)
    -a, --auto-types      Automatically convert string values to appropriate types
                          (default: True)
    -e, --encoding        Character encoding for input/output files (default: utf-8)
    -N, --null-values     Comma-separated values to be treated as null (default: "")
    -h, --help            Show this help message and exit
```

## Testing

To run the test suite and verify the converter is working correctly:

```bash
python test_converter.py
```

This will run a series of tests to confirm all features are functioning properly.

## Documentation

For detailed documentation, including a comprehensive user guide with examples and troubleshooting tips, see:

- [CSV_to_JSON_User_Guide.md](CSV_to_JSON_User_Guide.md)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request