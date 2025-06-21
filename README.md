# 🎬 Guest Appearances Tracker
## 📌 Overview

A Flask-based API for tracking guest appearances across various episodes, complete with ratings and occupation data.

## 🚀 Features

- **Episode Tracking**: Keep track of guest appearances across episodes.
- **Appearance Ratings**: Assign ratings to guest appearances.
- **Tracking of Guests**: Retrieve occupation data for guests.

## 🛠️ Setup Instructions

1. Clone the repository:
```bash
git clone git@github.com:Ian-wafula1/lateshow-ian-wafula.git
cd lateshow-ian-wafula
```

2. Create and activate a virtual environment

```bash
pipenv install
pipenv shell
```

3. Set up the database

```bash
cd server
flask db upgrade
```

4. Seed the database

```bash
python seed.py
```

5. Run the app

```bash
python app.py
```

## 🌐 API Endpoints

This API exposes the following routes:

- GET `/guests`: Retrieve a list of all guests.
- GET `/episodes`: Retrieve a list of all episodes.
- GET & DELETE `/episodes/{id}`: Retrieve a specific episode by ID or delete an episode by ID.
- POST `/appearances`: Create a new guest appearance.

## ✍️ Author

Ian Wafula
[GitHub](https://github.com/Ian-wafula1)
[email](mailto:ianwafula110@gmail.com)

## 📧 Support

If you have any questions or need further assistance, please don't hesitate to [contact me](mailto:ianwafula110@gmail.com) or raise an issue on [GitHub](https://github.com/Ian-wafula1/lateshow-ian-wafula/issues).

## ⚖️ License

This project is for educational purposes only. All rights reserved by the author.

## 🎉 Acknowledgements

- The chapati lady near our place (I love you 🤧🤧🤧)
- Chickens - for being so delicious 🤤
- Marvel Rivals - Best game out there 😎