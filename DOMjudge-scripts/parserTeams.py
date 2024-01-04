import pandas as pd


excel_file = "Cama2023Inscriptions2.xlsx"
df = pd.read_excel(excel_file)

selected_columns = df[['Full Name', 'Email', 'What are you competing as?']]

file = open("teams.json", "w")
file.write("[")
currId = 500
seenEmails = []

for i in range(0, len(df)):
    row = df.iloc[i]
    found = False
    for email in seenEmails:
        if email == row['Email']:
            found = True
            break
    if found == True:
        continue
    file.write("{\n")
    file.write(f"\"id\": \"{currId}\",\n")
    group_id = 6
    if row['What are you competing as?'] == "International highschool student":
        group_id = 5
    if row['What are you competing as?'] == "Spain highschool student":
        group_id = 4
    file.write(f"\"group_ids\": \"{group_id}\",\n")
    file.write(f"\"name\": \"team{currId}\",\n")
    file.write(f"\"display_name\": \"{row['Full Name']}\"\n")
    if i + 1 == len(df):
        file.write("}\n")
    else:
        file.write("},\n")
    currId += 1
    seenEmails.append(row['Email'])

file.write("]")
file.close()
