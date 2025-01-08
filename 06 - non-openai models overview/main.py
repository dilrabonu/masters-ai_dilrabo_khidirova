from database import SpaceMissionsDatabase
from agent import SpaceMissionsAgent
import os

def main():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the full path to the CSV file
    csv_path = os.path.join(current_dir, 'space_missions_dataset.csv')
    
    try:
        # Initialize database
        db = SpaceMissionsDatabase(csv_path)
        
        # Create agent
        agent = SpaceMissionsAgent(db)
        
        print("Space Missions Agent")
        print("-------------------")
        print("Ask questions about space missions. Type 'exit' to quit.")
        
        # Interactive loop
        while True:
            try:
                question = input("\nYour question: ")
                
                if question.lower() == 'exit':
                    break
                
                response = agent.answer_question(question)
                print("\nAgent's Response:")
                print(response)
                print("\n" + "-"*50)
            
            except Exception as e:
                print(f"An error occurred: {e}")
        
    except Exception as e:
        print(f"Failed to initialize the agent: {e}")
    
    finally:
        # Ensure database connection is closed
        if 'db' in locals():
            db.close_connection()

if __name__ == "__main__":
    main()