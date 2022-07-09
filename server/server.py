import predict 
import json
import sys
from typing_extensions import Required
from flask import Flask, jsonify, request
import csv
from flask_cors import CORS
app = Flask(__name__)
CORS(app ,resources={
    r"/*":{
        "origins":"*"
    }
})

@app.route('/post', methods=[ 'GET','POST'])

def post():
#save data to db
 data = request.get_json()
 name=data['name']
 age=data['age']
 gender=data['gender']
 answer=data['answer']
 user=data['user']
 time=data['time']

 fields=['Name','Age','Gender','Answer','User','Time']
 rows = [[name,age,gender,answer,user,time]]  

 filename = "datafile1.csv"
  
# writing to csv file
 with open(filename, 'a') as csvfile:
    # creating a csv writer object
     csvwriter = csv.writer(csvfile)
     
    # writing the fields
     #csvwriter.writerow(fields)
     
    # writing the data rows
     csvwriter.writerows(rows)
 return jsonify(predict.pretym);

# n=predict.pretym;
# print (n)

# sys.stdout=open('declare.js','w')
# jsonobj = json.dumps(n) 
# print("var jsonstr='{}' ".format(jsonobj))

if __name__ == "__main__":
    app.run(debug=True)
