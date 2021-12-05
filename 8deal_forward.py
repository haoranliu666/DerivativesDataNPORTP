import re
import json
import os

path = '/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/c11/'
file_list = os.listdir(path)


#deal Forward

re_c11_type = re.compile(r'a\. Type of derivative instrument that most closely\n\t\t\t\trepresents the investment, selected from among the following\n\t\t\t\t\(forward, future, option, swaption, swap \(including but not limited\n\t\t\t\tto total return swaps, credit default swaps, and interest rate\n\t\t\t\tswaps\), warrant, other\)\.<\/td><td><div class="fakeBox2">\n\t\t\t(.*)\n\t\t\t<span>Â\xa0<\/span><\/div><\/td><\/tr><\/table><p xmlns:n1="http:\/\/www\.sec\.gov\/edgar\/common_drp" xmlns:ns2="http:\/\/www\.sec\.gov\/edgar\/statecodes" xmlns:ns3="http:\/\/www\.sec\.gov\/edgar\/regacommon">b\. Counterparty\.<br>')

file_list.remove('.DS_Store')

accno = []
name = []
lei = []
amount_sold = []
des_sold = []
amount_pur = []
des_pur = []
date = []
unreal = []

re_name = re.compile(r'Name of counterparty\.<\/td><td><div class="fakeBox">(.*)<span>Â\xa0<\/span><\/div><\/td><\/tr><tr><td class="label">LEI \(if any\) of counterparty\.')
re_lei = re.compile(r'LEI \(if any\) of counterparty\.<\/td><td><div class="fakeBox2">(.*)<span>Â\xa0<\/span><\/div><\/td><\/tr><\/table><table xmlns:n1="http:\/\/www\.sec\.gov\/edgar\/common_drp" xmlns:ns2="http:\/\/www\.sec\.gov\/edgar\/statecodes" xmlns:ns3="http:\/\/www\.sec\.gov\/edgar\/regacommon"><tr><td>i\.\tAmount and description of currency sold\.<\/td><\/tr><\/table><table xmlns:n1="http:\/\/www\.sec\.gov\/edgar\/common_drp" xmlns:ns2="http:\/\/www\.sec\.gov\/edgar\/statecodes" xmlns:ns3="http:\/\/www\.sec\.gov\/edgar\/regacommon"><tr><td class="label">Amount of currency sold\.')
re_amount_sold = re.compile(r'Amount of currency sold\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*)<span>Â\xa0<\/span><\/div><\/td><\/tr><tr><td class="label">Description of currency sold\.')
re_des_sold = re.compile(r'Description of currency sold\.\n\t\t\t<\/td><td><div class="fakeBox4">\n\t\t\t\t(.*)\n\t\t\t<span>Â\xa0<\/span><\/div><\/td><\/tr><\/table><table xmlns:n1="http:\/\/www\.sec\.gov\/edgar\/common_drp" xmlns:ns2="http:\/\/www\.sec\.gov\/edgar\/statecodes" xmlns:ns3="http:\/\/www\.sec\.gov\/edgar\/regacommon"><tr><td>ii\.\tAmount and description of currency purchased\.')
re_amount_pur = re.compile(r'ii\.\tAmount and description of currency purchased\.<\/td><\/tr><\/table><table xmlns:n1="http:\/\/www\.sec\.gov\/edgar\/common_drp" xmlns:ns2="http:\/\/www\.sec\.gov\/edgar\/statecodes" xmlns:ns3="http:\/\/www\.sec\.gov\/edgar\/regacommon"><tr><td class="label">Amount of currency purchased\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*)<span>Â\xa0<\/span><\/div><\/td><\/tr><tr><td class="label">Description of currency purchased\.')
re_des_pur = re.compile(r'Description of currency purchased\.\n\t\t\t<\/td><td><div class="fakeBox4">\n\t\t\t\t(.*)\n\t\t\t<span>Â\xa0<\/span><\/div><\/td><\/tr><tr><td class="label">iii\.\tSettlement date\.')
re_date = re.compile(r'iii\.\tSettlement date\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*)<span>Â\xa0<\/span><\/div><\/td><\/tr><tr><td class="label">iv\.\tUnrealized appreciation or depreciation\. Depreciation shall be reported as a negative number\.')
re_unreal = re.compile(r'iv\.\tUnrealized appreciation or depreciation\. Depreciation shall be reported as a negative number\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*)<span>Â\xa0<\/span><\/div><\/td><\/tr><\/table>')

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
                if c11_type_temp[0] == 'Forward':
                    accno.append(file_accno)
                    name.append(re_name.findall(c11_item))
                    lei.append(re_lei.findall(c11_item))
                    amount_sold.append(re_amount_sold.findall(c11_item))
                    des_sold.append(re_des_sold.findall(c11_item))
                    amount_pur.append(re_amount_pur.findall(c11_item))
                    des_pur.append(re_des_pur.findall(c11_item))
                    date.append(re_date.findall(c11_item))
                    unreal.append(re_unreal.findall(c11_item))



with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'accno' + '.json', 'w') as handle:
    json.dump(accno, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'name' + '.json', 'w') as handle:
    json.dump(name, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'lei' + '.json', 'w') as handle:
    json.dump(lei, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'amount_sold' + '.json', 'w') as handle:
    json.dump(amount_sold, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'des_sold' + '.json', 'w') as handle:
    json.dump(des_sold, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'amount_pur' + '.json', 'w') as handle:
    json.dump(amount_pur, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'des_pur' + '.json', 'w') as handle:
    json.dump(des_pur, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'date' + '.json', 'w') as handle:
    json.dump(date, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'unreal' + '.json', 'w') as handle:
    json.dump(unreal, handle, indent=2)