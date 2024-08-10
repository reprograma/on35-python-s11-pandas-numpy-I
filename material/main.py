import file

#file.adjusts_all_files()

file.sample(2020,2023,'')

estados = ['AC','AL','AP','AM','BA','CE','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO','DF']

for estado in estados:
    file.sample(2020,2023, estado)