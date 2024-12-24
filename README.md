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
```bash
path = "https://bank.gov.ua/NBUStatService/v1/statdirectory/report/f3wx.xsd?reportdate=20250101"

output_file = 'output.sql'
table_name = 'XSD_PARSE'

id_param = 0

src_db_owner = "src_db_ownership"
src_db_table = "src_db_table"

a010 = None

start_date = None
nn_in_base_detail = None

```

7. Run the script
```bash
python src/main.py
```
