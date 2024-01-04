import pandas as pd
import random
import string

def generatePassword(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

excel_file = "Cama2023Inscriptions2.xlsx"
df = pd.read_excel(excel_file)

selected_columns = df[['Name', 'Email']]

file = open("accounts.json", "w")
file.write("[")

passwords = []
seenEmails = []
currId = 650

for i in range(0, len(df)):
    row = df.iloc[i]
    pswd = generatePassword(10)
    passwords.append(pswd)
    found = False
    for email in seenEmails:
        if email == row['Email']:
            found = True
            break
    if found == True:
        continue
    file.write("{\n")
    file.write(f"\"id\": \"{currId}\",\n")
    file.write(f"\"username\": \"user{currId}\",\n")
    file.write(f"\"password\": \"{pswd}\",\n")
    file.write(f"\"type\": \"team\",\n")
    file.write(f"\"team_id\": \"{currId-650+305}\"\n")
    if i + 1 == len(df):
        file.write("}\n")
    else:
        file.write("},\n")
    currId += 1
    seenEmails.append(row['Email'])

file.write("]")
file.close()

file = open("emails.json", "w")
file.write("[")

seenEmails = []
currId = 650

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
    file.write(f"\"to_email\": \"{row['Email']}\",\n")
    file.write(f"\"subject\": \"Credentials for the CAMA contest\",\n")
    file.write(f"\"message\": \"Hello!\\nHere are your credentials for the CAMA contest:\\nUser: user{currId}\\nPassword: {passwords[i]}\\nThe contest website is https://cama2023.cloudcontest.org/. Currently, there is a practice contest running so that you can test the environment. If you have any questions, you can ask via the clarifications system in DOMjudge, Discord or mail. \\n\\nHola!\\nAqui tienes tus credenciales para el concurso CAMA:\\nUsuario: user{currId}\\nContrasena: {passwords[i]}\\nEl sitio web del concurso es https://cama2023.cloudcontest.org/. Actualmente, hay un concurso de practica disponible para que puedas probar el entorno. Si tienes alguna pregunta, puedes preguntar a traves del sistema de clarificaciones de DOMjudge, por Discord o por mail.\\n\"\n")
    if i + 1 == len(df):
        file.write("}\n")
    else:
        file.write("},\n")
    currId += 1
    seenEmails.append(row['Email'])

file.write("]")
file.close()
