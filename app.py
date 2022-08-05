#!/usr/bin/python3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xvfD4bDDxswy@127.0.0.1:5432/stepn-tracker-db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Record(db.Model):
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    name = db.Column(db.String(), nullable=False)
    symbol = db.Column(db.String(), nullable=False)
    price = db.Column(db.Float(), nullable=False)

#create if they dont exist
db.create_all()

@app.route('/')
def index():
    return render_template('index.html', \
    data_sol = Record.query.filter_by(symbol='SOL').order_by(db.desc(Record.id)).first(),\
    data_gmt = Record.query.filter_by(symbol='GMT').order_by(db.desc(Record.id)).first(), \
    data_gst = Record.query.filter_by(symbol='GST').order_by(db.desc(Record.id)).first())

if __name__ == '__main__':
  app.run(host='0.0.0.0')
