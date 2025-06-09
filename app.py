from flask import Flask, render_template, request, send_file, jsonify
import os
import pandas as pd
from preprocessing import clean_and_map
from ai_query import ask_question
import plotly.express as px

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

latest_df = None

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/preprocess', methods=['POST'])
def preprocess():
    global latest_df
    if 'csvfile' not in request.files:
        return "No file part", 400
    file = request.files['csvfile']
    if file.filename == '':
        return "No selected file", 400
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    df, cleaned_path = clean_and_map(filepath)
    latest_df = df
    return f"<p><b>Preprocessing Completed!</b></p>" + df.head(20).to_html(classes='table table-striped', index=False)

@app.route('/ask', methods=['POST'])
def ask():
    global latest_df
    if latest_df is None:
        return jsonify({"response": "Please preprocess a file first."})
    data = request.get_json()
    question = data.get("question")
    if not question:
        return jsonify({"response": "Question is required."})

    try:
        # Pass the DataFrame directly (fix)
        response = ask_question(latest_df, question)
    except Exception as e:
        response = f"❌ AI Error: {e}"
    return jsonify({"response": response})

@app.route('/dashboard', methods=['POST'])
def dashboard():
    global latest_df
    if latest_df is None:
        return "Please preprocess data first.", 400

    chart_type = request.json.get("type")

    # Check for required columns
    if 'MSKU' not in latest_df.columns or 'Quantity' not in latest_df.columns:
        return "Required columns MSKU and Quantity not found in the uploaded data.", 400

    # Ensure data is not empty
    data_grouped = latest_df.groupby("MSKU")["Quantity"].sum().reset_index()
    if data_grouped.empty:
        return "No data available to generate the chart.", 400

    try:
        if chart_type == "bar":
            fig = px.bar(data_grouped, x="MSKU", y="Quantity", title="Quantity by MSKU")
        elif chart_type == "line":
            fig = px.line(data_grouped, x="MSKU", y="Quantity", title="Quantity by MSKU")
        elif chart_type == "pie":
            fig = px.pie(data_grouped, names="MSKU", values="Quantity", title="Quantity by MSKU")
        else:
            return "Invalid chart type.", 400

        # Ensure Plotly renders correctly
        fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
        return fig.to_html(full_html=False, include_plotlyjs=False)  # Exclude Plotly.js since it's already loaded
    except Exception as e:
        print(f"Chart generation error: {e}")
        return f"Error generating chart: {e}", 500



@app.route('/download/<filename>')
def download(filename):
    try:
        return send_file(os.path.join(PROCESSED_FOLDER, filename), as_attachment=True)
    except FileNotFoundError:
        return "File not found.", 404
    
if __name__ == '__main__':
    app.run(debug=True)
