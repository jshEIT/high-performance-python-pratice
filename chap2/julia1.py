"""PIL기반의 이미지 생성을 제외한 줄리아 집합 생성기 """
import time

x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193

def calc_pure_python(desired_width,max_iterations):
    """복소 좌표(zs)와 복소 인자(cs)리스트를 만들고
    줄리아 집합을 생성한다."""
    x_step = (x2 - x1) / desired_width
    y_step = (y1 - y2) / desired_width
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2: 
        x.append(xcoord)
        xcoord += x_step

    # 좌표리스트와 각 셀의 초기 조건 만들기
    # 초기 조건은 상수, 쉽게 제거 가능
    # 우리가 만든 함수의 몇몇 입력을 사용한 실제 시나리오를 시뮬레이션할 때 사용
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))
    print("Length of x:",len(x))
    print("Total elements:",len(zs))
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs,cs)
    end_time = time.time()
    secs = end_time - start_time
    print(calculate_z_serial_purepython.__name__ + "took",secs,"seconds")

    # 다음 sum은 1000^2 그리드에 반복 300번을 가정한 값
    # 우리가 의도한 대로 좌표가 변화하는지 확인
    assert sum(output) == 33219980 # 결과값이 기댓과가 같은지?


    # CPU를 집중적으로 사용하는 계산함수
def calculate_z_serial_purepython(maxiter,zs,cs):
    """줄리아 갱신 규칙을 사용해서 output 리스트 계산하기"""
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1
        output[i] = n
    return output


if __name__ == "__main__":
    calc_pure_python(desired_width = 1000, max_iterations = 300)