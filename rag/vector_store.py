from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS


load_dotenv()

loader = TextLoader(
    "rag/data/travel_data.txt"
)

docs = loader.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_documents(
    docs
)


embeddings = GoogleGenerativeAIEmbeddings( model="models/embedding-001" )

vector_db = FAISS.from_documents(
    chunks,
    embeddings
)


vector_db.save_local(
    "faiss_index"
)

print("Vector DB created")