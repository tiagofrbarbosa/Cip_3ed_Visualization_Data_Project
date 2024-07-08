import plotly.express as px
from die import Die

#Cria um D6 e um D10
die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Resultado do lançamento de um D6 e um D10 50.000 vezes"
labels = {'x':'Resultado','y':'Frequência'}
fig = px.bar(x=poss_results,y=frequencies,title=title,labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()