# Chatbot-conversational

Below is a sample `README.md` file for your project:

---

```markdown
# PDF Chatbot with Retrieval-Based Conversation Layer

This project demonstrates a simple PDF extraction and retrieval-based question answering system using Python. It extracts text from a PDF file, segments the text into sentences using spaCy, computes sentence embeddings using SentenceTransformers, and allows users to query the PDF content via a command line interface.

## Features

- **PDF Extraction:** Extracts text from PDF files using PyPDF2.
- **Text Segmentation:** Splits the extracted text into sentences using spaCy.
- **Embedding Computation:** Generates sentence embeddings with SentenceTransformers.
- **Retrieval-Based Conversation:** Answers user questions by retrieving the most relevant sentences based on cosine similarity.

## Prerequisites

- Python 3.x
- [Visual Studio Code](https://code.visualstudio.com/) (or any other Python IDE)
- Required Python packages:
  - PyPDF2
  - spacy
  - sentence-transformers
  - scikit-learn

## Installation

1. **Clone the Repository or Download the Code**

   Clone this repository or download the project files to your local machine.

2. **Install the Required Packages**

   Open a terminal in your project directory and run:

   pip install PyPDF2 sentence-transformers spacy scikit-learn

3. **Download the spaCy Model**

   Download the `en_core_web_sm` model by running in your terminal:

   python -m spacy download en_core_web_sm

## Usage

1. **Update the PDF File Path**

   Open the main Python script in VSCode and replace the placeholder path `"path/to/your_pdf_file.pdf"` ( replace with data.pdf) with the actual path to your PDF file.

2. **Run the Script**

   Run the script using VSCode's Run/Debug feature or from the terminal:

   ```bash
   python main.py
   ```

3. **Interact with the Chatbot**

   - When prompted, type your questions about the PDF content.
   - The system will display the most relevant sentences from the PDF.
   - Type `exit` or `quit` to end the conversation.

## Project Structure

```
.
├── main.py   # Main Python script with the PDF chatbot code
└── README.md             # This file
```

## Customization

- **Embedding Model:** You can change the SentenceTransformers model by modifying the model name in the code.
- **Text Formatting:** The code normalizes whitespace and wraps text for better console display. Adjust these settings as needed.
- **Conversation Loop:** The current interface is terminal-based. You can integrate a GUI or a web interface if desired.

## Contributing

Contributions, suggestions, or improvements are welcome! Please feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.
```

---

Simply save the above content into a file named `README.md` in your project directory, and you'll have a complete project readme for using the PDF chatbot with normal Python on VSCode.