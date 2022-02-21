def k_smallest_element(root, k):
	stack = []
	curr = root
	n = 0
	while curr and stack:
		stack.append(curr)
		while curr:
			curr = curr.left
 		curr = stack.pop
		n += 1
		if n == k:
			return curr.val
		else:
			curr = curr.right
