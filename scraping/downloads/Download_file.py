import urllib

#Example url
google_url = "http://chart.finance.yahoo.com/table.csv?s=GOOGL&a=7&b=20&c=2016&d=8&e=20&f=2016&g=d&ignore=.csv"

#Function
def download_data(csv_url):
    response = urllib.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv) #Convert to string
    csv_str_split = csv_str.split("\\n") #Apply Split

    dest_url = r'file.csv'
    fx = open(dest_url, "w") #Open a file in write mode

    for line in csv_str_split:
        fx.write(line + "\n") #Write Data to the file

    fx.close()

download_data(google_url)