# AI-Powered Shopify Analytics App

## Overview
This is a submission-ready interview assignment implementing an AI-powered analytics app for Shopify.
The system accepts natural language questions and returns business-friendly insights using an agent-based design.

## How It Works
User Question → Agent → ShopifyQL → Shopify API (mocked) → Explanation

## Run Locally
pip install -r requirements.txt
uvicorn main:app --reload

## Sample Request
POST /ask
{
  "store_id": "demo.myshopify.com",
  "question": "How much inventory should I reorder for next week?"
}
