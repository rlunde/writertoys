from .. import db


class Names(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    # Additional fields

    def __repr__(self):
        return 'Names {}>'.format(self.id)
