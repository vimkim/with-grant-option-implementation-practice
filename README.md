Simulate how ORACLE's WITH GRANT OPTION works.

```bash
py src/main.py
```

```log
A {'B', 'D', 'C'}
B {'A', 'D', 'C'}
C {'A', 'B', 'D'}
D {'A', 'B', 'C'}
E {'A', 'B', 'D', 'C'}
revoking E B
reachable_users: {'B', 'C', 'E', 'A', 'D'}
unreachable_users: set()

after revoking E's grant to B

A {'B', 'D', 'C'}
B {'A', 'D', 'C'}
C {'A', 'B', 'D'}
D {'A', 'B', 'C'}
E {'A', 'D', 'C'}
revoking E C
reachable_users: {'B', 'C', 'E', 'A', 'D'}
unreachable_users: set()

after revoking E's grant to C

A {'B', 'D', 'C'}
B {'A', 'D', 'C'}
C {'A', 'B', 'D'}
D {'A', 'B', 'C'}
E {'A', 'D'}
revoking E D
reachable_users: {'B', 'C', 'E', 'A', 'D'}
unreachable_users: set()

after revoking E's grant to D

A {'B', 'D', 'C'}
B {'A', 'D', 'C'}
C {'A', 'B', 'D'}
D {'A', 'B', 'C'}
E {'A'}
revoking E A
reachable_users: {'E'}
unreachable_users: {'A', 'B', 'D', 'C'}

after revoking E's grant to A

E set()


```
