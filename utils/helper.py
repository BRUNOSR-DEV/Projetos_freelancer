from datetime import date
from datetime import datetime

def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%y')

def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%y')

def formata_float_str_moeda(valor:float) -> str:
    return f'R${valor:,.2f}'

def formata_cpf_str(cpf: str) -> str:
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'


'''ret = (date_para_str(datetime.now()))
print(str_para_date(ret))

print(formata_cpf_str('41361568801'))'''