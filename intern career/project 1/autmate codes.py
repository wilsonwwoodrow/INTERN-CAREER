import time

# Number of times to run the loop
num_runs = 5
# Create chart_list if not already present
if 'chart_list' not in locals() and 'chart_list' not in globals():
    chart_list = []

# Loop to run the code multiple times
for _ in range(num_runs):
    # Code 1: Scrape Data
    exec(open('scrape_data.py').read())

    print(df['Currency'])

    # Pause for 20 seconds (adjust as needed)
    time.sleep(1)

    # Code 2: Extract Buying Rate
    exec(open('extract_buying_rate.py').read())

# Code 3: Plot Graph
exec(open('plot_graph.py').read())
