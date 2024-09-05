# graph.py

from typing import Dict, Set, List, Tuple

def make_grant_graph(grant_list: List[Tuple[str, str]]) -> Dict[str, Set[str]]:
    grant_graph: Dict[str, Set[str]] = {}
    for grant in grant_list:
        grantor, grantee = grant
        if grantor not in grant_graph:
            grant_graph[grantor] = set()
        grant_graph[grantor].add(grantee)
    return grant_graph

def print_grant_graph(grant_graph: Dict[str, Set[str]]) -> None:
    for gtor, gtee_set in grant_graph.items():
        print(gtor, gtee_set)

