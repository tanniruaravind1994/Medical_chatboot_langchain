from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_pdf_files(data):
    loader=DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    documents=loader.load()
    return documents

extract_text=load_pdf_files("Data")
print(extract_text)