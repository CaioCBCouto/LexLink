import os
import PyPDF2
import openai
import asyncio

client = openai.AsyncOpenAI(api_key='sk-proj-cAnWVdJTpxe3lgeU24GlT3BlbkFJijUxLhgbHVdMiTByaxpd')

async def summarize_text(text):
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an assistant focused on helping me summarize texts."},
                  {"role": "user", "content": f"Summarize the following text:\n{text}"}]
    )
    if response.choices:
        last_message = response.choices[0].message.content.strip() if response.choices[0].message.content else "No summary available."
    else:
        last_message = "No summary available."
    return last_message

def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text() + '\n'
    return text

async def main(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    summary = await summarize_text(text)
    print("Summary of the document:")
    print(summary)

if __name__ == "__main__":
    pdf_path = r'C:\Users\caiob\OneDrive\Documentos\Codes (CESAR and Others)\1st Semester (2024)\Projetos\test.pdf'
    asyncio.run(main(pdf_path))
