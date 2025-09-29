# Omie API Data Pipeline

This project is a data pipeline built in **Python** for extracting, transforming, and loading (ETL) data from the **Omie API**.  
It is designed with modularity and scalability in mind, allowing you to integrate multiple data sources and manage business information more efficiently.

## ⚙️ Requirements

- Python 3.10+  
- Virtual environment (`venv` recommended)


## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/carloshenriquecarvalho/omie_api.git
   cd omie_api
Create and activate a virtual environment:

python -m venv .venv

source .venv/bin/activate   # Linux/Mac

.venv\Scripts\activate      # Windows

Install dependencies:

pip install -r requirements.txt

## 🔑 Environment Variables

Create a .env file in the project root with your API credentials:

OMIE_API_KEY=your_api_key_here
OMIE_API_SECRET=your_api_secret_here


## ⚠️Important:

Never commit your .env file to version control.

Use .env-example as a template.

## ▶️ Usage
Run the main script to execute the pipeline:

python src/main.py

You can also run specific modules (e.g., extract clients):

python src/extract/clients.py


## 🛠️ Features
Modular ETL pipeline (Extract, Transform, Load)

Integration with Omie API

Organized codebase with clear separation of concerns

Easy to extend with new endpoints or transformations

## 📌 Roadmap
 Add logging and error handling

 Implement database integration in the load/ module

 Write unit tests

 Add Docker support

## 📄 License
This project is licensed under the MIT License.
See the LICENSE file for more details.
