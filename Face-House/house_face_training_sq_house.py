from psychopy import visual, core, event, logging, gui, data
import os, time

print(__doc__)


TRIALS_FILE = 'training_sq_house.csv' 
stimpath= 'C:\\Users\\Claire\\Desktop\\Face-House\\Stimuli\\'
#vismaskpath = '/home/claire/Documents/Experiment/Imagery/Clips/Animal/'
#pixpath = '/home/claire/Documents/Experiment/Imagery/Frames/Animals/cat_frame.png' 

if not os.path.exists(stimpath):
        raise RuntimeError("Check path !! Stimuli File could not be found:"+stimpath)

#if not os.path.exists(vismaskpath):
#        raise RuntimeError("Video File could not be found:"+vismaskpath)

#if not os.path.exists(pixpath):
#        raise RuntimeError("Video File could not be found:"+pixpath)



#---------------------------------------
# Set up parallel port
#---------------------------------------

pparallel = None
try:
    from psychopy import parallel

    pparallel = parallel.ParallelPort(address = 0x378) #888
except ImportError:

    class DummyParallel:
        def setData(self, val):
            print("Port parallele: setData %s" % val)
    pparallel = DummyParallel()


trigger_stim = int("00000011",2)
trigger_mask = int("00000101",2)
trigger_space = int("00010100", 2)
trigger_fixation = int("10100000",2)


from psychopy import visual, core, event, logging, gui, data
import os, time
import random
from ctypes import windll

print(__doc__)


stimpath= 'C:\\Users\\Claire\\Desktop\\Face-House\\Stimuli\\'
#vismaskpath = '/home/claire/Documents/Experiment/Imagery/Clips/Animal/'
#pixpath = '/home/claire/Documents/Experiment/Imagery/Frames/Animals/cat_frame.png' 

if not os.path.exists(stimpath):
        raise RuntimeError("Check path !! Stimuli File could not be found:"+stimpath)

#if not os.path.exists(vismaskpath):
#        raise RuntimeError("Video File could not be found:"+vismaskpath)

#if not os.path.exists(pixpath):
#        raise RuntimeError("Video File could not be found:"+pixpath)



#---------------------------------------
# Set up parallel port
#---------------------------------------

port_adress= 0xD050

def send_trigger(trigger_code):
   	windll.inpout32.Out32(port_adress, trigger_code)
	core.wait(0.005) 
	windll.inpout32.Out32(port_adress, 0)

trig_fix=40
trig_fix_2 = 44
trig_space=60
trig_gabor = 70

#---------------------------------------
# Store info about the experiment session
#---------------------------------------
expName = 'MI_House_Face'  
expInfo = {'participant':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel  
expInfo['date'] = data.getDateStr()  # add a simple timestamp  
expInfo['expName'] = expName





# Experiment handler
thisExp = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
	originPath=None,
	savePickle=False, 
	saveWideText=False) #prevent the experiment handler to write expe data upon termination (and overwriting our files)
	

#--------------------------------------
# Load trial files 
#---------------------------------------
# read from csv file
trialList = data.importConditions(TRIALS_FILE, returnFieldNames=False)
trials = data.TrialHandler(trialList, nReps=1, method='sequential', extraInfo=expInfo)
trials.data.addDataType('respKey')
trials.data.addDataType('respTime')
trials.data.addDataType('stimOnset')
trials.data.addDataType('imOnset')
trials.data.addDataType('imStop')


#----------------
# Set up logging 
#----------------
globalClock = core.Clock()
respTime= core.Clock()
trialClock=core.Clock()

logging.console.setLevel(logging.DEBUG)
#
if not os.path.isdir('Logdata'):
    os.makedirs('Logdata')  # if this fails (e.g. permissions) we will get error
filename = 'Logdata' + os.path.sep + '%s' %(expInfo['participant'])
logging.setDefaultClock(globalClock)
logFileExp = logging.LogFile(filename +'.log', level=logging.EXP)
logging.console.setLevel(logging.DEBUG)  # this outputs to the screen, not a file

saveFilePrefix = expInfo['participant']

saveFile = "data/" + str(saveFilePrefix) + ' (' + time.strftime('%Y-%m-%d %H-%M-%S', time.localtime()) +').csv'  # Filename for csv. E.g. "myFolder/subj1_cond2 (2013-12-28 09-53-04).csv"

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

fix_cross = visual.TextStim(win =win, 
        ori =0, 
        name='fix_cross', 
        text= '+',
        font= 'Arial', 
        pos=[0,0],
        height = 0.06, 
        color=[0.5, 0.5, 0.5]
        )

fix_cross_trial = visual.TextStim(win =win, 
        ori =0, 
        name='fix_cross', 
        text= '+',
        font= 'Arial', 
        pos=[0,0],
        height = 0.06, 
        color=[0.5, 0.5, 0.5]
        )

fix_cross_trial_start = visual.TextStim(win =win, 
        ori =0, 
        name='fix_cross', 
        text= '+',
        font= 'Arial', 
        pos=[0,0],
        height = 0.06, 
        color=[0.5,-1, -1]
        )

#sqrVertices = [ [0.2,-0.3], [-0.2,-0.3], [-0.2,0.3], [0.2,0.3] ]

frame = visual.ImageStim(win =win, 
            image = stimpath + 'frame.png', 
            pos = [0,0], 
            size = [300, 400], 
            opacity = 1,
            units = 'pix', 
            
            )

vis_mask = visual.ImageStim(win =win, 
            image = stimpath + 'vis_mask.png', 
            pos = [0,0], 
            size = [300, 400], 
            opacity = 1,
            units = 'pix', 
            
            )
#---------------------------------------------------------------

duration = 1.5
keyStop = ['x']

#---------------------------------------
# Setup text messages
#--------------------------------------- 


#instrPracticeClock = core.Clock()
stim_block_instr = visual.TextStim(win=win, ori=0, name='image_instr',
    text="Pictures will be presented on the screen. Please watch them carefully. Press the key when you see the target ", font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='grey', colorSpace='rgb', opacity=1,
    depth=0.0)



imagery_block_instr = visual.TextStim(win=win, ori=0, name='clip_instr',
    text="You will see cues indicating which previously seen stimuli you will have to imagine. Press the key when you see the target", font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='grey', colorSpace='rgb', opacity=1,
    depth=0.0)


end_block = visual.TextStim(win=win, ori=0, name='end_bloc',
    text="You have finished this bloc, press any key to continue", font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='grey', colorSpace='rgb', opacity=1,
    depth=0.0)

theEnd = visual.TextStim(win=win, ori=0, name='theEnd',
    text="End of the training!", font='Arial',
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


#-------------------------------------------
# Set Keys for response and experiment flow 
#-------------------------------------------

mouse= event.Mouse()

#-------------------------------------------------------------
# Define rating scale and questionnaire after each MI trial 
#-------------------------------------------------------------



def percept_instruction():
    stim_block_instr.draw()
    #frame.autoDraw=False
    win.flip()
    core.wait(6)
    pause2.draw()
    win.flip()
    event.waitKeys()

def imagery_instruction():
    imagery_block_instr.draw()
    #frame.autoDraw=False
    win.flip()
    core.wait(6)
    pause2.draw()
    win.flip()
    
def end_block_instruction(trigg):
    end_block.draw()
    send_trigger(int(trigg))
    win.flip()
    event.waitKeys()

def fixation():
    frame.draw()
    fix_cross.draw()
    send_trigger(trig_fix)
    win.flip()
    core.wait(1.5)
#    core.wait(1)
    

def start_trial(fix_duration):
    #frame.draw()
    #fix_cross.draw()
   # send_trigger(trig_fix)
    #win.flip()
    #core.wait(0.5)
    #vis_mask.draw()
    #frame.draw()
    #send_trigger(trig_gabor)
    #win.flip()
    #core.wait(1)
    frame.draw()
    fix_cross_trial.draw()
    send_trigger(trig_fix)
    win.flip()
    core.wait(fix_duration)
    frame.draw()
    fix_cross_trial_start.draw()
    send_trigger(trig_fix_2)
    win.flip()
    core.wait(fix_duration)
    

def takepause(trigg):
    pause1.draw()
    win.flip()
    core.wait(10)
    pause2.draw()
    win.flip()
    event.waitKeys()

#------------------
# Show picture 
#------------------
def percept_run_trial(stimpath, stim, cue, fix_duration, stim_duration, trigg_cue, trigg_stim):
    pix = visual.ImageStim(win =win, 
            image = stimpath + stim, 
            pos = [0,0], 
            size = [280, 380], 
            opacity = 1,
            units = 'pix'
            )

    stim_cue = visual.ImageStim(win =win, 
                image = stimpath + cue, 
                pos = [0,0], 
                #size = [100, 100], 
                opacity = 1,
                units = 'pix'
                )
                
    fixation()
    frame.draw()
    stim_cue.draw()
    send_trigger(int(trigg_cue))
    win.flip()
    core.wait(0.5)
    start_trial(fix_duration)
    frame.draw()
    pix.draw()
    send_trigger(int(trigg_stim))
    win.flip()
    stimOnset= trialClock.getTime()
    core.wait(duration)
    trials.addData('stimOnset', stimOnset)
#    trials.addData('respTime',respTime)  

#------------------------
# Mental Imagery trial 
#------------------------
def imagery_run_trial(stim_path, cue, fix_duration, stim_duration, trigg_cue, trigg_stim):
    stim_cue = visual.ImageStim(win =win, 
                image = stimpath + cue, 
                pos = [0,0], 
                #size = [100, 100], 
                opacity = 1,
                units = 'pix'
                )
    fixation()
    frame.draw()
    stim_cue.draw()
    send_trigger(int(trigg_cue))
    win.flip()
    core.wait(0.5)
    start_trial(fix_duration)
    frame.draw()
    send_trigger(int(trigg_stim))
    win.flip()
    imOnset= trialClock.getTime()
    core.wait(stim_duration)

    trials.addData('imOnset', imOnset)
#    trials.addData('imStop', imStop)  



def catch_trial(stimpath, cue, trigg_catch):
    stim_cue = visual.ImageStim(win =win, 
                image = stimpath + cue, 
                pos = [0,0], 
                #size = [100, 100], 
                opacity = 1,
                units = 'pix'
                )
    
    fixation()
    stim_cue.draw()
    frame.draw()
    send_trigger(int(trigg_catch))
    win.flip()
    stimOnset= trialClock.getTime()
# get key press 
    event.waitKeys(maxWait=1, keyList=keyStop)
    send_trigger(trig_space)
    respTime= trialClock.getTime()

    trials.addData('stimOnset', stimOnset)
    trials.addData('respTime', respTime)


#-----------------
# Run Experiment
#----------------

for thisTrial in trials:
    win.setMouseVisible(False)
    if event.getKeys(keyList=['escape']):
        win.close()
        core.quit()

    elif thisTrial['Stim'] == 'START-BLOC' and thisTrial['Run'] == 'percept':
        send_trigger(int(thisTrial['Trigger_Stim']))
        percept_instruction()
    elif thisTrial['Stim'] == 'START-BLOC' and thisTrial['Run'] == 'imagery':
        send_trigger(int(thisTrial['Trigger_Stim']))
        imagery_instruction()
    elif thisTrial['Stim'] == 'break':
        takepause(int(thisTrial['Trigger_Stim']))
    elif thisTrial['Stim'] == 'END-BLOC':
        end_block_instruction(int(thisTrial['Trigger_Stim']))
    elif thisTrial['Cue'] == 'catch.png':
         catch_trial(stimpath, thisTrial['Cue'],thisTrial['Trigger_Cue'])
    elif thisTrial['Run'] == 'percept':
        percept_run_trial(stimpath, thisTrial['Stim'], thisTrial['Cue'], thisTrial['Fix_Duration'], thisTrial['Stim_Duration'], thisTrial['Trigger_Cue'], thisTrial['Trigger_Stim'])
    elif thisTrial['Run'] == 'imagery':
        imagery_run_trial(stimpath, thisTrial['Cue'], thisTrial['Fix_Duration'], thisTrial['Stim_Duration'],thisTrial['Trigger_Cue'], thisTrial['Trigger_Stim'])
   


theEnd.draw(win)
win.flip()
core.wait(3)
win.close()

trials.saveAsWideText(expInfo["participant"]  +".csv")
core.quit()






#---------------------------------------
# Store info about the experiment session
#---------------------------------------
expName = 'MI_House_Face'  
expInfo = {'participant':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel  
expInfo['date'] = data.getDateStr()  # add a simple timestamp  
expInfo['expName'] = expName


TRIALS_FILE = 'training.csv' 



# Experiment handler
thisExp = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
	originPath=None,
	savePickle=False, 
	saveWideText=False) #prevent the experiment handler to write expe data upon termination (and overwriting our files)
	

#--------------------------------------
# Load trial files 
#---------------------------------------
# read from csv file
trialList = data.importConditions(TRIALS_FILE, returnFieldNames=False)
trials = data.TrialHandler(trialList, nReps=1, method='sequential', extraInfo=expInfo)
trials.data.addDataType('respKey')
trials.data.addDataType('respTime')
trials.data.addDataType('stimOnset')
trials.data.addDataType('imOnset')
trials.data.addDataType('imStop')


#----------------
# Set up logging 
#----------------
globalClock = core.Clock()
respTime= core.Clock()
trialClock=core.Clock()

logging.console.setLevel(logging.DEBUG)
#
if not os.path.isdir('Logdata'):
    os.makedirs('Logdata')  # if this fails (e.g. permissions) we will get error
filename = 'Logdata' + os.path.sep + '%s' %(expInfo['participant'])
logging.setDefaultClock(globalClock)
logFileExp = logging.LogFile(filename +'.log', level=logging.EXP)
logging.console.setLevel(logging.DEBUG)  # this outputs to the screen, not a file

saveFilePrefix = expInfo['participant']

saveFile = "data/" + str(saveFilePrefix) + ' (' + time.strftime('%Y-%m-%d %H-%M-%S', time.localtime()) +').csv'  # Filename for csv. E.g. "myFolder/subj1_cond2 (2013-12-28 09-53-04).csv"

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

fix_cross = visual.TextStim(win =win, 
        ori =0, 
        name='fix_cross', 
        text= '+',
        font= 'Arial', 
        pos=[0,0],
        height = 0.06, 
        color=[0.5, 0.5, 0.5]
        )

fix_cross_trial = visual.TextStim(win =win, 
        ori =0, 
        name='fix_cross', 
        text= '+',
        font= 'Arial', 
        pos=[0,0],
        height = 0.06, 
        color=[0.5, 0.5, 0.5]
        )

fix_cross_trial_start = visual.TextStim(win =win, 
        ori =0, 
        name='fix_cross', 
        text= '+',
        font= 'Arial', 
        pos=[0,0],
        height = 0.06, 
        color=[0.5,-1, -1]
        )

#sqrVertices = [ [0.2,-0.3], [-0.2,-0.3], [-0.2,0.3], [0.2,0.3] ]

frame = visual.ImageStim(win =win, 
            image = stimpath + 'frame.png', 
            pos = [0,0], 
            size = [300, 400], 
            opacity = 1,
            units = 'pix', 
            
            )



#---------------------------------------------------------------

duration = 1.5
keyStop = ['space']

#---------------------------------------
# Setup text messages
#--------------------------------------- 


#instrPracticeClock = core.Clock()
stim_block_instr = visual.TextStim(win=win, ori=0, name='image_instr',
    text="Pictures will be presented on the screen. Please watch them carefully.Press [] when you see the target", font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='grey', colorSpace='rgb', opacity=1,
    depth=0.0)



imagery_block_instr = visual.TextStim(win=win, ori=0, name='clip_instr',
    text="You will see cues indicating which previously seen stimuli you will have to imagine. Press [] when you see the target", font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='grey', colorSpace='rgb', opacity=1,
    depth=0.0)


end_block = visual.TextStim(win=win, ori=0, name='end_bloc',
    text="You have finished this bloc, press [] to continue", font='Arial',
    pos=[0, 0], height=0.04, wrapWidth=None,
    color='grey', colorSpace='rgb', opacity=1,
    depth=0.0)

theEnd = visual.TextStim(win=win, ori=0, name='theEnd',
    text="End of the experiment, thank you !", font='Arial',
    pos=[0, 0], height=0.04, wrapWidth=None,
    color='grey', colorSpace='rgb', opacity=1,
    depth=0.0)

pause1 = visual.TextStim(win=win, ori=0, name='pause',
    text="Please take a short break.", font='Arial',
    pos=[0, 0], height=0.04, wrapWidth=None,
    color='grey', colorSpace='rgb', opacity=1,
    depth=0.0)

pause2 = visual.TextStim(win=win, ori=0, name='pause',
    text="Press any key to continue", font='Arial',
    pos=[0, 0], height=0.04, wrapWidth=None,
    color='grey', colorSpace='rgb', opacity=1,
    depth=0.0)


#-------------------------------------------
# Set Keys for response and experiment flow 
#-------------------------------------------
keyStop = ['x'] # indicate stop of movie clip and stop of mental imagery


mouse= event.Mouse()

#-------------------------------------------------------------
# Define rating scale and questionnaire after each MI trial 
#-------------------------------------------------------------

#-----------------
# Fixation cross 
#-----------------


def percept_instruction():
    stim_block_instr.draw()
    #frame.autoDraw=False
    win.flip()
    event.waitKeys(keyList=keyStop)

def imagery_instruction():
    imagery_block_instr.draw()
    #frame.autoDraw=False
    win.flip()
    event.waitKeys(keyList=keyStop)
    
def end_block_instruction():
    end_block.draw()
    #frame.autoDraw=False
    win.flip()
    event.waitKeys(keyList=keyStop)

def fixation():
    frame.draw()
    fix_cross.draw()
    win.flip()
    core.wait(1.5)
#    core.wait(1)
    

def start_trial(fix_duration):
    frame.draw()
    fix_cross_trial.draw()
    win.flip()
    core.wait(fix_duration-fix_duration*1/3)
    frame.draw()
    fix_cross_trial_start.draw()
    win.flip()
    core.wait(fix_duration-fix_duration*2/3)
    

def takepause():
    pause1.draw()
    win.flip()
    core.wait(10)
    pause2.draw()
    win.flip()
    event.waitKeys()

#------------------
# Show picture 
#------------------
def percept_run_trial(stimpath, stim, cue, fix_duration, stim_duration):
    pix = visual.ImageStim(win =win, 
            image = stimpath + stim, 
            pos = [0,0], 
            size = [280, 380], 
            opacity = 1,
            units = 'pix'
            )

    stim_cue = visual.ImageStim(win =win, 
                image = stimpath + cue, 
                pos = [0,0], 
                #size = [100, 100], 
                opacity = 1,
                units = 'pix'
                )
                
    fixation()
    frame.draw()
    stim_cue.draw()
    win.flip()
    core.wait(0.5)
    start_trial(fix_duration)
    frame.draw()
    pix.draw()
  #  win.logOnFlip('parallel port trigger picture: %d' %trigger_stim , level=logging.EXP)
    win.flip()
    stimOnset= trialClock.getTime()
    core.wait(duration)
    trials.addData('stimOnset', stimOnset)
#    trials.addData('respTime',respTime)  

#------------------------
# Mental Imagery trial 
#------------------------
def imagery_run_trial(stim_path, cue, fix_duration, stim_duration):
    stim_cue = visual.ImageStim(win =win, 
                image = stimpath + cue, 
                pos = [0,0], 
                #size = [100, 100], 
                opacity = 1,
                units = 'pix'
                )
    fixation()
    frame.draw()
    stim_cue.draw()
    win.flip()
    core.wait(0.5)
    start_trial(fix_duration)
    frame.draw()
  #  win.logOnFlip('parallel port trigger picture: %d' %trigger_stim , level=logging.EXP)
    win.flip()
    imOnset= trialClock.getTime()
    core.wait(stim_duration)

    trials.addData('imOnset', imOnset)
#    trials.addData('imStop', imStop)  



def catch_trial(stimpath, cue):
    stim_cue = visual.ImageStim(win =win, 
                image = stimpath + cue, 
                pos = [0,0], 
                #size = [100, 100], 
                opacity = 1,
                units = 'pix'
                )
    
    fixation()
    stim_cue.draw()
    frame.draw()
    win.flip()
    stimOnset= trialClock.getTime()
# get key press 
    event.waitKeys(maxWait=1, keyList=keyStop)
    respTime= trialClock.getTime()

    trials.addData('stimOnset', stimOnset)
    trials.addData('respTime', respTime)


#-----------------
# Run Experiment
#----------------

for thisTrial in trials:
    win.setMouseVisible(False)
    if thisTrial['Stim'] == 'START-BLOC' and thisTrial['Run'] == 'percept':
        percept_instruction()
    elif thisTrial['Stim'] == 'START-BLOC' and thisTrial['Run'] == 'imagery':
        imagery_instruction()
    elif thisTrial['Stim'] == 'break':
        takepause()
    elif thisTrial['Stim'] == 'END-BLOC':
        end_block_instruction()
    elif thisTrial['Cue'] == 'catch.png':
         catch_trial(stimpath, thisTrial['Cue'])
    elif thisTrial['Run'] == 'percept':
        percept_run_trial(stimpath, thisTrial['Stim'], thisTrial['Cue'], thisTrial['Fix_Duration'], thisTrial['Stim_Duration'])
    elif thisTrial['Run'] == 'imagery':
        imagery_run_trial(stimpath, thisTrial['Cue'], thisTrial['Fix_Duration'], thisTrial['Stim_Duration'])




theEnd.draw(win)
win.flip()
core.wait(3)
win.close()

trials.saveAsWideText(expInfo["participant"]  +".csv")
core.quit()





