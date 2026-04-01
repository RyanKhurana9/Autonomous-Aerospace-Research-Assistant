import os 
from pathlib import Path
from typing import Annotated,TypedDict,Optional,List
from langchain_community.document_loaders import PyPDFLoader,TextLoader
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

CHROMA_DIR = "./chroma_db" # defining the folder to store the chroma database
EMBEDDING_MODEL = "all-MiniLM-L6-v2" # defining the embedding model to use
COLLECTION_NAME = "pdf_collection" # defining the collection name of the database in chromadb


def get_vector_Store()->Chroma:
    """Return existing ChromaDB vector store (read-only)."""
    embeddings=OllamaEmbeddings(model=EMBEDDING_MODEL) # initialize the embedding model
    vector_store=Chroma(collection_name=COLLECTION_NAME,embedding_function=embeddings)
    return Chroma(#intializ the vector store by connecting it to
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )
def ingest_documents(paths: List[str]) -> int:# input will be a list of file paths to ingert into the vetor store
    """
    Ingest PDF or text documents into the vector store.
    Returns the number of chunks added.
 
    Usage:
        from rag import ingest_documents
        ingest_documents(["papers/my_paper.pdf", "notes/rocket_notes.txt"])
    """
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    vectorstore = Chroma(# connect to the chroma vecotr->use the embedding model to create the embeddings and specify the collection name and the directory to store the database
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )

 
    splitter = RecursiveCharacterTextSplitter(# initialize the text splitter to split the documents into smaller chunks for better embedding and retrieval
        chunk_size=800,
        chunk_overlap=100,
        separators=["\n\n", "\n", ". ", " ", ""],# split in new line ,space,period
    )
 
    all_chunks = []
    for path_str in paths:
        path = Path(path_str)#convert it path object basically makes it easier to work with file paths and perform operations like checking if the file exists, getting the file name, etc.
        if not path.exists():#check if the file exists if the file does not exist then skip the file and print a warning that the file mentioned is the path does not exists and would be skipped
            print(f"[RAG] Warning: {path} not found, skipping.")
            continue
        if path.suffix.lower() == ".pdf":# if the path contains a pdf file then will use the pypdf laodet to load the pdf file else it will be a text file then we will use the text loader to laod the text file
            loader = PyPDFLoader(str(path))
        if path.suffix.lower()=='txt':
            loader = TextLoader(str(path), encoding="utf-8")
        docs = loader.load()
        chunks = splitter.split_documents(docs)
        for chunk in chunks:
            chunk.metadata["source"] = path.name
        all_chunks.extend(chunks)
        print(f"[RAG] Ingested {len(chunks)} chunks from {path.name}")
 
    if all_chunks:
        vectorstore.add_documents(all_chunks)
        print(f"[RAG] Total chunks in store: {vectorstore._collection.count()}")
 
    return len(all_chunks)
def retrieve_relevant_chunks(query: str, top_k: int = 5) -> List[Document]:
    """Retrieve relevant chunks from the vector store based on the query."""
    vectorstore = get_vector_Store()
    relevant_chunks = vectorstore.similarity_search(query, k=top_k)
    return relevant_chunks
if __name__ == "__main__":# the main purpose is  if we run this file else ignore it if we import this file in other files
    # Quick ingest test — drop PDFs in ./papers/ and run this file
    import sys
    if len(sys.argv) > 1:# if we provide the file paths as command line arguments then we will ingest those files into the vector store else we will look for the pdf files in the papers directory and ingest those files if there are no files in the papers directory then we will print a message to the user that there are no pdf files found in the papers directory and if there are no command line arguments provided and there are no pdf files in the papers directory then we will print a usage message to the user to provide the file paths as command line arguments
        added = ingest_documents(sys.argv[1:])# list of sys.argv[1:]
        print(f"Done. Added {added} chunks.")
    else:
        paper_dir = Path("./papers")
        if paper_dir.exists():
            pdfs = list(paper_dir.glob("*.pdf"))
            if pdfs:
                ingest_documents([str(p) for p in pdfs])
            else:
                print("No PDFs found in ./papers/")
        else:
            print("Usage: python rag.py path/to/paper.pdf [more files...]")
 
 

   
