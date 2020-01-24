import urllib.request, json, csv
import pandas as pd

url = "https://tanahairku-experimental-cl.firebaseio.com/.json"
csv_filename = "test.csv"
xlsx_filename = "test.xlsx"

with urllib.request.urlopen(url) as url_req:
    json_data = json.loads(url_req.read())
    print(json_data)

#Open the file stream
fr = open(csv_filename, "w+")
csv_file = csv.writer(fr)

#Write CSV Header (Columns)
header = ["sessionID", "userDate", "userInterval", "userLog"]
csv_file.writerow(header)

#Write the value to csv
for id, jd in json_data.items():
    csv_file.writerow([id, jd["userDate"], jd["userInterval"], jd["userLog"]])

#Close the file stream
fr.close()

#Convert csv to xlsx
xlsx_file = pd.read_csv(csv_filename).to_excel(xlsx_filename, index=None, header=True)