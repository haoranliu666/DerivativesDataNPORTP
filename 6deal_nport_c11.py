import re
import json
import os
import sys

n = sys.argv[1]
n = int(n)

#
path = '/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/nport_file/file/'

file_list = os.listdir(path)

re_c11 = re.compile(r'Item C\.11\. For derivatives, also provide:([\s\S]*?)Item C\.12\. Securities lending\.')

count = 0
for file_name in file_list:
    file_name_temp1 = file_name.split('_')
    file_name_temp2 = file_name_temp1[1].split('.')
    file_num = file_name_temp1[0]
    file_accno = file_name_temp2[0]
    if (int(file_num) >= n) & (int(file_num) < n + 4000):
        count += 1
        print(count)
        print(file_name)
        with open(path + file_name, 'r', encoding = 'ISO-8859-1') as f:
            content = f.read()
        with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(6) + 'c11_' + str(file_num) + '_' + str(file_accno) + '.json', 'w') as handle:
            json.dump(re_c11.findall(content), handle, indent=2)

