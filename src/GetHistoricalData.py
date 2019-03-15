import sys
import csv
import json
import requests

# %% Get console arguments
input_file_path = sys.argv[1]
output_folder_path = sys.argv[2]
api_key = sys.argv[3]

# %% Get optional console arguments
start = (int(sys.argv[4])
         if len(sys.argv) > 4
         else None)

end = (int(sys.argv[5])
       if len(sys.argv) > 5
       else None)

# %% Open Google location data file
input_file = open(input_file_path)

# %% Create CSV reader
csv_reader = csv.reader(input_file)

# %% Skip the header
next(csv_reader)

# %% Read the CSV data
data = [row for row in csv_reader]

# %% Limit API calls since maximum is 1000 per day
data = data[start:end]

# %% Process each day
for row in data:

    # Get data from row
    date = row[0]
    latitude = row[1]
    longitude = row[2]

    # Create ISO date-time string
    iso_date_time = date + "T00:00:00Z"

    # Create URL template
    url_template = "https://api.darksky.net/forecast/{}/{},{},{}?exclude=currently,hourly"

    # Create request URL
    request_url = url_template.format(
        api_key,
        latitude,
        longitude,
        iso_date_time)

    # Get historical weather data as JSON
    response = requests.get(request_url)

    # Handle unsuccessful response code
    if not response.ok:
        print(response.json())
        continue

    # Get JSON response
    json_data = response.json()

    # Create output JSON (cache) file
    output_json = open(
        file=output_folder_path + date + ".json",
        mode="wt")

    # Write JSON to output file
    json.dump(
        obj=json_data,
        fp=output_json,
        indent=4)

    # Close the JSON file
    output_json.close()

    # Notify user of status
    print(date)
