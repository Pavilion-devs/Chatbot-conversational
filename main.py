import PyPDF2
import spacy
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import textwrap  # Optional: for wrapping text

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from all pages of a PDF.
    """
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def segment_text(text, nlp):
    """
    Uses spaCy to segment the input text into sentences.
    """
    doc = nlp(text)
    # Return non-empty sentences stripped of extra spaces.
    sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]
    return sentences

def compute_sentence_embeddings(sentences, model):
    """
    Computes embeddings for each sentence using a SentenceTransformer model.
    """
    embeddings = model.encode(sentences, convert_to_tensor=False)
    return np.array(embeddings)

def retrieve_relevant_sentences(query, sentences, sentence_embeddings, model, top_k=3):
    """
    Given a query, compute its embedding and return the top_k most similar sentences.
    """
    query_embedding = model.encode([query], convert_to_tensor=False)
    query_embedding = np.array(query_embedding)
    similarities = cosine_similarity(query_embedding, sentence_embeddings)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]
    return [sentences[i] for i in top_indices]

def main():
    # --- Step 1: Load spaCy model ---
    nlp = spacy.load("en_core_web_sm")
    
    # --- Step 2: Extract text from PDF ---
    pdf_path = "data.pdf"  # Replace with your actual PDF file path.
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)
    
    if not text:
        print("No text could be extracted from the PDF. Please check the file.")
        return
    
    # --- Step 3: Segment the text into sentences ---
    print("Segmenting text into sentences...")
    sentences = segment_text(text, nlp)
    print(f"Total sentences extracted: {len(sentences)}")
    
    # --- Step 4: Load SentenceTransformer model ---
    print("Loading sentence-transformers model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # --- Step 5: Compute sentence embeddings ---
    print("Computing sentence embeddings...")
    sentence_embeddings = compute_sentence_embeddings(sentences, model)
    
    # --- Step 6: Start the conversation (retrieval loop) ---
    print("\nSetup complete. You can now ask questions about the PDF content.")
    print("Type 'exit' or 'quit' to end the conversation.\n")
    
    while True:
        query = input("Your question: ")
        if query.lower() in ['exit', 'quit']:
            print("Exiting...")
            break
        
        relevant_sentences = retrieve_relevant_sentences(query, sentences, sentence_embeddings, model, top_k=3)
        print("\nRelevant content from PDF:\n")
        for sent in relevant_sentences:
            # Normalize whitespace: removes extra newlines and spaces
            formatted_sent = " ".join(sent.split())
            # Optional: wrap text to 80 characters width for better console display
            wrapped_sent = textwrap.fill(formatted_sent, width=80)
            print("- " + wrapped_sent)
        print("\n")

if __name__ == "__main__":
    main()
