from collections import deque

def earliest_ancestor(ancestors, starting_node):
    verts = {}
    #p= parents, c=children
    for p, c in ancestors:
        if c not in verts:
            verts[c] = set()
            verts[c].add(p)
            if p not in verts:
                verts[p] = set()
        else:
            verts[c].add(p)
            if p not in verts:
                verts[p] = set()
    if len(verts[starting_node]) == 0:
        return -1

    stack = deque()
    e_gen = 0
    stack.append((starting_node, 0))
    term = {}
    while len(stack) > 0:
        cur_vert, cur_gen = stack.pop()
        if cur_gen > e_gen:
            e_gen = cur_gen
        if len(verts[cur_vert]) == 0:
            term[cur_gen] = term.get(cur_gen, [])
            term[cur_gen].append(cur_vert)
        for p in verts[cur_vert]:
            stack.append((p, cur_gen + 1))
    term[e_gen].sort()
    return term[e_gen][0]
