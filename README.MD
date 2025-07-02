
# 🌤️ Weather App

A beautiful, dynamic Django weather application that fetches real-time data using the OpenWeatherMap API and presents it with a responsive grid UI, custom background images, and weather icons.

---

## 🚀 Features

- 🌐 Real-time weather updates based on city name
- 🌈 Dynamic background changes with weather conditions
- 🌀 Weather icons from OpenWeatherMap
- 💡 Blurry glassmorphism UI design
- 📱 Fully responsive layout
- ✨ Smooth hover effects with animations

---

## 📸 Screenshot


```
media/demo.jpg
```

---

## 📁 Project Structure

```
WeatherApp/
├── media/                     # Contains background images (e.g. 01d.jpg)
│   └── 01d.jpg, 02n.jpg, ...
├── static/
│   └── home.css               # Main CSS styling
├── templates/
│   └── home.html              # Django HTML template
├── WeatherApp/
│   └── settings.py
├── views.py                   # Core weather fetching logic
├── .env                       # Environment file (API keys)
└── manage.py
```

---

## 🔧 Prerequisites

- Python 3.10 or later
- Django 5.2 or later
- An OpenWeatherMap API key (free)

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clonehttps://github.com/AvatanshuGupta/WeatherApp.git
cd weather-app
```

2. **Create a virtual environment**
```bash
python -m venv waenv
waenv\Scripts\activate      # For Windows
# Or
source waenv/bin/activate   # For Linux/macOS
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up `.env` file**
Create a `.env` file in the root directory and add:
```
WEATHER_API_KEY=your_openweathermap_api_key
```

5. **Run the Django development server**
```bash
python manage.py runserver
```




---

## 🧠 How It Works

- User enters a city.
- API request is made to OpenWeatherMap.
- Weather data is parsed and displayed.
- JavaScript dynamically changes the background image using the returned icon code.
- Weather info is shown in a styled grid with animations and hover effects.

---

## 📦 Requirements File

You can generate a requirements file using:
```bash
pip freeze > requirements.txt
```

Example entries:
```
Django>=5.2
python-dotenv>=1.0.0
requests>=2.30.0
```

---

## 📐 Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: CSS Grid, Flexbox, Blur Effects
- **API**: OpenWeatherMap

---


##  Acknowledgments

- [OpenWeatherMap API](https://openweathermap.org/api)
- [Django Framework](https://www.djangoproject.com/)
