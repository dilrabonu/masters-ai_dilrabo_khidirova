import os
import pdfplumber
import openai
from typing import List, Dict
import tiktoken
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Secure API Key handling
openai.api_key = os.getenv('OPENAI_API_KEY')

class PDFChatbot:
    def __init__(self, pdf_path: str, chunk_size: int = 1000, overlap: int = 200):
        """
        Initialize PDFChatbot with advanced text processing capabilities
        
        Args:
            pdf_path (str): Path to the PDF document
            chunk_size (int): Number of tokens per text chunk
            overlap (int): Number of tokens to overlap between chunks
        """
        self.pdf_path = pdf_path
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.document_text = self.extract_text_from_pdf()
        self.text_chunks = self.create_text_chunks()
    
    def extract_text_from_pdf(self) -> str:
        """
        Extract text from PDF with robust error handling
        
        Returns:
            str: Extracted text from PDF
        """
        try:
            text = ""
            with pdfplumber.open(self.pdf_path) as pdf:
                # Check document size
                total_pages = len(pdf.pages)
                if total_pages > 100:
                    print(f"Warning: Large document detected with {total_pages} pages")
                
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            
            if not text:
                raise ValueError("No text could be extracted from the PDF")
            
            return text
        
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
            return ""
    
    def create_text_chunks(self) -> List[str]:
        """
        Create overlapping text chunks for better context handling
        
        Returns:
            List[str]: List of text chunks
        """
        encoding = tiktoken.get_encoding("cl100k_base")
        tokens = encoding.encode(self.document_text)
        
        chunks = []
        for i in range(0, len(tokens), self.chunk_size - self.overlap):
            chunk = encoding.decode(tokens[i:i + self.chunk_size])
            chunks.append(chunk)
        
        return chunks
    
    def find_most_relevant_chunks(self, query: str, top_k: int = 3) -> List[str]:
        """
        Find most relevant text chunks for a given query
        
        Args:
            query (str): User's query
            top_k (int): Number of top chunks to return
        
        Returns:
            List[str]: Most relevant text chunks
        """
        # Simple relevance scoring (can be replaced with more advanced embedding-based search)
        chunks_with_scores = [
            (chunk, len(set(query.lower().split()) & set(chunk.lower().split())))
            for chunk in self.text_chunks
        ]
        
        return [chunk for chunk, _ in sorted(chunks_with_scores, key=lambda x: x[1], reverse=True)[:top_k]]
    
    def chat_with_pdf(self, query: str) -> str:
        """
        Generate response based on PDF context and user query
        
        Args:
            query (str): User's query
        
        Returns:
            str: AI-generated response
        """
        try:
            # Find most relevant chunks
            relevant_chunks = self.find_most_relevant_chunks(query)
            context = "\n\n".join(relevant_chunks)
            
            # Construct prompt
            prompt = f"""Context from PDF document:
{context}

User Query: {query}

Based on the context, provide a detailed and accurate response to the query."""
            
            # Generate response using OpenAI
            client = openai.OpenAI()
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant analyzing a PDF document."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            print(f"Error generating response: {e}")
            return "I'm sorry, but I couldn't process your query at the moment."

def main():
    # Example usage
    pdf_path = "Pride_and_Prejudice.pdf"  # Replace with your PDF path
    chatbot = PDFChatbot(pdf_path)
    
    while True:
        user_query = input("\nEnter your question about the PDF (or 'exit' to quit): ")
        
        if user_query.lower() == 'exit':
            break
        
        response = chatbot.chat_with_pdf(user_query)
        print("\nResponse:", response)

if __name__ == "__main__":
    main()