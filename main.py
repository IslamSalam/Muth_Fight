#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
import urandom
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font

ev3 = EV3Brick() #  ev3.speaker.beep()

dk1 = 0
dk2 = 0
dk3 = 0
dk4 = 0
chislitel = 0
znamenatel = 0
RezultatRight = 0
RezultatWrong = 0
choice = 1
proverit = False
touch_sensor_1 = TouchSensor(Port.S1)
touch_sensor_2 = TouchSensor(Port.S2)
touch_sensor_3 = TouchSensor(Port.S3)
touch_sensor_4 = TouchSensor(Port.S4)
pravilniy_1_igrok = 0
pravilniy_2_igrok = 0
font_1 = Font(size=20, bold=True) #размер и жирность шрифта    
font_2 = Font(size=30, bold=True) #размер и жирность шрифта

#реклама
NauRobot_font = Font(size = 32, bold = True)
ev3.screen.set_font(NauRobot_font)
ev3.screen.draw_text(52, 25, ' Nau')
ev3.screen.draw_text(42, 65, 'Robot')
ev3.screen.draw_circle(90, 60, 80)
ev3.screen.draw_circle(91, 60, 80)
ev3.screen.draw_circle(92, 60, 80)
ev3.screen.draw_circle(93, 60, 80) 
ev3.speaker.play_file(SoundFile.MAGIC_WAND)
while not Button.CENTER in (ev3.buttons.pressed()):
    pass
ev3.speaker.play_file(SoundFile.CLICK)
ev3.screen.clear()
wait(300)


#меню выбора 
#while not Button.CENTER in(ev3.buttons.pressed()): #цикл - повторять то что внутри цикла, пока не будет нажата центральная кнопка модуля
#        if Button.DOWN  in(ev3.buttons.pressed()):
#                ev3.speaker.play_file(SoundFile.CONFIRM)
#                choice += 1 
#                if choice > 3:
#                        choice = 1
#
 #       elif Button.UP in(ev3.buttons.pressed()):
  #              ev3.speaker.play_file(SoundFile.CONFIRM)
   #             choice -= 1
    #            if choice < 1:
#                  choice = 3
 #     #  else:   # если ничего не нажато ничего не делать
  #              wait(0)
   #     
    #    wait(100)
#
 #       #вывести на экран картинку с выбранным уровнем
  ##      if choice == 1: 
    #            ev3.screen.load_image(ImageFile.BOTTOM_LEFT)
#
 #       elif choice == 2: 
  #              ev3.screen.load_image(ImageFile.ANGRY)
#
 #       elif choice == 3: 
  #              ev3.screen.load_image(ImageFile.EVIL) 


while pravilniy_1_igrok != 10 and pravilniy_2_igrok != 10:    
  ev3.screen.clear()
  ev3.screen.draw_line(88, 1, 88, 127, width=5) #вывести разделительную линию
  ev3.screen.set_font(font_1) #применить шрифт
  ev3.screen.draw_text(42 ,2, pravilniy_1_igrok) #вывести на экран счет
  ev3.screen.draw_text(130 ,2, pravilniy_2_igrok) #вывести на экран счет
  chislitel = urandom.randint(5, 15) #cлучайный выбор числителя(или типа того)
  znamenatel = urandom.randint(1, 5) #cлучайный выбор знаменателя(или типа того)
  choice_Plus_ili_Minus = urandom.randint(1, 2) #случайный выбор: + - или умножить      
  K_NepravilniyVibor_plus_ili_minus = urandom.randint(1, 2) #т.е. неправильный ответ увеличиваем или уменьшаем
  SkolkoDobavit_Otnyat_k_NepravilnomuOtvetu = urandom.randint(1, 3) #не правильный ответ увеличивается на сколько
  PravilniyOtvet_sprava_ili_sleva = urandom.randint(1, 2) #правильный ответ окажется справа или слева 
  
  if choice_Plus_ili_Minus == 1: #Пример  прибавить или отнять.  Cложение +++++++++++++++++++++++++++++++++++++
   RezultatRight = chislitel + znamenatel #записать правильный ответ 
  if choice_Plus_ili_Minus == 2: #Пример  прибавить или отнять.  Вычитание -
   RezultatRight = chislitel - znamenatel #записать правильный ответ  
   
          
   
  if K_NepravilniyVibor_plus_ili_minus == 1: #если плюс
   RezultatWrong = SkolkoDobavit_Otnyat_k_NepravilnomuOtvetu + RezultatRight #неправильный ответ создать
  if K_NepravilniyVibor_plus_ili_minus == 2: #если минус
   RezultatWrong = RezultatRight - SkolkoDobavit_Otnyat_k_NepravilnomuOtvetu #неправильный ответ создать
    
  
  
  
  if PravilniyOtvet_sprava_ili_sleva == 1: #если правильный ответ Cлева <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
   if choice_Plus_ili_Minus == 1:
     #вывести на экран пример
     ev3.screen.set_font(font_2) #применить шрифт
     if chislitel < 10 and znamenatel < 10: #это нужно чтобы пример был по центру елси числитель и знаменатель меньше 10
       ev3.screen.draw_text(16 ,30, "{}+{}".format(chislitel,znamenatel)) #вывести на экран пример
       ev3.screen.draw_text(106 ,30, "{}+{}".format(chislitel,znamenatel)) #вывести на экран пример
     else:   
       ev3.screen.draw_text(3 ,30, "{}+{}".format(chislitel,znamenatel)) #вывести на экран пример
       ev3.screen.draw_text(93 ,30, "{}+{}".format(chislitel,znamenatel)) #вывести на экран пример

     #вывести на экран варианты ответа
     if RezultatRight < 10 and RezultatWrong < 10: #это нужно чтобы пример был по центру елси числитель и знаменатель меньше 10
       ev3.screen.draw_text(12 ,90, "{}   {}".format(RezultatRight,RezultatWrong)) #вывести на экран пример
       ev3.screen.draw_text(104 ,90, "{}   {}".format(RezultatRight,RezultatWrong)) #вывести на экран пример
     else:
       if RezultatRight < 10 or RezultatWrong < 10: #это нужно чтобы пример был по центру елси числитель и знаменатель меньше 10
         ev3.screen.draw_text(8 ,90, "{}  {}".format(RezultatRight,RezultatWrong)) #вывести на экран пример
         ev3.screen.draw_text(98 ,90, "{}  {}".format(RezultatRight,RezultatWrong)) #вывести на экран пример
       else:
         ev3.screen.draw_text(1 ,90, "{} {}".format(RezultatRight,RezultatWrong)) #правильный ответ выводится слева
         ev3.screen.draw_text(93 ,90, "{} {}".format(RezultatRight,RezultatWrong))
   if choice_Plus_ili_Minus == 2:
     #вывести на экран пример
     ev3.screen.set_font(font_2) #применить шрифт
     if chislitel < 10 and znamenatel < 10: #это нужно чтобы пример был по центру елси числитель и знаменатель меньше 10
       ev3.screen.draw_text(16 ,30, "{}-{}".format(chislitel,znamenatel)) #вывести на экран пример
       ev3.screen.draw_text(106 ,30, "{}-{}".format(chislitel,znamenatel)) #вывести на экран пример
     else:   
       ev3.screen.draw_text(3 ,30, "{}-{}".format(chislitel,znamenatel)) #вывести на экран пример
       ev3.screen.draw_text(93 ,30, "{}-{}".format(chislitel,znamenatel)) #вывести на экран пример

     #вывести на экран варианты ответа
     if RezultatRight < 10 and RezultatWrong < 10: #это нужно чтобы пример был по центру елси числитель и знаменатель меньше 10
       ev3.screen.draw_text(12 ,90, "{}   {}".format(RezultatRight,RezultatWrong)) #вывести на экран пример
       ev3.screen.draw_text(104 ,90, "{}   {}".format(RezultatRight,RezultatWrong)) #вывести на экран пример
     else:
       if RezultatRight < 10 or RezultatWrong < 10: #это нужно чтобы пример был по центру елси числитель и знаменатель меньше 10
         ev3.screen.draw_text(8 ,90, "{}  {}".format(RezultatRight,RezultatWrong)) #вывести на экран пример
         ev3.screen.draw_text(98 ,90, "{}  {}".format(RezultatRight,RezultatWrong)) #вывести на экран пример
       else:
         ev3.screen.draw_text(1 ,90, "{} {}".format(RezultatRight,RezultatWrong)) #правильный ответ выводится слева
         ev3.screen.draw_text(93 ,90, "{} {}".format(RezultatRight,RezultatWrong))
  
  wait(200)

  if PravilniyOtvet_sprava_ili_sleva == 2: #если правильный ответ Справа >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
   if choice_Plus_ili_Minus == 1:
     #вывести на экран пример
     ev3.screen.set_font(font_2) #применить шрифт
     if chislitel < 10 and znamenatel < 10: #это нужно чтобы пример был по центру елси числитель и знаменатель меньше 10
       ev3.screen.draw_text(16 ,30, "{}+{}".format(chislitel,znamenatel)) #вывести на экран пример
       ev3.screen.draw_text(106 ,30, "{}+{}".format(chislitel,znamenatel)) #вывести на экран пример
     else:   
       ev3.screen.draw_text(3 ,30, "{}+{}".format(chislitel,znamenatel)) #вывести на экран пример
       ev3.screen.draw_text(93 ,30, "{}+{}".format(chislitel,znamenatel)) #вывести на экран пример

     #вывести на экран варианты ответа
     if RezultatRight < 10 and RezultatWrong < 10: #это нужно чтобы пример был по центру елси числитель и знаменатель меньше 10
       ev3.screen.draw_text(12 ,90, "{}   {}".format(RezultatWrong,RezultatRight)) #вывести на экран пример
       ev3.screen.draw_text(104 ,90, "{}   {}".format(RezultatWrong,RezultatRight)) #вывести на экран пример
     else:
       if RezultatRight < 10 or RezultatWrong < 10: #это нужно чтобы пример был по центру елси числитель и знаменатель меньше 10
         ev3.screen.draw_text(8 ,90, "{}  {}".format(RezultatWrong,RezultatRight)) #вывести на экран пример
         ev3.screen.draw_text(98 ,90, "{}  {}".format(RezultatWrong,RezultatRight)) #вывести на экран пример
       else:
         ev3.screen.draw_text(1 ,90, "{} {}".format(RezultatWrong,RezultatRight)) #правильный ответ выводится слева
         ev3.screen.draw_text(93 ,90, "{} {}".format(RezultatWrong,RezultatRight))
   if choice_Plus_ili_Minus == 2:
     #вывести на экран пример
     ev3.screen.set_font(font_2) #применить шрифт
     if chislitel < 10 and znamenatel < 10: #это нужно чтобы пример был по центру елси числитель и знаменатель меньше 10
       ev3.screen.draw_text(16 ,30, "{}-{}".format(chislitel,znamenatel)) #вывести на экран пример
       ev3.screen.draw_text(106 ,30, "{}-{}".format(chislitel,znamenatel)) #вывести на экран пример
     else:   
       ev3.screen.draw_text(3 ,30, "{}-{}".format(chislitel,znamenatel)) #вывести на экран пример
       ev3.screen.draw_text(93 ,30, "{}-{}".format(chislitel,znamenatel)) #вывести на экран пример

     #вывести на экран варианты ответа
     if RezultatRight < 10 and RezultatWrong < 10: #это нужно чтобы пример был по центру елси числитель и знаменатель меньше 10
       ev3.screen.draw_text(12 ,90, "{}   {}".format(RezultatWrong,RezultatRight)) #вывести на экран пример
       ev3.screen.draw_text(104 ,90, "{}   {}".format(RezultatWrong,RezultatRight)) #вывести на экран пример
     else:
       if RezultatRight < 10 or RezultatWrong < 10: #это нужно чтобы пример был по центру елси числитель и знаменатель меньше 10
         ev3.screen.draw_text(8 ,90, "{}  {}".format(RezultatWrong,RezultatRight)) #вывести на экран пример
         ev3.screen.draw_text(98 ,90, "{}  {}".format(RezultatWrong,RezultatRight)) #вывести на экран пример
       else:
         ev3.screen.draw_text(1 ,90, "{} {}".format(RezultatWrong,RezultatRight)) #правильный ответ выводится слева
         ev3.screen.draw_text(93 ,90, "{} {}".format(RezultatWrong,RezultatRight))

  
  while True:
    
    if touch_sensor_1.pressed():
      ev3.speaker.beep()
      if PravilniyOtvet_sprava_ili_sleva == 1:
        proverit = True
      if PravilniyOtvet_sprava_ili_sleva == 2:
        proverit = False
      if proverit == True:
        pravilniy_1_igrok += 1
      if proverit == False:
        pravilniy_1_igrok -=  1
        if pravilniy_1_igrok < 0:
          pravilniy_1_igrok = 0        
      break
    
    if touch_sensor_2.pressed():
      ev3.speaker.beep()
      if PravilniyOtvet_sprava_ili_sleva == 1:
        proverit = False
      if PravilniyOtvet_sprava_ili_sleva == 2:
        proverit = True
      if proverit == True:
        pravilniy_1_igrok += 1
      if proverit == False:
        pravilniy_1_igrok -=  1
        if pravilniy_1_igrok < 0:
          pravilniy_1_igrok = 0
      
      break

    if touch_sensor_3.pressed():
      ev3.speaker.beep()
      if PravilniyOtvet_sprava_ili_sleva == 1:
        proverit = True
      if PravilniyOtvet_sprava_ili_sleva == 2:
        proverit = False
      if proverit == True:
        pravilniy_2_igrok += 1
      if proverit == False:
        pravilniy_2_igrok -=  1
        if pravilniy_2_igrok < 0:
          pravilniy_2_igrok = 0
      break

    if touch_sensor_4.pressed():
      ev3.speaker.beep()
      if PravilniyOtvet_sprava_ili_sleva == 1:
        proverit = False
      if PravilniyOtvet_sprava_ili_sleva == 2:
        proverit = True
      if proverit == True:
        pravilniy_2_igrok += 1
      if proverit == False:
        pravilniy_2_igrok -=  1
        if pravilniy_2_igrok < 0:
          pravilniy_2_igrok = 0
      break

ev3.screen.clear()
if pravilniy_1_igrok == 10:
 ev3.screen.draw_text(40,50, "Igrok 1")
if pravilniy_2_igrok == 10:
 ev3.screen.draw_text(40,50, "Igrok 2")
ev3.speaker.play_file(SoundFile.CHEERING)  



