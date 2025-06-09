Warehouse Management MVP
Overview
The Warehouse Management MVP is a web application for analyzing warehouse inventory data. It allows users to upload CSV files, preprocess data, visualize it through interactive charts, and query insights using an AI-powered chatbot. Built with Flask, Pandas, Plotly, and integrated with the Together.ai API, this tool provides a modern interface with a dark theme and violet accents, featuring a floating chatbot for natural language queries.

Features
CSV Upload & Preprocessing: Upload a CSV file, clean it (remove missing MSKU/FNSKU rows, ensure numeric Quantity), and display the processed data.
Interactive Charts: Generate bar, line, or pie charts to visualize Quantity by MSKU using Plotly.
AI Chatbot: Query data with natural language (e.g., "Show MSKUs with quantity > 5") and download filtered results as CSV.
Modern UI: Black background with violet accents, a floating chatbot button, and a responsive modal for AI interactions.
Prerequisites
Python: Version 3.8 or higher.
Together.ai API Key: Required for AI chatbot functionality.
Web Browser: Chrome, Firefox, or any modern browser for the web interface.
Dependencies
The project uses the following Python libraries (extracted from the code):

flask (web framework)
pandas (data processing)
plotly (interactive charts)
requests (API calls to Together.ai)
Install them using:

bash




pip install flask pandas plotly requests
Project Structure
text



warehouse-management-mvp/
├── static/
│   └── chatbot-icon.png  # Place your chatbot image here
├── templates/
│   └── index.html       # Main web interface
├── uploads/             # Folder for uploaded CSV files
├── processed/           # Folder for cleaned and filtered CSV outputs
├── app.py               # Flask application
├── ai_query.py          # AI chatbot logic with Together.ai API
├── preprocessing.py     # Data cleaning and preprocessing logic
└── README.md            # This file
Setup Instructions
Clone the Repository (or create the project structure):
bash




git clone <repository-url>
cd warehouse-management-mvp
Install Dependencies: Create a virtual environment and install the required libraries:
bash




python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install flask pandas plotly requests
Set Up Environment Variables:
Obtain a Together.ai API key from Together.ai.
Set the API key as an environment variable:
bash




export TOGETHER_API_KEY="your-api-key"  # On Windows: set TOGETHER_API_KEY=your-api-key
Add Chatbot Image:
Place your chatbot icon (e.g., chatbot-icon.png) in the static folder.
Ensure the image is 32x32 pixels or adjust the .chatbot-button img CSS in index.html if needed.
Alternatively, replace the <img> tag in index.html with an emoji:
html



<span class="text-2xl">🤖</span>
Prepare a CSV File:
The application expects a CSV with at least the following columns:
MSKU: Product identifier (string).
FNSKU: Fulfillment SKU (string).
Quantity: Numeric quantity (integer).
Example CSV (sample.csv):
csv



MSKU,FNSKU,Quantity
Widget_A,FNSKU001,10
Gadget_B,FNSKU002,7
Item_C,FNSKU003,8
Save the CSV in a convenient location for uploading.
Create Folders: Ensure the uploads and processed folders exist:
bash




mkdir uploads processed
Running the Application
Start the Flask Server:
bash




python app.py
The app will run on http://127.0.0.1:5000 by default (debug mode enabled).
Access the Web Interface:
Open a browser and navigate to http://127.0.0.1:5000.
You’ll see a dark-themed interface with a file upload section and chart selector.
Using the Application:
Upload CSV: Click "Choose File" to select a CSV, then click "Preprocess" to clean and display the data.
Generate Charts: Select a chart type (Bar, Line, Pie) and click "Generate Chart" to visualize Quantity by MSKU.
AI Chatbot: Click the floating chatbot button (bottom-left, with your image or 🤖 emoji) to open the chat modal. Ask questions like:
“Show MSKUs with quantity > 5” (includes a download link for filtered data).
“What is the total quantity?”
The chatbot responds in natural language, and filtered results can be downloaded as CSV.
File Details
app.py:
Flask application with routes:
/: Serves the index.html template.
/preprocess: Handles CSV uploads, cleans data, and returns an HTML table.
/dashboard: Generates Plotly charts (bar, line, pie) based on MSKU and Quantity.
/ask: Processes AI queries via Together.ai and returns responses.
/download/<filename>: Serves processed or filtered CSV files.
Stores the latest DataFrame in latest_df for chart and AI query use.
ai_query.py:
Integrates with the Together.ai API to answer questions about the uploaded data.
Handles specific queries (e.g., “Show MSKUs with quantity > X”) by filtering the DataFrame and generating a downloadable CSV.
Uses a sample of the data (head(20)) for general queries to stay within API limits.
preprocessing.py:
Cleans CSV data:
Strips column names.
Drops rows with missing MSKU or FNSKU.
Converts Quantity to numeric, setting negatives to 0 and NaN to 0.
Saves cleaned data to processed/cleaned_output.csv.
index.html:
Web interface with a black background and violet accents.
Features:
File upload form and preprocessed data table.
Chart selector for generating Plotly visualizations.
Floating chatbot button that opens a modal with a chat log and input.
Uses Tailwind CSS (via CDN) and custom CSS for styling.
JavaScript handles preprocessing, chart rendering, and AI queries with error handling.
Expected CSV Format
The CSV must include:

MSKU: Unique product identifier (string).
FNSKU: Fulfillment SKU (string).
Quantity: Product quantity (integer, negative values are set to 0 during preprocessing).
Example:

csv



MSKU,FNSKU,Quantity
Widget_A,FNSKU001,10
Gadget_B,FNSKU002,7
Item_C,FNSKU003,8
Troubleshooting
Chart Not Displaying:
Ensure the CSV has MSKU and Quantity columns.
Check the browser console (F12) for errors.
Verify Plotly is loaded (<script src="https://cdn.plot.ly/plotly-latest.min.js">).
AI Chatbot Errors:
Ensure the TOGETHER_API_KEY is set correctly.
Preprocess a CSV before asking questions, as the chatbot relies on latest_df.
If responses are incorrect, check the CSV data or rephrase the question.
Chatbot Image Not Showing:
Confirm the image is in the static folder and the path in index.html is correct (/static/chatbot-icon.png).
Use the emoji fallback (<span class="text-2xl">🤖</span>) if the image isn’t available.
Download Link Issues:
Ensure the processed folder exists and is writable.
Check that the /download route in app.py is serving files correctly.
Development Notes
Security: The eval in index.html for Plotly scripts is safe for trusted server responses but should be replaced with Plotly.newPlot for production.
Performance: For large CSVs, consider sampling data in ai_query.py to avoid API timeouts.
Deployment: For production, use a WSGI server (e.g., Gunicorn) and host static files on a CDN. Set debug=False in app.py.
Future Improvements
Add keyboard accessibility (e.g., close chat modal with Escape key).
Support more chart types or custom filters.
Implement user authentication for secure data uploads.
Optimize AI queries for larger datasets by filtering relevant rows before sending to the API.
License
This project is for educational purposes and not licensed for commercial use. Ensure compliance with Together.ai’s API terms.

Notes
Assumptions:
Project name: "Warehouse Management MVP."
Local development setup, no deployment instructions included (let me know if you need these).
CSV format based on code requirements (MSKU, FNSKU, Quantity).
Chatbot image is assumed to be in static/chatbot-icon.png; emoji fallback provided.
Dependencies extracted from code; no specific versions assumed (latest versions work as of June 2025).
Together.ai API Key: The README includes instructions to set the environment variable, as ai_query.py relies on it.
Chatbot Image: Instructions assume a custom image in the static folder. If you share the image or its specs, I can refine the CSS or instructions.
Execution: The README assumes users run the app locally with python app.py.