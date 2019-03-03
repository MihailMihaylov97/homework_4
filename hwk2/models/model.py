from extensions import db


class StudentModel(db.Model):

    id_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class CourseModel(db.Model):

    id_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class EventModel(db.Model):

    id_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()