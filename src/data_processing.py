#  NAME:  SHAKHRIZOD
#  FILE:  Process file of application
#  REQUIREMENTS:  None



#  Process data function
def process_data(data):
    """
    gets data in <list> type
    """
    processed = []
    for item in data:
        new_value = item['value'] ** 2  # Example of operations
        processed.append({"id": item['id'], "new_value": new_value})  #  Adding new value
    return processed
