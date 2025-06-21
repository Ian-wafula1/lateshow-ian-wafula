import csv
from app import db, Appearance, Guest, Episode, app
import random

def seed_database():
    with open('seed.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            guest = Guest(name=row['Raw_Guest_List'], occupation=row['GoogleKnowlege_Occupation'])
            episode = Episode(date=row['Show'], number=random.randint(1, 100))
            db.session.add_all([guest, episode])
            db.session.commit()
        
        
        for i in range(120):
            with db.session.no_autoflush:
                appearance = Appearance(rating=random.randint(1, 5))
                appearance.guest = random.choice(Guest.query.all())
                appearance.episode = random.choice(Episode.query.all())
                db.session.add(appearance)
                db.session.commit()
            
if __name__ == '__main__':
    with app.app_context():
        print('Clearing Database')
        Appearance.query.delete()
        Guest.query.delete()
        Episode.query.delete()
        
        print('Seeding Database')
        seed_database()
        db.session.commit()
        print('Database Seeded')