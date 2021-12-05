import requests
import re
import json

#get cik,series,accno data
#2cik->2series
#2series->3series
#3series->3accno
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/2cik_unique.json', 'r') as handle:
    cik_unique = json.load(handle)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/2series.json', 'r') as handle:
    series = json.load(handle)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/3series_unique.json', 'r') as handle:
    series_unique = json.load(handle)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/3accno.json', 'r') as handle:
    accno = json.load(handle)

#download nport file
url_prefix = "https://www.sec.gov/Archives/edgar/data/"
url_suffix = "/xslFormNPORT-P_X01/primary_doc.xml"

# headers = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
# }

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
}

file_count = 0

for i in range(0, len(cik_unique)):
    for series_id in series[i]:
        for accno_id in accno[series_unique.index(series_id)]:
            url = url_prefix + cik_unique[i].lstrip('0') + '/' + accno_id + url_suffix
            print(url)
            r = requests.get(url, headers = headers)
            if 'File Not Found Error Alert (404)' not in r.text:                            
                file_count += 1
                print(file_count)
                with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/nport_file/' + str(file_count) + '_' + str(accno_id) + '.html', 'w', encoding='ISO-8859-1') as f:
                    f.write(r.text)
            else:
                print("File not found")

