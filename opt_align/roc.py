# File containing functions for plotting ROC
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
from opt_align import align

def calc_thresh(tpr, scores):
    # Calculate threshold given tpr and scores for positive sequences
    # TPR = # TP > thresh / # TPs
    expected = tpr*(len(scores)-1)
    thresh = sorted(scores, reverse=True)[int(expected)]
    return thresh

def plot_ROC(fprs, tprs, outfile):
    """
    Function to plot ROC given list of fprs and tprs
    """
    plt.figure(figsize=(5,5))
    for k, v in fprs.items():
        plt.plot(v, tprs, label = k)
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve: Pos vs. Neg")
    plt.legend()
    plt.savefig(outfile, type="pdf")

def output_ROC_all(pos_scores_dict, neg_scores_dict, outfile="part1-2b.pdf"):
    """
    Output the ROC curve for each method
    """
    performance = {}

    tprs = np.arange(0,1.01,0.01)
    for mat, scores in pos_scores_dict.items():
        fprs_mat = []
        scores_neg = neg_scores_dict.get(mat)
        for rate in tprs:
            thresh = calc_thresh(rate, scores)
            fpr = len(scores_neg[scores_neg >= thresh])/len(scores_neg)
            fprs_mat.append(fpr)
        performance[mat] = fprs_mat 
    plot_ROC(performance, tprs, outfile)
    return performance

def output_ROC_best(pos_seqs, neg_seqs, performance, score_mats,best_mat, outfile="part1-3.pdf"):
    """
    Output the ROC for the best matrix with normalized and normal scores
    """
    pos_scores_norm = align.run_alignment(pos_seqs, score_mats.get(best_mat), normalize=True)
    neg_scores_norm = align.run_alignment(neg_seqs, score_mats.get(best_mat), normalize=True)
    performance_with_norm = {best_mat: performance.get(best_mat)}
    tprs = np.arange(0,1.01,0.01)
    fprs_norm = []
    for rate in tprs:
        thresh = calc_thresh(rate, pos_scores_norm)
        fpr = len(neg_scores_norm[neg_scores_norm >= thresh])/len(neg_scores_norm)
        fprs_norm.append(fpr)
    performance_with_norm[best_mat+"_norm"] = fprs_norm
    plot_ROC(performance_with_norm, tprs, outfile)
