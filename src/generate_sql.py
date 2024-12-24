def generate_sql(data_list, table_name, output_file):
    sql_statements = []
    with open(output_file, 'w', encoding="utf-8") as file:
        for row in data_list:
            columns = ', '.join(row.keys())
            values = ', '.join(
                f"'{value}'" if isinstance(
                    value, str) else 'NULL' if value is None else str(value)
                for value in row.values()
            )
            sql = f"INSERT INTO {
                table_name} ({columns}) \nVALUES ({values});\n"
            sql_statements.append(sql)
            file.write(sql + '\n')
    return sql_statements
