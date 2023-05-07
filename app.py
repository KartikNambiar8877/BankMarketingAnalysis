from flask import Flask, request ,render_template
import pickle
import numpy as np
app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
model_1 =pickle.load(open('model_1.pkl','rb'))
model_2 =pickle.load(open('model_2.pkl','rb'))
model_3 =pickle.load(open('model_3.pkl','rb'))
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    h=float(request.form['h'])
    i=int(request.form['i'])
    j=float(request.form['j'])
    k=0
    l=0
    m=0
    n=0
    o=0
    p=0
    q=0
    r=0
    s=0
    t=0
    u=0
    v=0
    w=0
    x=0
    y=0
    z=int(request.form['i'])
    a1=0
    a2=0
    a3=0
    input_data = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,a1,a2,a3]
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    prediction_1 = model_1.predict(input_data)
    prediction_2 = model_2.predict(input_data)
    prediction_3 = model_3.predict(input_data)
    total_prediction= prediction+prediction_1+prediction_2+prediction_3
    print(total_prediction)
    if total_prediction>=2:
        return render_template('yes.html')
    return render_template('no.html')
if __name__ == '__main__':
    app.run(host='26.144.125.240',port=5000, debug=True)
