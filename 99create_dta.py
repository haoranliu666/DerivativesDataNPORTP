import json
import numpy as np
import pandas as pd

#Forward

data = pd.DataFrame()

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'accno' + '.json', 'r') as handle:
    content = json.load(handle)

data['accno'] = content

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'name' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    temp.append(content[i][0])

data['name_of_counterparty'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'lei' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['lei_of_counterparty'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'amount_sold' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['amount_of_currency_sold'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'des_sold' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['description_of_currency_sold'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'amount_pur' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['amount_of_currency_purchased'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'des_pur' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['description_of_currency_purchased'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'date' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['settlement_date'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(8) + 'Forward' + '_' + 'unreal' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['unrealized_appreciation_or_depreciation'] = temp


data.to_stata('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/Forward.dta', version = 117)



#Future

data = pd.DataFrame()

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'accno' + '.json', 'r') as handle:
    content = json.load(handle)

data['accno'] = content

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'name' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['name_of_counterparty'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'lei' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['lei_of_counterparty'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'payoff' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['payoff_profile'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'name_issuer' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['name_of_issuer'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'title_issue' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['title_of_issue'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'cusip' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['cusip'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'isin' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['isin'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'ticker' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['ticker'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'exp_date' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['expiration_date'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'aggregate' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['contract_value'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'isocurrency' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['currency_code'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(10) + 'Future' + '_' + 'unreal' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['unrealized_appreciation_or_depreciation'] = temp

data.to_stata('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/Future.dta', version = 117)

#Option

data = pd.DataFrame()

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'accno' + '.json', 'r') as handle:
    content = json.load(handle)

data['accno'] = content


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'name' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['name_of_counterparty'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'lei' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['lei_of_counterparty'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'put_call' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['put_call'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'payoff' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['payoff_profile'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'name_issuer' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')


data['name_of_issuer'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'title_issue' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')


data['title_of_issue'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'cusip' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['cusip'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'isin' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['isin'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'ticker' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['ticker'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'exp_date' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['expiration_date'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'number_of_shares' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['number_of_shares'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'exe_price' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['exercise_price_or_rate'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'exe_currency' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['currency_code'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'delta' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['delta'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'unreal' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['unrealized_appreciation_or_depreciation'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'index_name' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['index_name'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'index_identifier' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['index_identifier'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(11) + 'Option' + '_' + 'index_narrative' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['index_narrative'] = temp

data.to_stata('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/Option.dta', version = 117)


#ticker cik
data = pd.DataFrame()

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/1ticker.json', 'r') as handle:
    ticker = json.load(handle)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/1cik.json', 'r') as handle:
    cik = json.load(handle)

ticker_temp = []
cik_temp = []

for i in range(0, len(ticker)):
    if len(cik[i]) == 0:
        ticker_temp.append(ticker[i])
        cik_temp.append('')
    else:
        for cik_id in cik[i]:
            ticker_temp.append(ticker[i])
            cik_temp.append(cik_id)

data['ticker'] = ticker_temp
data['cik'] = cik_temp

data.to_stata('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/ticker_cik.dta', version = 117)

#nport main

data = pd.DataFrame()

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'file_accno' + '.json', 'r') as handle:
    content = json.load(handle)

data['accno'] = content

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'ciknum' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['filer_cik'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'seriesid' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['seriesid'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'name' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['name_of_registrant'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'filenumber' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['investment_company_act_file_number'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'lei_reg' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['lei_of_registrant'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'street1' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['street_address_1'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'street2' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['street_address_2'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'state' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['state'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'country' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['country'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'zipcode' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['zipcode'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'telephone' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['telephone'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'nameofseries' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['name_of_series'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'lei_series' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['lei_of_series'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'date1' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['date_of_fiscal_year_end'] = temp


with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'date2' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['date_of_reported'] = temp

data.to_stata('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/Nport.dta', version = 117)

#nport class id

data = pd.DataFrame()

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'file_accno' + '.json', 'r') as handle:
    accno = json.load(handle)

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(5) + 'class_id' + '.json', 'r') as handle:
    class_id = json.load(handle)


accno_temp = []
class_id_temp = []

for i in range(0, len(accno)):
    if len(class_id[i]) == 0:
        accno_temp.append(accno[i])
        class_id_temp.append('')
    else:
        for class_id_i in class_id[i]:
            accno_temp.append(accno[i])
            class_id_temp.append(class_id_i)

data['accno'] = accno_temp
data['class_id'] = class_id_temp

data.to_stata('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/nport_classid.dta', version = 117)


#Swap
data = pd.DataFrame()

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'accno' + '.json', 'r') as handle:
    content = json.load(handle)

data['accno'] = content

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'name' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    temp.append(content[i][0])

data['name_of_counterparty'] = temp

with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'lei' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['lei_of_counterparty'] = temp

 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'index_name' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['index_name'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'index_identifier' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['index_identifier'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'index_narrative' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['index_narrative'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'non_index_name' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['non_index_name'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'non_index_title' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['non_index_title'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'non_index_cusip' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['non_index_cusip'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'non_index_isin' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['non_index_isin'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'receipts_type' + '_' + 'lei' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['receipts_type'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_type' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['payments_type'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_fixed_rate' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['receipts_fixed_rate'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_base_currency' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['receipts_base_currency'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_floating_rate_index' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['receipts_floating_rate_index'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_floating_rate_spread' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['receipts_floating_rate_spread'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_floating_rate_reset_dates' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['receipts_floating_rate_reset_dates'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_floating_rate_reset_dates_unit' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['receipts_floating_rate_reset_dates_unit'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_floating_rate_tenor' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['receipts_floating_rate_tenor'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_floating_rate_tenor_unit' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['receipts_floating_rate_tenor_unit'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_base_currency' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['receipts_base_currency'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_amount' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['receipts_amount'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'receipts_description_of_other' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['receipts_description_of_other'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_fixed_rate' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['payments_fixed_rate'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_floating_rate_index' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['payments_floating_rate_index'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_floating_rate_spread' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['payments_floating_rate_spread'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_floating_rate_reset_dates' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['payments_floating_rate_reset_dates'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_floating_rate_reset_dates_unit' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['payments_floating_rate_reset_dates_unit'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_floating_rate_tenor' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['payments_floating_rate_tenor'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_floating_rate_tenor_unit' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['payments_floating_rate_tenor_unit'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_base_currency' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['payments_base_currency'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_amount' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['payments_amount'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_termination_date' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['payments_termination_date'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'payments_description_of_other' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['payments_description_of_other'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'upfront_payments' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['upfront_payments'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'upfront_payments_iso' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['upfront_payments_iso'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'upfront_receipts' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['upfront_receipts'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'upfront_receipts_iso' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['upfront_receipts_iso'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'notional_amount' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['notional_amount'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'notional_amount_iso' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['notional_amount_iso'] = temp
 
with open('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/' + str(9) + 'Swap' + '_' + 'unrealized_appreciation' + '.json', 'r') as handle:
    content = json.load(handle)

temp = []
for i in range(0, len(content)):
    if len(content[i]) >= 1:
        temp.append(content[i][0])
    else:
        temp.append('')

data['unrealized_appreciation'] = temp

data.to_stata('/Users/haoranliu/香港中文大学/XintongZhan/Linjia_MutualFundDeriData/Swap.dta', version = 117)
