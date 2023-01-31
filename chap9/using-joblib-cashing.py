from multiprocessing import Pool
import random
import time
import os

from joblib import Parallel,delayed,Memory

memory = Memory("./joblib_cache", verbose=0)

@memory.cache
def estimate_nbr_points_in_quarter_circle_with_idx(nbr_estimates, idx):
    print(f"Executing estimate_nbr_points_in_quarter_circle with \
            {nbr_estimates} on sample {idx} on pid {os.getpid()}")
    nbr_trials_in_quarter_unit_circle = 0
    for step in range(int(nbr_estimates)):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        is_in_unit_circle = x * x + y * y <= 1.0
        nbr_trials_in_quarter_unit_circle += is_in_unit_circle

    return nbr_trials_in_quarter_unit_circle

if __name__ == "__main__":
    nbr_samples_in_total = 1e8
    nbr_parallel_blocks = 8
    pool = Pool(processes=nbr_parallel_blocks)
    nbr_samples_per_worker = nbr_samples_in_total / nbr_parallel_blocks
    print("Making {:,} samples per {} worker".format(nbr_samples_per_worker,
                                                     nbr_parallel_blocks))
    nbr_trials_per_process = [nbr_samples_per_worker] * nbr_parallel_blocks
    t1 = time.time()
    nbr_in_quarter_unit_circles = Parallel(n_jobs=nbr_parallel_blocks) \
        (delayed(
	    estimate_nbr_points_in_quarter_circle_with_idx) \
        (nbr_samples_per_worker, idx) for idx in range(nbr_parallel_blocks))
    pi_estimate = sum(nbr_in_quarter_unit_circles) * 4 / float(nbr_samples_in_total)
    
    print("Estimated pi", pi_estimate)
    print("Delta:", time.time() - t1)