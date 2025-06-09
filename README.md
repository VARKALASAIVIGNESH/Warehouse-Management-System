
# 📦 Warehouse Management MVP

## 🧠 Overview
Warehouse Management MVP is a modern, AI-powered web app for analyzing inventory data. Users can upload CSV files, clean the data, visualize trends with interactive charts, and query insights using a built-in chatbot.

---

## 🚀 Features
- 📂 **CSV Upload & Preprocessing**: Clean data by removing empty rows, ensuring numeric quantities.
- 📊 **Interactive Charts**: Create bar, line, or pie charts showing Quantity by MSKU using Plotly.
- 🤖 **AI Chatbot**: Ask natural language questions like “Show MSKUs with quantity > 5” and download filtered results.
- 💅 **Modern UI**: Dark theme with violet accents, floating chatbot button, responsive layout.

---

## 🔧 Prerequisites
- Python 3.8 or higher
- Together.ai API Key (for chatbot)
- Any modern browser (Chrome, Firefox, Edge, etc.)

---

## 📦 Dependencies

Install required libraries:

```bash
pip install flask pandas plotly requests
````

---

## 📁 Project Structure

```
warehouse-management-mvp/
├── static/
│   └── chatbot-icon.png         # Optional: 32x32 chatbot image
├── templates/
│   └── index.html               # Frontend interface
├── uploads/                    # Stores uploaded CSVs
├── processed/                  # Stores cleaned/filtered CSVs
├── app.py                      # Main Flask app
├── ai_query.py                 # AI logic with Together.ai API
├── preprocessing.py            # CSV cleaning logic
└── README.md                   # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone ..........
cd warehouse-management-mvp
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate           # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install flask pandas plotly requests
```

### 4. Set Your API Key

```bash
export TOGETHER_API_KEY="your-api-key"       # Linux/macOS
set TOGETHER_API_KEY="your-api-key"          # Windows
```

### 5. Prepare Folders

```bash
mkdir uploads processed
```

### 6. Run the App

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📋 CSV Format

Required columns:

* **MSKU** (string)
* **FNSKU** (string)
* **Quantity** (integer)

Example:

```csv
MSKU,FNSKU,Quantity
Widget_A,FNSKU001,10
Gadget_B,FNSKU002,7
Item_C,FNSKU003,8
```

---

## 🧪 How to Use

1. Upload a CSV → Click **Preprocess**
2. View cleaned data table
3. Choose a chart type (Bar, Line, Pie) → Click **Generate Chart**
4. Click the 🤖 button → Ask:

   * “What is the total quantity?”
   * “Show MSKUs with quantity > 5”
5. Download CSV if shown in chatbot response

---

## 🛠️ Troubleshooting

* **Charts not showing?**

  * Make sure MSKU and Quantity columns exist
  * Check browser console (F12) for JS errors
  * Ensure Plotly script is loading properly

* **Chatbot not working?**

  * Set `TOGETHER_API_KEY`
  * Ensure a CSV has been uploaded and preprocessed

* **Image not loading?**

  * Verify `chatbot-icon.png` is in `/static/`
  * Or replace with an emoji: `<span class="text-2xl">🤖</span>`

---

## 📽️ Loom Video Instructions (Include in Your Repo!)

Record a Loom video (\~2–3 mins) covering:

1. **What you built**: Tech stack and logic (Flask, Plotly, Together.ai)
2. **How you built it**: Preprocessing + chatbot AI integration
3. **How to use it**: Upload, chart, chat, download
4. **Setup steps**: Virtualenv, API key, run `app.py`

---

## 🧠 Tech Stack

* **Flask** — Backend server
* **Pandas** — Data preprocessing
* **Plotly.js** — Interactive charting
* **Together.ai API** — AI chatbot
* **HTML + Tailwind CSS** — Frontend
* **JavaScript** — Client-side interaction

---

## 🚧 Future Improvements

* Save and retrieve past uploads
* User login support
* More advanced charting options
* Chat history and export
* Better error handling on frontend

---

## 🛡️ License

Educational purposes only. Ensure compliance with Together.ai terms for API use.

---

## ✨ Summary

Simple, fast, and AI-powered warehouse data analysis in one clean app. Upload a CSV, generate visual insights, and chat with your data — no code needed.

```

