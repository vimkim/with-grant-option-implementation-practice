# revoke.py

from abc import ABC
from typing import Dict, Set, List

def get_unreachable_users(grant_graph: Dict[str, Set[str]], owner: str) -> Set[str]:
    all_users: Set[str] = set(grant_graph.keys())
    reachable_users_by_owner: Set[str] = set()

    # DFS from owner
    stack: List[str] = [owner]
    while stack:
        node = stack.pop()
        if node not in reachable_users_by_owner:
            reachable_users_by_owner.add(node)
            stack.extend(grant_graph[node])

    unreachable_users: Set[str] = all_users - reachable_users_by_owner
    print('reachable_users:', reachable_users_by_owner)
    print('unreachable_users:', unreachable_users)
    return unreachable_users

def revoke(grant_graph: Dict[str, Set[str]], owner: str, grantor: str, grantee: str) -> None:
    print('revoking', grantor, grantee)

    if grantee in grant_graph[grantor]:
        grant_graph[grantor].remove(grantee)

        unreachable_users = get_unreachable_users(grant_graph, owner)

        for unreachable in unreachable_users:
            if unreachable in grant_graph:
                del grant_graph[unreachable]
