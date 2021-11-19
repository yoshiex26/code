import turtle
def poly(t,x,y,size,side,color):
	t.speed(255)
	t.pencolor('#000000')
	t.fillcolor(color)
	t.begin_fill()
	for n in range (0,4):
		t.forward(size)
		t.left(360/side)
	t.end_fill()

	turtle.update()

def matrix(t,x,y,):
	# color list White = 0 Black = 1 Hair = 2 2nd Hair = 3 outer flower = 4 inner flower = 5 eye = 6 skin = 7 green = 8 brown = 9
	cl = ["#FFFFFF" , "#4A4A4A" ,"#CACA83" ,	"#E3E3B2" ,"#E04ADC" ,
			"#F893F5" ,	"#368BC0" ,"#F1D9C5" ,"#67844B" ,"#8B7460" ]
	# design design list
	mlist = ["000000011111111000000000",
			 "000011122222222111000000",
			 "010122222222222222440000",
			 "011222222222222224554000",
			 "012222222222222244554400",
			 "001232222222222455235540",
			 "001322322222222454224540",
			 "012323232322232345545481",
			 "122222222222212245545410",
			 "122222212222171224484400",
			 "012222171221777122188100",
			 "012221767121776712181000",
			 "001217767711776771210000",
			 "001217767771776771210000",
			 "001221777777777712210000",
			 "001210177777777101210000",
			 "000100011111111000100000",
			 "000000101800810100000000",
			 "000001008888880010000000",
			 "000017018888881071000000",
			 "000177188888888177100000",
			 "000177188888888177100000",
			 "000011191111119111000000",
			 "000000199999999100000000",
			 "000000199999999100000000",
			 "000000177100177100000000",
			 "000000111100111100000000",
			 "000000101100110100000000",
			 "000000011000011000000000"]
	print(t,x,y)
	t.width(1)
	for k in range(0,29):
		for h in range(0,24):
			colorstring = mlist[k][h]
			colorint = int(colorstring)
			color = cl[colorint]
			print(x*20,y*20)
			print(" color ",color," ",end="")
			t.penup()
			t.goto(h*20,k*-20)
			t.pendown()
			poly(t,h,k,20,4,color)
			


def main():
	screen = turtle.Screen()
	#turtle.TurtleScreen._RUNNING = True
	turtle.screensize(canvwidth=1500, canvheight=2000, bg=None)
	x = 400; y = 500
	w = turtle.Screen()
	w.clear()
	w.bgcolor("#ffffff")
	t = turtle.Turtle()

	#turtle.tracer(0, 0)
	
	matrix(t,x,y)
	turtle.update()
	screen.exitonclick()	
	
if __name__ == '__main__':
	main()

'''
cl = ["#f8f8f8","#e8e8e8" ,"#d8d8d8" ,"#b8b8b8" ,
				"#585858" ,"#383838" ,"#282828" , "#181818" ,
				"#ab4642" ,	"#dc9656" ,"#f79a0e" ,"#538947" ,
				"#4b8093" ,"#7cafc2" ,"#96609e" ,"#a16946" ]

'''
