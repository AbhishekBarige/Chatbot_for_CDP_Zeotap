
# Support Agent Chatbot for CDP "How-to" Questions

## Overview  
This project involves developing a chatbot designed to answer "how-to" questions related to four major Customer Data Platforms (CDPs): Segment, mParticle, Lytics, and Zeotap. The chatbot utilizes the official documentation of these platforms to guide users in performing tasks or achieving specific outcomes.


### Data Sources:  
- **Segment Documentation**: [Segment Docs](https://segment.com/docs/?ref=nav)  
- **mParticle Documentation**: [mParticle Docs](https://docs.mparticle.com/)  
- **Lytics Documentation**: [Lytics Docs](https://docs.lytics.com/)  
- **Zeotap Documentation**: [Zeotap Docs](https://docs.zeotap.com/home/en-us/)
---

## Features  

### 1. Core Functionalities  
- **"How-to" Question Handling**:  
  The chatbot can understand and respond to queries about using features or performing tasks in the four CDPs.  
  Examples:  
  - "How do I set up a new source in Segment?"  
  - "How can I create a user profile in mParticle?"  

- **Documentation Retrieval**:  
  The chatbot retrieves relevant instructions or steps directly from the provided documentation links. It identifies sections that address the user's query and extracts relevant information.  

- **Variation Handling**:  
  Robust NLP or indexing ensures questions of varying lengths and phrasing are processed effectively.  
  Irrelevant queries (e.g., non-CDP-related questions) are identified and handled gracefully.  

### 2. Bonus Features  
- **Cross-CDP Comparisons**:  
  The chatbot can compare functionalities or approaches between Segment, mParticle, Lytics, and Zeotap.  
  Example: "How does Segment's audience creation process compare to Lytics'?"  

- **Advanced "How-to" Questions**:  
  Handles complex questions involving advanced configurations, integrations, or unique use cases.  

### 3. User Experience  
- Friendly and intuitive chatbot interaction with clear responses.  
- Provides detailed step-by-step instructions where applicable.  

---

## Tech Stack  

### Backend  
- **Node.js with Express.js**: Handles API requests and chatbot interactions.  
- **Flask**: lightweight Python web framework used for building web applications and APIs. 

### Frontend  
- **React.js**: Creates an interactive and responsive chatbot interface.  

### Natural Language Processing  
- **LangChain**: For advanced NLP processing and integration with documentation parsing.  
- **OpenAI GPT API**: Processes user queries and retrieves contextually relevant responses.  

### Documentation Parsing  
- **BeautifulSoup**: Scrapes and processes HTML-based documentation for query answers.  
- **Elasticsearch**: Indexes documentation for efficient retrieval.  

---

## Installation and Usage  

### Prerequisites  
- Node.js and npm/yarn installed.  
- Flask  

### Steps  
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/AbhishekBarige/Chatbot_for_CDP_Zeotap.git
   cd Chatbot_for_CDP_Zeotap 
   ```

2. **Environment Setup**  
   Create a `.env` file in the root directory with the following:  
   ```env
  
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
Run the Application:
   ```

4. **Run the Application**  
   Start the backend:  
   ```bash
   npm start
   ```  
   Start the frontend:  
   ```bash
   python run.py
  

   ```  

5. **Access the Application**  
   Access the Chatbot: Open your browser and navigate to http://127.0.0.1:5000.

---

## Testing  
Unit tests for chatbot functionality and API endpoints can be run with:  
```bash
npm test
```

---

## Security and Performance Enhancements  
- **Security**:  
  - Input sanitization to prevent XSS attacks.  
  - Secure API key storage using environment variables.  
- **Performance**:  
  - Cached document indexing for faster query responses.  
  - Rate limiting to prevent abuse.  

---

## Project Structure  

```
cdp-chatbot/
├── app/
│   ├── __init__.py         # App initialization
│   ├── chatbot.py          # Main chatbot logic
│   ├── cdps/
│   │   ├── segment.py      # Segment-specific query handling
│   │   ├── mparticle.py    # mParticle-specific query handling
│   │   ├── lytics.py       # Lytics-specific query handling
│   │   └── zeotap.py       # Zeotap-specific query handling
│   ├── templates/
│   │   └── index.html      # Frontend HTML for the chatbot
│   └── static/
│       └── style.css       # Styling for the chatbot
├── requirements.txt        # Python dependencies
├── run.py                  # Main entry point for the application
└── README.md               # Documentation
``
