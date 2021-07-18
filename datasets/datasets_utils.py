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


def write_excel(excel_file, excel_sheet_name, data, *append_write):
    excel_write_mode = 'w'
    if append_write.__len__() != 0:
        if append_write[0] and type(append_write[0]).__name__ == 'bool':
            excel_write_mode = 'a'
    with pd.ExcelWriter(excel_file, mode=excel_write_mode) as writer:
        pd.DataFrame(data).to_excel(writer, sheet_name=excel_sheet_name, index=False, header=False)


def write_csv(csv_file, data, *append_write):
    csv_write_mode = 'w'
    if append_write.__len__() != 0:
        if append_write[0] and type(append_write[0]).__name__ == 'bool':
            csv_write_mode = 'a'
    with open(csv_file, csv_write_mode) as writer:
        pd.DataFrame(data).to_csv(writer, encoding = 'utf-8', index=False, header=False, line_terminator='\n')


def read_csv(csv_file):
    return pd.read_csv(csv_file, encoding='gbk', lineterminator='\n')


