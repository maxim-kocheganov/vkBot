import sqlalchemy
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import desc

from sqlalchemy.orm import declarative_base

base = declarative_base()

class User(base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    secondName = sqlalchemy.Column(sqlalchemy.String)
    conferenceId = sqlalchemy.Column(sqlalchemy.Integer)
    vkId = sqlalchemy.Column(sqlalchemy.Integer)
    count = sqlalchemy.Column(sqlalchemy.Integer, default=1)
    #def __repr__(self):
        #return '<User(name="{}", fullname="{}")>'.format(self.name, self.vkId)

class Storage:
    engine = None
    session = None
    def __init__(self, debug = False):
        self.engine = sqlalchemy.create_engine("sqlite:///db.db", echo=debug)
        base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)()
    def getConferenceStat(self,conferenceId):
        q = self.session.query(User).filter_by(conferenceId=conferenceId).order_by(User.count.desc())
        res = []
        for user in q:
            res.append({"name": user.name + " " + user.secondName, "count":user.count})
        return res
    def raiseCountOnUser(self,conferenceId, userVkId, name, lastName):
        q = self.session.query(User).filter_by(conferenceId=conferenceId,vkId=userVkId)
        if (q.count() == 0):
            self.session.add(User(name=name, secondName=lastName, conferenceId=conferenceId, vkId=userVkId, count=1))
        else:
            q.first().count += 1
        self.session.commit()
