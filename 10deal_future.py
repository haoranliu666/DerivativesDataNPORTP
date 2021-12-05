import re
import json
import os

path = '/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/c11/'
file_list = os.listdir(path)


#deal Forward

re_c11_type = re.compile(r'a\. Type of derivative instrument that most closely\n\t\t\t\trepresents the investment, selected from among the following\n\t\t\t\t\(forward, future, option, swaption, swap \(including but not limited\n\t\t\t\tto total return swaps, credit default swaps, and interest rate\n\t\t\t\tswaps\), warrant, other\)\.<\/td><td><div class="fakeBox2">\n\t\t\t(.*?)\n\t\t\t<span>Â\xa0<\/span><\/div><\/td><\/tr><\/table><p xmlns:n1="http:\/\/www\.sec\.gov\/edgar\/common_drp" xmlns:ns2="http:\/\/www\.sec\.gov\/edgar\/statecodes" xmlns:ns3="http:\/\/www\.sec\.gov\/edgar\/regacommon">b\. Counterparty\.<br>')

file_list.remove('.DS_Store')

accno = []
name = []
lei = []
payoff = []
name_issuer = []
title_issue = []
cusip = []
isin = []
ticker = []
exp_date = []
aggregate = []
isocurrency = []
unreal = []

re_name = re.compile(r'Name of counterparty\.<\/td><td><div class="fakeBox">(.*?)<span>Â\xa0')
re_lei = re.compile(r'LEI \(if any\) of counterparty\.<\/td><td><div class="fakeBox2">(.*?)<span>Â\xa0')
re_payoff = re.compile(r'Payoff profile, selected from among the following \(long, short\)\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_name_issuer = re.compile(r'Name of issuer\.\n\t\t\t\t<\/td><td><div class="fakeBox">(.*?)<span>Â\xa0')
re_title_issue = re.compile(r'Title of issue\.\n\t\t\t\t<\/td><td><div class="fakeBox">(.*?)<span>Â\xa0')
re_cusip = re.compile(r'CUSIP\.<\/span><\/td><td><div class="fakeBox3">(.*?)<span>Â\xa0')
re_isin = re.compile(r'ISIN \(if CUSIP is not available\)\.<\/span><\/td><td><div class="fakeBox3">(.*?)<span>Â\xa0')
re_ticker = re.compile(r'Ticker \(if CUSIP and ISIN are not available\)\.<\/span><\/td><td><div class="fakeBox3">(.*?)<span>Â\xa0')
re_exp_date = re.compile(r'Expiration date\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_aggregate = re.compile(r'Aggregate notional amount or contract value on trade date\. \n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_isocurrency = re.compile(r'ISO Currency Code\.\n\t\t\t<\/td><td><div class="fakeBox4">\n\t\t\t\t(.*?)\n\t\t\t<span>Â\xa0')
re_unreal = re.compile(r'Unrealized appreciation or depreciation\.  Depreciation shall be reported as a negative number\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')

for file_name in file_list:
    file_name_temp1 = file_name.split('_')
    file_name_temp2 = file_name_temp1[2].split('.')
    file_num = file_name_temp1[1]
    file_accno = file_name_temp2[0]
    with open(path + file_name, 'r') as handle:
        content = json.load(handle)
    not_empty_c11 = []
    for c11 in content:
        if len(c11) >= 20:
            not_empty_c11.append(c11)
    if not_empty_c11 != []:
        for c11_item in not_empty_c11:
            c11_type_temp = re_c11_type.findall(c11_item)
            if len(c11_type_temp) == 1:
                if c11_type_temp[0] == 'Future':
                    accno.append(file_accno)
                    name.append(re_name.findall(c11_item))
                    lei.append(re_lei.findall(c11_item))
                    payoff.append(re_payoff.findall(c11_item))
                    name_issuer.append(re_name_issuer.findall(c11_item))
                    title_issue.append(re_title_issue.findall(c11_item))
                    cusip.append(re_cusip.findall(c11_item))
                    isin.append(re_isin.findall(c11_item))
                    ticker.append(re_ticker.findall(c11_item))
                    exp_date.append(re_exp_date.findall(c11_item))
                    aggregate.append(re_aggregate.findall(c11_item))
                    isocurrency.append(re_isocurrency.findall(c11_item))
                    unreal.append(re_unreal.findall(c11_item))






with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'accno' + '.json', 'w') as handle:
    json.dump(accno, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'name' + '.json', 'w') as handle:
    json.dump(name, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'lei' + '.json', 'w') as handle:
    json.dump(lei, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'payoff' + '.json', 'w') as handle:
    json.dump(payoff, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'name_issuer' + '.json', 'w') as handle:
    json.dump(name_issuer, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'title_issue' + '.json', 'w') as handle:
    json.dump(title_issue, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'cusip' + '.json', 'w') as handle:
    json.dump(cusip, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'isin' + '.json', 'w') as handle:
    json.dump(isin, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'ticker' + '.json', 'w') as handle:
    json.dump(ticker, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'exp_date' + '.json', 'w') as handle:
    json.dump(exp_date, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'aggregate' + '.json', 'w') as handle:
    json.dump(aggregate, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'isocurrency' + '.json', 'w') as handle:
    json.dump(isocurrency, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'unreal' + '.json', 'w') as handle:
    json.dump(unreal, handle, indent=2)

