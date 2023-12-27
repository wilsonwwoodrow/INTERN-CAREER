if len(chart_list)==0:
    keyword = input('What chart do you wanna print: ')
    rate = input('Would you like to display \'BID RATE (1), \'ASK RATE (2)\': ')
rate = int(rate)  # Convert rate to an integer

search_1 = df[df['Currency'] == keyword]
while rate != 1 and rate != 2:
    rate = input('Would you like to display \'BID RATE (1), \ASK RATE (2): ')
    rate = int(rate)
if rate == 1:
    chart_list.append(search_1['buying'])
elif rate == 2:
    chart_list.append(search_1['selling'])
else:
    print('Invalid choice')  

print(chart_list)
if len(chart_list) >= 50:
    chart_list.pop(0)
