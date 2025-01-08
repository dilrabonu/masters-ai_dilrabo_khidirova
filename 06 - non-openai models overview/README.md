# Space Missions Agent

## Project Overview
This is an intelligent agent-based system for querying and analyzing space missions data using natural language processing and SQL.

## Features
- Convert natural language queries to SQL
- Interactive command-line interface
- Comprehensive space missions dataset analysis
- Dynamic query generation

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the main script:
```bash
python main.py
```

### Example Queries
- "How many missions were successful?"
- "What is the average mission cost?"
- "List all colonization missions"
- "How many total missions are there?"

## Project Structure
- `main.py`: Entry point and interactive interface
- `agent.py`: Natural language to SQL query agent
- `database.py`: Database management and query execution
- `space_missions_dataset.csv`: Source data

## Technologies
- Pandas
- SQLite
- Python

## Future Improvements
- Advanced NLP query parsing
- Machine learning-based query understanding
- Visualization of mission data

## License
MIT License

https://www.kaggle.com/datasets/sameerk2004/space-missions-dataset