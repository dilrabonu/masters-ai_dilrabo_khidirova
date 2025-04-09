import requests
import os
from dotenv import load_dotenv
from langchain_core.messages import ToolCall, ToolMessage


class GitHubIssueCreator:
    def __init__(self):
        load_dotenv()
        self.github_api_url = os.getenv("GITHUB_API_URL")
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.headers = {
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def create_issue(self, username, email, summary, description):
        """Create a new GitHub issue as a support ticket"""
        
        # Add user information to description
        full_description = f"Submitted by: {username}\nEmail: {email}\n\n{description}"
        
        # Prepare the payload
        payload = {
            "title": summary,
            "body": full_description,
            "labels": ["support"]
        }
        
        try:
            response = requests.post(
                self.github_api_url,
                headers=self.headers,
                json=payload
            )
            
            # Check if request was successful
            if response.status_code == 201:
                data = response.json()
                issue_url = data["html_url"]
                issue_number = data["number"]
                return {
                    "success": True,
                    "message": f"Support ticket created successfully",
                    "issue_url": issue_url,
                    "issue_number": issue_number
                }
            else:
                return {
                    "success": False,
                    "message": f"Failed to create issue: {response.status_code} - {response.text}"
                }
        
        except Exception as e:
            return {
                "success": False,
                "message": f"Error creating GitHub issue: {str(e)}"
            }