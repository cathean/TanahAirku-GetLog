import urllib.request, json, csv
import pandas as pd

url = "https://tanahairku-experimental-cl.firebaseio.com/users.json"
csv_filename = "test.csv"
xlsx_filename = "test.xlsx"

with urllib.request.urlopen(url) as url_req:
    json_data = json.loads(url_req.read())
    #print(json_data)

#Open the file stream
fr = open(csv_filename, "w+")
csv_file = csv.writer(fr)
log_user_list = []

#Write CSV Header (Columns)
#header = ["sessionID", "Date", "Items_Interval", "Items_Log"]
#csv_file.writerow(header)

for device_id, l in json_data.items():
    print("Device_ID : " + device_id)
    for dir_name, jd in l.items():
        if(dir_name == "log"):
            for session_id, dt in jd.items():
                print("Session_ID     : " + session_id)
                print("Date           : " + dt["Date"])
                print("Items_Interval : " + dt["Items_Interval"])
                print("Items_Log      :" + dt["Items_Log"])
                #csv_file.writerow([session_id, dt["Date"], dt["Items_Interval"], dt["Items_Log"]])
                for dt_name, it in dt.items():
                    if(dt_name == "Items_Log"):
                        #Strip the whitespace and by comma
                        log_user = [x.strip() for x in it.split(',')]
                        log_user_list.append(log_user)
                        print(log_user)

log_user_list.sort(key=len, reverse=True)

for i in log_user_list:
    csv_file.writerow(i)

#Close the file stream
fr.close()

#Convert csv to xlsx
xlsx_file = pd.read_csv(csv_filename).to_excel(xlsx_filename, index=None)