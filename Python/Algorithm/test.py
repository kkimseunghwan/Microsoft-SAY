import time
import tracemalloc
import gc

def aliasingObj():
    a = [i for i in range(100000)]
    b = a  # 에일리어싱
    b[0] = -1  # 변경

def copyObj():
    a = [i for i in range(100000)]
    b = a.copy()  # 복사 → 별도 객체
    b[0] = -1  # 변경

# 측정 함수
def measure(func):
    gc.collect()  # 먼저 가비지 수거해서 측정 방해 제거
    
    tracemalloc.start() # 사용 메모리 검사
    start_time = time.perf_counter()
    func()
    elapsed = time.perf_counter() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"[{func.__name__}] Time: {elapsed:.6f}s | Mem current: {current / 1024:.1f} KB | Peak: {peak / 1024:.1f} KB")

measure(aliasingObj)
measure(copyObj)
