from server.app import create_app
from server.models import db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

app = create_app()
app.app_context().push()

db.drop_all()
db.create_all()

# Users
u1 = User(username="admin")
u1.set_password("admin123")

# Guests
g1 = Guest(name="Taylor Swift", occupation="Musician")
g2 = Guest(name="Elon Musk", occupation="Entrepreneur")
g3 = Guest(name="Zendaya", occupation="Actress")
g4 = Guest(name="Trevor Noah", occupation="Comedian")

# Episodes
e1 = Episode(date="2025-01-01", number=101)
e2 = Episode(date="2025-01-02", number=102)
e3 = Episode(date="2025-01-03", number=103)

# Appearances
a1 = Appearance(rating=5, guest=g1, episode=e1)
a2 = Appearance(rating=4, guest=g2, episode=e1)
a3 = Appearance(rating=3, guest=g3, episode=e2)
a4 = Appearance(rating=2, guest=g4, episode=e3)
a5 = Appearance(rating=5, guest=g1, episode=e3)

# Save to DB
db.session.add_all([u1, g1, g2, g3, g4, e1, e2, e3, a1, a2, a3, a4, a5])
db.session.commit()

print("✅ Database seeded successfully.")
