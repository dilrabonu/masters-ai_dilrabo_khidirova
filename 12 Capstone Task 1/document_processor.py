import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings 
from langchain_community.vectorstores import FAISS
import faiss

class DocumentProcessor:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.documents = []
        self.embeddings = OpenAIEmbeddings(
            model="text-embedding-3-large",
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        self.vectorstore = None

    def load_documents(self):
        """Load all documents from the data directory"""
        for filename in os.listdir(self.data_dir):
            file_path = os.path.join(self.data_dir, filename)
            
            if filename.endswith('.pdf'):
                loader = PyPDFLoader(file_path)
                pages = loader.load()
                
                for page in pages:
                    page.metadata['source'] = filename
                    page.metadata['page_number'] = page.metadata.get('page', 0) + 1
                
                self.documents.extend(pages)
                print(f"Loaded PDF: {filename} with {len(pages)} pages")
            
            elif filename.endswith('.txt'):
                loader = TextLoader(file_path)
                documents = loader.load()
                for doc in documents:
                    doc.metadata['source'] = filename
                self.documents.extend(documents)
                print(f"Loaded text file: {filename}")
        
        print(f"Total documents loaded: {len(self.documents)}")
        return self.documents


    def load_faiss_index(self):
        """Load FAISS index from local storage"""
        self.vectorstore = FAISS.load_local("faiss_index", self.embeddings, allow_dangerous_deserialization=True)
        print("Loaded FAISS index from disk")

    def create_embeddings(self):
        if not self.documents:
            print("No documents loaded. Call load_documents() first.")
            return None

        if os.path.exists("faiss_index"):
            print("FAISS index already exists. Loading existing index.")
            self.load_faiss_index()
            return self.vectorstore
       

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
        )
        splits = text_splitter.split_documents(self.documents)
        print(f"Split into {len(splits)} chunks for embeddings")

        sample_embedding = self.embeddings.embed_query("test")
        index = faiss.IndexFlatL2(len(sample_embedding))

        # ✅ Correct usage with keyword arguments
        self.vectorstore = FAISS.from_documents(
            documents=splits,
            embedding=self.embeddings,
        )

        self.vectorstore.save_local("faiss_index")
        print("Vector store saved to disk")
        self.push_to_git()
        return self.vectorstore

    def push_to_git(self):
        """Push the FAISS index to Git repository"""
        os.system("git add faiss_index")
        os.system("git commit -m 'Update FAISS index'")
        os.system("git push")
        print("FAISS index pushed to Git")

    def search_documents(self, query, k=3):
        """Search documents for relevant information"""
        if not self.vectorstore:
            try:
                self.vectorstore = FAISS.load_local("faiss_index", self.embeddings, allow_dangerous_deserialization=True)
                print("Loaded vector store from disk")
            except:
                print("No vector store found. Create embeddings first.")
                return []
        
        results = self.vectorstore.similarity_search_with_relevance_scores(query, k=k)
        return results
