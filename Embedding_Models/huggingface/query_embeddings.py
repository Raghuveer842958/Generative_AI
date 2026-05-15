from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

query_embedding = embeddings.embed_query("What is a sentence embedding?")
doc_embeddings = embeddings.embed_documents(
    [
        "Sentence embeddings map text to dense vectors.",
        "LangChain provides a standard Embeddings interface.",
    ]
)

print("Query embedding:", query_embedding)
print("Document embeddings:", doc_embeddings)


# from langchain_huggingface import HuggingFaceEmbeddings

# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# result = embeddings.embed_query("What is Node.js?")

# print(result)   # first 10 values
# print(len(result))   # embedding dimension