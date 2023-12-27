# Forex Data Scraping and Visualization

This repository contains Python scripts for scraping live forex exchange rates, extracting buying rates, and visualizing the data using Matplotlib.

## Scripts

### 1. scrape_data.py

This script uses Selenium and BeautifulSoup to scrape live exchange rates from OANDA's currency converter webpage.

**Dependencies:**
- Selenium
- BeautifulSoup

**How to Run:**
- Ensure you have the necessary dependencies installed (`pip install selenium beautifulsoup4`).
- Download the appropriate WebDriver for your browser and update the path in the script.
- Run the script: `python scrape_data.py`.

### 2. extract_buying_rate.py

This script extracts the buying rates for a specified currency from the scraped data.

**How to Run:**
- Ensure `scrape_data.py` has been run first to generate the necessary data.
- Run the script: `python extract_buying_rate.py`.

### 3. plot_graph.py

This script plots a graph of the buying rates over time using Matplotlib.

**Dependencies:**
- Matplotlib

**How to Run:**
- Ensure `extract_buying_rate.py` has been run to generate the `chart_list`.
- Run the script: `python plot_graph.py`.

### 4. run_scripts.py

This script automates the execution of the above scripts in a loop for a specified number of runs.

**How to Run:**
- Edit the script to set the number of runs (`num_runs`).
- Run the script: `python run_scripts.py`.

## Important Notes

- Make sure to comply with the terms of use of the website being scraped.
- Adjust sleep intervals and other parameters as needed.
- Update WebDriver paths and other configurations based on your environment.

## Contributors

- Woodrow W. Wilson

Feel free to contribute, report issues, or suggest improvements!
