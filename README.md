# GST FAQ Chatbot

A conversational AI assistant that helps users find answers to their GST (Goods and Services Tax) related questions.

## Project Structure

```
├── data/                   # Data files
│   ├── raw/               # Original, immutable data
│   ├── processed/         # Processed data
│   └── README.md          # Data documentation
├── src/                   # Source code
│   ├── ingest.py          # Document ingestion logic
│   ├── llm_interface.py   # LLM communication
│   └── app.py             # Streamlit application
├── .gitignore             # Git ignore file
└── requirements.txt       # Python dependencies
```

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd gst-faq-chatbot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\\venv\\Scripts\activate  # On Windows
   source venv/bin/activate    # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run src/app.py
   ```

2. Open your browser and navigate to `http://localhost:8501`

## Development Roadmap

### Phase 1: Setup & Basic Functionality
- [x] Project structure setup
- [x] Basic Streamlit UI
- [x] LLM interface skeleton
- [ ] Document ingestion pipeline

### Phase 2: Core Features
- [ ] PDF processing
- [ ] Vector database integration
- [ ] Advanced search capabilities
- [ ] User authentication

### Phase 3: Enhancements
- [ ] Multi-language support
- [ ] Analytics dashboard
- [ ] API endpoints

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
