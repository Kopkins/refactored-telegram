
class Table():
    def __init__(self, rows):
        string_rows = [list(map(str, row)) for row in rows]
        self.rows = self.create_table_rows(string_rows)

    def create_table_rows(self, rows):
        column_widths = self.get_formatting(rows)
        table_rows = []
        for row in rows:
            strings = [('{:{}}\t'.format(row[i], column_widths[i])) for i in range(0, len(row))]
            table_rows.append(''.join(strings))
        return table_rows
                

    def get_formatting(self, rows):
        columns = [[row[i] for row in rows] for i in range(0, len(rows[0]))]
        widths = [(max(len(value) for value in column)) for column in columns]
        return widths

    def __str__(self):
        return '\n'.join(self.rows)
