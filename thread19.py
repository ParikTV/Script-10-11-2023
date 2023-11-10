import threading
import requests


def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
        print(f"{filename} downloaded")


# URLs of two files to be downloaded
urls = ["https://data.ny.gov/api/views/d6yy-54nr/rows.csv?accessType=DOWNLOAD",
        "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD"]
filenames = ["Lottery_Powerball_Winning_Numbers__Beginning_2010.csv", "Electric_Vehicle_Population_Data.csv"]
# https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD
# http://api.datosabiertos.muniesparza.go.cr/api/v2/dashboards/MEDID-CLIMA.json/?auth_key=oBJEThwwdsXhSuen2ZPRRgB7PeFJFu9Bw7Murb2Q"
# http://api.datosabiertos.muniesparza.go.cr/api/v2/datastreams/HISTO-65535/data.json/?auth_key=R3ViN0vgxRzyzDRtpt74CJrWjTfqOVA21gcTnkqY&limit=50
# http://api.datosabiertos.muniesparza.go.cr/api/v2/datastreams/DECLA-DE-BIENE-INMUE-2021/data.xls/
# ?auth_key=bVNfoMbMrNGX2qHbloRTAIPYUSdVYC01tucj12AX&limit=50&"

# create and start two threads
for i in range(2):
    t = threading.Thread(target=download_file, args=(urls[i], filenames[i]))
    t.start()
