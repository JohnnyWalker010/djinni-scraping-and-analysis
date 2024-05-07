# Djinni Scraping and Analysis

This project is designed to help Python developers understand the most in-demand technologies in the job market by scraping job vacancies from Djinni and performing data analysis on the extracted data.


## Installation

1. ### Clone the repository:

   `git clone https://github.com/your-username/djinni-scraping-and-analysis.git`

2. ### Navigate to the project directory:

`cd djinni-scraping-and-analysis`

3. ### Install the required dependencies using pip:

`pip install -r requirements.txt`

## Usage
1. ### Run the scraping spider to gather job vacancies from Djinni:


`scrapy crawl vacancies -o vacancies.csv`

This command will scrape job vacancies related to Python and save the data to a CSV file named vacancies.csv.
2. ### Run the data analysis script to analyze the scraped data:

`python analyze_data.py`

This command will read the data from vacancies.csv, perform data analysis, and generate a bar chart showing the top 10 popular technologies in job vacancies.

## Project Structure

### The project structure is organized as follows:

* **scraping/:** Contains the Scrapy spider (vacancies.py) for scraping job vacancies from Djinni.
* **data_analysis/:** Contains the script (analyze_data.py) for analyzing the scraped data and generating visualizations.
* **vacancies.csv:** CSV file to store the scraped job vacancies data.
* **requirements.txt:** File containing the required Python packages for the project.

## Scraping
The scraping part of the project utilizes Scrapy to crawl Djinni's job listings for Python-related vacancies. The spider (vacancies.py) follows links to individual job postings and extracts information such as job title and required technologies.

## Data Analysis
The data analysis part of the project involves using pandas and matplotlib to analyze the scraped data. The script (analyze_data.py) reads the CSV file (vacancies.csv), cleans the data, counts the occurrences of each technology, and generates a bar chart showing the top 10 popular technologies in job vacancies.

## Results
After running the data analysis script, you will see a bar chart titled "Top 10 Popular Technologies in Job Vacancies" showing the count of each technology mentioned in the job listings.

## Contributing
Contributions to improve the project are welcome! If you have any suggestions, bug reports, or feature requests, please feel free to open an issue or submit a pull request.