'''
Generate trial list for Visemi experiment: present pictures and videos with associated visual masks
'''
from psychopy import  gui, data


import random
import os
import csv
import numpy as np

expName = 'MI_House_Face'  
expInfo = {'participant':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel  
expInfo['date'] = data.getDateStr()  # add a simple timestamp  
expInfo['expName'] = expName


stim_path = 'C:\\Users\\Claire\\Desktop\\Face-House\\Stimuli\\'
n_trials = 300
n_bloc= 6

n_trial_per_bloc = n_trials/n_bloc

STIM1 = 'stim3.gif'
STIM2 = 'stim1.gif'


CUE1 = 'cue1.png'
CUE2 = 'cue2.png'
PAUSE= 'break'
CATCH = 'catch.png'

blocks=['percept', 'imagery']* (n_bloc/2)

# Triggers
trig_cue1 = 10
trig_cue2 = 20
trig_catch = 30
trig_break = 550
trig_start = 500
trig_end = 555


with open(  'trial_list_' + 'subj_' + expInfo["participant"] + '.csv','wb') as out:
        csv_out = csv.writer(out, delimiter = ",")
        csv_out.writerow([ 'Run', 'Cue', 'Stim', 'Fix_Duration','Stim_Duration', 'Trigger_Cue', 'Trigger_Stim' ])
    
        for block in blocks:
            if block in 'percept':
                trig_stim1 = 101
                trig_stim2 = 102
            elif block in 'imagery':
                trig_stim1 = 202
                trig_stim2 = 201
           
            trial_list=[[CUE1, STIM1, trig_cue1, trig_stim1],[CUE2, STIM2, trig_cue2, trig_stim2]]*(n_trial_per_bloc/2)
            
            trial_list += [[CATCH,"", trig_catch, "" ]] * int(0.10 * len(trial_list))
            
            #list_catch = [CATCH ]* (len(trial_list)/100*20)
            
            random.shuffle(trial_list)
            
            ok = False
            while not ok:
                ok = True
                prev = trial_list[0]
                for i, t in enumerate(trial_list[1:]):
                    if prev == [CATCH, " ", trig_catch, "" ] and (prev == t or prev == trial_list[i + 2]):
                        ok = False
                        random.shuffle(trial_list)
                        break
                    prev = t
                
                
            
            #for i in range(1,len(trial_list)+10, len(trial_list)/10):
            #    if i!=1:
            trial_list.insert(n_trial_per_bloc/2,["", PAUSE, "", trig_break])
            
            trial_list.insert(0, ["", 'START-BLOC', "", trig_start])
            trial_list += [["", 'END-BLOC', "", trig_end]]
                
            
            stim_duration = np.random.uniform(low=1.9, high=2.2, size=(len(trial_list)))
            fix_duration = np.random.uniform(low=0.9, high=1.2, size=(len(trial_list)))
            
        
            
            if 'percept' in block:
                run = ['percept'] * len(trial_list)
            else:
                run = ['imagery'] * len(trial_list)
                
            cues, stims, trig_cue, trig_stim = zip(*trial_list)
            complete = zip(run,  cues, stims, fix_duration, stim_duration, trig_cue, trig_stim)
            
            ## write csv
            
            
            for row in complete:
                csv_out.writerow(row)
    








