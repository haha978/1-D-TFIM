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
    E_hist = load_l("noisy_E_hist.pkl")
    HR_dist_hist = load_l("HR_dist_hist.pkl")
    fid_hist = load_l("fid_hist.pkl")
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
    fig, ax = plt.subplots()
    param_idx_l = list(range(len(E_hist)))
    ax.scatter(param_idx_l, E_hist, alpha = 1, c = "#0072B2", s = 20, marker = ".", label = "Energy")
    ax.set_xlabel('VQE Iterations', fontsize = 12)
    ax.set_ylabel("Energy", fontsize = 12)
    ax.legend(bbox_to_anchor=(1.28, 1.30), fontsize = 12)
    ax2 = ax.twinx()
    ax2.scatter(param_idx_l, HR_dist_hist, alpha = 1, c = "#D55E00", s = 20, marker=".", label = "HR distance")
    ax2.scatter(param_idx_l, fid_hist, c = '#009E73', alpha = 0.8, marker=".", label = "Fidelity")
    ax2.set_ylabel("HR distance | Fidelity", fontsize = 12)
    ax2.legend(bbox_to_anchor=(1.28, 1.22), fontsize = 12)
    plt.savefig("plot_2b.svg", dpi = 300, bbox_inches='tight')

def get_hist_avg(avg_num, hist):
    hist_avg = []
    for idx in list(range(len(hist) - avg_num + 1)):
        avg = 0
        for i in range(idx, idx + avg_num):
            avg += hist[i]
        avg = avg / avg_num
        hist_avg.append(avg)
    return hist_avg

def make_avg_plot():
    avg_num = 3
    HR_dist_hist = load_l("HR_dist_hist.pkl")
    param_idx_l = list(range(len(HR_dist_hist)))
    E_hist = load_l("noisy_E_hist.pkl")
    fid_hist = load_l("fid_hist.pkl")
    param_idx_l_avg = get_hist_avg(avg_num, param_idx_l)
    E_hist_avg = get_hist_avg(avg_num, E_hist)
    HR_dist_hist_avg = get_hist_avg(avg_num, HR_dist_hist)
    fid_hist_avg = get_hist_avg(avg_num, fid_hist)
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
    fig, ax = plt.subplots()
    ax.scatter(param_idx_l_avg, E_hist_avg, alpha = 1, c = "#0072B2", s = 20, marker = ".", label = "Energy")
    ax.set_xlabel('VQE Iterations', fontsize = 12)
    ax.set_ylabel("Energy", fontsize = 12)
    ax.legend(bbox_to_anchor=(1.28, 1.30), fontsize = 12)
    ax2 = ax.twinx()
    ax2.scatter(param_idx_l_avg, HR_dist_hist_avg, alpha = 1, c = "#D55E00", s = 20, marker=".", label = "HR distance")
    ax2.scatter(param_idx_l_avg, fid_hist_avg, c = '#009E73', alpha = 0.8, marker=".", label = "Fidelity")
    ax2.set_ylabel("HR distance | Fidelity", fontsize = 12)
    ax2.legend(bbox_to_anchor=(1.28, 1.22), fontsize = 12)
    plt.savefig(f"plot_2b_avg_{avg_num}.svg", dpi = 300, bbox_inches='tight')

def main():
    make_avg_plot()

if __name__ == '__main__':
    main()
