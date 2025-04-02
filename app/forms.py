from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class MovieForm(FlaskForm):
    title=StringField("Title",validators=[InputRequired()])
    text=TextAreaField("Description",validators=[InputRequired()])
    image=FileField("Poster",validators=[FileRequired(),FileAllowed("png","jpeg"),"Only png and jpeg files are allowed!"])

    
