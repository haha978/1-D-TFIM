import numpy as np
import matplotlib.pyplot as plt
import os
import pickle
from cycler import cycler

def load_l(name):
    output = None
    with open(os.path.join(name), "rb") as fp:
        output = pickle.load(fp)
    return output

def get_mark_cycler():
    marker_cycler = (cycler(color=["#E69F00", "#56B4E9", "#009E73", "#0072B2", "#D55E00", "#CC79A7", "#F0E442"]) +
                 cycler(linestyle=["none", "none", "none", "none", "none", "none", "none"]) +
                 cycler(marker=["4", "2", "3", "1", "+", "x", "."]))
    return marker_cycler

def make_plot():
    avg_num = 20
    param_idx_l = np.load("param_idx_l.npy", allow_pickle = True)
    HR_dist_hist_dep = load_l("HR_dist_hist_dep.pkl")
    HR_dist_hist_dep = [HR_dist_hist_dep[idx] for idx in param_idx_l]
    HR_dist_hist_ionq = load_l("HR_dist_hist_ionq.pkl")
    fid_hist_dep = load_l("fid_hist_dep.pkl")
    fid_hist_dep = [fid**2 for fid in fid_hist_dep]

    #get average
    param_idx_l_avg = get_hist_avg(avg_num, param_idx_l)
    HR_dist_hist_dep_avg = get_hist_avg(avg_num, HR_dist_hist_dep)
    #get average for dep
    HR_dist_hist_ionq_avg = get_hist_avg(avg_num, HR_dist_hist_ionq)
    fid_hist_dep_avg = get_hist_avg(avg_num, fid_hist_dep)

    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Times New Roman'] + plt.rcParams['font.sans-serif']
    fig, ax = plt.subplots()
    ax.scatter(param_idx_l, HR_dist_hist_dep, alpha = 0.1, c = "#D55E00", s = 20, marker=".")
    ax.scatter(param_idx_l_avg, HR_dist_hist_dep_avg, alpha = 1, c = "#D55E00", s = 20, marker=".", label = "HR distance (dep)")
    ax.scatter(param_idx_l, HR_dist_hist_ionq, alpha = 0.1, c = "#F0E442", s = 20, marker=".")
    ax.scatter(param_idx_l_avg, HR_dist_hist_ionq_avg, alpha = 1, c = "#F0E442", s = 20, marker=".", label = "HR distance (ionq)")
    ax.scatter(param_idx_l_avg, fid_hist_dep_avg, c = '#CC79A7', alpha = 1, marker=".", label = "Fidelity (dep)")
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    ax.set_ylabel("HR distance | Fidelity", fontsize = 14)
    ax.legend(bbox_to_anchor=(1.6, 1.14), fontsize = 14)
    plt.savefig(f"plot_2a_fid_HR_{avg_num}.svg", dpi = 300, bbox_inches='tight')

def get_hist_avg(avg_num, hist):
    hist_avg = []
    for idx in list(range(len(hist) - avg_num + 1)):
        avg = 0
        for i in range(idx, idx + avg_num):
            avg += hist[i]
        avg = avg / avg_num
        hist_avg.append(avg)
    return hist_avg

def main():
    make_plot()
    #make_avg_plot()

if __name__ == '__main__':
    main()
