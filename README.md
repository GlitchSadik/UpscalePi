# UpscalePi
### 🚀 Project Overview
UpscalePi is a cutting-edge, privacy-first document Q&A assistant designed to unlock insights from your text-based knowledge—right on your local machine. Leveraging the powerful LLaMA 2 model running locally via Ollama, it delivers fast, accurate answers without compromising your data privacy.

### 🔍 How It Works
1. Smart Data Preparation
By default, the project scripts are set up to pull data from the [Twilio API](https://github.com/twilio/twilio-oai), but you’re free to customize this. Just tweak the load_docs.py script to load any documents or data sources you want download and work on as your knowledge base.

2. Semantic Embeddings & Fast Storage
When you ask a question, the bot converts it to an embedding, searches for the closest matches, and combines your query with this rich context. It then leverages the local Ollama API running LLaMA 2 to generate clear, accurate answers tailored to your data.

3. Intelligent Query & Response
User questions are converted into embeddings, matched with the closest document chunks, and combined to form an enriched prompt. This prompt is fed into the local LLaMA 2 model via Ollama to generate precise, context-aware answers.

### 🔧 Key Technologies

- LLaMA 2 via Ollama API: Fully local model inference ensures maximum privacy and control.

- Pinecone Vector DB: Industry-leading semantic search for ultra-responsive query handling.

- Modular Python Scripts: Clean, maintainable code handles everything from chunking to answering.

### 🌟 Coming Soon
A sleek, user-friendly web interface built with Streamlit or Gradio will be launched within 2 days — making it easier than ever to interact with your personal knowledge assistant right from your browser.

### 🚀 Future Enhancements
-LRU Cache System: To speed up repeated queries by caching recent results efficiently.
-Advanced Chunk Ranking: Implement smarter ranking algorithms to prioritize and manage the most relevant document chunks for improved answer accuracy and relevance.

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/GlitchSadik/UpscalePi.git
cd UpscalePi
```
### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```
### 3. Install Requirements
```bash
pip install -r UpscalePi/requirements.txt
```
### 4. Prepare Your .env File
Create a .env file in the root folder
```bash
touch .env
```
paste the following content in it and replace with your own credentials:
```bash
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=your_pinecone_env
PINECONE_INDEX_NAME=your_pinecone_index
```
### 5. Run All Scripts Automatically
Run the main script that will execute all required scripts in order:
```bash
cd UpscalePi
python main.py
```

# LLM Setup (Ollama with LLaMA 2)
This project uses a local LLaMA 2 model served via Ollama for natural language understanding and querying.

### ⚙️ Step 1: Install Ollama
If you haven’t already, install Ollama from the official website:

🔗 https://ollama.com

For macOS, you can also use:
```bash
brew install ollama
```
### 📦 Step 2: Pull the LLaMA 2 Model
Run the following command in your terminal:
```bash
ollama pull llama2
```

### 🚀 Step 3: Start the model before running any scripts in this project:
```bash
ollama run llama2
```
### ✅ Confirm It's Running
You can verify Ollama is active by visiting:
http://localhost:11434
If this opens, you're good to go!

# Issue: No module named 'pinecone'

![Screenshot 2025-05-27 at 3 36 08 AM](https://github.com/user-attachments/assets/e667f9e1-fade-4ab6-9e0b-e4ebf8682b03)

### Click on the python environment on bottom right corner

![Screenshot 2025-05-27 at 3 38 15 AM](https://github.com/user-attachments/assets/3c7a8a8b-47bb-474c-a5e8-73687a98b7b2)

### Click on create Virtual Environment

![Screenshot 2025-05-27 at 3 39 08 AM](https://github.com/user-attachments/assets/a169edff-fee5-4995-92d0-8308233bb106)

### Click on Venv 

![Screenshot 2025-05-27 at 3 40 55 AM](https://github.com/user-attachments/assets/2e028381-44bc-41a8-8d86-281693eaed48)

### Check the option and press OK!

![Screenshot 2025-05-27 at 3 43 29 AM](https://github.com/user-attachments/assets/8428fa8a-3cd0-4cc2-a589-6837e47ce878)

