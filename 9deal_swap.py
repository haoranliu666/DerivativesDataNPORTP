import re
import json
import os

path = '/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/c11/'
file_list = os.listdir(path)


#deal Swap

re_c11_type = re.compile(r'a\. Type of derivative instrument that most closely\n\t\t\t\trepresents the investment, selected from among the following\n\t\t\t\t\(forward, future, option, swaption, swap \(including but not limited\n\t\t\t\tto total return swaps, credit default swaps, and interest rate\n\t\t\t\tswaps\), warrant, other\)\.<\/td><td><div class="fakeBox2">\n\t\t\t(.*)\n\t\t\t<span>Â\xa0<\/span><\/div><\/td><\/tr><\/table><p xmlns:n1="http:\/\/www\.sec\.gov\/edgar\/common_drp" xmlns:ns2="http:\/\/www\.sec\.gov\/edgar\/statecodes" xmlns:ns3="http:\/\/www\.sec\.gov\/edgar\/regacommon">b\. Counterparty\.<br>')

file_list.remove('.DS_Store')

accno = []
name = []
lei = []
index_name = []
index_identifier = []
index_narrative = []
non_index_name = []
non_index_title = []
non_index_cusip = []
non_index_isin = []
# non_index_ticker = []
receipts_type = []
payments_type = []
receipts_fixed_rate = []
receipts_base_currency = []
receipts_floating_rate_index = []
receipts_floating_rate_spread = []
receipts_floating_rate_reset_dates = []
receipts_floating_rate_reset_dates_unit = []
receipts_floating_rate_tenor = []
receipts_floating_rate_tenor_unit = []
receipts_base_currency = []
receipts_amount = []
receipts_description_of_other = []
payments_fixed_rate = []
payments_floating_rate_index = []
payments_floating_rate_spread = []
payments_floating_rate_reset_dates = []
payments_floating_rate_reset_dates_unit = []
payments_floating_rate_tenor = []
payments_floating_rate_tenor_unit = []
payments_base_currency = []
payments_amount = []
payments_termination_date = []
payments_description_of_other = []
upfront_payments = []
upfront_payments_iso = []
upfront_receipts = []
upfront_receipts_iso = []
notional_amount = []
notional_amount_iso = []
unrealized_appreciation = []


re_name = re.compile(r'Name of counterparty\.<\/td><td><div class="fakeBox">(.*?)<span>Â\xa0<\/span><\/div><\/td><\/tr><tr><td class="label">LEI \(if any\) of counterparty\.')
re_lei = re.compile(r'LEI \(if any\) of counterparty\.<\/td><td><div class="fakeBox2">(.*?)<span>Â\xa0<\/span><\/div><\/td><\/tr><\/table><p xmlns:n1="http:\/\/www\.sec\.gov\/edgar\/common_drp" xmlns:ns2="http:\/\/www\.sec\.gov\/edgar\/statecodes" xmlns:ns3="http:\/\/www\.sec\.gov\/edgar\/regacommon">\n\t\t\t3\.\tIf the reference instrument is')
re_index_name = re.compile(r'Index name\.\n\t\t\t\t</td><td><div class="fakeBox">(.*?)<span>Â\xa0')
re_index_identifier = re.compile(r'Index identifier, if any\.\n\t\t\t\t</td><td><div class="fakeBox">(.*?)<span>Â\xa0')
re_index_narrative = re.compile(r'Narrative description\.\n\t\t\t\t</td><td><div class="fakeBox">(.*?)<span>Â\xa0')
re_non_index_name = re.compile(r'Name of issuer\.\n\t\t\t\t<\/td><td><div class="fakeBox">(.*?)<span>Â\xa0')
re_non_index_title = re.compile(r'Title of issue\.\n\t\t\t\t<\/td><td><div class="fakeBox">(.*?)<span>Â\xa0')
re_non_index_cusip = re.compile(r'CUSIP\.<\/span><\/td><td><div class="fakeBox3">(.*?)<span>Â\xa0')
re_non_index_isin = re.compile(r'ISIN \(if CUSIP is not available\)\.<\/span><\/td><td><div class="fakeBox3">(.*?)<span>Â\xa0')
# re_non_index_ticker = re.compile(r'Ticker \(if CUSIP and ISIN are not available\)\.<\/span><\/td><td><div class="fakeBox3">(.*?)<span>Â\xa0')
re_receipts_type_temp = re.compile(r'Receipts: fixed, floating or other([\w\W]*?)\tOther')
re_payments_type_temp = re.compile(r'Payments: fixed, floating or other([\w\W]*?)\tOther')
re_receipts_fixed_rate = re.compile(r'Receipts: Fixed rate\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_receipts_floating_rate_index = re.compile(r'Receipts: Floating rate Index\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_receipts_floating_rate_spread = re.compile(r'Receipts: Floating rate Spread\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_receipts_floating_rate_reset_dates = re.compile(r'Receipt: Floating Rate Reset Dates\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_receipts_floating_rate_reset_dates_unit = re.compile(r'Receipt: Floating Rate Reset Dates Unit\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_receipts_floating_rate_tenor = re.compile(r'Receipts: Floating Rate Tenor\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_receipts_floating_rate_tenor_unit = re.compile(r'Receipts: Floating Rate Tenor Unit\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_receipts_base_currency = re.compile(r'Receipts: Base currency\.\n\t\t\t<\/td><td><div class="fakeBox4">\n\t\t\t\t(.*?)\n\t\t\t<span>Â\xa0')
re_receipts_amount = re.compile(r'Receipts: Amount\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_receipts_description_of_other = re.compile(r'Description of Other Receipts\n\t\t\t<\/td><td><div class="fakeBox3">(.*)<span>Â\xa0')
re_payments_fixed_rate = re.compile(r'Payments: Fixed rate\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_payments_floating_rate_index = re.compile(r'Payments: Floating rate Index\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_payments_floating_rate_spread = re.compile(r'Payments: Floating rate Spread\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_payments_floating_rate_reset_dates = re.compile(r'Payment: Floating Rate Reset Dates\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_payments_floating_rate_reset_dates_unit = re.compile(r'Payment: Floating Rate Reset Dates Unit\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_payments_floating_rate_tenor = re.compile(r'Payment: Floating Rate Tenor\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_payments_floating_rate_tenor_unit = re.compile(r'Payment: Floating Rate Tenor Unit\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_payments_base_currency = re.compile(r'Payments: Base currency\n\t\t\t<\/td><td><div class="fakeBox4">\n\t\t\t\t(.*?)\n\t\t\t<span>Â\xa0')
re_payments_amount = re.compile(r'Payments: Amount\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_payments_termination_date = re.compile(r'Termination or maturity date\.\n\t\t\t</td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_payments_description_of_other = re.compile(r'Description of Other Payments\n\t\t\t<\/td><td><div class="fakeBox3">(.*)<span>Â\xa0')
re_upfront_payments_temp = re.compile(r'(Upfront payments[\w\W]*?)Upfront receipts')
re_upfront_payments = re.compile(r'Upfront payments\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_upfront_payments_iso = re.compile(r'ISO Currency Code\.\n\t\t\t<\/td><td><div class="fakeBox4">\n\t\t\t\t(.*?)\n\t\t\t<span>Â\xa0')
re_upfront_receipts_temp = re.compile(r'(Upfront receipts[\w\W]*?)Notional amount')
re_upfront_receipts = re.compile(r'Upfront receipts\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_upfront_receipts_iso = re.compile(r'ISO Currency Code\.\n\t\t\t<\/td><td><div class="fakeBox4">\n\t\t\t\t(.*?)\n\t\t\t<span>Â\xa0')
re_notional_amount_temp = re.compile(r'(Notional amount[\w\W]*?)Unrealized appreciation or depreciation')
re_notional_amount = re.compile(r'Notional amount\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_notional_amount_iso = re.compile(r'ISO Currency Code\.\n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')
re_unrealized_appreciation = re.compile(r'Unrealized appreciation or depreciation\. Depreciation shall be reported as a negative number\. \n\t\t\t<\/td><td><div class="fakeBox4">(.*?)<span>Â\xa0')


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
                if c11_type_temp[0] == 'Swap':
                    accno.append(file_accno)
                    name.append(re_name.findall(c11_item))
                    lei.append(re_lei.findall(c11_item))
                    index_name.append(re_index_name.findall(c11_item))
                    index_identifier.append(re_index_identifier.findall(c11_item))
                    index_narrative.append(re_index_narrative.findall(c11_item))
                    non_index_name.append(re_non_index_name.findall(c11_item))
                    non_index_title.append(re_non_index_title.findall(c11_item))
                    non_index_cusip.append(re_non_index_cusip.findall(c11_item))
                    non_index_isin.append(re_non_index_isin.findall(c11_item))
                    receipts_type_temp = re_receipts_type_temp.findall(c11_item)
                    if len(receipts_type_temp) != 1:
                        receipts_type.append('')
                    elif 'Fixed is checked' in receipts_type_temp[0]:
                        receipts_type.append('fixed')
                    elif 'Floating is checked' in receipts_type_temp[0]:
                        receipts_type.append('floating')
                    elif 'Other is checked' in receipts_type_temp[0]:
                        receipts_type.append('other')
                    else:
                        receipts_type.append('')
                    payments_type_temp = re_payments_type_temp.findall(c11_item)
                    if len(payments_type_temp) != 1:
                        payments_type.append('')
                    elif 'Fixed is checked' in payments_type_temp[0]:
                        payments_type.append('fixed')
                    elif 'Floating is checked' in payments_type_temp[0]:
                        payments_type.append('floating')
                    elif 'Other is checked' in payments_type_temp[0]:
                        payments_type.append('other')
                    else:
                        payments_type.append('')
                    receipts_fixed_rate.append(re_receipts_fixed_rate.findall(c11_item))
                    receipts_floating_rate_index.append(re_receipts_floating_rate_index.findall(c11_item))
                    receipts_floating_rate_spread.append(re_receipts_floating_rate_spread.findall(c11_item))
                    receipts_floating_rate_reset_dates.append(re_receipts_floating_rate_reset_dates.findall(c11_item))
                    receipts_floating_rate_reset_dates_unit.append(re_receipts_floating_rate_reset_dates_unit.findall(c11_item))
                    receipts_floating_rate_tenor.append(re_receipts_floating_rate_tenor.findall(c11_item))
                    receipts_floating_rate_tenor_unit.append(re_receipts_floating_rate_tenor_unit.findall(c11_item))
                    receipts_base_currency.append(re_receipts_base_currency.findall(c11_item))
                    receipts_amount.append(re_receipts_amount.findall(c11_item))
                    receipts_description_of_other.append(re_receipts_description_of_other.findall(c11_item))
                    payments_fixed_rate.append(re_payments_fixed_rate.findall(c11_item))
                    payments_floating_rate_index.append(re_payments_floating_rate_index.findall(c11_item))
                    payments_floating_rate_spread.append(re_payments_floating_rate_spread.findall(c11_item))
                    payments_floating_rate_reset_dates.append(re_payments_floating_rate_reset_dates.findall(c11_item))
                    payments_floating_rate_reset_dates_unit.append(re_payments_floating_rate_reset_dates_unit.findall(c11_item))
                    payments_floating_rate_tenor.append(re_payments_floating_rate_tenor.findall(c11_item))
                    payments_floating_rate_tenor_unit.append(re_payments_floating_rate_tenor_unit.findall(c11_item))
                    payments_base_currency.append(re_payments_base_currency.findall(c11_item))
                    payments_amount.append(re_payments_amount.findall(c11_item))
                    payments_termination_date.append(re_payments_termination_date.findall(c11_item))
                    payments_description_of_other.append(re_payments_description_of_other.findall(c11_item))
                    unrealized_appreciation.append(re_unrealized_appreciation.findall(c11_item))
                    upfront_payments_temp = re_upfront_payments_temp.findall(c11_item)
                    upfront_receipts_temp = re_upfront_receipts_temp.findall(c11_item)
                    notional_amount_temp = re_notional_amount_temp.findall(c11_item)
                    if len(upfront_payments_temp) != 0:
                        upfront_payments.append(re_upfront_payments.findall(upfront_payments_temp[0]))
                        upfront_payments_iso.append(re_upfront_payments_iso.findall(upfront_payments_temp[0]))
                    else:
                        upfront_payments.append('')
                        upfront_payments_iso.append('')
                    if len(upfront_receipts_temp) != 0:
                        upfront_receipts.append(re_upfront_receipts.findall(upfront_receipts_temp[0]))
                        upfront_receipts_iso.append(re_upfront_receipts_iso.findall(upfront_receipts_temp[0]))
                    else:
                        upfront_receipts.append('')
                        upfront_receipts_iso.append('')
                    if len(notional_amount_temp) != 0:
                        notional_amount.append(re_notional_amount.findall(notional_amount_temp[0]))
                        notional_amount_iso.append(re_notional_amount_iso.findall(notional_amount_temp[0]))
                    else:
                        notional_amount.append('')
                        notional_amount_iso.append('')
                    


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'accno' + '.json', 'w') as handle:
    json.dump(accno, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'name' + '.json', 'w') as handle:
    json.dump(name, handle, indent=2)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'lei' + '.json', 'w') as handle:
    json.dump(lei, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'index_name' + '.json', 'w') as handle:
    json.dump(index_name, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'index_identifier' + '.json', 'w') as handle:
    json.dump(index_identifier, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'index_narrative' + '.json', 'w') as handle:
    json.dump(index_narrative, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'non_index_name' + '.json', 'w') as handle:
    json.dump(non_index_name, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'non_index_title' + '.json', 'w') as handle:
    json.dump(non_index_title, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'non_index_cusip' + '.json', 'w') as handle:
    json.dump(non_index_cusip, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'non_index_isin' + '.json', 'w') as handle:
    json.dump(non_index_isin, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_type' + '.json', 'w') as handle:
    json.dump(receipts_type, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_type' + '.json', 'w') as handle:
    json.dump(payments_type, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_fixed_rate' + '.json', 'w') as handle:
    json.dump(receipts_fixed_rate, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_base_currency' + '.json', 'w') as handle:
    json.dump(receipts_base_currency, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_floating_rate_index' + '.json', 'w') as handle:
    json.dump(receipts_floating_rate_index, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_floating_rate_spread' + '.json', 'w') as handle:
    json.dump(receipts_floating_rate_spread, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_floating_rate_reset_dates' + '.json', 'w') as handle:
    json.dump(receipts_floating_rate_reset_dates, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_floating_rate_reset_dates_unit' + '.json', 'w') as handle:
    json.dump(receipts_floating_rate_reset_dates_unit, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_floating_rate_tenor' + '.json', 'w') as handle:
    json.dump(receipts_floating_rate_tenor, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_floating_rate_tenor_unit' + '.json', 'w') as handle:
    json.dump(receipts_floating_rate_tenor_unit, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_base_currency' + '.json', 'w') as handle:
    json.dump(receipts_base_currency, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_amount' + '.json', 'w') as handle:
    json.dump(receipts_amount, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_description_of_other' + '.json', 'w') as handle:
    json.dump(receipts_description_of_other, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_fixed_rate' + '.json', 'w') as handle:
    json.dump(payments_fixed_rate, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_floating_rate_index' + '.json', 'w') as handle:
    json.dump(payments_floating_rate_index, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_floating_rate_spread' + '.json', 'w') as handle:
    json.dump(payments_floating_rate_spread, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_floating_rate_reset_dates' + '.json', 'w') as handle:
    json.dump(payments_floating_rate_reset_dates, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_floating_rate_reset_dates_unit' + '.json', 'w') as handle:
    json.dump(payments_floating_rate_reset_dates_unit, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_floating_rate_tenor' + '.json', 'w') as handle:
    json.dump(payments_floating_rate_tenor, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_floating_rate_tenor_unit' + '.json', 'w') as handle:
    json.dump(payments_floating_rate_tenor_unit, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_base_currency' + '.json', 'w') as handle:
    json.dump(payments_base_currency, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_amount' + '.json', 'w') as handle:
    json.dump(payments_amount, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_termination_date' + '.json', 'w') as handle:
    json.dump(payments_termination_date, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_description_of_other' + '.json', 'w') as handle:
    json.dump(payments_description_of_other, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'upfront_payments' + '.json', 'w') as handle:
    json.dump(upfront_payments, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'upfront_payments_iso' + '.json', 'w') as handle:
    json.dump(upfront_payments_iso, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'upfront_receipts' + '.json', 'w') as handle:
    json.dump(upfront_receipts, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'upfront_receipts_iso' + '.json', 'w') as handle:
    json.dump(upfront_receipts_iso, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'notional_amount' + '.json', 'w') as handle:
    json.dump(notional_amount, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'notional_amount_iso' + '.json', 'w') as handle:
    json.dump(notional_amount_iso, handle, indent=2)


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'unrealized_appreciation' + '.json', 'w') as handle:
    json.dump(unrealized_appreciation, handle, indent=2)
