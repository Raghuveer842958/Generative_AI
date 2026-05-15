from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

doc_embeddings = embeddings.embed_documents(
    [
        "Sentence embeddings map text to dense vectors.",
        "LangChain provides a standard Embeddings interface.",
    ]
)

print("Document embeddings:", doc_embeddings)