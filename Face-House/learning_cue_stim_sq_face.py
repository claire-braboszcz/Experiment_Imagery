# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 10:08:51 2017

@author: claire
"""

from psychopy import visual, core, event, logging, gui, data
import os, time
print(__doc__)



stim_path = 'C:\\Users\\Claire\\Desktop\\Face-House\\Stimuli\\'




stim = 'assoc_cuestim_1.png'
#stim = 'assoc_cuestim_2.png'


#--------------------------------------
#Define experiment constant 
#------------------------------------
win = visual.Window(size=(1024, 768), 
        fullscr=True, 
        screen=0, 
        allowGUI=False, 
        allowStencil=False, 
        monitor='testMonitor', 
        color=[-0.3,-0.3,-0.3], 
        colorSpace='rgb', 
        blendMode='avg', 
        useFBO=True,)
        
        
        
learning_instr = visual.TextStim(win=win, ori=0, name='image_instr',
    text="In the experiment you will see two pictures. They are associated with two geometrical shapes that will always precede them. \n In the next screen you will learn these associations. \n Press any key to continue.", font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='grey', colorSpace='rgb', opacity=1,
    depth=0.0)
    
    

next_screen = visual.TextStim(win, 
        text = 'Press any key to continue \n\n',
        height= 0.07, 
        units= 'norm'
        )


fix_cross = visual.TextStim(win =win, 
        ori =0, 
        name='fix_cross', 
        text= '+',
        font= 'Arial', 
        pos=[0,0],
        height = 0.06, 
        color=[0.5, 0.5, 0.5]
        )
        

stim = visual.ImageStim(win =win, 
        image = stim_path + stim, 
        pos = [0,0], 
        size = [600, 500], 
        opacity = 1,
        units = 'pix'
        )

# functions for expe

def instructions():
    learning_instr.draw()
    win.flip()
    event.waitKeys()


    

instructions()

stim.draw()
win.flip()
event.waitKeys(keyList ='q')
win.close()

    
































