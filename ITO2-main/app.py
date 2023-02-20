import sqlite3
from flask import Flask , render_template, g
import Log, time
#import datetime



app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('/home/pi/Desktop/det hele/Sensordata.db')
      #  db = g._database = sqlite3.connect('Sensordata.db')

        cursor = db.cursor()
        cursor.execute("select * from Sensor_data")
        all_data = cursor.fetchall()
        db.close()
    return all_data


### Fixer "sqlite3.OperationalError: unable to open database file"
# conn=sqlite3.connect('../Sensordata.db')

# conn=sqlite3.connect("/home/pi/Desktop/det hele/Sensordata.db")
# curs=conn.cursor()
#####

# def getLastData():
# 	for row in curs.execute("SELECT * FROM Sensor_data ORDER BY timestamp DESC LIMIT 1"):
# 		time = str(row[0])
# 		butval = row[1]
# 		motion = row[2]
# 	conn.close()
# 	return time, butval, motion

	
@app.route("/")
def index():	
	buttonhtml = Log.getButtondata()
	motionhtml = Log.getMotiondata()
		
	return render_template('index.html',buttonhtml=buttonhtml,motionhtml=motionhtml)
		
@app.route("/forside")
def forside():
    data = get_db()
    print(data)
    return render_template("forside.html", all_data = data)

# if Log.getMotiondata is True:
@app.route("/db")
def tilbud():
	return render_template("test.html")

# if Log.getMotiondata and Log.getButtondata is True:
#     @app.route("/blank")
#     def blank():
#         return render_template("index.html")

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()



if __name__ == '__main__':
    app.run()           


