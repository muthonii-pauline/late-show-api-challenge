from . import db

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    number = db.Column(db.Integer, nullable=False, unique=True)

    appearances = db.relationship(
        'Appearance',
        backref='episode',
        cascade='all, delete',
        lazy=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date.isoformat(),
            "number": self.number
        }
