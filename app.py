from flask import Flask, jsonify, request, redirect
from datetime import date, datetime
import pandas as pd
import string
import os
from datetime import datetime
from random import choices

FILE_NAME = 'data.csv'
host = 'http://localhost:105/'

app = Flask(__name__)

@app.route('/')
def url_shortner():
    original_url = request.args['original_url']
    print(original_url)
    return generate_short_link(original_url)

def generate_short_link(original_url):

    result = existing_url(original_url)

    if result.keys():
        return jsonify(result)
    else:
        characters = string.digits + string.ascii_letters
        randomStr = ''.join(choices(characters, k=3))
        short_url = host + randomStr

        result = {"original_url": original_url, "short_url":short_url, "visits":1, "date_created": str(datetime.now().strftime("%m-%d-%Y"))}
        df = pd.DataFrame(result, index=[0])
        df.to_csv(FILE_NAME, mode='a', header=False, index=False)

        return jsonify(result)
        

def existing_url(original_url):

    # check if file data file exist
    if(os.path.exists(FILE_NAME)):

        # If file exist open the file and load the data into dataframe
        df = pd.read_csv(FILE_NAME)

        if original_url in df.values:
            
            # if url already exists in the file increase the count of visits
            df.loc[df['original_url'] == original_url, 'visits'] += 1

            # get the updated row from dataframe matches the original url value
            df_row = df.loc[df['original_url'] == original_url]
            
            # write updated data to file
            df.to_csv(FILE_NAME, index=False)

            return df_row.to_dict('r')[0]

        else:   

            # if url does not exist in the file, return blank dictionary
            return {}
    else:

        # if file do not exist, then create the file and save column names in csv file.
        column_names = ["original_url", "short_url", "visits", "date_created"]
        df = pd.DataFrame(columns=column_names)
        df.to_csv(FILE_NAME, index=False)
        
        # return blank dictionary as data is not present.
        return {}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105, debug=True)