from multiprocessing import Pool
import random
import time
import os
import numpy as np

def estimate_nbr_points_in_quarter_circle(nbr_samples):
    """벡터화한 numpy배열을 활용한 원주율 계산"""
    np.random.seed() # 시드는 프로세스마다 설정해야 한다.
    xs = np.random.uniform(0, 1, nbr_samples)
    ys = np.random.uniform(0, 1, nbr_samples)
    estimate_inside_quarter_unit_circle = (xs * xs + ys * ys) <= 1
    nbr_trials_in_quarter_unit_circle = np.sum(estimate_inside_quarter_unit_circle)
    return nbr_trials_in_quarter_unit_circle

if __name__ == "__main__":
    nbr_samples_in_total = 1e8
    nbr_parallel_blocks = 4
    pool = Pool(processes=nbr_parallel_blocks)
    nbr_samples_per_worker = nbr_samples_in_total / nbr_parallel_blocks
    print("Making {:,} samples per {} worker".format(nbr_samples_per_worker,
                                                     nbr_parallel_blocks))
    nbr_trials_per_process = [int(nbr_samples_per_worker)] * nbr_parallel_blocks
    t1 = time.time()
    nbr_in_quarter_unit_circles = pool.map(estimate_nbr_points_in_quarter_circle,
                                           nbr_trials_per_process)
    pi_estimate = sum(nbr_in_quarter_unit_circles) * 4 / float(nbr_samples_in_total)
    print("Estimated pi", pi_estimate)
    print("Delta:", time.time() - t1)