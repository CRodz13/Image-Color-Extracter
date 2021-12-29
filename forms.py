from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.fields import FileField, SubmitField
from wtforms.validators import DataRequired


class ImageForm(FlaskForm):
    image = FileField("Image",
                      validators=[DataRequired(), FileRequired(), FileAllowed(['jpeg', 'jpg', 'png'], 'Images only!')])
    submit = SubmitField('Generate Colors')
