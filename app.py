from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='SuperSecretKey'

class OrderForm(FlaskForm):
    colour = StringField('Colour of Cloth:', validators=[DataRequired()])
    type = StringField('Type of Cloth:', validators=[DataRequired()])
    size = StringField('Size of Cloth:', validators=[DataRequired()])

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Stem Clothing Kenya')

@app.route('/MakeOrder', methods=['GET', 'POST'])
def make_order():
    form = OrderForm()
    if form.validate_on_submit():
        return "<h2> Your order has been received for a {0} {1} {2}".format(form.colour.data, form.type.data, form.size.data)
    
    
    return render_template('MakeOrder.html', form=form, pageTitle='My Order')

if __name__ == '__main__':
    app.run(debug=True)