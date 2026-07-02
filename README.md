# 🏨 AI-Powered Hotel Recommendation Chatbot

An intelligent hotel recommendation chatbot built with **Django**, **Python**, **spaCy**, and **Scikit-learn**. The chatbot understands natural language queries and recommends hotels based on user preferences such as location, price range, star rating, and hotel name through a conversational interface.

## 🌐 Live Demo

https://ai-assistant-chatbot-2cb0.onrender.com

---

## ✨ Features

- 🤖 NLP-based intent recognition using **spaCy**
- 🧠 Machine learning intent classification using **Scikit-learn (SVM)**
- 🏨 Search hotels by:
  - Area
  - Price range
  - Star rating
  - Hotel name
- 💬 Multi-turn conversational interaction
- 🗄️ SQLite database integration for hotel information
- 📱 Responsive web interface
- ⚡ Real-time chatbot responses

---

## 🛠️ Tech Stack

### Backend
- Python
- Django

### Machine Learning & NLP
- spaCy
- Scikit-learn (SVM)
- Joblib

### Database
- SQLite

### Frontend
- HTML
- CSS
- JavaScript

### Deployment
- Render

---

## 📂 Project Structure

```
ai_assistant_chatbot/
│
├── chatbot/
│   ├── ml/
│   ├── static/
│   ├── templates/
│   ├── views.py
│   └── chatbot_engine.py
│
├── config/
├── data/
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/amankr72/ai_assistant_chatbot.git
```

### Navigate to the project

```bash
cd ai_assistant_chatbot
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 💬 Example Queries

- Find a cheap hotel in south
- Find a 3-star hotel
- Find Lake Resort
- I want a luxury hotel
- Show me hotels in the north
- Recommend a budget hotel

---

## 🧠 Machine Learning Workflow

1. User enters a message.
2. spaCy processes the input text.
3. The trained SVM model predicts the user's intent.
4. Relevant hotel information is retrieved from the SQLite database.
5. The chatbot returns a conversational response.

---

## 📸 Screenshots

Add screenshots of your chatbot here.

Example:

```
screenshots/homepage.png
screenshots/chat.png
```

---

## 📦 Requirements

- Python 3.12+
- Django
- spaCy
- Scikit-learn
- NumPy
- Pandas
- Joblib

---

## 🔮 Future Improvements

- Hotel images
- Google Maps integration
- User authentication
- Hotel booking functionality
- Voice-based interaction
- Conversation history
- Additional hotel filters
- API integration

---

## 👨‍💻 Author

**Aman Kumar**

GitHub: https://github.com/amankr72

LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
