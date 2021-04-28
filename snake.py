 #Snake
import turtle #
import time #para retrasar un poco
import random #

posponer = 0.1

#Configuracion de la ventana

wn = turtle.Screen() #crear ventana
#wn.mainloop() #para que no se cierre la ventana
wn.title("Snake") #titulo
wn.bgcolor("black") #color de fondo
wn.setup(width= 600, height= 600) #dimenciones
wn.tracer(0) #animacion fluida

#Cabeza de la serpiente

cabeza = turtle.Turtle() #cabeza
cabeza.color("green")
cabeza.speed(0) #aparezca el obejeto
cabeza.shape("circle") #forma de cuadrado
cabeza.penup() #no deje rastro
cabeza.goto(0,0) #posicion
cabeza.direccion = "stop"

#Comida

comida = turtle.Turtle() 
comida.color("red")
comida.speed(0) 
comida.shape("circle") #forma de manzana xd
comida.penup() 
comida.goto(0,100) 

#Marcador

score = 0
high_score = 0

#Texto

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0       Hight Score: 0", align = "center", font =("Courier", 24, "normal"))

#Segmentos / Cuerpo

segmentos = []

#Funciones
    #Movimiento

def arriba():
    cabeza.direccion = "up" 
def abajo():
    cabeza.direccion = "down"
def izquierda():
    cabeza.direccion = "left"
def derecha():
    cabeza.direccion = "right"       

#Teclado
wn.listen()
wn.onkey(arriba, "Up")
wn.onkey(abajo, "Down")
wn.onkey(izquierda, "Left")
wn.onkey(derecha, "Right")

#Movimiento
def mov():
    if cabeza.direccion == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)    #Movimiento en y

    if cabeza.direccion == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direccion == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)    #Movimiento en x

    if cabeza.direccion == "right":
        x = cabeza.xcor() 
        cabeza.setx(x + 20)    

while True:  #para que no se cierre la pantalla
    wn.update()

    #Colisiones bordes

    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direccion = "stop"

    #Escoder los segmentos.
        for segmento in segmentos:
            #segmento.goto(1000, 1000)
            segmento.hideturtle()
        #limpiar lista de segmentos
        segmentos.clear()

        #Resetear marcador
        score = 0
        texto.clear()
        texto._write("Score: {}   Hight Score: {}".format(score, high_score), align = "center", font =("Courier", 24, "normal"))    


    #Colisiones Comida

    if cabeza.distance(comida) < 20: #20 pixeles (tamaño de objeto)
        x = random.randint(-280,280) #Comida aleatoria
        y = random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle() #Objeto para la lista
        nuevo_segmento.color("grey")
        nuevo_segmento.speed(0) 
        nuevo_segmento.shape("circle")
        nuevo_segmento.penup() 
        segmentos.append(nuevo_segmento)

        #Aumentar marcador
        score += 10

        if score > high_score:
            high_score = score

        texto.clear() #Borrar marcador anterior

        texto._write("Score: {}        Hight Score: {}".format(score, high_score), align = "center", font =("Courier", 24, "normal"))    

    #Mover cuerpo de snake
        #Aumentar tamaño
    
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1): #Ultimo segmento siga al anterior, sin incluir el 0
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)   

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
        
       
    mov()
    time.sleep(posponer)

