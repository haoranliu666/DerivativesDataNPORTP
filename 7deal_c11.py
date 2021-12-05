import re
import json
import os

#get cik,series,accno data
#2cik->2series
#2series->3series
#3series->3accno

#open data
# with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/2cik_unique.json', 'r') as handle:
#     cik_unique = json.load(handle)

# with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/2series.json', 'r') as handle:
#     series = json.load(handle)

# with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/3series_unique.json', 'r') as handle:
#     series_unique = json.load(handle)

# with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/3accno.json', 'r') as handle:
#     accno = json.load(handle)

path = '/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/c11/'
file_list = os.listdir(path)


#check how many cik has non-empty c11
# cik_c11 = []
# for i in range(0, len(cik_unique)):
#     cik_c11.append(0)

# for i in range(0, len(cik_unique)):
#     print(i)
#     for series_id in series[i]:
#         for accno_id in accno[series_unique.index(series_id)]:
#             for file_name in file_list:
#                 if file_name != '.DS_Store':
#                     file_name_temp1 = file_name.split('_')
#                     file_name_temp2 = file_name_temp1[2].split('.')
#                     file_num = file_name_temp1[1]
#                     file_accno = file_name_temp2[0]
#                     if file_accno == accno_id:
#                         with open(path + file_name, 'r') as handle:
#                             content = json.load(handle)
#                         not_empty_c11 = []
#                         for c11 in content:
#                             if len(c11) >= 20:
#                                 not_empty_c11.append(c11)
#                         if len(not_empty_c11) != 0:
#                             cik_c11[i] += 1
#     print(cik_c11[i])

# len(cik_c11)
# count = 0

# for i in cik_c11:
#     if i >= 5:
#         count += 1

# count


#check how many nport file has non-empty c11
# for file_name in file_list:
#     if file_name != '.DS_Store':
#         file_name_temp1 = file_name.split('_')
#         file_name_temp2 = file_name_temp1[2].split('.')
#         file_num = file_name_temp1[1]
#         file_accno = file_name_temp2[0]
#         with open(path + file_name, 'r') as handle:
#             content = json.load(handle)
#         not_empty_c11 = []
#         for c11 in content:
#             if len(c11) >= 10:
#                 not_empty_c11.append(c11)


# #check derivative type for each c11, and count

# re_c11_type = re.compile(r'a\. Type of derivative instrument that most closely\n\t\t\t\trepresents the investment, selected from among the following\n\t\t\t\t\(forward, future, option, swaption, swap \(including but not limited\n\t\t\t\tto total return swaps, credit default swaps, and interest rate\n\t\t\t\tswaps\), warrant, other\)\.<\/td><td><div class="fakeBox2">\n\t\t\t(.*)\n\t\t\t<span>Â\xa0<\/span><\/div><\/td><\/tr><\/table><p xmlns:n1="http:\/\/www\.sec\.gov\/edgar\/common_drp" xmlns:ns2="http:\/\/www\.sec\.gov\/edgar\/statecodes" xmlns:ns3="http:\/\/www\.sec\.gov\/edgar\/regacommon">b\. Counterparty\.<br>')

# file_list.remove('.DS_Store')

# count_Forward = 0
# count_Future = 0
# count_Option = 0
# count_Swap = 0
# count_Swaption = 0 
# count_Warrant = 0
# count_Other = 0
# count_double = 0

# for file_name in file_list:
#     file_name_temp1 = file_name.split('_')
#     file_name_temp2 = file_name_temp1[2].split('.')
#     file_num = file_name_temp1[1]
#     file_accno = file_name_temp2[0]
#     with open(path + file_name, 'r') as handle:
#         content = json.load(handle)
#     not_empty_c11 = []
#     for c11 in content:
#         if len(c11) >= 20:
#             not_empty_c11.append(c11)
#     if not_empty_c11 != []:
#         for c11_item in not_empty_c11:
#             c11_type_temp = re_c11_type.findall(c11_item)
#             if len(c11_type_temp) == 1:
#                 if c11_type_temp[0] == 'Forward':
#                     count_Forward += 1
#                 elif c11_type_temp[0] == 'Future':
#                     count_Future += 1
#                 elif c11_type_temp[0] == 'Option':
#                     count_Option += 1
#                 elif c11_type_temp[0] == 'Swap':
#                     count_Swap += 1
#                 elif c11_type_temp[0] == 'Swaption':
#                     count_Swaption += 1
#                 elif c11_type_temp[0] == 'Warrant':
#                     count_Warrant += 1
#             elif len(c11_type_temp) == 2:
#                 count_double += 1
#             else:
#                 count_Other += 1

# count_Forward
# count_Future
# count_Option
# count_Swap
# count_Swaption
# count_Warrant
# count_Other
# count_double



                    