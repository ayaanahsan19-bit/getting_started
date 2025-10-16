import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

crops = pd.read_csv("soil_measures.csv")

crops.isna().sum()

crops.crop.unique()

X = crops.drop(columns="crop")
y = crops["crop"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

feature_performance = {}
for feature in ["N", "P", "K", "ph"]:
    log_reg = LogisticRegression(multi_class="multinomial")
    log_reg.fit(X_train[[feature]], y_train)
    y_pred = log_reg.predict(X_test[[feature]])
    f1 = metrics.f1_score(y_test, y_pred, average="weighted")
    feature_performance[feature] = f1
    print(f"F1-score for {feature}: {f1}")
    
best_predictive_feature = {"K": feature_performance["K"]}
best_predictive_feature