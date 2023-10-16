
import csv


with open('BSC_1_1_annotated.csv', 'r', newline='') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        # Itera pelas linhas do arquivo CSV
        for linha in leitor_csv:
            timeConv  = (int(linha['timestamp']))
            timestamp = timeConv /10000
            timestampstr = str(timestamp)
            concTime = []
            for i in range(0, len(timestampstr),2):
                concTime = timestampstr[i:i+2]
                timeFinal = ":".join(concTime)
        print(timeFinal)
