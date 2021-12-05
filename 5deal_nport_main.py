import re
import json
import os

#
path = '/Volumes/My Passport/file/'

file_list = os.listdir(path)

file_num = []
file_accno = []
class_id = []
name = []
filenumber = []
ciknum = []
lei_reg = []
street1 = []
street2 = []
state = []
country = []
zipcode = []
telephone = []
nameofseries = []
seriesid = []
lei_series = []
date1 = []
date2 = []



re_class_id = re.compile(r'Class \(Contract\) ID<\/td><td><div class="fakeBox2">(C\d*)<span>')
re_name = re.compile(r'Name of Registrant\n\t\t\t\t<\/td><td><div class="fakeBox">(.*)<span> <\/span><\/div><\/td><\/tr><tr><td class="label">b\. Investment Company Act file number for Registrant')
re_filenumber = re.compile(r'<\/td><td><div class="fakeBox2">(.*)<span> <\/span><\/div><\/td><\/tr><tr><td class="label">c\. CIK number of Registrant')
re_ciknum = re.compile(r'<\/td><td><div class="fakeBox2">(.*)<span> <\/span><\/div><\/td><\/tr><tr><td class="label">d\. LEI of Registrant')
re_lei_reg = re.compile(r'<\/td><td><div class="fakeBox2">(.*)<span> <\/span><\/div><\/td><\/tr><\/table><br xmlns:n1="http:\/\/www\.sec\.gov\/edgar\/common_drp"')
re_street1 = re.compile(r'<\/td><td><div class="fakeBox">(.*)<span> <\/span><\/div><\/td><\/tr><tr><td class="label">Street Address 2')
re_street2 = re.compile(r'<\/td><td><div class="fakeBox">(.*)<span> <\/span><\/div><\/td><\/tr><tr><td class="label">City')
re_state = re.compile(r'<\/span><\/div><\/td><\/tr><tr><td class="label">State, if applicable<\/td><td><div class="fakeBox2">\n\t\t\t\t(.*)\n\t\t\t<span> <\/span><\/div><\/td><\/tr><tr><td class="label">Foreign country, if applicable<\/td><td><div class="fakeBox4">')
re_country = re.compile(r'<span> <\/span><\/div><\/td><\/tr><tr><td class="label">Foreign country, if applicable<\/td><td><div class="fakeBox4">\n\t\t\t\t(.*)\n\t\t\t<span> <\/span><\/div><\/td><\/tr><tr><td class="label">Zip \/ Postal Code')
re_zipcode = re.compile(r'<\/td><td><div class="fakeBox2">(.*)<span> <\/span><\/div><\/td><\/tr><tr><td class="label">Telephone number')
re_telephone = re.compile(r'<\/td><td><div class="fakeBox2">(.*)<span> <\/span><\/div><\/td><\/tr><\/table><h4 xmlns:n1="http:\/\/www\.sec\.gov\/edgar\/common_drp" xmlns:ns2="http:\/\/www\.sec\.gov\/edgar\/statecodes" xmlns:ns3="http:\/\/www\.sec\.gov\/edgar\/regacommon" xmlns:n4="http:\/\/www\.sec\.gov\/edgar\/nportcommon">Item A\.2\. Information about the Series\.<\/h4><table xmlns:n1="http:\/\/www\.sec\.gov\/edgar\/common_drp" xmlns:ns2="http:\/\/www\.sec\.gov\/edgar\/statecodes" xmlns:ns3="http:\/\/www\.sec\.gov\/edgar\/regacommon" xmlns:n4="http:\/\/www\.sec\.gov\/edgar\/nportcommon"><tr><td class="label">a\. Name of Series\.')
re_nameofseries = re.compile(r'<\/td><td><div class="fakeBox">(.*)<span> <\/span><\/div><\/td><\/tr><tr><td class="label">b\. EDGAR series identifier \(if any\)\.')
re_seriesid = re.compile(r'<\/td><td><div class="fakeBox2">(.*)<span> <\/span><\/div><\/td><\/tr><tr><td class="label">c\. LEI of Series\.')
re_lei_series = re.compile(r'<\/td><td><div class="fakeBox2">(.*)<span> <\/span><\/div><\/td><\/tr><\/table><h4 xmlns:n1="http:\/\/www\.sec\.gov\/edgar\/common_drp" xmlns:ns2="http:\/\/www\.sec\.gov\/edgar\/statecodes" xmlns:ns3="http:\/\/www\.sec\.gov\/edgar\/regacommon" xmlns:n4="http:\/\/www\.sec\.gov\/edgar\/nportcommon">Item A\.3\. Reporting period\.<\/h4><table xmlns:n1="http:\/\/www\.sec\.gov\/edgar\/common_drp" xmlns:ns2="http:\/\/www\.sec\.gov\/edgar\/statecodes" xmlns:ns3="http:\/\/www\.sec\.gov\/edgar\/regacommon" xmlns:n4="http:\/\/www\.sec\.gov\/edgar\/nportcommon"><tr><td class="label">a\. Date of fiscal year-end\.')
re_date1 = re.compile(r'<\/td><td><div class="fakeBox2">(.*)<span> <\/span><\/div><\/td><\/tr><tr><td class="label">b\. Date as of which information is reported\. ')
re_date2 = re.compile(r'<\/td><td><div class="fakeBox2">(.*)<span> <\/span><\/div><\/td><\/tr><\/table><h4 xmlns:n1="http:\/\/www\.sec\.gov\/edgar\/common_drp" xmlns:ns2="http:\/\/www\.sec\.gov\/edgar\/statecodes" xmlns:ns3="http:\/\/www\.sec\.gov\/edgar\/regacommon" xmlns:n4="http:\/\/www\.sec\.gov\/edgar\/nportcommon">Item A\.4\. Final filing<\/h4><table xmlns:n1="http:\/\/www\.sec\.gov\/edgar\/common_drp" xmlns:ns2="http:\/\/www\.sec\.gov\/edgar\/statecodes" xmlns:ns3="http:\/\/www\.sec\.gov\/edgar\/regacommon" xmlns:n4="http:\/\/www\.sec\.gov\/edgar\/nportcommon"><tr><td class="label">Does the Fund anticipate that this will be its final filing on Form N PORT\?<\/td><td><span class="yesNo"><img src="\/Images\/radio-unchecked\.jpg" alt="Yes is not checked">')

count = 0

for file_name in file_list:
    if file_name != '.DS_Store':
        count += 1
        print(count)
        file_name_temp1 = file_name.split('_')
        file_name_temp2 = file_name_temp1[1].split('.')
        file_num.append(file_name_temp1[0])
        file_accno.append(file_name_temp2[0])
        with open(path + file_name, 'r') as f:
            content = f.read()
        class_id.append(re_class_id.findall(content))
        name.append(re_name.findall(content))
        filenumber.append(re_filenumber.findall(content))
        ciknum.append(re_ciknum.findall(content))
        lei_reg.append(re_lei_reg.findall(content))
        street1.append(re_street1.findall(content))
        street2.append(re_street2.findall(content))
        state.append(re_state.findall(content))
        country.append(re_country.findall(content))
        zipcode.append(re_zipcode.findall(content))
        telephone.append(re_telephone.findall(content))
        nameofseries.append(re_nameofseries.findall(content))
        seriesid.append(re_seriesid.findall(content))
        lei_series.append(re_lei_series.findall(content))
        date1.append(re_date1.findall(content))
        date2.append(re_date2.findall(content))
        

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'file_num' + '.json', 'w') as handle:
    json.dump(file_num, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'file_accno' + '.json', 'w') as handle:
    json.dump(file_accno, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'class_id' + '.json', 'w') as handle:
    json.dump(class_id, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'name' + '.json', 'w') as handle:
    json.dump(name, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'filenumber' + '.json', 'w') as handle:
    json.dump(filenumber, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'ciknum' + '.json', 'w') as handle:
    json.dump(ciknum, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'lei_reg' + '.json', 'w') as handle:
    json.dump(lei_reg, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'street1' + '.json', 'w') as handle:
    json.dump(street1, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'street2' + '.json', 'w') as handle:
    json.dump(street2, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'state' + '.json', 'w') as handle:
    json.dump(state, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'country' + '.json', 'w') as handle:
    json.dump(country, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'zipcode' + '.json', 'w') as handle:
    json.dump(zipcode, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'telephone' + '.json', 'w') as handle:
    json.dump(telephone, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'nameofseries' + '.json', 'w') as handle:
    json.dump(nameofseries, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'seriesid' + '.json', 'w') as handle:
    json.dump(seriesid, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'lei_series' + '.json', 'w') as handle:
    json.dump(lei_series, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'date1' + '.json', 'w') as handle:
    json.dump(date1, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'date2' + '.json', 'w') as handle:
    json.dump(date2, handle, indent=2)

