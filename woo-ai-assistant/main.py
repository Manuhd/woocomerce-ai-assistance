import os
import requests
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
wp_api_url = os.getenv("WP_API_URL")
wc_ck = os.getenv("WC_CONSUMER_KEY")
wc_cs = os.getenv("WC_CONSUMER_SECRET")

# Initialize Gemini model via LangChain
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)

# Fetch WooCommerce product data
def fetch_products():
    try:
        res = requests.get(wp_api_url, auth=(wc_ck, wc_cs))
        res.raise_for_status()
        products = res.json()
        context = "\n".join([
            f"Product: {p['name']}\nPrice: {p['price']}\nDescription: {p.get('short_description', '')}\n"
            for p in products
        ])
        return context
    except Exception as e:
        print(" Error fetching products:", e)
        return ""

# Create prompt template
template = """
You are a helpful product assistant for an eCommerce store.
Use the below product data to answer the user's question clearly and briefly.

Product Data:
{context}

User Question:
{question}
"""

prompt = PromptTemplate(template=template, input_variables=["context", "question"])
chain = LLMChain(prompt=prompt, llm=llm)

# Run assistant
def run_assistant():
    print(" AI Product Assistant Ready!\n")
    context = fetch_products()

    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = chain.run({"context": context, "question": question})
        print("\n AI:", response, "\n")

if __name__ == "__main__":
    run_assistant()

