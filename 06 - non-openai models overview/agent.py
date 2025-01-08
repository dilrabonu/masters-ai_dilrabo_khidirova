from database import SpaceMissionsDatabase
import re

class SpaceMissionsAgent:
    def __init__(self, database):
        self.database = database
    
    def generate_sql_query(self, natural_language_query):
        # Convert natural language to SQL query
        query = natural_language_query.lower()
        
        # Mapping of common query patterns to SQL
        if 'most expensive' in query:
            return "SELECT * FROM missions ORDER BY `Mission Cost (billion USD)` DESC LIMIT 1"
        
        if 'how many' in query and 'missions' in query:
            if 'successful' in query:
                return "SELECT COUNT(*) as successful_missions FROM missions WHERE `Mission Success (%)` = 100.0"
            return "SELECT COUNT(*) as total_missions FROM missions"
        
        if 'average' in query:
            if 'cost' in query:
                return "SELECT AVG(`Mission Cost (billion USD)`) as avg_mission_cost FROM missions"
            if 'duration' in query:
                return "SELECT AVG(`Mission Duration (years)`) as avg_mission_duration FROM missions"
        
        if 'list' in query:
            if 'colonization' in query:
                return "SELECT * FROM missions WHERE `Mission Type` = 'Colonization'"
            if 'exploration' in query:
                return "SELECT * FROM missions WHERE `Mission Type` = 'Exploration'"
        
        # Target-specific queries
        if 'target' in query or 'missions to' in query:
            targets = ['Mars', 'Titan', 'Europa', 'Ceres', 'Proxima b', 'Betelgeuse', 'Io']
            for target in targets:
                if target.lower() in query.lower():
                    return f"SELECT * FROM missions WHERE `Target Name` = '{target}'"
        
        # Default query if no pattern matches
        return "SELECT * FROM missions LIMIT 10"
    
    def answer_question(self, question):
        # Generate SQL query
        sql_query = self.generate_sql_query(question)
        
        # Execute query
        result = self.database.query_missions(sql_query)
        
        # Convert result to natural language response
        return self.format_response(question, result)
    
    def format_response(self, question, result):
        # Convert query result to human-readable format
        if result.empty:
            return "I couldn't find any information matching your query."
        
        if 'how many' in question.lower():
            return f"Based on the query, the result is: {result.iloc[0, 0]}"
        
        if 'average' in question.lower():
            return f"The average value is: {result.iloc[0, 0]:.2f}"
        
        if 'most expensive' in question.lower():
            mission = result.iloc[0]
            return f"The most expensive mission is {mission['Mission Name']} with a cost of {mission['Mission Cost (billion USD)']} billion USD"
        
        # For listing queries, provide a summary
        return result.to_string(index=False)