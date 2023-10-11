# install libraries with following commands
# pip install uvicorn
# pip install scikit-learn==1.2.2
# pip install fastapi
# pip install pickle

import uvicorn
from fastapi import FastAPI
from data_cols import data_cols
import pickle


app = FastAPI()
pickle_in = open("model_tree.pkl","rb")
classifier = pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.post('/predict')
def predict_class(data: data_cols):
    data_dict = data.dict()
    features = [
        data_dict['Gender'],
        data_dict['Age'],
        data_dict['Height'],
        data_dict['Weight'],
        data_dict['family_history_with_overweight'],
        data_dict['FAVC'],
        data_dict['CAEC'],
        data_dict['SMOKE'],
        data_dict['CH2O'],
        data_dict['CALC'],
        data_dict['MTRANS']
    ]
    prediction = classifier.predict([features])

    if(prediction[0] == 1):
        prediction="Normal Weight"
    elif prediction[0] in (2, 4, 3, 6, 7):
        prediction = 'Overweight'
    else:
        prediction = 'Insufficient Weight'

    return {
        'prediction': prediction #.tolist()
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)



#terminal command : uvicorn app:app --reload

#acces api form :  http://127.0.0.1:8000/docs

# {
#   "Gender": 2,
#   "Age": 27,
#   "Height": 1.80,
#   "Weight": 87,
#   "family_history_with_overweight": 0,
#   "FAVC": 0,
#   "CAEC": 1,
#   "SMOKE": 0,
#   "CH2O": 2,
#   "CALC": 3,
#   "MTRANS": 2
# }
