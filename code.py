file = open('movielist.csv')

try:
    arquivo = file.readlines()
finally:
    file.close()


class Record:
    def __init__(self, ano):
        self.ano = ano
        self.quant_filmes = 0
        self.filme_vencedor = "" 


string1 = ''
base = [[],[],[],[],[]]
cont = 0
for linha in arquivo[1:]:
    for c in linha:
        string1 = string1 + str(c)
        if c == ';' or c == '\n':
            base[cont].append(string1[0:-1])
            string1 = ''
            cont += 1
            if cont == 5:
                cont = 0
    

anos = []
for ano in base[0]:
    if ano not in anos:
        record = Record(ano)
        x = 0
        while x < len(base[1]):
            if ano == base[0][x]:
                #print(f"Ano: {ano}\nFilme: {base[1][x]}")
                record.quant_filmes += 1
                if base[4][x]:
                    record.filme_vencedor = "Título: {}. Estúdio: {}. Produtor(es): {}".format(base[1][x], base[2][x], base[3][x]) 
            x += 1
        anos.append(ano)
        print(f"Ano: {record.ano}\nFilmes: {record.quant_filmes}\nVencedor:\n {record.filme_vencedor}\n")
        
