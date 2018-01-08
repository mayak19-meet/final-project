import turtle

class B (turtle):
	def__init__(self,shape,size,x,y,dx,dy,r,color):
	turtle.__init__(self)
	self.goto(x)
	self.goto(y)
	self.x=x
	self.y=y
	self.dx=dx
	self.dy=dy
	self.r=r
	self.size(r/10)
	self.shape("circle")

	def move (self,screen_width,screen_height):
		current_x=xcor
		new_x=(x+dx)
		current_y=ycor
		new_y=(y+dy)
		right_side_ball=(new_x+r)
		left_side_ball=(new_x-r)
		up_side_ball=(new_y+r)
		down_side_ball=(new_y-r)
		self.goto(new_x,new_y)
		if right_side_ball>=screen_width/2:
			self.dx=-dx
		if left_side_ball<=screen_width/2:
			self.dx=-dx
		if up_side_ball>=screen_height/2:
			self.dy=-dy
		if down_side_ball<=screen_height/2:
			self.dy=-dy