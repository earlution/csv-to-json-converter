# CSV to JSON Converter - User Guide

## Introduction

The CSV to JSON Converter is a tool that helps you transform CSV (Comma-Separated Values) files into JSON (JavaScript Object Notation) format. This guide will walk you through how to use this tool, even if you have no technical background.

### What is CSV?

CSV is a simple file format used to store tabular data, such as a spreadsheet or database. CSV files typically use commas to separate values (though other characters can be used), and each new line indicates a new row of data. Many applications can export data as CSV files, including:

- Microsoft Excel
- Google Sheets
- Database software
- Financial software
- Customer Relationship Management (CRM) systems

### What is JSON?

JSON is a lightweight data format that is easy for humans to read and write and easy for machines to parse and generate. It's commonly used for transmitting data in web applications and is a popular alternative to XML.

## Getting Started

### Basic Usage

To convert a CSV file to JSON, you simply need to run the converter and specify your CSV file:

```
python csv_to_json.py your_file.csv
```

This will convert your CSV file to JSON format and display the result in your console window.

### Saving to a File

To save the JSON output to a file instead of displaying it on screen:

```
python csv_to_json.py your_file.csv -o output.json
```

## Examples

Below are examples of increasing complexity to help you understand how to use the converter.

### Working with Different File Types

#### Tab-Separated Values (TSV) Files

Many systems export data as TSV files instead of CSV. These files use tabs instead of commas to separate values. Here's how to convert them:

**File: sample.tsv**
```
Name    Department    Salary    Start Date
John Smith    Engineering    75000    2022-01-15
Maria Garcia    Marketing    68000    2022-03-22
Robert Johnson    Finance    82000    2021-11-05
Sarah Lee    Human Resources    61000    2022-06-10
```

**Command for TSV files:**
```
python csv_to_json.py sample.tsv -d $'\t' -o sample_tsv.json
```

**Result (sample_tsv.json):**
```json
[
    {
        "Name": "John Smith",
        "Department": "Engineering",
        "Salary": 75000,
        "Start Date": "2022-01-15"
    },
    {
        "Name": "Maria Garcia",
        "Department": "Marketing",
        "Salary": 68000,
        "Start Date": "2022-03-22"
    },
    ...
]
```

#### Converting Excel/Google Sheets Data

To convert data from Excel or Google Sheets:

1. **In Excel:**
   - Select your data range
   - Click "File" → "Save As"
   - Choose "CSV (Comma delimited) (*.csv)" as the file type
   - Save the file

2. **In Google Sheets:**
   - Select "File" → "Download" → "Comma-separated values (.csv)"
   - Save the file to your computer

3. **Then use the converter:**
   ```
   python csv_to_json.py your_excel_export.csv -o excel_data.json
   ```

For Excel files with special characters, you might need to specify the encoding:
```
python csv_to_json.py your_excel_export.csv -e utf-8 -o excel_data.json
```

### Simple Example

Let's start with a simple CSV file containing basic information:

**File: simple.csv**
```
Name,Age,City
John,30,New York
Sarah,25,Boston
Mike,45,Chicago
```

**Command to run:**
```
python csv_to_json.py simple.csv -o simple.json
```

**Result (simple.json):**
```json
[
    {
        "Name": "John",
        "Age": 30,
        "City": "New York"
    },
    {
        "Name": "Sarah",
        "Age": 25,
        "City": "Boston"
    },
    {
        "Name": "Mike",
        "Age": 45,
        "City": "Chicago"
    }
]
```

Notice how:
- Each row becomes a JSON object (items inside curly braces {})
- Column headers become the property names
- Numbers are automatically detected and not treated as text
- The entire result is an array (inside square brackets [])

### Average Example

Now let's look at a more complex example with more data and some missing values:

**File: average.csv**
```
First Name,Last Name,Email,Age,Department,Salary
John,Smith,john.smith@example.com,35,Marketing,65000
Jane,Doe,jane.doe@example.com,28,Engineering,78000
Robert,Johnson,robert.j@example.com,42,Finance,82000
Emily,Williams,emily.w@example.com,31,Human Resources,58000
,Brown,michael.b@example.com,39,Sales,72000
Sarah,Miller,,27,Engineering,76000
```

**Command to run:**
```
python csv_to_json.py average.csv -o average.json
```

**Result (average.json):**
```json
[
    {
        "First Name": "John",
        "Last Name": "Smith",
        "Email": "john.smith@example.com",
        "Age": 35,
        "Department": "Marketing",
        "Salary": 65000
    },
    {
        "First Name": "Jane",
        "Last Name": "Doe",
        "Email": "jane.doe@example.com",
        "Age": 28,
        "Department": "Engineering",
        "Salary": 78000
    },
    {
        "First Name": "Robert",
        "Last Name": "Johnson",
        "Email": "robert.j@example.com",
        "Age": 42,
        "Department": "Finance",
        "Salary": 82000
    },
    {
        "First Name": "Emily",
        "Last Name": "Williams",
        "Email": "emily.w@example.com",
        "Age": 31,
        "Department": "Human Resources",
        "Salary": 58000
    },
    {
        "First Name": null,
        "Last Name": "Brown",
        "Email": "michael.b@example.com",
        "Age": 39,
        "Department": "Sales",
        "Salary": 72000
    },
    {
        "First Name": "Sarah",
        "Last Name": "Miller",
        "Email": null,
        "Age": 27,
        "Department": "Engineering",
        "Salary": 76000
    }
]
```

Notice how:
- Missing values are represented as `null` in the JSON output
- Headers with spaces are preserved correctly

### Complex Example

Now let's look at a more complex example with various data types and special formatting:

**File: complex.csv**
```
Order ID,Customer ID,Product Name,Quantity,Unit Price,Order Date,Shipping Address,Payment Status,Tracking Number,Discount,Tax Rate,Delivery Notes
10045,"CUST-1001","Premium Wireless Headphones",2,129.99,"2023-05-15","123 Main St, Apt 4B, New York, NY 10001","Paid","TRK-7890-XYZ",15.5%,8.875%,"Leave at door, no signature required"
10046,"CUST-1002","Smart Watch Series 5",1,249.99,"2023-05-16","456 Oak Ave, Chicago, IL 60611","Pending","",0%,10.25%,"Call customer before delivery"
10047,"CUST-1001","USB-C Fast Charging Cable",3,19.99,"2023-05-16","123 Main St, Apt 4B, New York, NY 10001","Paid","TRK-7891-ABC",0%,8.875%,""
10048,"CUST-1003","Laptop Backpack - Waterproof",1,79.99,"2023-05-17","789 Pine St, San Francisco, CA 94109","Failed","",5%,8.5%,"Signature required"
10049,"CUST-1004","Bluetooth Speaker - Waterproof",1,89.99,"2023-05-18","101 Maple Dr, Austin, TX 78701","Paid","TRK-7892-DEF",20%,6.25%,"Deliver to back entrance"
10050,,"Wireless Mouse - Ergonomic",2,45.99,"2023-05-18","","Paid","TRK-7893-GHI",10%,9.5%,"N/A"
```

**Command for handling this complex data with special formatting:**
```
python csv_to_json.py complex.csv -o complex.json -d ',' -q '"'
```

This example demonstrates:
- Double quotes used within data (-q '"')
- Commas within quoted text
- Percentage values
- Empty fields

## Advanced Options

The converter offers many options to handle different types of CSV files:

### CSV Format Options

- **Delimiter**: Change the character used to separate values
  ```
  python csv_to_json.py data.csv -d ';'  # Use semicolon instead of comma
  ```

- **Quote Character**: Change the character used to quote text
  ```
  python csv_to_json.py data.csv -q "'"  # Use single quotes instead of double quotes
  ```

- **Skip Initial Space**: Ignore spaces after delimiters
  ```
  python csv_to_json.py data.csv -s
  ```

### Output Options

- **Pretty Print**: Format JSON with proper indentation (default)
  ```
  python csv_to_json.py data.csv -p  # Pretty print (default)
  python csv_to_json.py data.csv --no-pretty  # Compact output without formatting
  ```

- **Indentation**: Change the indentation level for pretty printing
  ```
  python csv_to_json.py data.csv -i 2  # Use 2 spaces for indentation
  ```

- **Output as Records**: Output as array of arrays instead of array of objects
  ```
  python csv_to_json.py data.csv -r
  ```

### Data Processing Options

### Understanding Type Conversion

When the converter reads your CSV file, it tries to guess what type of data each value is. For example:
- "42" becomes the number 42
- "3.14" becomes the decimal 3.14
- "true" or "yes" becomes a boolean true value
- "false" or "no" becomes a boolean false value
- Empty values become null

Let's look at a simple example:

**File: custom_types.csv**
```
ID,Item,Quantity,Price,In Stock,Rating
1,Keyboard,5,29.99,Yes,4.5
2,Mouse,3,19.99,No,4.2
3,Monitor,1,149.99,Yes,4.8
4,Laptop,0,899.99,No,4.7
```

#### With Automatic Type Detection (Default)

```
python csv_to_json.py custom_types.csv -o custom_types_auto.json
```

**Result (custom_types_auto.json):**
```json
[
    {
        "ID": 1,
        "Item": "Keyboard",
        "Quantity": 5,
        "Price": 29.99,
        "In Stock": true,
        "Rating": 4.5
    },
    ...
]
```

Notice how:
- Numbers are converted to numeric values (no quotes)
- "Yes" is converted to `true` (boolean)
- "No" is converted to `false` (boolean)

#### Without Automatic Type Detection (Everything as Strings)

```
python csv_to_json.py custom_types.csv -o custom_types_strings.json --no-auto-types
```

**Result (custom_types_strings.json):**
```json
[
    {
        "ID": "1",
        "Item": "Keyboard",
        "Quantity": "5",
        "Price": "29.99",
        "In Stock": "Yes",
        "Rating": "4.5"
    },
    ...
]
```

Notice how all values remain as strings (with quotes), exactly as they were in the CSV file.

### When to Turn Off Automatic Type Detection

You might want to turn off automatic type detection when:
- You have numbers that should be treated as text (like ZIP codes that start with zero)
- You have dates that shouldn't be converted
- You want to preserve the exact format of your data

### Other Data Processing Options

- **Null Values**: Specify values to be treated as null
  ```
  python csv_to_json.py data.csv -N "NA,N/A,null"  # Treat "NA", "N/A", and "null" as null values
  ```

- **Encoding**: Specify character encoding for input/output files
  ```
  python csv_to_json.py data.csv -e utf-8  # Use UTF-8 encoding (default)
  ```

## Common Use Cases

### 1. Converting Exported Data

If you have exported data from a spreadsheet, database, or CRM system, you can convert it to JSON for use in web applications or data analysis tools.

### 2. Data Migration

When migrating data between systems, JSON is often a more flexible format than CSV, especially for nested or complex data structures.

### 3. API Integration

Many APIs accept or return data in JSON format. Converting your CSV data to JSON makes it easier to integrate with these APIs.

### 4. Data Analysis

Converting data to JSON can make it easier to work with in some programming languages or data analysis tools.

## Troubleshooting

### Common Problems and Solutions

#### "File not found" Error

If you see a message like:
```
ERROR: Input file not found: your_file.csv
```

**Check that:**
- The file exists in the location you're running the command
- You've typed the filename correctly (including uppercase/lowercase letters)
- You're in the correct folder when running the command

**Solution Example:**
If your file is in a different folder, provide the full path:
```
python csv_to_json.py C:\MyFolder\your_file.csv
```
or
```
python csv_to_json.py /home/user/MyFolder/your_file.csv
```

#### CSV Parsing Errors

If you see errors about your CSV file format:

**Check if your CSV:**
- Uses a different delimiter (like semicolons or tabs instead of commas)
- Has text fields that contain commas within them
- Has quote characters within data fields

**Solution Examples:**

For semicolon-delimited files (common in Europe):
```
python csv_to_json.py your_file.csv -d ';'
```

For tab-delimited files:
```
python csv_to_json.py your_file.csv -d $'\t'
```

#### Wrong Data Types

If your numbers are showing up as strings (with quotes) or vice versa:

**Solutions:**
- To keep everything as strings: `--no-auto-types`
- To specify certain values as null: `-N "NA,N/A,null"`

#### Special Characters Not Displaying Correctly

If you see weird symbols instead of proper characters:

**Try specifying the encoding:**
```
python csv_to_json.py your_file.csv -e latin1
```
or
```
python csv_to_json.py your_file.csv -e utf-16
```

### Visual Guide to Common Errors

#### Problem: Comma in Your Data

Your CSV file:
```csv
Name,Address,City
John Smith,"123 Main St, Apt 4",New York
```

If you don't use quotes properly, the converter will think "Apt 4" is a separate column.

**Correct way:**
Make sure text with commas is enclosed in quotes as shown above.

#### Problem: Missing Headers

Your CSV file:
```csv
John,30,New York
Sarah,25,Boston
```

Without headers, the converter doesn't know what to name each field.

**Correct way:**
Add a header row:
```csv
Name,Age,City
John,30,New York
Sarah,25,Boston
```

#### Problem: Inconsistent Columns

Your CSV file:
```csv
Name,Age,City
John,30,New York
Sarah,25
Mike,45,Chicago,Software Engineer
```

**Issues:**
- The second row is missing the City
- The fourth row has an extra column

**Correct way:**
Make sure each row has the same number of columns:
```csv
Name,Age,City,Occupation
John,30,New York,
Sarah,25,,
Mike,45,Chicago,Software Engineer
```

## Command Reference

```
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
```

## Tips for Working with CSV Files

1. **Check your headers**: Make sure your CSV file has headers in the first row for best results.

2. **Mind your quotes**: If your data contains commas or quotes, make sure they are properly escaped in your CSV file.

3. **Watch for special characters**: If your data contains non-English characters, make sure to use the correct encoding.

4. **Consistency is key**: Try to keep your data consistent across rows (same number of columns, same data types in each column).

5. **Clean your data**: Remove any unnecessary whitespace, special characters, or formatting before conversion.

---

This tool was built with Python and uses standard libraries to ensure maximum compatibility and performance.