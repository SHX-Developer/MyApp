#  NAME:  SHAKHRIZOD
#  FILE:  Main file of application
#  REQUIREMENTS:  json



#  Import modules
import json
from data_processing import process_data


#  Example of data
def main():
    data = [
        {"id": 1, "value": 100},
        {"id": 2, "value": 200},
        {"id": 3, "value": 300}]

    #  Data processing
    processed = process_data(data)

    #  Saving result
    with open("result.json", mode = "w") as file:
        json.dump(processed, file, indent = 4)
    
    #  Print success result text
    print("Processing completed. Results saved to result.json.")


#  Launch program
if __name__ == "__main__":
    main()
