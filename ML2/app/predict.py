import numpy as np
import pandas as pd
import joblib

model = joblib.load('models/predicted_house_price_model.joblib')
pipeline = joblib.load('models/pipeline.joblib')

def preprocess(data):
 
    """
    Default values for the features known to the machine learning model.
    Integers: Most frequent
    Objects: Most frequent
    Float: Median
    """
    
    feature_values = {
        
        'MSSubClass': 20,
        'MSZoning': "RL",
        'LotFrontage': 65.0,
        'LotArea': 7200,
        'Street': "Pave",
        'LotShape': "Reg",
        'LandContour': "Lvl",
        'Utilities': "AllPub",
        'LotConfig': "Inside",
        'LandSlope': "Gtl",
        'Neighborhood': "NAmes",
        'Condition1': "Norm",
        'Condition2': "Norm",
        'BldgType': "1Fam",
        'HouseStyle': "1Story",
        'OverallQual': 5,
        'OverallCond': 5,
        'YearBuilt': 2006,
        'YearRemodAdd': 1950,
        'RoofMatl': "CompShg",
        'RoofStyle': "Gable",
        'Exterior1st': "VinylSd",
        'Exterior2nd': "VinylSd",
        'MasVnrType': "None",
        'MasVnrArea': 196.0,
        'ExterQual': "TA",
        'ExterCond': "TA",
        'Foundation': "PConc",
        'BsmtQual': "TA",
        'BsmtCond': "TA",
        'BsmtExposure': "No",
        'BsmtFinType1': "Unf",
        'BsmtFinSF1': 0,
        'BsmtFinType2': "Unf",
        'BsmtFinSF2': 0,
        'BsmtUnfSF': 0,
        'TotalBsmtSF': 0,
        'Heating': "GasA",
        'HeatingQC': "Ex",
        'CentralAir': "Y",
        'Electrical': "SBrkr",
        '1stFlrSF': 864,
        '2ndFlrSF': 0,
        'LowQualFinSF': 0,
        'GrLivArea': 864,
        'BsmtFullBath': 0,
        'BsmtHalfBath': 0,
        'FullBath': 2,
        'HalfBath': 0,
        'BedroomAbvGr': 3,
        'KitchenAbvGr': 1,
        'KitchenQual': "TA",
        'TotRmsAbvGrd': 6,
        'Functional': "Typ",
        'Fireplaces': 0,
        'FireplaceQu': "None",
        'GarageType': "Attchd",
        'GarageYrBlt': 2003.0,
        'GarageFinish': "Unf",
        'GarageCars': 2,
        'GarageArea': 0,
        'GarageQual': "TA",
        'GarageCond': "TA",
        'PavedDrive': "Y",
        'WoodDeckSF': 0,
        'OpenPorchSF': 0,
        'EnclosedPorch': 0,
        '3SsnPorch': 0,
        'ScreenPorch': 0,
        'PoolArea': 0,
        'MiscVal' : 0,
        'MoSold': 6,
        'YrSold': 2009,
        'SaleType': "WD",
        'SaleCondition': "Normal"
    }

    # Takes input from the user submitted form and overwrites the default values specified above. 
    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]

    return feature_values


def predict(data): 
    # Store the data in an array with the same order as the data is formatted in. 
    # Removed attributes, Alley, PoolQC, Fence, MiscFeature
 
    column_order = ['MSSubClass',   'MSZoning',     'LotFrontage',  'LotArea',      'Street',  
                    'LotShape',     'LandContour',  'Utilities',    'LotConfig',    'LandSlope',    
                    'Neighborhood', 'Condition1',   'Condition2',   'BldgType',     'HouseStyle',   
                    'OverallQual',  'OverallCond',  'YearBuilt',    'YearRemodAdd', 'RoofStyle',    
                    'RoofMatl',     'Exterior1st',  'Exterior2nd',  'MasVnrType',   'MasVnrArea',   
                    'ExterQual',    'ExterCond',    'Foundation',   'BsmtQual',     'BsmtCond',     
                    'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1',   'BsmtFinType2', 'BsmtFinSF2',   
                    'BsmtUnfSF',    'TotalBsmtSF',  'Heating',      'HeatingQC',    'CentralAir',
                    'Electrical',   '1stFlrSF',     '2ndFlrSF',     'LowQualFinSF', 'GrLivArea',    
                    'BsmtFullBath', 'BsmtHalfBath', 'FullBath',     'HalfBath',     'BedroomAbvGr', 
                    'KitchenAbvGr', 'KitchenQual',  'TotRmsAbvGrd', 'Functional',   'Fireplaces',   
                    'FireplaceQu',  'GarageType',   'GarageYrBlt',  'GarageFinish', 'GarageCars',   
                    'GarageArea',   'GarageQual',   'GarageCond',   'PavedDrive',   'WoodDeckSF',   
                    'OpenPorchSF',  'EnclosedPorch','3SsnPorch',    'ScreenPorch',  'PoolArea',     
                    'MiscVal',      'MoSold',       'YrSold',       'SaleType',     'SaleCondition']
                    
    
    
    data = np.array([data[feature] for feature in column_order], dtype=object)
    data = data.reshape(1,-1)
    
    pdData = pd.DataFrame(data, columns = column_order)
    
    # We use the pipeline we created in the notebook
    preparedData = pipeline.transform(pdData)
    
    # We use the model we created in the notebook to predict the price based upon default values
    # combined with the values supplied by the end user. 
    pred = model.predict(preparedData)

    return pred


def postprocess(prediction):
    '''
    Basic validation of user input
    '''

    pred = prediction
    try: 
        int(pred[0]) > 0
    except:
        pass
        
    pred = str(pred[0])

    return_dict = {'pred': pred}
    return return_dict