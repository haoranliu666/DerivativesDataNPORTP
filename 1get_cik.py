import xlrd 
import requests
import re
import json

#get ticker data
rb = xlrd.open_workbook("/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/ticker_1103.xlsx")
sh = rb.sheet_by_name('Sheet1')
ticker = []
for i in range(0, 14745):
    ticker.append(sh.cell_value(i, 0))


#get CIK for ticker

url_prefix = "https://www.sec.gov/cgi-bin/series?ticker="
url_suffix = "&CIK=&sc=companyseries&type=N-PX&Find=Search"

re_cik = re.compile(r'<td colspan="3" nowrap="nowrap"><a class="search" href="\/cgi-bin\/browse-edgar\?CIK=(.*)&amp;action=getcompany">')

cik = []
for i in range(0, len(ticker)):
    r = requests.get(url_prefix + ticker[i] + url_suffix)
    cik.append(re_cik.findall(r.text))
    if i%100 == 0:
        print(i)
        print(cik[i])

#save data
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/1ticker.json', 'w') as handle:
    json.dump(ticker, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/1cik.json', 'w') as handle:
    json.dump(cik, handle, indent=2)
