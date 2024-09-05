# initialize.py

from typing import List, Tuple

def initialize_grant_list(grant_list: List[Tuple[str, str]]) -> Tuple[List[Tuple[str, str]], str]:
    users = "ABCD"

    for user in users:
        for user2 in users:
            if user != user2:
                grant_list.append((user, user2))

    owner = "E"

    for user in users:
        grant_list.append((owner, user))

    return grant_list, owner

