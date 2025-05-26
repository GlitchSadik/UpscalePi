# UpscalePi

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
#Create a .env file in the root folder with the following content and replace with your own credentials:
```bash
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=your_pinecone_env
PINECONE_INDEX_NAME=your_pinecone_index
```
### 5. Run All Scripts Automatically
#Run the main script that will execute all required scripts in order:
```bash
cd UpscalePi
python main.py
```
### Issue: No module named 'pinecone'

![Screenshot 2025-05-27 at 3 36 08 AM](https://github.com/user-attachments/assets/e667f9e1-fade-4ab6-9e0b-e4ebf8682b03)

### Click on the python environment on bottom right corner

![Screenshot 2025-05-27 at 3 38 15 AM](https://github.com/user-attachments/assets/3c7a8a8b-47bb-474c-a5e8-73687a98b7b2)

### Click on create Virtual Environment

![Screenshot 2025-05-27 at 3 39 08 AM](https://github.com/user-attachments/assets/a169edff-fee5-4995-92d0-8308233bb106)

### Click on Venv 

![Screenshot 2025-05-27 at 3 40 55 AM](https://github.com/user-attachments/assets/2e028381-44bc-41a8-8d86-281693eaed48)

### Check the option and press OK!

![Screenshot 2025-05-27 at 3 43 29 AM](https://github.com/user-attachments/assets/8428fa8a-3cd0-4cc2-a589-6837e47ce878)
