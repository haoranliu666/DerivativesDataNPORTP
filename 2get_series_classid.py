import requests
import re
import json

#get cik data
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/1cik.json', 'r') as handle:
    cik = json.load(handle)

cik_unique = []

for cik_list in cik:
    for cik_num in cik_list:
        cik_unique.append(cik_num)

cik_unique = list(set(cik_unique))


#get CIK for ticker

url_prefix = "https://www.sec.gov/cgi-bin/series?ticker="
url_suffix = "&CIK=&sc=companyseries&type=N-PX&Find=Search"

re_series = re.compile(r'<td><\/td><td colspan="2" nowrap="nowrap"><a class="hot" href="\/cgi-bin\/browse-edgar\?CIK=(.*)&amp;action=getcompany&amp;scd=filings">')
re_classid = re.compile('<td><\/td><td><\/td><td nowrap="nowrap"><a class="nav" href="\/cgi-bin\/browse-edgar\?CIK=(.*)&amp;action=getcompany&amp;scd=filings">')

series = []
classid = []

for i in range(0, len(cik_unique)):
    r = requests.get(url_prefix + cik_unique[i] + url_suffix)
    series.append(re_series.findall(r.text))
    classid.append(re_classid.findall(r.text))
    if i%100 == 0:
        print(i)
        print(series[i])
        print(classid[i])

#save data
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/2cik_unique.json', 'w') as handle:
    json.dump(cik_unique, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/2series.json', 'w') as handle:
    json.dump(series, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/2classid.json', 'w') as handle:
    json.dump(classid, handle, indent=2)