import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def plot_bar_x(label,class_training,title,xlabel,ylabel):
    index = np.arange(len(label))
    plt.bar(index, class_training)
    plt.xlabel(xlabel, fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
    plt.xticks(index, label, fontsize=10, rotation=15)
    plt.title(title)
    plt.show()
video=pd.read_csv('IP data.csv')
size=video.shape
print(size)
target=video['target']
cols_to_drop=['Time','Info','No.']
video_feature = video.drop(cols_to_drop,axis=1)
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
video_feature['Protocol'] = label_encoder.fit_transform(video_feature['Protocol'])
video_feature['Source'] = label_encoder.fit_transform(video_feature['Source'])
video_feature['Destination'] = label_encoder.fit_transform(video_feature['Destination'])
video_feature['target'] = label_encoder.fit_transform(video_feature['target'])
cols_to_drop = ['target']
video_feature = video_feature.drop(cols_to_drop,axis=1)
seed=7 #To generate same sequence of random numbers
import sklearn
from sklearn.model_selection import train_test_split

#Splitting the data for training and testing(90% train,10% test)

train_data,test_data, train_label, test_label = train_test_split(video_feature, target, test_size=.1,random_state=seed)


from sklearn.naive_bayes import GaussianNB
import time as t
classifier=GaussianNB()
t0=t.time()
classifier = classifier.fit(train_data, train_label)
nbtt=round(t.time()-t0, 5)
print("training time nbc:",nbtt,"s")
t1=t.time()
video_predicted_target=classifier.predict(test_data)
nbpt=round(t.time()-t1, 5)
print("predict time nbc :",nbpt, "s")
score1= classifier.score(test_data, test_label)
print('Naive Bayes : ',score1)


from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_jobs=2, random_state=5)
t0=t.time()
classifier = classifier.fit(train_data, train_label)
rftt=round(t.time()-t0, 5)
print("training time rfc:", rftt,"s")
t1=t.time()
video_predicted_target=classifier.predict(test_data)
rfpt=round(t.time()-t1, 5)
print("predict time rfc:",rfpt, "s")
score2 = classifier.score(test_data, test_label)
print('Random Forest Classifier : ',score2)
label = ['Source port', 'Destination port', 'Protocol', 'Packet Size']
class_training = classifier.feature_importances_

plot_bar_x(label,class_training,"Feature importance in Random Forest","Features","Importance of feature")



from sklearn import tree
decision_tree = tree.DecisionTreeClassifier(criterion='gini')
classifier=decision_tree.fit(train_data, train_label)
print('The accuracy of the Decision Tree classifier on test data is {:.2f}'.format(decision_tree.score(test_data, test_label)))
t0=t.time()
classifier = classifier.fit(train_data, train_label)
dttt=round(t.time()-t0, 5)
score3 = classifier.score(test_data, test_label)
print("training time of Decision tree :",dttt ,"s")
t1=t.time()
video_predicted_target=classifier.predict(test_data)
dtpt=round(t.time()-t1, 5)
print("predict time of decision tree:",dtpt , "s")
label = ['Source port', 'Destination port', 'Protocol', 'Packet Size']
class_training = classifier.feature_importances_

plot_bar_x(label,class_training,"Feature importance in Decision Tree","Features","Importance of feature")


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 7, p = 2, metric='minkowski')
classifier=knn.fit(train_data, train_label)
print('The accuracy of the Knn classifier on test data is {:.2f}'.format(knn.score(test_data, test_label)))
t0=t.time()
classifier = classifier.fit(train_data, train_label)
kntt=round(t.time()-t0, 5)
print("training time of knn :",kntt,"s")
t1=t.time()
video_predicted_target=classifier.predict(test_data)
score4 = classifier.score(test_data, test_label)
knpt=round(t.time()-t1, 5)
print("predict time of knn:",knpt , "s")


from sklearn.svm import SVC
svm = SVC(kernel='rbf', random_state=0, gamma=.10, C=1.0)
classifier=svm.fit(train_data, train_label)
print('The accuracy of the SVM classifier on test data is {:.2f}'.format(svm.score(test_data, test_label)))
t0=t.time()
classifier = classifier.fit(train_data, train_label)
svtt=round(t.time()-t0, 5)
print("training time of SVM :",svtt,"s")
t1=t.time()
video_predicted_target=classifier.predict(test_data)
svpt=round(t.time()-t1, 5)
score5 = classifier.score(test_data, test_label)
print("predict time of SVM :",svpt, "s")
label = ['Naive bayees', 'Random forest', 'decision tree', 'knn', 'svm']
class_training = [
nbtt,
rftt,
dttt,
kntt,
svtt
]

plot_bar_x(label,class_training,"Training time","Classifier","time")
label = ['Naive bayees', 'Random forest', 'decision tree', 'knn', 'svm']
class_prediction = [
nbpt,
rfpt,
dtpt,
knpt,
svpt
]
plot_bar_x(label,class_training,"Predict time","classifiers","time")
label = ['Naive bayees', 'Random forest', 'decision tree', 'knn', 'svm']
class_score = [
score1*100,
score2*100,
score3*100,
score4*100,
score5*100
]

plot_bar_x(label,class_score,"Accuracy score","classifiers","percentage")