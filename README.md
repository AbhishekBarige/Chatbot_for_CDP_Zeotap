
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
- **MongoDB**: Stores user queries and processed responses.  

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
- MongoDB instance (local or remote).  

### Steps  
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/shreyash0019/chat-bot-zeotap-assignment.git
   cd chat-bot-zeotap-assignmen
   ```

2. **Environment Setup**  
   Create a `.env` file in the root directory with the following:  
   ```env
   PORT=5000
   MONGO_URI=mongodb://localhost:27017/cdp-chatbot
   OPENAI_API_KEY=your_openai_api_key
   ELASTICSEARCH_URI=http://localhost:9200
   ```

3. **Install Dependencies**  
   ```bash
   cd client
   npm install
   cd ../server
   npm install
   ```

4. **Run the Application**  
   Start the backend:  
   ```bash
   npm start
   ```  
   Start the frontend:  
   ```bash
   npm run dev
   ```  

5. **Access the Application**  
   Open your browser and go to `http://localhost:5173`.  

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
cdp-support-agent-chatbot/
├── client/                 # Frontend code
│   ├── src/
│   │   ├── components/     # Chat interface and utility components
│   │   ├── pages/          # Main pages (Home, Chatbot, etc.)
│   │   ├── App.js          # Routes and app structure
│   └── package.json
├── server/                 # Backend code
│   ├── routes/             # API routes
│   ├── models/             # Database models
│   ├── controllers/        # Business logic
│   ├── app.js              # Express app setup
│   └── package.json
└── README.md
``
