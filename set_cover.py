from typing import List, Set

def set_cover(universe: Set[int], sets: List[Set[int]]) -> List[Set[int]]:
    covered = set()
    solution = []
    while covered != universe:
        best_set = None
        best_coverage = 0
        for i, s in enumerate(sets):
            if i not in solution:
                coverage = len(s - covered)/len(s)
                if coverage > best_coverage:
                    best_set = i
                    best_coverage = coverage
        solution.append(sets[best_set])
        covered |= sets[best_set]
    return solution
