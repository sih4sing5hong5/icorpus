''''' 
Created on 2012-11-9 
 
@author: Pandara 
'''  
def lcs_len(a, b):  
	''''' 
	a, b: strings 
	'''  
	n = len(a)  
	m = len(b)  
	  
	l = [([0] * (m + 1)) for i in range(n + 1)]  
	direct = [([0] * m) for i in range(n)]#0 for top left, -1 for left, 1 for top  
	  
	for i in range(n + 1)[1:]:  
		for j in range(m + 1)[1:]:  
			if a[i - 1] == b[j - 1]:  
				l[i][j] = l[i - 1][j - 1] + 1  
			elif l[i][j - 1] > l[i - 1][j]:   
				l[i][j] = l[i][j - 1]  
				direct[i - 1][j - 1] = -1  
			else:  
				l[i][j] = l[i - 1][j]  
				direct[i - 1][j - 1] = 1  
				  
	return l, direct  
  
def get_lcs(direct, a, i, j):  
	''''' 
	direct: martix of arrows 
	a: the string regarded as row 
	i: len(a) - 1, for initialization 
	j: len(b) - 1, for initialization 
	'''  
	lcs = []  
	get_lcs_inner(direct, a, i, j, lcs)  
	return lcs  
		  
	def get_lcs_inner(direct, a, i, j, lcs):	  
		if i < 0 or j < 0:  
			return  
		  
		if direct[i][j] == 0:  
			get_lcs_inner(direct, a, i - 1, j - 1, lcs)  
			lcs.append(a[i])  
				   
		elif direct[i][j] == 1:  
			get_lcs_inner(direct, a, i - 1, j, lcs)  
		else:  
			get_lcs_inner(direct, a, i, j - 1, lcs)  
	  
	if __name__ == "__main__":  
		a = "abcbdab"  
		b = "bdcaba"  
		  
		l, direct = lcs_len(a, b)  
		lcs = get_lcs(direct, a, len(a) - 1, len(b) - 1)  
		  
		print "the length of lcs is:", l[len(a)][len(b)]  
		print "one of the lcs:", "".join(lcs)  