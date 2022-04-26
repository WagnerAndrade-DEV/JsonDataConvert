from pytz import timezone 
from datetime import datetime

#YYY-MM-DD para Json Date
d = timezone('America/Sao_Paulo').localize(datetime(1995, 9, 14, 00, 00, 00))

#Json Date para YYY-MM-DD
j = datetime.fromtimestamp(811047600.0)

print('YYY-MM-DD para Json','\n', d.timestamp()) 
print()
print('Json para YYY-MM-DD', '\n', j)

#documentação 
#https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp
#https://hkotsubo.github.io/blog/2019-05-02/o-que-e-timestamp#javascript