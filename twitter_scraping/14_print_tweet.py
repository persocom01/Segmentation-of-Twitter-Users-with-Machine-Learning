import pandas as pd
import sys
import io
import json
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

save_folder = 'data'
filename = '#cancelnetflix'

# import_path = r'.\data\#michellewilliams.csv'
# data = pd.read_csv(import_path, low_memory=False)
# print(data.shape)
# print(data.columns)
# print(data['user.id_str'][223])

import_path = r'.\data\#cancelnetflix.json'
with open(import_path, 'r') as f:
    dic = json.load(f)
print(len(dic))

df = pd.io.json.json_normalize(dic)  # Flattens the json file.
export_path = f'.\\{save_folder}\\{filename}.csv'
df.to_csv(export_path, index=None)


# data = data.rename(columns={'text': 'full_text'})
# df = pd.DataFrame(data[(data['lang'] == 'en') | (data['lang'] == 'und')])
# print(df.shape)

# import_path = r'.\data\#michellewilliams2.csv'
# data2 = pd.read_csv(import_path, low_memory=False)
# df2 = pd.DataFrame(data2)
# print(df2.shape)
# last_row = df2.shape[0] - 1
# print(df2['id_str'][last_row])
# df2 = df2.drop([last_row])
#
# df3 = df2.append(df, sort=False)
# print(df3.shape)
# export_path = r'.\data\#michellewilliams3.csv'
# df3.to_csv(export_path, index=False)


# df['created_at'] = pd.to_datetime(df['created_at'])
# print(df.dtypes)
# print(df['created_at'][0])
# print(df['created_at'][0].replace(tzinfo=None) > datetime.datetime(2019, 12, 19))
# i_drop = []
# for row in df[['created_at']].iteritems():
#     print(row)
#     if row.replace(tzinfo=None) < datetime.datetime(2019, 12, 19):
#         i_drop.append = row.index
# print(i_drop)
# df = pd.DataFrame(data[data['created_at'].map(replace(tzinfo=None))
#                        > datetime.datetime(2019, 12, 19)])
# print(df.shape)
# # print(df['id_str'])
# export_path = r'.\data\replies_to_jk_1207646162813100033.csv'
# df.to_csv(export_path, index=False)

# Number of rows should be excel_row -1

#
#

#
#
# df3 = df2.append(df, sort=False)
# print(df3.shape)
# export_path = r'.\data\#michellewilliams3.csv'
# df3.to_csv(export_path, index=False)