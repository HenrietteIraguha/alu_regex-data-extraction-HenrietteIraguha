Data Extraction 

This project is a Python-based text data extractor that scans a raw text file and automatically extracts:

 Data Types Extracted
The program extracts the following **four (4)** data types using regex patterns:

Email addresses (with masking for privacy)
   - Example: user@example.com, firstname.lastname@company.co.uk


 URLs (HTTP/HTTPS only)
    - Example: https://www.example.com, http://sub.domain.org/page?id=1


 Phone numbers (common formats)
    - Example: (123) 456-7890, 123-456-7890, 123.456.7890


 Time values (12-hour and 24-hour formats)
    - Example: 9:00 AM, 14:30


The extracted data is then saved in a clean, structured JSON file.

Sensitive consideration
  - Invalid emails, phone numbers, URLs, and time formats are ignored.

  - HTML or script-like content present in the input is not executed and is safely ignored.
   
  - Email addresses are masked before being written to the output file to prevent unnecessary exposure.