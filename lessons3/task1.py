from datetime import datetime

current_datetime = datetime.now()
day = (current_datetime.day)
month = (current_datetime.month)
temperature = 9

print('Сегодня ' + str(day) +'/' + str(month) + '/2023. На улице ' + str(temperature)+' градусов.')
if temperature < 0: print('Холодно, лучше останьтесь дома')
