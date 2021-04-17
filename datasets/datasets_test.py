from python_common.global_param import GlobalParam
from datasets.datasets_utils import read_excel

# read excel, use converters decide column type, if all column type is str,
# function equals:read_excel(excel_datasets, 'movie', True, dtype=str)
result = read_excel(GlobalParam.get_excel_datasets(), 'movie_maria', True, converters={
    'id': int,
    'name': str,
    'chnname': str,
    'main_cast': str,
    'year': str,
    'region': str,
    'type': str,
    'viewed': str,
    'want_to_review': str})
print(result)
