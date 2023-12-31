tree = [
        [
            [
                [84, -29], [-37, -25]
            ],
            [
                [1, 43],[-75, 49]
            ]
        ],
        [
            [
                [-21, -51], [58, -46]
            ],
            [
                [-3,-13], [26, 79]
            ]
        ]
]
root = 0
pruned = 0

def children(branch, depth, alpha, beta):
    global tree
    global root
    global pruned
    i = 0
    for child in branch:
        if type(child) is list:
            (nalpha, nbeta) = children(child, depth+1, alpha, beta)
            if depth % 2 ==1:
                beta = nalpha if nalpha < beta else beta
            else:
                alpha = nbeta if nbeta > alpha else alpha
            branch[i] = alpha if depth % 2 == 0 else beta
            i += 1
        else:
            if depth % 2 == 0 and alpha < child:
                alpha = child
            if depth % 2 == 1 and beta > child:
                beta = child
            if alpha >= beta:
                pruned += 1
                break
    if depth == root:
        tree = alpha if root == 0 else beta
    return (alpha, beta)


def alphabeta(in_tree = tree, start = root, upper = -100, lower = 100):
    global tree
    global pruned
    global root
    (alpha, beta) = children(tree, start, upper, lower)
    if __name__ == "__main__":
        print("(alpha, beta):",alpha,beta)
        print("Result:", tree)
        print("Times pruned:", pruned)
    return(alpha, beta, tree, pruned)


if __name__ == "__main__":
    alphabeta(None)

