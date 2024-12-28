# 🐾 Animal Database AI Query Assistant

## 📝 Project Overview

This project is an innovative AI-powered database query system that allows users to ask natural language questions about animals and receive precise, data-driven answers. By leveraging OpenAI's GPT model and SQLite, the application translates human-readable questions into SQL queries, making complex database exploration intuitive and accessible.

## ✨ Key Features

- 🤖 **AI-Powered Query Translation**: Convert natural language questions to SQL queries
- 🔍 **Flexible Database Exploration**: Query animal information dynamically
- 💡 **Intelligent Responses**: Retrieve detailed animal data with minimal effort
- 🛡️ **Robust Error Handling**: Comprehensive error management and input validation

## 🛠 Technologies Used

- **Backend**: Flask
- **AI Model**: OpenAI GPT-4
- **Database**: SQLite
- **Environment Management**: python-dotenv

## 🚀 Quick Start Guide

### Prerequisites

- Python 3.8+
- OpenAI API Key

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/animal-database-ai
   cd animal-database-ai
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

### Running the Application

```bash
python main.py
```

The application will start on `http://localhost:5000`

## 🔬 API Endpoints

### Root Endpoint
- `GET /`: Returns a welcome message

### Query Endpoint
- `POST /query`: Submit natural language questions about animals

#### Example Query
```bash
curl -X POST http://localhost:5000/query \
     -H "Content-Type: application/json" \
     -d '{"question": "List animals taller than 2 meters with their top speeds"}'
```

## 📊 Database Structure

**Table**: `animals_info`
**Columns**: 
- Name
- Kingdom
- Phylum
- Class
- Order
- Family
- Genus
- Species
- Top Speed
- Weight
- Height
- Length
- Distribution
- Diet
- Habitat

## 🧠 How It Works

1. User submits a natural language question
2. OpenAI GPT translates the question into a SQL query
3. Query is executed against the SQLite database
4. Results are returned in JSON format

## 🛡️ Error Handling

- Missing API key triggers a `ValueError`
- Invalid queries return descriptive error responses
- Database connection errors are gracefully managed

## 🔮 Potential Improvements

- Implement query caching
- Add more sophisticated NLP preprocessing
- Create a web interface
- Expand database with more animal information

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📜 License

Distributed under the MIT License.

## 📞 Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/animal-database-ai](https://github.com/yourusername/animal-database-ai)

## 🙏 Acknowledgements

- OpenAI for GPT technology
- Flask Web Framework
- SQLite Database
