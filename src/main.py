# main.py

from typing import Dict, Set, List, Tuple
from initialize import initialize_grant_list
from graph import make_grant_graph, print_grant_graph
from revoke import revoke

def main() -> None:
    grant_graph: Dict[str, Set[str]]

    grant_list: List[Tuple[str, str]] = []

    grant_list, owner = initialize_grant_list(grant_list)

    grant_graph = make_grant_graph(grant_list)

    for gtor, gtee_set in grant_graph.items():
        print(gtor, gtee_set)

    revoke(grant_graph, owner, 'E', 'B')
    print("\nafter revoking E's grant to B\n")
    print_grant_graph(grant_graph)

    revoke(grant_graph, owner, 'E', 'C')
    print("\nafter revoking E's grant to C\n")
    print_grant_graph(grant_graph)

    revoke(grant_graph, owner, 'E', 'D')
    print("\nafter revoking E's grant to D\n")
    print_grant_graph(grant_graph)

    revoke(grant_graph, owner, 'E', 'A')
    print("\nafter revoking E's grant to A\n")
    print_grant_graph(grant_graph)

if __name__ == '__main__':
    main()

