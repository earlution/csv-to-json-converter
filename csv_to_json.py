#!/usr/bin/env python3
"""
CSV to JSON Converter

This script converts CSV files to JSON format with support for various 
CSV configurations and output options.

Usage:
    python csv_to_json.py input.csv [options]

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
"""

import argparse
import csv
import json
import sys
import os
import logging
from typing import List, Dict, Any, Optional, Union, Tuple, IO


def setup_logging():
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: %(message)s'
    )


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments.
    
    Returns:
        argparse.Namespace: Parsed command line arguments
    """
    parser = argparse.ArgumentParser(
        description='Convert CSV files to JSON format.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        'input_file',
        help='Input CSV file'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output JSON file (default: stdout)',
        default=None
    )
    
    parser.add_argument(
        '-d', '--delimiter',
        help='CSV delimiter',
        default=','
    )
    
    parser.add_argument(
        '-q', '--quotechar',
        help='CSV quote character',
        default='"'
    )
    
    parser.add_argument(
        '-n', '--quoting',
        help='CSV quoting mode',
        choices=['minimal', 'all', 'nonnumeric', 'none'],
        default='minimal'
    )
    
    parser.add_argument(
        '-s', '--skipinitialspace',
        help='Skip initial space in CSV fields',
        action='store_true'
    )
    
    parser.add_argument(
        '-i', '--indent',
        help='JSON indentation level',
        type=int,
        default=4
    )
    
    parser.add_argument(
        '-p', '--pretty',
        help='Pretty print JSON output',
        action='store_true',
        default=True
    )
    
    parser.add_argument(
        '--no-pretty',
        help='Disable pretty printing',
        action='store_false',
        dest='pretty'
    )
    
    parser.add_argument(
        '-r', '--records',
        help='Output as array of arrays instead of array of objects',
        action='store_true'
    )
    
    parser.add_argument(
        '-a', '--auto-types',
        help='Automatically convert string values to appropriate types',
        action='store_true',
        default=True
    )
    
    parser.add_argument(
        '--no-auto-types',
        help='Disable automatic type conversion',
        action='store_false',
        dest='auto_types'
    )
    
    parser.add_argument(
        '-e', '--encoding',
        help='Character encoding for input/output files',
        default='utf-8'
    )
    
    parser.add_argument(
        '-N', '--null-values',
        help='Comma-separated values to be treated as null',
        default=''
    )
    
    return parser.parse_args()


def get_quoting_mode(quoting_str: str) -> int:
    """Convert quoting mode string to csv module constant.
    
    Args:
        quoting_str: String representation of quoting mode
        
    Returns:
        int: Corresponding csv module quoting constant
    """
    quoting_modes = {
        'minimal': csv.QUOTE_MINIMAL,
        'all': csv.QUOTE_ALL,
        'nonnumeric': csv.QUOTE_NONNUMERIC,
        'none': csv.QUOTE_NONE
    }
    return quoting_modes.get(quoting_str.lower(), csv.QUOTE_MINIMAL)


def try_parse_value(value: str, auto_types: bool, null_values: List[str]) -> Any:
    """Try to parse a string value into an appropriate Python type.
    
    Args:
        value: String value to parse
        auto_types: Whether to automatically convert types
        null_values: List of strings to treat as null
        
    Returns:
        Parsed value in the most appropriate type
    """
    if value in null_values:
        return None
    
    if not auto_types:
        return value
    
    # Try to convert to appropriate type
    value = value.strip()
    
    # Check for boolean
    if value.lower() in ('true', 'yes', 'y', '1'):
        return True
    if value.lower() in ('false', 'no', 'n', '0'):
        return False
    
    # Check for null/None
    if value.lower() in ('null', 'none', 'na', 'n/a'):
        return None
    
    # Check for integer
    try:
        if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
            return int(value)
    except ValueError:
        pass
    
    # Check for float
    try:
        if '.' in value or 'e' in value.lower():
            return float(value)
    except ValueError:
        pass
    
    # Return as string if no conversion was successful
    return value


def read_csv_file(
    file_path: str,
    delimiter: str,
    quotechar: str,
    quoting: int,
    skipinitialspace: bool,
    encoding: str
) -> Tuple[List[str], List[List[str]]]:
    """Read CSV file and return headers and data.
    
    Args:
        file_path: Path to CSV file
        delimiter: CSV delimiter character
        quotechar: CSV quote character
        quoting: CSV quoting mode
        skipinitialspace: Whether to skip initial spaces
        encoding: File encoding
        
    Returns:
        Tuple containing headers and rows
        
    Raises:
        FileNotFoundError: If the input file does not exist
        csv.Error: If there is an error parsing the CSV file
    """
    try:
        with open(file_path, 'r', encoding=encoding, newline='') as csvfile:
            reader = csv.reader(
                csvfile,
                delimiter=delimiter,
                quotechar=quotechar,
                quoting=quoting,
                skipinitialspace=skipinitialspace
            )
            
            # Read header row
            try:
                headers = next(reader)
            except StopIteration:
                raise ValueError("CSV file is empty or has no headers")
            
            # Read data rows
            rows = list(reader)
            
            return headers, rows
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {file_path}")
    except csv.Error as e:
        raise csv.Error(f"Error parsing CSV file: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error reading CSV file: {e}")


def csv_to_json(
    headers: List[str],
    rows: List[List[str]],
    as_records: bool,
    auto_types: bool,
    null_values: List[str]
) -> List[Any]:
    """Convert CSV data to JSON-compatible Python structure.
    
    Args:
        headers: List of column headers
        rows: List of data rows
        as_records: Whether to output as array of arrays
        auto_types: Whether to automatically convert types
        null_values: List of strings to treat as null
        
    Returns:
        JSON-compatible Python structure
    """
    if as_records:
        # Convert to array of arrays with header as first row
        result = [headers]
        for row in rows:
            # Convert values to appropriate types
            parsed_row = [try_parse_value(val, auto_types, null_values) for val in row]
            # Ensure row has the same length as headers
            while len(parsed_row) < len(headers):
                parsed_row.append(None)
            result.append(parsed_row[:len(headers)])
    else:
        # Convert to array of objects
        result = []
        for row in rows:
            row_obj = {}
            for i, header in enumerate(headers):
                if i < len(row):
                    row_obj[header] = try_parse_value(row[i], auto_types, null_values)
                else:
                    row_obj[header] = None
            result.append(row_obj)
    
    return result


def write_json(
    data: Any,
    output_file: Optional[str],
    indent: Optional[int],
    encoding: str
) -> None:
    """Write JSON data to file or stdout.
    
    Args:
        data: Data to write as JSON
        output_file: Output file path or None for stdout
        indent: JSON indentation level or None
        encoding: File encoding
        
    Raises:
        IOError: If there is an error writing to the output file
    """
    try:
        json_str = json.dumps(data, indent=indent)
        
        if output_file:
            with open(output_file, 'w', encoding=encoding) as f:
                f.write(json_str)
            logging.info(f"JSON data written to {output_file}")
        else:
            # Write to stdout
            print(json_str)
    except IOError as e:
        raise IOError(f"Error writing to output file: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error writing JSON: {e}")


def main():
    """Main function that orchestrates the CSV to JSON conversion."""
    setup_logging()
    
    try:
        # Parse command line arguments
        args = parse_arguments()
        
        # Process null values
        null_values = [val.strip() for val in args.null_values.split(',')] if args.null_values else ['']
        
        # Get CSV quoting mode
        quoting = get_quoting_mode(args.quoting)
        
        # Read CSV file
        logging.info(f"Reading CSV file: {args.input_file}")
        headers, rows = read_csv_file(
            args.input_file,
            args.delimiter,
            args.quotechar,
            quoting,
            args.skipinitialspace,
            args.encoding
        )
        
        # Convert CSV to JSON
        logging.info("Converting CSV data to JSON")
        json_data = csv_to_json(
            headers,
            rows,
            args.records,
            args.auto_types,
            null_values
        )
        
        # Set indent for pretty printing
        indent = args.indent if args.pretty else None
        
        # Write JSON to output file or stdout
        logging.info(f"Writing JSON data to: {args.output or 'stdout'}")
        write_json(
            json_data,
            args.output,
            indent,
            args.encoding
        )
        
        logging.info("Conversion completed successfully")
        
    except FileNotFoundError as e:
        logging.error(e)
        return 1
    except csv.Error as e:
        logging.error(f"CSV error: {e}")
        return 1
    except json.JSONDecodeError as e:
        logging.error(f"JSON error: {e}")
        return 1
    except IOError as e:
        logging.error(e)
        return 1
    except ValueError as e:
        logging.error(e)
        return 1
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
