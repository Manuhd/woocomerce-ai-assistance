# WooCommerce AI Product Assistant

A Python-based AI assistant that fetches product data from a WooCommerce store and answers user questions using **Google Gemini** via LangChain.

---

## Features

- Fetch products from WooCommerce using REST API.
- Integrates with **LangChain** and **Google Gemini (Gemini-2.5)** for AI responses.
- Interactive terminal assistant for answering product-related questions.
- Handles product name, price, and description automatically.
- Easy to configure with `.env` file.

---

## Prerequisites

- Python 3.10+
- WooCommerce store with **REST API enabled**
- Google Cloud API key with access to Gemini
- Libraries: `requests`, `python-dotenv`, `langchain-google-genai`, `langchain`

---

# Setup
## 1 Install dependencies:
`pip install -r requirements.txt`



## 2 Create a .env file in the root:

- GOOGLE_API_KEY=your_google_api_key
- WP_API_URL=http://ecomerce-agentic-ai.local/wp-json/wc/v3/products (add your local URL)
- WC_CONSUMER_KEY=ck_your_consumer_key
- WC_CONSUMER_SECRET=cs_your_consumer_secret

## 3 Ensure your WooCommerce REST API keys have read access and WooCommerce is active.
