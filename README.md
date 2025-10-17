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
```
pip install langchain langchain-community langchain-google-genai google-generativeai python-dotenv
```



## 2 Create a .env file in the root:

``` env
 GOOGLE_API_KEY=your_google_api_key
 WP_API_URL=http://ecomerce-agentic-ai.local/wp-json/wc/v3/products (add your local URL)
 WC_CONSUMER_KEY=ck_your_consumer_key
 WC_CONSUMER_SECRET=cs_your_consumer_secret
 ```

## 3 Ensure your WooCommerce REST API keys have read access and WooCommerce is active.

 Install WooCommerce plugin and create an **API key**:
- Go to **WooCommerce → Settings → Advanced → REST API → Add Key**
- User: Administrator
- Permissions: Read/Write (or Read-only)
- Copy `Consumer Key` and `Consumer Secret`

## 4. Add the **temporary filter** for local API access in `functions.php` or a plugin:

```php
add_filter('woocommerce_rest_check_permissions', function($permission = false, $context = '', $object_id = 0, $post_type = '', $user_id = null, $cap = '') {
 if (strpos($_SERVER['HTTP_HOST'], '.local') !== false) {
     return true;
 }
 return $permission;
}, 10, 6);
```

## Usage

### Run the AI assistant:

`` python wootest.py ``


### Example interaction:
```
 AI Product Assistant Ready!

 You: What is the price of Sample Product?
 AI: Sample Product costs $49.99.
```

Type exit or quit to end the assistant.

## How it Works

- Fetches product data from WooCommerce API (name, price, short_description).

- Builds a context string with all products.

- Passes context + user question to LangChain prompt.

- Returns AI-generated answers using Gemini LLM.

## Notes

- Only works on stores with WooCommerce REST API enabled.

- For local development, make sure API access is allowed (see WooCommerce 401 fixes if needed).

- This is a terminal-based assistant; you can extend it to web apps or chatbots.
