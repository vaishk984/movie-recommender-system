# 🎬 Movie Recommender System

A **Movie Recommender System** built using **Streamlit** and **Machine Learning**. This app suggests movies based on user preferences.

---

## 🚀 Features
- 📌 Movie recommendations based on similarity scores
- 🔍 Search for a movie and get similar suggestions
- 🌐 Deployed using **Render**

---

## 📂 Project Structure
```
📁 movie-recommender-system
├── 📄 app.py               # Streamlit app
├── 📄 requirements.txt     # Dependencies
├── 📄 movies_dict.pkl      # Movie data
├── 📄 similarity.pkl       # Precomputed similarity matrix
├── 📄 README.md            # Project documentation
```

---

## 🛠 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/vaishk984/movie-recommender-system.git
cd movie-recommender-system
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)
```sh
python -m venv .venv
source .venv/bin/activate  # For macOS/Linux
.venv\Scripts\activate     # For Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Download `similarity.pkl`
Since `similarity.pkl` is large, download it manually and place it in the project folder:

```python
import gdown
file_id = "14RoniihiPwk1BsIjyHaCTeYDwuoQn9OV"
gdown.download(f"https://drive.google.com/uc?id={file_id}", "similarity.pkl", quiet=False)
```

---

## ▶️ Running the App Locally
```sh
streamlit run app.py
```

This will launch the app in your browser.

## 📜 License
This project is open-source and available under the MIT License.

---

## 💡 Future Improvements
- 🎨 Improve UI
- 🎞️ Add movie posters
- 🚀 Optimize model for better recommendations

Feel free to contribute! 🎉

