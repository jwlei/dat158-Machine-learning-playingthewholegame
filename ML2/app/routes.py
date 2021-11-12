from app import app
from flask import render_template, session, redirect, url_for, request
import pickle

from app.forms import DataForm
from app.predict import preprocess, predict, postprocess


app.config['SECRET_KEY'] = 'ML2'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():

    """
    We use flask to create a form based on forms.py, the user inputs data in all the fields
    We validate and pass run it through the pipeline and model, and predict. 
    """

    # Form request
    form = DataForm()
    if form.validate_on_submit():
    
        for fieldname, value in form.data.items():
            session[fieldname] = value

        data = preprocess(session)
        pred = predict(data)
        pred = postprocess(pred)

        session['pred'] = pred

        return redirect(url_for('index'))

    return render_template('index.html', form=form)
