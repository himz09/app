import os
import PyPDF2
import openai
from langchain import OpenAI, LangChain

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# Initialize LangChain with the OpenAI LLM
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
langchain = LangChain(llm)

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.getNumPages()):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

def summarize_text(text):
    prompt = f"Please summarize the following text:\n\n{text}"
    response = langchain.generate(prompt)
    return response

def main(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    summary = summarize_text(text)
    print("Summary of the PDF:\n")
    print(summary)

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    main(pdf_path)
