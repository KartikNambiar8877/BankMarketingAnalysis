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
    a=float(request.form['a'])
    b=float(request.form['b'])
    c=int(request.form['c'])
    d=float(request.form['d'])
    e=int(request.form['e'])
    f=int(request.form['f'])
    g=int(request.form['g'])
    h=float(request.form['h'])
    i=int(request.form['i'])
    j=float(request.form['j'])
    k=int(request.form['k'])
    l=int(request.form['l'])
    m=int(request.form['m'])
    n=int(request.form['n'])
    o=int(request.form['o'])
    p=int(request.form['p'])
    q=int(request.form['q'])
    r=int(request.form['r'])
    s=int(request.form['s'])
    t=int(request.form['t'])
    u=int(request.form['u'])
    v=int(request.form['v'])
    w=int(request.form['w'])
    x=int(request.form['x'])
    y=int(request.form['y'])
    z=int(request.form['z'])
    a1=int(request.form['a1'])
    a2=int(request.form['a2'])
    a3=int(request.form['a3'])
    input_data = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,a1,a2,a3]
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    prediction_1 = model_1.predict(input_data)
    prediction_2 = model_2.predict(input_data)
    prediction_3 = model_3.predict(input_data)
    print(prediction,prediction_1,prediction_2,prediction_3)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(port=5000, debug=True)
