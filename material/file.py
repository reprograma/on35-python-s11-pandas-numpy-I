import os
import pandas as pd

def get_years():
    years = []
    for year in [x[0] for x in os.walk("clima\\bruto")]:
        if(year.replace("clima\\bruto",'') != ''):
            years.append(int(year.replace("clima\\bruto\\",'')))
    return years

def adjusts_all_files():
    for year in get_years():
        adjusts_files(year)    

def adjusts_files(year):
    for file in os.listdir("clima\\bruto\\" + str(year)):

        with open('clima\\bruto\\'+ str(year) +'\\' + file) as f:
            lines = f.readlines()
            f.close()

        if not os.path.isdir('clima\\tratado\\' + str(year)) :
            os.mkdir('clima\\tratado\\' + str(year)) 

        with open('clima\\tratado\\' + str(year) +'\\' + file, "w") as f:
            for i in range(8, len(lines)):
                f.write(lines[i])
            f.close()

def file_head():

    year = get_years()[0]

    file = os.listdir("clima\\bruto\\" + str(year))[0]
    arquivo = open('clima\\bruto\\' + str(year) + '\\' + file,'r')

    cabecalho = []

    for i in range(8):
        line = arquivo.readline()
        cabecalho.append(line.split(';')[0].replace(':',''))

    return cabecalho

def files_range_info(year_ini, year_fim, uf):
    arquivos = []

    for year in range(year_ini, year_fim):
        arquivos += files_info(year, uf)

    return arquivos

def files_uf_info(uf):
    arquivos = []

    for year in get_years():
        arquivos += files_info(year,uf)

    return arquivos

def files_all_info():
    arquivos = []

    for year in get_years():
        arquivos += files_info(year,'')

    return arquivos

def files_info(year, uf):
    arquivos = []

    for file in os.listdir("clima\\bruto\\" + str(year)):

        arquivo = open('clima\\bruto\\' + str(year) + '\\' + file,'r')
        dados_arquivo = {}

        cabecalho = []

        for i in range(8):
            line = arquivo.readline()
            cabecalho.append(line.split(';')[0].replace(':',''))
            dados_arquivo[line.split(';')[0].replace(':','')] = line.split(';')[1].replace('\n','')

        arquivo.close()

        dados_arquivo['file'] = file

        dados_arquivo['year'] = year

        if((dados_arquivo['UF'] == uf) | (uf == '')):
            arquivos.append(dados_arquivo)

    return arquivos

def sample(year_ini, year_fim,uf):

    cabecalho = file_head()

    print(cabecalho)

    if year_ini != year_fim:
        arquivos = files_range_info(year_ini,year_fim,uf)
    else:
        arquivos = files_info(year_ini,uf)

    dados = []

    for info_data in arquivos:

        dt = pd.read_csv('clima\\tratado\\' + str(info_data['year']) + '\\' + info_data['file'], sep=';' , encoding='latin-1')

        dt.drop('Unnamed: 19', axis=1, inplace=True)

        for c in cabecalho:
            dt[c] = info_data[c]

        dados.append(dt)

    dt_all = pd.concat(dados)

    dt_all = dt_all.sample(100000)

    dt_all.to_csv('clima\\data_sample_' + uf + '.csv', index=False, sep=';')

    with open('clima\\data_sample_' + uf + '.csv', 'r', encoding="utf8") as f:
        lines = f.readlines()
        f.close()

    with open('clima\\data_sample_' + uf + '.csv', "w", encoding="utf8") as f:
        f.write('Data;Hora UTC;PRECIPITAO TOTAL. HORARIO (mm);PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO. HORARIA (mB);PRESSAO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB);PRESSAO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB);RADIACAO GLOBAL (Kj/m2);TEMPERATURA DO AR - BULBO SECO. HORARIA (C);TEMPERATURA DO PONTO DE ORVALHO (C);TEMPERATURA MAXIMA NA HORA ANT. (AUT) (C);TEMPERATURA MINIMA NA HORA ANT. (AUT) (C);TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (C);TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (C);UMIDADE REL. MAX. NA HORA ANT. (AUT) (%);UMIDADE REL. MIN. NA HORA ANT. (AUT) (%);UMIDADE RELATIVA DO AR. HORARIA (%);VENTO. DIREAO HORARIA (gr) ((gr));VENTO. RAJADA MAXIMA (m/s);VENTO. VELOCIDADE HORARIA (m/s);REGIAO;UF;ESTACAO;CODIGO (WMO);LATITUDE;LONGITUDE;ALTITUDE;DATA DE FUNDACAO\n')
        for i in range(1 , len(lines)):
            f.write(lines[i].replace(',','.'))
        f.close()

def adjusts(year_ini, year_fim, uf):
    adjusts_all_files()

    cabecalho = file_head()

    print(cabecalho)

    if year_ini != year_fim:
        arquivos = files_range_info(year_ini,year_fim,uf)
    else:
        arquivos = files_info(year_ini,uf)

    dados = []

    for info_data in arquivos:

        dt = pd.read_csv('clima\\tratado\\' + str(info_data['year']) + '\\' + info_data['file'], sep=';' , encoding='latin-1')

        dt.drop('Unnamed: 19', axis=1, inplace=True)

        for c in cabecalho:
            dt[c] = info_data[c]

        dados.append(dt)

    dt_all = pd.concat(dados)

    dt_all.to_csv('clima\\all_data_' + uf + '.csv', index=False, sep=';')

    with open('clima\\all_data_' + uf + '.csv', 'r', encoding="utf8") as f:
        lines = f.readlines()
        f.close()

    with open('all_data_' + uf + '.csv', "w", encoding="utf8") as f:
        f.write('Data;Hora UTC;PRECIPITAO TOTAL. HORARIO (mm);PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO. HORARIA (mB);PRESSAO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB);PRESSAO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB);RADIACAO GLOBAL (Kj/m2);TEMPERATURA DO AR - BULBO SECO. HORARIA (C);TEMPERATURA DO PONTO DE ORVALHO (C);TEMPERATURA MAXIMA NA HORA ANT. (AUT) (C);TEMPERATURA MINIMA NA HORA ANT. (AUT) (C);TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (C);TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (C);UMIDADE REL. MAX. NA HORA ANT. (AUT) (%);UMIDADE REL. MIN. NA HORA ANT. (AUT) (%);UMIDADE RELATIVA DO AR. HORARIA (%);VENTO. DIREAO HORARIA (gr) ((gr));VENTO. RAJADA MAXIMA (m/s);VENTO. VELOCIDADE HORARIA (m/s);REGIAO;UF;ESTACAO;CODIGO (WMO);LATITUDE;LONGITUDE;ALTITUDE;DATA DE FUNDACAO\n')
        for i in range(1 , len(lines)):
            f.write(lines[i].replace(',','.'))
        f.close()