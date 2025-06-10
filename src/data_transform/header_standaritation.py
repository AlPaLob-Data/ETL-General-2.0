from typing import List, Dict, Any

def header_standardization(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    '''
    Standardizes the headers of a list of dictionaries to be lowercase and snake_case replace spaces and removce the accent mark.
    Args:
        data(List[Dict[str,Any]]): A list of dictionaries representing rows of data.
    Returns:
        List[Dict[str,Any]]: A new list of dictionaries with standardized headers.
    Raises:
        ValueError: If the input data is not in the expected format.
        TypeError: If the input data contains non-string keys
    '''
    import unicodedata
    try:
        data_standarized = []
        original_headers = list(data[0].keys())
        standarize_headers = []
    #Remove accent mark and replace spaces with underscores
        for header in original_headers:
            normalized_header = unicodedata.normalize('NFD', header)
            header_without_accent = ''.join(char for char in normalized_header if unicodedata.category(char) != 'Mn')
            standarize_headers.append(header_without_accent.replace(" ", "_").lower().strip())

    #Iclude standarized headers in a new list
        for row in data:
            standarized_row = {}
            for old_header, value in row.items():
                 index = original_headers.index(old_header)
                 new_header = standarize_headers[index]
                 standarized_row[new_header] = value
                 data_standarized.append(standarized_row)
        return data_standarized         

    except KeyError as e:
        raise ValueError(f"The input data is not in the expected format: {str(e)}")
    except TypeError as e:
        raise TypeError(f"The input data contains non-string keys : {str(e)}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")




    
