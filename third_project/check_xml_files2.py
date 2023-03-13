import json

from sepa import parser
import re
from glob import glob
import pandas as pd
import xmltodict


# Utility function to remove additional namespaces from the XML
def strip_namespace(xml):
    return re.sub(' xmlns="[^"]+"', '', xml, count=1)


# Read file
with open('_data_/CAMT053_A_accounts_20220701_20220930.xml', 'r') as f:
    input_data = f.read()

# Parse the bank statement XML to dictionary
camt_dict = parser.parse_string(parser.bank_to_customer_statement, bytes(strip_namespace(input_data), 'utf8'))
# print(camt_dict['group_header'])
statements = pd.DataFrame.from_dict(camt_dict['statements'])
# print(statements.columns)

temp_arr = []
for index, statement in statements.iterrows():
    data = statement.to_dict()
    # print(data)
    # temp_dict = {
    #     'id': data['id'],
    #     'electronic_sequence_number': data['electronic_sequence_number'],
    #     'creation_date_time': data['creation_date_time'],
    #     'account_id_iban': data['account']['id']['iban'],
    #     'currency': data['account']['currency'],
    #     'name': data['account']['name'],
    #     'balance': data['balance'],
    # }
    for balance in data['balance']:
        temp_dict = {
            "date": balance['date']['date'],
            "amount": balance['amount']['_value'],
            "currency": balance['amount']['currency'],
        }

        temp_arr.append(temp_dict)

new_df = pd.DataFrame(temp_arr)
new_df.to_excel("output.xlsx", index=False)

# print(statements.head())
# all_entries = []

# with open("dsfds.json", 'w') as s:
#     s.write(str(camt_dict))


# import xml.etree.ElementTree as ET
#
# tree = ET.parse('_data_/CAMT053_A_accounts_20220701_20220930.xml')
# xml_data = tree.getroot()
# # here you can change the encoding type to be able to set it to the one you need
# xmlstr = ET.tostring(xml_data, encoding='utf-8', method='xml')
# data_dict = dict(xmltodict.parse(xmlstr))
# with open("files_data.json", 'w') as s:
#     s.write(json.dumps(data_dict))
