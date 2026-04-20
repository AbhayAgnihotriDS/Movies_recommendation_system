# 🎬 Movie Recommendation System

A modern **AI-powered Movie Recommendation Web App** built using **Flask**, featuring a sleek UI, real-time search suggestions, and dynamic movie poster fetching using the OMDb API.

---

## 🚀 Features

* 🔍 **Smart Movie Search** (Netflix-style dropdown suggestions)
* 🎯 **Content-Based Recommendation System**
* 🖼️ **Dynamic Movie Posters (OMDb API)**
* ⚡ **Fast & Lightweight Flask Backend**
* 🎨 **Modern Responsive UI (HTML + CSS + JS)**
* ❌ **Error Handling for Invalid Inputs**
* 🌐 **Deployment Ready (Render / Cloud Platforms)**

---

## 🧠 How It Works

This project uses a **Content-Based Filtering Algorithm**:

* Movies are vectorized based on features (like genres, keywords, etc.)
* A **similarity matrix** is computed
* When a user selects a movie:

  * The system finds similar movies
  * Displays top recommendations with posters

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask
* Pandas
* Pickle

### Frontend

* HTML
* CSS (Modern UI + Animations)
* JavaScript (Live Search Dropdown)

### API

* OMDb API (for movie posters)

---

## 📁 Project Structure

```
📦 Movie-Recommender
 ┣ 📂 templates
 ┃ ┗ 📄 index.html
 ┣ 📄 app.py
 ┣ 📄 movies.pkl
 ┣ 📄 similarity.pkl
 ┣ 📄 requirements.txt
 ┣ 📄 .env
 ┗ 📄 README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API Key

Create a `.env` file:

```
OMDB_API_KEY=your_api_key_here
```

Get your API key from OMDb.

---

### 5. Run the App

```bash
python app.py
```

Open in browser:

```
[http://127.0.0.1:5000/](https://movies-recommendation-system-mqm4.onrender.com/)
```

---

## 📸 Screenshots

* 🔎 Search with dropdown suggestions
* 🎬 Recommended movies with posters
* 💻 Clean modern UI

  

---

## 🌐 Deployment

This project is ready to deploy on:

* Render
* Railway
* AWS (Advanced)

---

## 💡 Future Improvements

* ⭐ Add movie ratings & reviews
* 🎥 Trailer integration (YouTube API)
* 🤖 Hybrid recommendation system (Collaborative + Content-based)
* 📱 Mobile-first UI optimization

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit pull requests.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Developed by **Abhay Agnihotri**

---

⭐ If you like this project, give it a star on GitHub!
