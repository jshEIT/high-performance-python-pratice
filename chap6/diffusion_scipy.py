from scipy.ndimage.filters import laplace
def laplacian(grid,out):
    laplace(grid,out,mode="wrap")

grid_shape = (640,640)
