import plotly.express as px
from die import Die

#Cria um D6
die = Die()
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Resultado do lançamento de um D6 1000 vezes"
labels = {'x':'Resultado','y':'Frequência'}
fig = px.bar(x=poss_results,y=frequencies,title=title,labels=labels)
fig.show()