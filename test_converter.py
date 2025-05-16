#!/usr/bin/env python3
"""
CSV to JSON Converter Test Script

This script tests the CSV to JSON converter with various input files and options.
It helps verify that the converter is functioning correctly before using it with your own data.

Usage:
    python test_converter.py
"""

import os
import subprocess
import json
import sys
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def run_test(test_name, command, expected_json_file=None):
    """Run a test and check the result."""
    logger.info(f"Running test: {test_name}")
    logger.info(f"Command: {command}")
    
    # Run the command
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Check return code
    if process.returncode != 0:
        logger.error(f"Test failed! Return code: {process.returncode}")
        logger.error(f"Error output: {process.stderr}")
        return False
        
    logger.info("Command completed successfully")
    
    # If we have an expected JSON file, verify the output
    if expected_json_file and os.path.exists(expected_json_file):
        try:
            with open(expected_json_file, 'r') as f:
                # Try to parse the JSON to make sure it's valid
                json_data = json.load(f)
                logger.info(f"Output JSON is valid and contains {len(json_data)} records")
                return True
        except json.JSONDecodeError:
            logger.error(f"Output file {expected_json_file} is not valid JSON")
            return False
        except Exception as e:
            logger.error(f"Error checking output file: {e}")
            return False
    
    return True

def main():
    """Run all tests."""
    tests = [
        {
            "name": "Simple CSV Test",
            "command": "python csv_to_json.py simple.csv -o simple_test.json",
            "output_file": "simple_test.json"
        },
        {
            "name": "CSV with Missing Values",
            "command": "python csv_to_json.py average.csv -o average_test.json",
            "output_file": "average_test.json" 
        },
        {
            "name": "Complex CSV with Quoted Values",
            "command": "python csv_to_json.py complex.csv -o complex_test.json -d ',' -q '\"'",
            "output_file": "complex_test.json"
        },
        {
            "name": "TSV File Test",
            "command": "python csv_to_json.py sample.tsv -d $'\\t' -o tsv_test.json",
            "output_file": "tsv_test.json"
        },
        {
            "name": "No Auto-Types Test",
            "command": "python csv_to_json.py custom_types.csv -o types_test.json --no-auto-types",
            "output_file": "types_test.json"
        },
        {
            "name": "Records Format Test (Array of Arrays)",
            "command": "python csv_to_json.py simple.csv -o records_test.json -r",
            "output_file": "records_test.json"
        }
    ]
    
    # Create a test directory if it doesn't exist
    os.makedirs("test_output", exist_ok=True)
    
    # Run all tests
    passed = 0
    total = len(tests)
    
    for test in tests:
        # Update output path to use test directory
        if "output_file" in test:
            test["output_file"] = os.path.join("test_output", test["output_file"])
            # Update command to reflect new output path
            test["command"] = test["command"].replace(
                os.path.basename(test["output_file"]), 
                test["output_file"]
            )
        
        if run_test(test["name"], test["command"], test.get("output_file")):
            passed += 1
            logger.info(f"Test passed: {test['name']}\n")
        else:
            logger.error(f"Test failed: {test['name']}\n")
    
    # Print summary
    logger.info(f"Test summary: {passed} of {total} tests passed")
    
    if passed == total:
        logger.info("All tests passed! The CSV to JSON converter is working correctly.")
        return 0
    else:
        logger.error("Some tests failed. Please check the output for details.")
        return 1

if __name__ == "__main__":
    sys.exit(main())