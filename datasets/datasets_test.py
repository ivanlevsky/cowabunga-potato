from python_common.global_param import excel_datasets, csv_datasets
from datasets.datasets_utils import read_excel

# read excel, use converters decide column type, if all column type is str,
# function equals:read_excel(excel_datasets, 'movie', True, dtype=str)
result = read_excel(excel_datasets, 'movie', True, converters={
    'id': int,
    'name': str,
    'chnname': str,
    'cast': str,
    'year': str,
    'region': str,
    'type': str,
    'viewed': str,
    'want_to_review': str})
print(result)
