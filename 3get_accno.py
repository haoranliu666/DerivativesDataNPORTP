import requests
import re
import json

#get series data
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/2series.json', 'r') as handle:
    series = json.load(handle)

series_unique = []

for series_list in series:
    for series_num in series_list:
        series_unique.append(series_num)

series_unique = list(set(series_unique))

#get accno 
url_prefix = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="
url_suffix =  "&type=NPORT-P&dateb=&count=100&scd=filings&search_text="

re_accno = re.compile(r'Monthly Portfolio Investments Report on Form N-PORT \(Public\)<br \/>Acc-no: (.*)&nbsp;\(40 Act\)&nbsp;')

# headers = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
# }

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40'
}


accno = []

for i in range(0, len(series_unique)):
    r = requests.get(url_prefix + series_unique[i] + url_suffix, headers = headers)
    accno.append(re_accno.findall(r.text))
    if accno[i] != []:
        print(i)
        print(accno[i])

accno_cleaned = []
for accno_list in accno:
    accno_list_temp = []
    for accno_num in accno_list:
        temp = accno_num.split('-')
        accno_list_temp.append(temp[0] + temp[1] + temp[2])
    accno_cleaned.append(accno_list_temp)

#save data
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/3series_unique.json', 'w') as handle:
    json.dump(series_unique, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/3accno.json', 'w') as handle:
    json.dump(accno_cleaned, handle, indent=2)
