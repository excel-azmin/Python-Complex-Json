import csv
import json
import ast
import re

data_list = []
data_arr = []
all_data = []

csvFilePath = r'20221226_062827.csv'
jsonFilePath = r'data.json'
pattern = re.compile("[A-Za-z]+")

with open(csvFilePath, encoding='utf-8') as csvf:
    csvReader = csv.DictReader(csvf)
    for rows in csvReader:
        create_date = ''
        modified_by = ''
        customer = ''
        previous_credit_limit = ''
        updated_credit_limit = ''
        modified_by = ''
        credit_limit = ''
        if rows['docname'] == 'ETLCUST-00833':

            data_arr.append(str(' {} '.format(rows["data"])))
            json_data = ast.literal_eval(json.dumps(data_arr))
            for res in range(len(json_data)):
                data_list.append(json.loads(json_data[res]))

            for d in range(1, len(data_list)):
                try:
                    if data_list[d]['row_changed']:
                        # print("\n\n "+customer+"\t"+str(data_list[d]['row_changed'][0][3][0][1])+"\n\n")
                        # print(data_list[d]['row_changed'][0][3][0][0])
                        if str(data_list[d]['row_changed'][0][3][0][0]) in "credit_limit":
                            # create_date = str(rows["Date"])
                            # modified_by = str(rows["modified_by"])
                            customer = str(rows["docname"])
                            credit_limit = str(rows["credit_limit"])
                            previous_credit_limit = data_list[d]["row_changed"][0][3][0][1]
                            updated_credit_limit = data_list[d]["row_changed"][0][3][0][2]
                except:
                    pass
        if previous_credit_limit and updated_credit_limit and not pattern.match(
                previous_credit_limit):
            # extend_credit_limit = updated_credit_limit - credit_limit
            row = {
                "create_date": create_date,
                "modified_by": modified_by,
                "customer": customer,
                "previous_credit_limit": previous_credit_limit,
                "updated_credit_limit": updated_credit_limit,
                "credit_limit": credit_limit,
                # "extend_credit_limit" : str(extend_credit_limit)
            }
            all_data.append(row)
print([i for n, i in enumerate(all_data) if i not in all_data[n + 1:]])
