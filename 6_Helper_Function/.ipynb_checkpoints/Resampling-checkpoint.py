from imblearn.over_sampling import RandomOverSampler
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

def random_undersample(X_train,y_train):
    rus = RandomUnderSampler(random_state=1)
    X_resampled, y_resampled = rus.fit_resample(X_train, y_train)
    return X_resampled, y_resampled

def random_oversample(X_train,y_train):
    ros = RandomOverSampler(random_state=1)
    X_resampled, y_resampled = ros.fit_resample(X_train, y_train)
    return X_resampled, y_resampled

def smote_oversample(X_train,y_train):
    sm = SMOTE(random_state=1)
    X_resampled, y_resampled = sm.fit_resample(X_train, y_train)
    return X_resampled, y_resampled
