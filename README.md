
# Python Data Processing Pipeline

## Project Overview
A Python-based data processing pipeline that reads raw data from CSV, JSON files, and APIs, cleans and transforms the data, and generates structured output.

## Features
- Read CSV and JSON files
- Fetch data from APIs
- Handle missing values
- Remove duplicate records
- Convert data types
- Transform employee data
- Calculate annual salary
- Export cleaned data into CSV and JSON
- Logging and error handling
- YAML configuration management

## Technologies Used
- Python
- Pandas
- PyYAML
- Requests
- Git and GitHub

## Project Structure
```text
data-processing-pipeline/
├── data/
│   ├── input/
│   └── output/
├── src/
│   ├── main.py
│   ├── reader.py
│   ├── cleaner.py
│   ├── transformer.py
│   ├── writer.py
│   ├── logger.py
│   └── api_reader.py
├── config/
│   └── config.yaml
├── logs/
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository.
2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the environment:

```powershell
.\venv\Scripts\Activate
```

4. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Project

```bash
python src/main.py
```

## Input Sources
- CSV files
- JSON files
- REST API

Configure the input source and output path in `config/config.yaml`.

## Output
Processed data is saved in the `data/output/` directory.

## Logging
Pipeline activities and errors are recorded in `logs/pipeline.log`.

## Author
Amiksha Kulal
