# import psycopg2
# import environ

# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )

# # def pull_from_azure():
# source_conn = psycopg2.connect(
#     host='35.244.10.172',
#     user='proxyuser',
#     password='8riFeagANcmCscDm',
#     dbname='niflr-machine-dev',
#     port='5432',
# )

# source_cursor = source_conn.cursor()

# # source_cursor.execute("SELECT niflr_edge_store_machinesessions.id FROM niflr_edge_store_machinesessions WHERE niflr_edge_store_machinesessions.created_at>= %s AND niflr_edge_store_machinesessions.created_at<= %s", (start_time,str(output_str)))
# source_cursor.execute('SELECT "scaleMachineId", "variantId", "refWeight", "threshold" FROM "Scales"')
# print('\nScales info : ------------>')
# rows = source_cursor.fetchall()
# # print(rows)

# for row in rows:
#     print(row)

# source_cursor.close()
# source_conn.close()

import pandas as pd
import requests

url = 'https://as-api.niflrpassdev.com/api/machines/E9584565-23E3-454E-A30A-1193B29F4E64' # Replace with the API endpoint URL

headers = {
    'x-access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijc2Y2E4ZDIzLTJjOTUtNDgyZC1hN2RjLWU0M2JkMDE2M2IwNCIsIm5hbWUiOiJLdXNoYWwiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE2NzkwNDM3OTEsImV4cCI6MTY3OTEzMDE5MX0.CbvhM2XodXSEiiesLYHWV6s8W_HGChpiqqivGAyvNL8'
}

response = requests.get(url, headers=headers)

if response.status_code == 200: # If the request was successful
    data = response.json() # Parse the response data as JSON
    # print(data) # Display the data
else:
    print('Request failed with status code:', response.status_code)


df = pd.DataFrame(data)

print("data:", data)
# Run a query on the data
# query_result = df.query('column1 > 5 and column2 == "foo"')

# Display the query result
# print(query_result)
# print(df['id'])
print("Machine IDs: ")
machine_ids = Machines.objects.values_list('machine_id', flat=True)
print(machine_ids)