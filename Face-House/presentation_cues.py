# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:42:48 2017

@author: claire
"""
from psychopy import visual, core, event, logging, gui, data
import os, time

import random
import os
import csv
import numpy as np
from ctypes import windll

print(__doc__)


stim_path = 'C:\\Users\\Claire\\Desktop\\Face-House\\Stimuli\\'

###################
# define trials
###################
n_trials = 50

CUE1 = 'cue1.png'
CUE2 = 'cue2.png'
CATCH = 'catch.png'
trig_cue1 = 10
trig_cue2 = 20
trig_catch = 30
PAUSE= 'break'
trig_break = 550


trial_list = [[CUE1,trig_cue1], [CUE2,trig_cue2]]*(n_trials/2)
trial_list += [[CATCH,trig_catch ]] * int(0.10 * len(trial_list))

random.shuffle(trial_list)

stim_duration = np.random.uniform(low=1.9, high=2.2, size=(len(trial_list)))
fix_duration = np.random.uniform(low=1, high=1.5, size=(len(trial_list)))

trial_list.insert(n_trials/2,[PAUSE, trig_break])


cues, trig_cues = zip(*trial_list)

complete = zip(cues, fix_duration, stim_duration, trig_cues)


with open('simple_cue_presentation.csv','wb') as out:
        csv_out = csv.writer(out, delimiter = ",")
        csv_out.writerow([ 'Cue', 'Fix_Duration','Stim_Duration', 'Trigger_Cue'])
        for row in complete:
            csv_out.writerow(row)




####################
# define experiment
####################

#---------------------------------------
# Set up parallel port
#---------------------------------------

port_adress= 0xD050

def send_trigger(trigger_code):
   	windll.inpout32.Out32(port_adress, trigger_code)
	core.wait(0.005) 
	windll.inpout32.Out32(port_adress, 0)


trig_fix=40


expName = 'Cue_simple_presentation'  
expInfo = {'participant':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel  
expInfo['date'] = data.getDateStr()  # add a simple timestamp  
expInfo['expName'] = expName

TRIALS_FILE ='simple_cue_presentation.csv'

# Experiment handler
thisExp = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
	originPath=None,
	savePickle=False, 
	saveWideText=False) #prevent the experiment handler to write expe data upon termination (and overwriting our files)

trialList = data.importConditions(TRIALS_FILE, returnFieldNames=False)
trials = data.TrialHandler(trialList, nReps=1, method='sequential', extraInfo=expInfo)
trials.data.addDataType('respKey')
trials.data.addDataType('respTime')
trials.data.addDataType('stimOnset')
trials.data.addDataType('imOnset')
trials.data.addDataType('imStop')


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

fix_cross = visual.TextStim(win =win, 
        ori =0, 
        name='fix_cross', 
        text= '+',
        font= 'Arial', 
        pos=[0,0],
        height = 0.06, 
        color=[0.5, 0.5, 0.5]
        )

instr = visual.TextStim(win=win, ori=0, name='image_instr',
    text="Pictures will be presented on the screen. Please watch them carefully. Press the key when you see the target. Press any key to start.", font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='grey', colorSpace='rgb', opacity=1,
    depth=0.0)

pause1 = visual.TextStim(win=win, ori=0, name='pause',
    text="Please take a short break.", font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='grey', colorSpace='rgb', opacity=1,
    depth=0.0)

pause2 = visual.TextStim(win=win, ori=0, name='pause',
    text="Press any key to continue", font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='grey', colorSpace='rgb', opacity=1,
    depth=0.0)
    

theEnd = visual.TextStim(win=win, ori=0, name='theEnd',
    text="End of this part !", font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='grey', colorSpace='rgb', opacity=1,
    depth=0.0)

def takepause(trigg):
    pause1.draw()
    win.flip()
    core.wait(6)
    pause2.draw()
    win.flip()
    event.waitKeys()

###########################
# run experiment
###########################

instr.draw()
win.flip()
event.waitKeys()

for thisTrial in trials:
    win.setMouseVisible(False)
    if event.getKeys(keyList=['escape']):
        win.close()
        core.quit()
    elif thisTrial['Cue'] == 'break':
        takepause(int(thisTrial['Trigger_Cue']))
    else: 
        stim = visual.ImageStim(win =win, 
                image = stim_path + thisTrial['Cue'], 
                pos = [0,0], 
                #size = [100, 100], 
                opacity = 1,
                units = 'pix'
                )
        fix_cross.draw()
        send_trigger(trig_fix)
        win.flip()
        core.wait(int(thisTrial['Fix_Duration']))
        stim.draw()
        send_trigger(int(thisTrial['Trigger_Cue']))
        win.flip()
        core.wait(int(thisTrial['Stim_Duration']))


theEnd.draw(win)
win.flip()
core.wait(3)
win.close()

win.close()

trials.saveAsWideText(expInfo["participant"] +".csv")
core.quit()
    
    
    
    
    
    
    
    
    
    