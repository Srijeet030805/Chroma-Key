import statistics



class Color:
	def __init__(self,r=0,g=0,b=0):
		if(type(r)==list):
			self.r=r
			self.g=g
			self.b=b
		else:
			self.r=r[2]
			self.g=g[1]
			self.b=b[0]
	def __add__(self,col):
		return Color(self.r + col.r, self.g + col.g, self.b + col.b)
	def __sub__(self,col):
		return Color(self.r - col.r, self.g - col.g, self.b - col.b)
	def __abs__(self):
		return Color(abs(self.r), abs(self.g), abs(self.b))

class Image:

	def __init__(self,data):
		self.data = data
		self.dim()
		self.components()
		
	def dim(self):
		self.x= len(self.data)
		self.y= len(self.data[0])

	def components(self):
		self.r= [self.data[i][j][2] for i in range(self.x) for j in range(self.y)] 
		self.g= [self.data[i][j][1] for i in range(self.x) for j in range(self.y)] 
		self.b= [self.data[i][j][0] for i in range(self.x) for j in range(self.y)]

	def colEstimator(self):
		mr=statistics.mode(self.r)
		mg=statistics.mode(self.g)
		mb=statistics.mode(self.b)
		self.bg= Color(mr,mg,mb)
		
	def chromaKey(self,bg):
		buffer= self.data.copy()
		self.colEstimator()
		for i in range(self.x):
			for j in range(self.y):
				if inNbhd(self.bg, 50 ,Color(data[i][j])):
					buffer[i][j]=bg[i][j]
		return buffer



def inNbhd(c,r,p):
	d= abs(p-c)
	return d.r<r and d.g<g and d.b<b

