# path to the XSD document
path = "https://bank.gov.ua/NBUStatService/v1/statdirectory/report/f3wx.xsd?reportdate=20250101"

output_file = 'output.sql'  # file where the SQL code will be delivered
table_name = 'XSD_PARSE'  # name of the table

id_param = 0  # optional parameter, by which the id will be incremented

src_db_owner = "src_db_ownership"  # owner of the database
src_db_table = "src_db_table"  # table name

a010 = None  # a010 is parsed by script, but can be passed manually

start_date = None  # start_date is parsed by script, but can be passed manually
nn_in_base_detail = None
