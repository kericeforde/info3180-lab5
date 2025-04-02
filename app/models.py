from app import db


class Movie(db.Model):
    #Table name
    __tablename__= "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(255))
    poster =db.Column(db.String(80))
    created_at =db.Column(db.Datetime)

    def __init__(self, title,description,poster):
        self.title=title
        self.description=description
        self.poster=poster




