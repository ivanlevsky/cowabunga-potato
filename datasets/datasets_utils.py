import pandas as pd


def read_excel(excel_file, sheet_name, *remove_header, **excel_converter):
    excel_data = pd.read_excel(excel_file, sheet_name, **excel_converter).fillna('')
    cols = list(excel_data)
    result = [cols]
    for i in excel_data.index:
        temp_list = []
        for c in cols:
            temp_list.append(excel_data[c][i])
        result.append(temp_list)
    if remove_header[0] and type(remove_header[0]).__name__ == 'bool':
        result.pop(0)
    return result

