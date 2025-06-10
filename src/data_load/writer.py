from typing import List, Dict, Any

def csv_writer(data: List[Dict[str, Any]], new_file_path: str) -> None:
    '''
    Write a CSV file from the data read and transformed.
    Args:
        List[Dict[str: Any]]: Data in formated list of dictionaries to be written into CSV.
        str: Path where the new CSV file will be saved. 
    Returns:
        None: Writes a CSV file in the specified path and does not return anything.
    Raises:
        Exception: If an error occurs while writing the CSV file. 
    '''
    import csv
    try:
        with open(new_file_path, mode='w', newline='', encoding='utf') as new_file:
            writer = csv.DictWriter(new_file, fieldnames = data[0].keys())
            writer.writeheader()
            for row in data:
                writer.writerows(row)
    except Exception as e:
        raise Exception (f"An error occurred while writing the CSV file '{new_file_path}': {str(e)}")
    
def json_writer(data: List[Dict[str, Any]], new_file_path: str) -> None:
    '''
    Write a JSON file from the data read and transformed.
    Args:
        List[Dict[str: Any]]: Data in formated list of dictionaries to be written into JSON.
        str: Path where the new JSON file will be saved. 
    Returns:
        None: Writes a JSON file in the specified path and does not return anything.
    Raises:
        Exception: If an error occurs while writing the JSON file. 
    '''
    import json
    try:
        with open(new_file_path, mode='w', newline='', encoding='utf-8') as new_file:
            json.dump(data, new_file, indent=4)
    except Exception as e:
        raise Exception(f"An error occurred while writing the JSON file '{new_file_path}': {str(e)}")













