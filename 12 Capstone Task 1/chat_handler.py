from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os
from dotenv import load_dotenv

class ChatHandler:
    def __init__(self, document_processor):
        load_dotenv()
        self.document_processor = document_processor
        openai_key = os.environ.get("OPENAI_API_KEY", "")
        if not openai_key:
            raise ValueError("OpenAI API key not set. Please enter it in the sidebar.")
            
        self.llm = ChatOpenAI(model_name="gpt-4o-mini") 
        self.company_info = {
            "name": "AutoMotive Support",
            "phone": "+1-800-555-AUTO",
            "email": "support@automotivesupport.com",
            "website": "https://automotivesupport.com"
        }
        self.conversation_history = []
        
    def get_context_from_documents(self, query):
        """Retrieve relevant document chunks for the query"""
        results = self.document_processor.search_documents(query)
    
        if not results:
            return ""
    
        
        top_results = results[:3]

        
        context = ""
        for doc, score in top_results:
            print(f"Using chunk with score: {score}")  
        
            source = doc.metadata.get('source', 'Unknown')
            page = doc.metadata.get('page_number', 'N/A')
            context += f"\nCONTENT: {doc.page_content}\nSOURCE: {source}, Page: {page}\n\n"
    
        return context
    
    def format_system_prompt(self):
        """Create system prompt with company information"""
        return f"""You are a helpful customer support assistant for {self.company_info['name']}.
You answer questions based on the provided document context.
If you don't know the answer or can't find it in the context, suggest creating a support ticket.
Always cite your sources when answering questions, mentioning the document name and page number.
Company contact information:
- Phone: {self.company_info['phone']}
- Email: {self.company_info['email']}
- Website: {self.company_info['website']}

If the user wants to create a support ticket, ask for their name and email if not already provided.
"""
    
    def process_message(self, user_message):
        """Process user message and generate a response"""
        self.conversation_history.append(HumanMessage(content=user_message))
    
        # Step 1: Try to get context from documents
        context = self.get_context_from_documents(user_message)
    
        # Step 2: Start with default system prompt
        system_prompt = self.format_system_prompt()

        if context:
            # If context exists, guide the LLM to use it
            context_message = SystemMessage(content=f"Use the following context to answer the user's question: {context}")
        else:
            # If no context, instruct LLM to use general knowledge politely
            context_message = SystemMessage(content=(
                "No document context was found for the user's question. "
                "Please use your own knowledge to help, while staying professional. "
                "Offer to create a support ticket if appropriate."
            ))

        # Step 3: Prepare messages for the LLM
        messages = [
            SystemMessage(content=system_prompt),
            context_message
        ]
    
        # Include conversation history (last 5 exchanges)
        messages.extend(self.conversation_history[-10:])
    
        # Step 4: Get and return LLM response
        response = self.llm.invoke(messages)
        self.conversation_history.append(AIMessage(content=response.content))
    
        return response.content
    
        
    def check_ticket_intent(self, message):
        """Check if user intends to create a ticket"""
        ticket_phrases = [
            "create a ticket",
            "open a ticket",
            "submit a ticket",
            "raise a ticket",
            "support ticket",
            "help ticket",
            "new ticket"
        ]
        
        message_lower = message.lower()
        return any(phrase in message_lower for phrase in ticket_phrases)