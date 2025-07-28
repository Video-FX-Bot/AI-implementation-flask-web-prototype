# AI Implementation Flask/ FastAPI Web Prototype

This project is a temporary web-based frontend that connects with our Flask-based AI API backend. The goal is to **simulate and visualize the AI responses through a browser** before integrating everything into our final Flutter application.

---

## 🎯 Objective

- Build a minimal and working frontend using **HTML, CSS, and JavaScript**
- Connect it with the existing **Flask API backend**
- Make it demo-ready to **present to stakeholders and investors**
- Enable a smooth transition to **Flutter later**

---

## 👥 Team Responsibilities

### 🔹 1. Flask/Fast Backend (API Layer)

- Create endpoints like:
  - `GET /get-response`
  - `POST /user-query`
- Return JSON data (mocked or real from the AI engine)
- Ensure CORS is enabled for cross-origin calls
- Test APIs locally via Postman or browser

🗂️ File: `backend/app.py`

---

### 🔹 2. Web Frontend (UI Layer)
**Assigned To:** [Your Name / Team Member]

- Build the structure using `index.html`
- Apply styling using `style.css`
- Use `script.js` to:
  - Call Flask API using `fetch()`
  - Display response on the web page
  - Handle loading states, error messages, etc.

🗂️ Files: `frontend/index.html`, `frontend/style.css`, `frontend/script.js`

---

### 🔹 3. Integration Testing
**Everyone**

- Make sure API URLs match local server (`http://127.0.0.1:5100`)
- Validate if the frontend correctly displays backend data
- Check console logs for any fetch errors
- Debug together if something breaks

---

## 🧪 Project Structure

```

ai-flask-web-prototype/
├── backend/
│   └── app.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── requirements.txt
└── README.md

````

---

## 🛠 Getting Started

### 1. Start Flask Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r ../requirements.txt
python app.py
````

### 2. Run Frontend

Open `frontend/index.html` in your browser.
Make sure `script.js` points to the correct API endpoint (default: `http://127.0.0.1:5100`).


---

## 🧠 Notes

* Keep the code modular and clean
* Push your updates in separate commits
* Ping the team lead when your part is done

---

> Let’s work smart and fast to build a great AI prototype together. 💻🚀
