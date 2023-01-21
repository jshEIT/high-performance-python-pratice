import main
import time

start_vanilla = time.time()
main.prime_finder_vanilla(20000)
end_vanilla = time.time()

print(end_vanilla - start_vanilla)

start_c = time.time()
main.prime_finder_optimized(20000)
end_c = time.time()

print(end_c - start_c)