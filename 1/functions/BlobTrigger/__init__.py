##### LIBRARY #####
# library for functions
import logging
import azure.functions as func
# library for general purpose
import json, requests, uuid
# library for table storage
from azure.data.tables import TableClient

##### PARAMETER #####
# API URI of custom vision prediction endpoint and prediction key
API_URI = ""
CUSTOMVISION_PREDICTION_KEY = ""
# Connection string of storage account
STORAGE_CONNECT_STR = ""


# function to convert a resopnse to dictionary
def convert_response_to_dict(response_text):
    return json.loads(response_text)

def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    img_uri = myblob.uri
    logging.info(f"Image URI: {img_uri}")

    # make a http post request to custom vision prediction endpoint
    options = {
        "method": "POST",
        "headers": {
            "Prediction-Key": CUSTOMVISION_PREDICTION_KEY,
            "Content-Type": "application/json"
        },
        "body": {"Url": img_uri}
    }

    # submit the request to custom vision prediction endpoint
    response = requests.request("POST", API_URI, headers=options["headers"], json=options["body"])
    logging.info(f"Response: {response.text}")

    # store the response to azure table storage
    tableClient = TableClient.from_connection_string(conn_str=STORAGE_CONNECT_STR, table_name="result")

    # convert the json resopns to dictionary
    response_dict = convert_response_to_dict(response.text)

    # get the prediction result
    prediction = response_dict["predictions"][0]["tagName"]
    logging.info(f"Prediction: {prediction}")
    probability = response_dict["predictions"][0]["probability"]
    logging.info(f"Probability: {probability}")

    # generate a row key for the table storage
    row_key = str(uuid.uuid4())
    logging.info(f"Row Key: {row_key}")

    # make an entity to store in azure table storage
    entity = {
        "PartitionKey": "result",
        "RowKey": row_key,
        "Prediction": prediction,
        "Probability": probability
    }

    # insert the entity to azure table storage
    tableClient.create_entity(entity=entity)
