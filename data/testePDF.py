import pymupdf4llm
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_core.documents import Document
from pathlib import Path

base_path = Path(__file__).parent
path_archive = base_path / "archives" / "CIC.pdf"

md = pymupdf4llm.to_markdown(path_archive)

text_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[
        ("#", "Header 1"), 
        ("##", "Header 2"), 
        ("###", "Header 3"),
        ("####", "Header 4"), 
        ("#####", "Header 5"), 
        ("######", "Header 6"),
    ],
    strip_headers=False
)

chunks = text_splitter.split_text(md)
limit = 5
print(f"quantidade de chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    if i >= limit:
        break
    print(f"chunk {i}:\n")
    print(chunk.page_content)