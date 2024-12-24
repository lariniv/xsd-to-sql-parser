# Project Name

## Overview

Python script that parses and converts NBU xsd statreports to SQL.

## Prerequisites

- Python (3.13+) - [Download Python](https://www.python.org/downloads/)
- pip (24.3+) - Comes pre-installed with the latest Python.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/lariniv/xsd-to-sql-parser.git
   cd xsd-to-sql-parser
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Upgrade pip to the latest version:

   ```bash
   python -m pip install --upgrade pip
   ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
6. Configure the src/consts.py file with valid data
```python
path = "https://bank.gov.ua/NBUStatService/v1/statdirectory/report/f3wx.xsd?reportdate=20250101" # path to the XSD document

output_file = 'output.sql' # file where the SQL code will be delivered
table_name = 'XSD_PARSE' # name of the table

id_param = 0 # optional parameter, by which the id will be incremented

src_db_owner = "src_db_ownership" # owner of the database
src_db_table = "src_db_table" # table name

a010 = None # a010 is parsed by script, but can be passed manually

start_date = None # start_date is parsed by script, but can be passed manually
nn_in_base_detail = None 

```

7. Run the script
```bash
python src/main.py
```
