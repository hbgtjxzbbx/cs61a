def tree(root. branches=[]):
	for branch in branches:
		assert is tree(branch), "branches must be tree"
	return [root]+list[branches]

def root(tree):
	return tree[0]

def  branches(tree):
	return tree[1:]

def is_tree(tree):
	if type(tree)!=list or len(tree)<1:
		return False
	for branch in braches(tree):
		if not is_tree(branch):
			return False
	return True

def is_leaf(tree):
	return not branches(tree)

def count_leaves(tree):
	if is_leaf(tree):
		return 1
	else:
		branches_count=[count_leaves(b) for b in branches]
		return sum(branches_count)

def fib_tree(n):
	if n==0 or n==1:
		return tree(n)
	else:
		left,right =fib_tree(n-2), fib_tree(n-1)
		fib_n=root(left)+root(right)
		return tree(fib_n,[left,right])

def leaves(tree):
	if is_leaf(tree):
		return [root(tree)]
	else:
		return sum([leaves(branch) for branch in branches],[])