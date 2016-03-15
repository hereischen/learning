def diamond(n):
	if n > 0 and n%2!= 0:
		diamond_builder = []
		i = 1
	   	while i <=n:
	   		diamond_builder.append(i)
	   		i +=2
	   	index = len(diamond_builder) - 1
	  	head_d =  diamond_builder[:index]
	  	head_d.reverse()
	   	diamond_builder = diamond_builder + head_d
	   	s = ""
	   	for star in diamond_builder:
	   		s += " " * ( (n - star) /2) +"*" * star + "\n"
	   	return s
	else:
		return None	
# this could be better
def diamond_best(n):
    if n % 2 == 0 or n < 1: return None
    d = [' ' * ((n-i)/2) + '*' * i for i in xrange(1, n, 2)]
    d.extend([' ' * ((n-i)/2) + '*' * i for i in xrange(n, 0, -2)])
    return '\n'.join(d) + '\n'

a =diamond(101)
print a