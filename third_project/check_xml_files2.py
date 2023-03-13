from sepa import parser
import re
from glob import glob
import pandas as pd


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
    temp_dict = {
        'id': data['id'],
        'electronic_sequence_number': data['electronic_sequence_number'],
        'creation_date_time': data['creation_date_time'],
        'account_id_iban': data['account']['id']['iban'],
        'currency': data['account']['currency'],
        'name': data['account']['name'],
        # 'balance': data['balance'],
    }
    temp_arr.append(temp_dict)

new_df = pd.DataFrame(temp_arr)
new_df.to_excel("output.xlsx", index=False)
# print(statements.head())
# all_entries = []

# with open("dsfds.json", 'w') as s:
#     s.write(str(camt_dict))