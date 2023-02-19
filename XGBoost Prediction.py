import numpy as np
import pandas as pd
import xgboost as xgb
#import shutil
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

if __name__ == '__main__':

    #загружаем тренировочные данные (для обучения)
    train = pd.read_csv('active_diffs_timestamp.csv')

    #загружаем проверочные данные
    features = ["is_active", "axial_1", "vertical_1", "horizontal_1",
                "axial_2", "vertical_2", "horizontal_2",
                "axial_3", "vertical_3", "horizontal_3",
                "axial_4", "vertical_4", "horizontal_4"]

    params_xgb = {
        "objective": "binary:logistic",
        "eval_metric": 'logloss',
        "eta": 0.05,
        "max_depth": 3,
        "subsample": 0.8,
        "colsample_bytree": 0.9,
    }
    num_boost_round = 250
    early_stopping_rounds = 20

    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    #print(train.head())

    train = train.astype('float64')

    a=['is_active']

    newtrain = train.loc[0:3*int(len(train)/4)] #берем половину тренировочных данных
    newtest = train.loc[int(len(train) / 4)+1:int(len(train))]  # вторая половина идет в тест


    dtrain = xgb.DMatrix(newtrain[features].values, newtrain['is_active'].values) #собираем обучающий датасет
    #только из столбцов features, и в качестве цели указываем столбец Leave_Next_Month
    dvalid = xgb.DMatrix(newtest[features].values, newtest['is_active'].values)
    #аналогично для валидации
    watchlist = [(dtrain, 'train'), (dvalid, 'eval')]
    gbm = xgb.train(params_xgb, #настройки выше, подбираются условно на глаз
                    dtrain, # тренировочный датасет
                    num_boost_round, # сколько учиться
                    evals=watchlist, # dtrain - для обучения, dvalid - для валидации
                    early_stopping_rounds=early_stopping_rounds, # через сколько останавливаться, если нет прогресса
                    verbose_eval=10) # каждые 10 раундов выводить текущий результат обучения

    pred = gbm.predict(xgb.DMatrix(newtest[features].values), ntree_limit=gbm.best_iteration + 1) #используя лучшую итерацию
    #print(pred)
    #predict=np.concatenate(test['id'], pred)

    predict = pd.DataFrame(pred) #создаем пандасовский датафрейм из предсказания
    predict = pd.DataFrame(newtest['extract']).join(pd.DataFrame(pred)) # приклеиваем к нему id
    #predict = predict.astype('int')

    new_column_names = ['extract', 'is_active']
    predict.to_csv('submission.csv', index=False, header=new_column_names)
    print(predict)
    #accuracy = accuracy_score(newtest['Leave_Next_Month'].values, np.round(pred))
    #auc = roc_auc_score(newtest['Leave_Next_Month'].values, pred)
    #print('Accuracy: {:.2f} %, ROC AUC: {:.2f}'.format(100 * accuracy, auc))
    #shutil.copy('/kaggle/input/m-lab-1/sample_submission.csv', 'submission.csv')