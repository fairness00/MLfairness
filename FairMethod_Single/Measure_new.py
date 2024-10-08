import numpy as np
import copy, math
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.neighbors import KDTree
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import accuracy_score,recall_score,precision_score, f1_score,roc_auc_score,matthews_corrcoef
from aif360.metrics import ClassificationMetric
from aif360.datasets import BinaryLabelDataset

def measure_final_score(dataset_orig_test, dataset_orig_predict,privileged_groups,unprivileged_groups):

    y_test = dataset_orig_test.labels
    y_pred = dataset_orig_predict.labels

    accuracy = accuracy_score(y_test, y_pred)
    recall_macro = recall_score(y_test, y_pred, average='macro')
    precision_macro = precision_score(y_test, y_pred, average='macro')
    f1score_macro = f1_score(y_test, y_pred, average='macro')
    mcc = matthews_corrcoef(y_test, y_pred)

    classified_metric_pred = ClassificationMetric(dataset_orig_test, dataset_orig_predict,
                                                  unprivileged_groups=unprivileged_groups,
                                                  privileged_groups=privileged_groups)

    srp = classified_metric_pred.selection_rate(privileged=True)
    sru = classified_metric_pred.selection_rate(privileged=False)
    fprp = classified_metric_pred.false_positive_rate(privileged=True)
    fpru = classified_metric_pred.false_positive_rate(privileged=False)
    tprp = classified_metric_pred.true_positive_rate(privileged=True)
    tpru = classified_metric_pred.true_positive_rate(privileged=False)
    spd = abs(classified_metric_pred.statistical_parity_difference())
    aod = abs(classified_metric_pred.average_odds_difference())
    eod = abs(classified_metric_pred.equal_opportunity_difference())

    return accuracy, recall_macro,  precision_macro,  f1score_macro, mcc, srp, sru, fprp, fpru, tprp, tpru, spd, aod, eod
