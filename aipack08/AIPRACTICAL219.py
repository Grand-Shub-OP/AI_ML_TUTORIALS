# Save and Load AI/ML Learning Models : (2 Methods)
#-----------------------------------------------------------
#This allows you to save your model to file and load it later
# in order to make predictions in future.

#Method-1) Use pickle to serialize(=dump) and deserialize(=load)
#          machine learning models.

#Method-2) Use Joblib to serialize(=dump) and deserialize(=load)
#          machine learning models.

# Save Model Using Pickle
import warnings
warnings.filterwarnings(action='ignore')

import pandas  as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

filename = 'indians-diabetes.data.csv'
hnames=['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
seed = 7
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=seed)
#  1       2        3       4
model = LogisticRegression()
model.fit(X_train, Y_train)   # Fit the model on 67% data,  This step calculates m, c
#            1       3

# save the model to disk
filename =  "finalized_model.sav"
pickle.dump(model, open(filename,  "wb" ))

print( "Model dumped successfully into a file by Pickle....\n...\n...\n...")

print("-----------------------\n\n\n")
print("some time later...  ")
print("\n\n\n-----------------------")

# load the model from disk
import pickle
filename =  "finalized_model.sav"
loaded_model = pickle.load(  open(filename,  "rb" ) )
print( "Model loaded successfully from file by Pickle")

result = loaded_model.score(X_test, Y_test)
print( "Accuracy Result : " , result)