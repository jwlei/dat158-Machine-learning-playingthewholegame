from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):
    '''
    Name:            Correlation coeff:
    OverallQual      0.790982
    GrLivArea        0.708624
    GarageCars       0.640409
    GarageArea       0.623431
    TotalBsmtSF      0.613581
    
    # Not able to use           
    # 1stFlrSF       0.605852
    # Since python doesnt like an integer as first character of a variable.
    # We added GarageYrBlt instead.
    
    FullBath         0.560664
    TotRmsAbvGrd     0.533723
    YearBuilt        0.522897
    YearRemodAdd     0.507101
    GarageYrBlt      0.486362
    '''
    
    # 10 features with highest impact that we have chosen to use for this system.
    OverallQual     =   IntegerField('1. OverallQual: Rates the overall material and finish of the house', validators=[NumberRange(min=1, max=10)])
    GrLivArea       =   IntegerField('2. GrLivArea: Above grade (ground) living area square feet')
    GarageCars      =   IntegerField('3. GarageCars: Size of garage in car capacity')
    GarageArea      =   IntegerField('4. GarageArea: Size of garage in square feet')
    TotalBsmtSF     =   IntegerField('5. TotalBsmtSF: Total square feet of basement area')
   
   ## Would also have used 1stFloorSF, but python does not like integers as the first
    ## so for simplicity, we skip it.
    ## 1stFloorSF = IntegerField('1stFlrSF: First Floor square feet')
    
    FullBath        =   IntegerField('6. FullBath: Full bathrooms above grade')
    TotRmsAbvGrd    =   IntegerField('7. TotRmsAbvGrd: Total rooms above grade (does not include bathrooms)')
    YearBuilt       =   IntegerField('8. YearBuilt: Original construction date')
    YearRemodAdd    =   IntegerField('9. YearRemodAdd (same as construction date if no remodeling or additions)')
    GarageYrBlt     =   FloatField('10. GarageYrBlt: Year garage was built')
 
    submit = SubmitField('Submit')

pass
