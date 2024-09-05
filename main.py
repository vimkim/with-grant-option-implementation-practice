from typing import Dict


def initialize_grant_list(grant_list):
    users = "ABCD"

    for user in users:
        for user2 in users:
            if user != user2:
                grant_list.append((user, user2))

    owner = "E"

    for user in users:
        grant_list.append((owner, user))

    return grant_list, owner

def make_grant_graph(grant_list):
    grant_graph = {}
    for grant in grant_list:
        grantor, grantee = grant
        if grantor not in grant_graph:
            grant_graph[grantor] = set()
        grant_graph[grantor].add(grantee)
    return grant_graph

def reachable_from(grant_graph, visited, from_, to_):

    if from_ == to_:
        return True
    if from_ in visited:
        return False
    visited.add(from_)
    if from_ not in grant_graph:
        return False
    for gtee in grant_graph[from_]:
        if reachable_from(grant_graph, visited, gtee, to_):
            return True
    return False


def revoke(grant_graph, owner, grantor, grantee):
    print('revoking', grantor, grantee)

    if grantee in grant_graph[grantor]:
        grant_graph[grantor].remove(grantee)

        for gtee in list(grant_graph[grantee]):
            if gtee in grant_graph[grantee]:
                if not reachable_from(grant_graph, set(), owner, gtee):
                    revoke(grant_graph, owner, grantee, gtee)



def print_grant_graph(grant_graph):
    for gtor, gtee_set in grant_graph.items():
        print(gtor, gtee_set)


def main():
    grant_graph: Dict
    print('Hello, World!')

    grant_list = []

    grant_list, owner = initialize_grant_list(grant_list)

    grant_graph: Dict = make_grant_graph(grant_list)

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
