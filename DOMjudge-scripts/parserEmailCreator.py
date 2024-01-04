import pandas as pd
import random
import string

excel_file = "Cama2023Inscriptions2.xlsx"
df = pd.read_excel(excel_file)

selected_columns = df[['Email']]

file = open("emails.json", "w")
file.write("[")

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
    file.write(f"\"to_email\": \"{row['Email']}\",\n")
    file.write(f"\"subject\": \"Last instructions for the CAMA contest\",\n")
    file.write(f"\"message\": \"Hello again!\\nJust a few hours until the start of the competition, we hope you are excited. We just want to remind you that the contest website is https://cama2023.cloudcontest.org/ and that, if you have any doubts, you can check our website: https://www.camacontest.online/, where there's also an available link to join our Discord server. If you don't have any problems logging into the DOMjudge server, you should ask your questions via the clarifications system. Otherwise, you can open a ticket in the Discord server or send an email.\\nWe also want to remind you to use fast I/O, as there are problems with big inputs and you could get TLE otherwise. For more information about fast I/O you can check: https://usaco.guide/general/fast-io .\\nMoreover, some problems will have more than one test case in each input file, so you will have to read the number of test cases and loop over them. If you have never seen a similar thing, you should try problem B from the practice contest, just to check that you know how to do it.\\nFinally, some information about the divisions. You are able to change between divisions in the DOMjudge server, so if you see that the one you chose is too hard or too easy for you, you can switch to the other division, but you will only be eligible for prizes in the division you selected when you registered. Additionally, you will be disqualified if you submit a problem first in the division you didn't select on the registration, and then you send it on the division you selected, because it will count as cheating. So, if you decide to change divisions, the change must be permanent. You can check in which division you currently are in the top right corner of the DOMjudge interface. \\nLast but not least, good luck!\\n\\nHola de nuevo!\\nYa solo quedan unas pocas horas hasta el inicio de la competicion, esperamos que estes emocionado. Solo queremos recordarte que el sitio web del concurso es https://cama2023.cloudcontest.org/ y que, si tienes alguna duda, puedes consultar nuestro sitio web: https://www.camacontest.online/, donde tambien hay un enlace disponible para unirte a nuestro servidor de Discord. Si no tienes problemas iniciando sesion en el servidor DOMjudge, debes hacer tus preguntas a traves del sistema de aclaraciones. De lo contrario, puedes abrir un ticket en el servidor de Discord o enviar un correo electronico.\\nTambien queremos recordarte que debes usar entrada y salida rapida, ya que hay problemas con entradas grandes y podrias recibir TLE de lo contrario. Para obtener mas informacion sobre entrada y salida rapida, puedes consultar: https://usaco.guide/general/fast-io.\\nAdemas, algunos problemas tendran mas de un caso de prueba en cada archivo de entrada, por lo que tendras que leer el numero de casos de prueba e iterar sobre ellos. Si nunca has visto algo similar, deberias intentar el problema B del concurso de practica, solo para comprobar que sabes hacerlo.\\nFinalmente, algo de informacion sobre las divisiones. Tendras la capacidad de cambiar entre divisiones en el servidor DOMjudge, por lo que si ves que la que elegiste es demasiado dificil o demasiado facil para ti, puedes cambiar a la otra division, pero solo seras elegible para premios en la division que seleccionaste al registrarte. Ademas, seras descalificado si envias un problema primero en la division que no seleccionaste en el registro, y luego lo envias en la division que seleccionaste, porque se considerara trampa. Entonces, si decides cambiar de divisiones, el cambio debe ser permanente. Puedes verificar la division en que te encuentras actualmente en la esquina superior derecha de la interfaz de DOMjudge. \\nPor ultimo, pero no menos importante, buena suerte!\"\n")
    if i + 1 == len(df):
        file.write("}\n")
    else:
        file.write("},\n")
    seenEmails.append(row['Email'])

file.write("]")
file.close()
