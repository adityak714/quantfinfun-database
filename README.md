# QFFun-Postgresql

- A quantitative finance project where S&P500 company asset tickers are retrieved, as well as stock history, and populated in a database for portfolio optimization. 

## File Structure

```
│ docker-compose.yml  
| Dockerfile.dev
| Makefile
| requirements-dev.txt
| requirements.txt       
├─.github/workflows
│  └─ static-test.yml
├─data_models
│  └─ stock_price.py
├─scripts
│  │  create_database.py
│  │  populate_database.py
│  │  populate_datasets.py
│  │  stock_downloader.py
│  └─ __init__.py
└─tables
    │  benchmark_dataset.py
    │  distribution_table.py
    │  stock_price.py
    │  training_dataset.py
    └─ __init__.py
└─utils
    └─ __init__.py
```

## Usage Instructions
Before running the script, it is important to set the Database URL for sqlalchemy as an environment variable. To set it as an environment variable, one can use the following commands:

```
# Windows
$env:DB_URL = '...'

# Linux
export DB_URL='...'
```

In order to begin the creation of the tables in the database, run the following command from the root of the repository:

```
$ python -m scripts.create_database
```

To populate the stock price table, the script gets the entire history of a particular stock from Wikipedia's list of S&P500 companies, creates individual entries for the table and then uploads it to the database. This functionality is present in the `StockDownloader` module. 

## Methods
```py
get_SNP500() -> List[str]
```
`arguments`: None \
`returns`: pd.DataFrame containing a list of tickers

```py
fill_database(tickers: List[str])
```
`arguments`: tickers that are used to locate the S&P500 assets, with information such as date, asset name, high/low figures and more. \
`Returns`: void

```py
download_stocks(tickers: str):
```

`arguments`: tickers (str): Ticker of the asset in question \
`returns`: pd.DataFrame containing full history of the stock

## Contributors: 
Mohd Sadiq [@ms2892](https://github.com/ms2892)