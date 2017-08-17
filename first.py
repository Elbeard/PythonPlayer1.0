# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.filedialog as fdl
import pyglet


root = Tk()
player = pyglet.media.Player()
btnPlay = False
rf = root.filename = ['5.mp3']

def LoadFile(ev):
	global rf
	rf = [fdl.askopenfilename()]
	loadMusic = pyglet.media.load(rf[0])
	player.queue(loadMusic)
	return rf
def PlayPause(ev):
	global btnPlay
	btnPlay = not btnPlay
	if btnPlay == True:
		player.play()
	else:
		player.pause()

def Stop(ev):
	player.delete()

#----------------------блок отрисовки----------------------
panelFrame = Frame(root, height=60, width=330, bg='gray')
panelFrame.pack(side = 'top', fill = 'x')

loadBtn = Button(panelFrame,
			text="Open File",
			width=10,height=1)
loadBtn.place(x=125, y=15)

loadBtn.bind("<Button-1>", LoadFile)

stopBtn = Button(panelFrame, 
			text="Stop",
			width=10,height=1)
stopBtn.place(x=230, y=15)

stopBtn.bind("<Button-1>", Stop)

btn = Button(panelFrame,				#Родительское окно
			 text="Play/Pause",			#надпись на кнопке
			 width=10,height=1,			#ширина и высота
			 bg="white",fg="black")		#цвет фона и надписи

btn.bind("<Button-1>", PlayPause)		#При нажатии ЛКМ на кнопку вызывается функция PlayPause

btn.place(x=20,y=15)					#расположить кнопку на главном окне


#-----------------------запуск главного цикла-------------------------------
root.mainloop()