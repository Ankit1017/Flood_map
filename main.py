from flask import Flask, render_template, request,jsonify
import numpy as np
from model import mod

app=Flask(__name__)

@app.route('/home', methods=['POST','GET'])
def tdy():
    input=dict(request.form)
    us = input['loginName']
    ps =input['loginPassword']
    if(us=="disaster"  ):
        if(ps=="prd"):
            return render_template('index.html',user=100)
        else:
            return render_template("login.html",ar="Invalid Credentials")
        
    else:
        return render_template("login.html",ar="Invalid Credentials")
    
@app.route('/donation')
def donation():
    return render_template('donation.html')
@app.route('/home2')
def home2():
    return render_template('index.html',user=100)
@app.route('/')
def art():
    return render_template('login.html')

@app.route('/pred', methods=['POST','GET'])
def pred():
    input = dict(request.form)

    fin= input['tyt']
    ad=mod(int(fin))
    
    
    return render_template('index.html',user=ad)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=4000)
