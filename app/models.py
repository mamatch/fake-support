########################################################
# File to handler different models used in in the app  #
########################################################

from . import db


class Scammer(db.Model):
    """
    A class to abstracts the scammer table
    """
    __tablename__ = "scammers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    test = "fuck"

    def __repr__(self):
        return f"<Scammer {self.name}>"
