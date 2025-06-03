# 🤖 Oracle AI Assistant — Multi-Tool Smart Chatbot

Oracle is a smart AI chatbot built using **LangChain**, **Groq’s LLaMA3**, and **Streamlit**. It intelligently analyzes your query and selects the best tool to answer it: weather reporting, fact-checking via Wikipedia, or just general chit-chat.

---

## 📦 Features

- ✅ **Tool Selection with LangChain**: Uses LangChain’s `bind_tools` for automatic routing.
- 🌦️ **Weather Analysis Tool**: Parses time-sensitive weather queries and gives news-style summaries.
- 📚 **Wikipedia Fact Search**: Returns reliable facts from Wikipedia.
- 💬 **General Chat Handler**: Handles casual and general discussions.
- 🧠 **Oracle Decision Engine**: Decides which tool to use based on your input.
- 🖥️ **Streamlit Interface**: Clean and simple front-end for interaction.

---

## 📁 Project Structure

```
oracle_chatbot/
├── app.py               # Main Streamlit application
├── .env                 # Your API key configuration
└── README.md            # This documentation
```

---

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/oracle-chatbot.git
   cd oracle-chatbot
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your Groq API key to a `.env` file**:
   ```env
   Groq_Api=your_groq_api_key_here
   ```

---

## 🚀 How to Run

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. The user enters a query in the Streamlit app.
2. The **Oracle** function decides which tool to use:
   - `weather_details` → For weather-based questions
   - `Fact_search` → For factual/wikipedia-type inquiries
   - `General_topics` → For regular conversational queries
3. The chosen tool is executed.
4. A summary is generated and returned to the user through Streamlit.

---

## 🛠️ Built With

- [LangChain](https://www.langchain.com/)
- [Groq LLaMA3](https://groq.com/)
- [Streamlit](https://streamlit.io/)
- [Wikipedia API Wrapper](https://python.langchain.com/docs/integrations/tools/wikipedia/)

---

## 💬 Example Queries

- "What's the weather like in Bangalore tomorrow at noon?"
- "Tell me the history of the Taj Mahal."
- "Hey! How are you doing today?"

---

## 🔮 Future Improvements

- Voice input and text-to-speech output
- Support for multi-turn conversations (memory)
- Integration with real-time weather APIs (e.g., OpenWeatherMap)
- Logging and analytics dashboard

---

