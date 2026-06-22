import math

"""
### 문제 4: **내장 모듈을 활용한 카피바라의 업무 효율성 계산**

카피바라는 자신의 업무 효율성을 계산하려고 합니다. `math` 모듈을 사용하여 아래 요구사항을 구현하세요.

1. 매일 처리한 업무량을 기록한 배열이 [10, 12, 8, 15, 9]라면 평균 업무량을 출력하세요.
2. 평균 업무량보다 많이 처리한 날의 개수를 계산하세요.
"""

tasks = [10,12,8,15,9]
if __name__ == "__main__":
    print("직접 실행한다.")
    avg_task = sum(tasks)/len(tasks)
    # over_avg_task_count = 0
    # for task in task:
    #     if task > avg_task:
    #         over_avg_task_count +=1
    over_avg_task_count = sum(1 for task in tasks if task > avg_task)
    print(over_avg_task_count)
