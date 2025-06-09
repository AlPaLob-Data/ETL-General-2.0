from typing import List, Dict, Tuple, Any

def csv_reader(file_path:str) -> tuple[List[Dict[str: Any]], Dict[str: int]]:
    '''
    Reader function for CSV files. Returns a list of dictionaries and a tuple with the number of rows, columns and file_size in bytes.

    Args:
        file_path (str): The path of the CSV file to read.
    Returns:
        List[Dict[str: Any]]: List of dicctionaries where each dictionary represents a row in the CSV.
        Dict[str: int]: Dictionary with the number of rows, columns and file_size in bytes. 

    Raises:
        FileNotFoundError: If the file is not found
        Exception: If any other error occurs during the reader of the CSV.

    '''
    import csv
    import os
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8')as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            row_data = len(data)
            column_data = len(reader[0]) if reader else 0
            size = os.path.getsize(file_path)
            resumen = {
                "rows": row_data,
                "columns": column_data,
                "file_size": size
            }    
            return data, resumen
    except FileNotFoundError:
        raise FileNotFoundError(f"the file '{file_path}' was not found")
    except Exception as e:
        raise Exception(f"An error occurred while reading the CSV file '{file_path}': {str(e)}")

    
def json_reader(file_path:str) -> Tuple[List[Dict[str: Any]], Dict[str: int]]:
    '''Reads a JSON file and returns the list of dictionaries and a summary dictionary.
    Args:
       file_path (str): The path to the JSON file.
    Returns:
       Tuple[List[Dict[str: Any]]: A list of diccionarios representing the rows of the JSON file.
       Dict[str: int]: A dictionary containing the summary of the JSON file.
    Raises:
       FileNotFoundError: If the specified JSON file does not exist.
       Exception: If an error occurs while reading the JSON file.    
    '''
    import json
    import os
    try:
        with open(file_path, mode='r', newline= '' , encoding='utf-8') as file:
            data = json.load(file)
            row_data = len(data)
            column_data = len(data[0]) if data else 0
            size = os.path.getsize(file_path)
            resumen = {
                "rows": row_data,
                "columns": column_data,
                "file_size": size
            }
            return  data, resumen
    except FileNotFoundError:
        raise FileNotFoundError(f"the file '{file_path}' was not found")
    except Exception as e:
        raise Exception(f"An error occurred while reading the CSV file '{file_path}': {str(e)}")


    
