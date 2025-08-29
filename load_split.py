import pickle
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def main():
    # Step 1: Load your markdown/text file
    loader = TextLoader(r"C:\Users\achut\Downloads\alice_in_wonderland.md", encoding="utf-8")
    documents = loader.load()

    # Step 2: Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=500)
    texts = splitter.split_documents(documents)

    print(f"✅ Loaded {len(documents)} document(s)")
    print(f"✅ Split into {len(texts)} chunks")

    # Step 3: Save chunks to disk
    with open("texts.pkl", "wb") as f:
        pickle.dump(texts, f)

    print("📂 Text chunks saved to texts.pkl")

if __name__ == "__main__":
    main()

