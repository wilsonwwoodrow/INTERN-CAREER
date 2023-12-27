from datetime import datetime
current_time = datetime.now()
formatted_time = current_time.strftime("%H:%M:%S")
from matplotlib import pyplot as plt
plt.plot(chart_list)
plt.title(keyword)
plt.xlabel()
plt.ylabel('RATE')
plt.show()
