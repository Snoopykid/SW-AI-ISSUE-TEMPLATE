"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3] 

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    # TODO: 그래프와 진입 차수 초기화

    graph = dict()
    verqueue = []
    defDict = dict()
    
    # TODO: 그래프 구성 및 진입 차수 계산
    for ver in range(vertices):
        graph.setdefault(ver, [])
        defDict.setdefault(ver, [])
    for ent in range(len(edges)):
        for key in graph.keys():
            if edges[ent][0] == key:
                graph[key].append(edges[ent][1])
    for ent in range(len(edges)):
        for key in defDict.keys():
            if edges[ent][1] == key:
                defDict[key].append(edges[ent][0])

    in_degree = {v: len(defDict[v]) for v in defDict}

    """
    vertices(4)회 만큼 for문을 돌며
    각 정점에 대한 키-값쌍의 딕셔너리인 graph를 만든다
    간선인 endges는 총 3개의 튜플로 3회의 for문을 돌며
    각 그래프의 키를 순회하며
    edges의 [ent][0], 즉 간선의 출발점이 graph의 각 key와 동일한 정수인지 확인한다.
    만약 같다면 그래프 키 값의 리스트에 edges간선의 도착점을 추가한다. 
    """
    
    # TODO: 진입 차수가 0인 정점들을 큐에 추가
    
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            verqueue.append(i)
            



    """
    진입 차수가 0인 정점을 큐에 삽입한다.
    큐에서 원소를 꺼내 해당 원소에 연결된 간선을 제거한다.
    간선을 제거한 후 진입 차수가 0이 된 정점을 큐에 삽입한다.
    위 과정을 반복한다.
    """    

    result = []
    
    # TODO: 큐가 빌 때까지 반복
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들의 진입 차수 감소
    while verqueue:
        v = verqueue.pop(0)
        result.append(v) 
        for j in graph[v]:
            in_degree[j] -= 1
            if in_degree[j] == 0:
                verqueue.append(j)
    
    return result

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
