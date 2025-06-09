import requests
import os
import pandas as pd
import re

# Set your Together.ai API key
API_KEY = os.getenv("TOGETHER_API_KEY", "enter api key from together ai")
API_URL = "https://api.together.xyz/v1/chat/completions"
MODEL = "meta-llama/Llama-3-8b-chat-hf"

def ask_question(dataframe, question):
    try:
        # Check for specific query patterns
        if re.search(r"MSKU.*quantity\s*>\s*(\d+)", question, re.IGNORECASE):
            threshold = int(re.search(r"(\d+)", question).group(1))
            filtered_df = dataframe[dataframe['Quantity'] > threshold][['MSKU', 'Quantity']]
            
            if filtered_df.empty:
                return "No MSKUs found with quantity greater than {}.".format(threshold)
            
            # Save filtered data to CSV
            output_path = os.path.join("processed", "filtered_output.csv")
            filtered_df.to_csv(output_path, index=False)
            
            # Generate natural language response
            response = f"Found {len(filtered_df)} MSKUs with quantity greater than {threshold}:\n"
            for _, row in filtered_df.iterrows():
                response += f"- {row['MSKU']}: {row['Quantity']}\n"
            response += f'<a href="/download/filtered_output.csv" download>Download filtered data as CSV</a>'
            return response

        # General AI query for other questions
        sample_data = dataframe.head(20).to_csv(index=False)
        prompt = f"""You are a data analyst AI. Here is a sample of the warehouse data:\n\n{sample_data}\n\n
        Answer the question in natural language, as if explaining to a non-technical user. Do not include code or technical terms like 'pandas' or 'DataFrame'. Focus on clear, concise, and helpful answers based on the data. If the question involves filtering or summarizing data, describe the results naturally and avoid showing raw code or errors. Question: {question}"""

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": "You are a helpful data analyst who communicates clearly and avoids technical jargon."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.5,
            "max_tokens": 500
        }

        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        reply = response.json()["choices"][0]["message"]["content"]
        return reply.strip()

    except Exception as e:
        return f"Sorry, I encountered an issue: {e}. Please try rephrasing your question or check the data."
