# API Magic  

Welcome to **API Magic**! This repository showcases a variety of projects demonstrating the use of APIs to automate tasks, gather data, and perform creative functions. Each project highlights the versatility of Python and third-party APIs in solving practical problems.  

---

## Projects  

### 1. **FableFrog-AI**
This project brings storytelling to life by using AI to create interactive and engaging stories tailored for children. It integrates a text-to-speech feature for audio narration, making it an immersive experience.  

#### Project Details:
- **Description**: A fun storytelling application powered by AI for generating creative tales.
- **Features**:
  - Generates interactive stories based on user input.
  - Narrates stories using realistic text-to-speech technology.
  - Includes various genres to keep storytelling fun and engaging.
- **Tools Used**:
  - **OpenAI API**: For AI-driven story creation.
  - **ElevenLabs API**: For natural-sounding audio narration.
  - **Gradio**: For user-friendly web interfaces.
- **File(s)**:
  - `openai_chat_stream.py` - Manages the storytelling workflow.
  - `Text_to_Speech.py` - Handles text-to-speech conversion.


### 2. **Flight Deals Tracker**  
This project automates tracking flight prices and notifies users when deals are found. It fetches flight data from the Amadeus API, stores it in Google Sheets via Sheety, and uses Twilio and SMTP to send notifications to users.

#### Project Details:
- **Description**: Automates flight deal tracking and sends notifications when prices drop.
- **Features**:
  - Fetches flight data from the Amadeus API.
  - Sends notifications via Twilio and email (using SMTP) when prices drop below user-defined thresholds.
  - Manages user and pricing data with the Sheety API.
- **Tools Used**:
  - **Amadeus API**: For flight search data.
  - **Twilio**: For sending SMS notifications.
  - **SMTP**: For sending email notifications.
  - **Sheety API**: For managing Google Sheets data.
- **File(s)**:
  - `main.py` - Orchestrates the logic for tracking and notifying users.
  - `flight_search.py` - Handles flight search operations via the Amadeus API.
  - `flight_data.py` - Parses flight data to find the cheapest flights.
  - `notification_manager.py` - Manages SMS and email notifications using Twilio and SMTP.
  - `data_manager.py` - Manages Google Sheets data with Sheety.


### 3. **Habit Tracker**  
This project helps users track their daily habits by integrating with the Pixela API to log and visualize activities like study hours.

#### Project Details:
- **Description**: A habit tracker that allows users to log their daily activities and track progress.
- **Features**:
  - Tracks habit progress by logging data (e.g., hours studied) using the Pixela API.
  - Allows for updating and deleting habit entries for past and future dates.
  - Visualizes progress in a graph format.
- **Tools Used**:
  - **Pixela API**: For creating and managing user graphs and logging data.
- **File(s)**:
  - `main.py` - Handles the creation, updating, and deletion of habit logs using the Pixela API.


### 4. **ISS Overhead Alert**
This project sends an email notification when the International Space Station (ISS) is overhead at your location during the night.

#### Project Details:
- **Description**: Alerts you when the ISS is visible overhead during the night.
- **Features**:
  - Checks the position of the ISS using the **ISS API** and compares it with your location.
  - Verifies if it's night at your location using the **Sunrise-Sunset API**.
  - Sends an email notification when the ISS is overhead.
- **Tools Used**:
  - **ISS API**: For retrieving real-time ISS location data.
  - **Sunrise-Sunset API**: For checking daylight conditions.
  - **SMTP**: For sending email notifications.
- **File(s)**:
  - `main.py` - Contains the logic for checking the ISS location and sending email alerts.


### 5. **Kanye Quotes Generator**
This project fetches random quotes from Kanye West using the **Kanye Rest API** and displays them in a graphical interface built with **Tkinter**.

#### Project Details:
- **Description**: A simple application that generates and displays random Kanye West quotes.
- **Features**:
  - Fetches random quotes from the **Kanye Rest API**.
  - Displays quotes in a graphical interface built with **Tkinter**.
  - Includes a button to fetch new quotes.
- **Tools Used**:
  - **Kanye Rest API**: For retrieving Kanye West quotes.
  - **Tkinter**: For building the graphical user interface.
- **File(s)**:
  - `main.py` - Contains the logic for fetching and displaying Kanye's quotes.
  - `kanye.png` - Image used in the interface for the button.
  - `background.png` - Background image for the graphical interface.


### 6. **Rain Alert**  
This project sends a notification via **Twilio** if it’s going to rain in the user's location based on the forecast from the **OpenWeatherMap API**.

#### Project Details:
- **Description**: Checks weather forecasts to determine if it will rain, and sends a reminder message.
- **Features**:
  - Fetches weather forecast data using the **OpenWeatherMap API**.
  - Sends SMS notifications via **Twilio** if rain is expected.
- **Tools Used**:
  - **OpenWeatherMap API**: For fetching weather forecast data.
  - **Twilio**: For sending SMS notifications.
- **File(s)**:
  - `main.py` - Contains the logic for checking the weather and sending rain alerts.
 

### 7. **Stock News Tracker**  
This project monitors **Tesla Inc.'s (TSLA)** stock price and sends SMS notifications with related news articles when significant price fluctuations occur.

#### Project Details:
- **Description**: Monitors Tesla's stock price and sends SMS alerts with the latest news articles when price changes exceed a set threshold.
- **Features**:
  - Tracks Tesla's stock price using the **Alpha Vantage API**.
  - Fetches the latest news related to Tesla using the **News API**.
  - Sends notifications via **Twilio** when Tesla's stock price changes exceed 3%.
- **Tools Used**:
  - **Alpha Vantage API**: For tracking Tesla's stock price changes.
  - **News API**: For retrieving news articles related to Tesla.
  - **Twilio**: For sending SMS notifications.
- **File(s)**:
  - `main.py` - Contains the logic for tracking Tesla's stock price changes and sending news notifications.
  
 
### 8. **Workout Tracker**  
This project logs workout and nutrition data, integrating with the **Nutritionix API** for exercise information and the **Sheety API** for data storage in Google Sheets.

#### Project Details:
- **Description**: Logs workout and nutrition details, providing insights into fitness progress by storing the data in Google Sheets.
- **Features**:
  - Logs workouts using the **Nutritionix API**.
  - Stores and retrieves workout data with the **Sheety API**.
  - Provides summaries and tracking of progress.
- **Tools Used**:
  - **Nutritionix API**: For logging and retrieving exercise data.
  - **Sheety API**: For managing and storing data in Google Sheets.
- **File(s)**:
  - `main.py` - Contains logic for logging workouts, retrieving nutrition info, and storing data with Sheety.
 
---
