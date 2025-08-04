# nSIMON 📚

Hi! I am a highschool student in year 11 in Melbourne, Australia. Our school recently updated their online portal called SIMON, and pretty much everyone has complained about it due to its lack of features compared to our old one, as well as its appearance. Because of this, I decided to create my own version of it, utilising their APIs.
![alt text](https://i.imgur.com/VcDxYZi.png "Logo Title Text 1")

## Features

- **Timetable**: Ability to view your timetable for the day, including room numbers, teachers, as well as substitute teacher lesson plans.
- **Daily Messages**: Ability to view daily messages posted by teachers, showing which messages are new.
- **Daily Messages Settings**: Ability to disable the viewing of MUSIC/SPORT/CANTEEN daily messages if you chose to.
- **Class Resources**: Ability to view Due, Overdue, and Results for class tasks.
- **Quick Links**: Ability to quickly access school related links on the dashboard in one click.
- **Weather**: Ability to view weather, such as current temp, conditions, UV, max temp, and min temp.
- **Share Timetable**: Ability to create a link to share your timetable with other users.
- **Database**: Uses a MongoDB database to store user information such as their cookie and username to easily access without creating a selenium web browser to login and get the cookie again.

### Planned Features

- **Download Timetable**: Ability to download a printable copy of your timetable.
- **Class View**: Ability to view information about classes, and the ability to set notes and reminders.
- **Customisation**: Ability to completely customise the theme and layout of the dashboard.
- **Student Dashboard**: Ability to view info about yourself including assessment reports, attendence, commendations, etc.

## Installation

If you know that your school uses SIMON, you are able to set this up for yourself, however no guarantees that it will work as it isn't really possible for me to test it! :)

### Prerequisites

- Python 3.8 or higher
- MongoDB instance (local or cloud)
- Chrome browser (for Selenium automation for logins)

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/Catch-c/nsimon.git
   cd nsimon
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **.ENV**
   Create a `.env` file in the root directory:

   ```env
   FLASK_SECRET=your-flask-secret-key
   SIMON_LINK=https://simon.sfx.vic.edu.au
   MONGO_DB_URI=mongodb://localhost:27017/
   APP_VERSION=1.0.0
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

   The application will be available at `http://localhost:8080`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Issues & Support

If you encounter any issues or have questions, please [open an issue](https://github.com/Catch-c/nsimon/issues) on GitHub.

---

Made with ❤️ for students at SFX :)
