#Here, a Graphical User Interface (GUI) is designed in which the user can answer the Spanish version of the 
#Spanish version of the Edinburgh Handedness Inventory (Albayay J, Villarroel-Gruner P, Bascour-Sandoval C, Parma V, Gálvez-
#García G. Psychometric properties of the Spanish version of the Edinburgh
#Handedness Inventory in a sample of Chilean undergraduates.Brain Cogn. 2019;137:103618.)

#All responses are stored in a .csv file
#and are stored in a folder named "data" that is automatically created within the directory where this code is located. 


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'Handedness'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\EdinburghHandednessInventory\\Handedness.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(2256, 1504), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instrucciones"
instruccionesClock = core.Clock()
instr = visual.TextStim(win=win, name='instr',
    text='¡Hola! Gracias por haber aceptado participar en este estudio. \n\nPor favor, indica tus preferencias en el uso de las manos en las siguientes actividades.\n\nAlgunas de las actividades requieren de ambas manos.\nEn estos casos, la parte de la tarea u objeto para la cual se busca la preferencia manual se indica entre paréntesis.\n\nPresiona la tecla de espacio para comenzar.\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instr = keyboard.Keyboard()

# Initialize components for Routine "Edinburgh_Handedness_Inventory"
Edinburgh_Handedness_InventoryClock = core.Clock()

writing = visual.TextStim(win=win, name='writing',
    text='escribir',
    font='Arial',
    pos=(-0.37, 0.44), height=0.03, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

escribir = visual.RatingScale(win=win, name='escribir', marker='triangle', size=1.0, pos=[-0.5, 0.75], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.5, choices = ['Siempre \nderecha', 'Usualmente \nderecha', 'Ambas \npor igual', 'Usualmente \nizquierda', 'Siempre \nizquierda'], scale='', singleClick=True, showAccept=False)

draw = visual.TextStim(win=win, name='draw',
    text='dibujar',
    font='Arial',
    pos=(0.37, 0.44), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

dibujar = visual.RatingScale(win=win, name='dibujar', marker='triangle', size=1.0, pos=[0.5, 0.75], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.5, choices = ['Siempre \nderecha', 'Usualmente \nderecha', 'Ambas \npor igual', 'Usualmente \nizquierda', 'Siempre \nizquierda'], scale='', singleClick=True, showAccept=False)

throw = visual.TextStim(win=win, name='throw',
    text='lanzar',
    font='Arial',
    pos=(-0.37, 0.27), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

lanzar = visual.RatingScale(win=win, name='lanzar', marker='triangle', size=1.0, pos=[-0.5, 0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.5, choices = ['Siempre \nderecha', 'Usualmente \nderecha', 'Ambas \npor igual', 'Usualmente \nizquierda', 'Siempre \nizquierda'], scale='', singleClick=True, showAccept=False)

scissors = visual.TextStim(win=win, name='scissors',
    text='tijeras',
    font='Arial',
    pos=(0.37, 0.27), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

tijeras = visual.RatingScale(win=win, name='tijeras', marker='triangle', size=1.0, pos=[0.5, 0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.5, choices = ['Siempre \nderecha', 'Usualmente \nderecha', 'Ambas \npor igual', 'Usualmente \nizquierda', 'Siempre \nizquierda'], scale='', singleClick=True, showAccept=False)

toothbrush = visual.TextStim(win=win, name='toothbrush',
    text='cepillo de dientes',
    font='Arial',
    pos=(-0.37, 0.10), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

cepillo = visual.RatingScale(win=win, name='cepillo', marker='triangle', size=1.0, pos=[-0.5, 0.05], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.5, choices = ['Siempre \nderecha', 'Usualmente \nderecha', 'Ambas \npor igual', 'Usualmente \nizquierda', 'Siempre \nizquierda'], scale='', singleClick=True, showAccept=False)

knife = visual.TextStim(win=win, name='knife',
    text='cuchillo (sin tenedor)',
    font='Arial',
    pos=(0.37, 0.10), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

cuchillo = visual.RatingScale(win=win, name='cuchillo', marker='triangle', size=1.0, pos=[0.5, 0.05], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.5, choices = ['Siempre \nderecha', 'Usualmente \nderecha', 'Ambas \npor igual', 'Usualmente \nizquierda', 'Siempre \nizquierda'], scale='', singleClick=True, showAccept=False)

spoon = visual.TextStim(win=win, name='spoon',
    text='cuchara',
    font='Arial',
    pos=(-0.37, -0.08), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

cuchara = visual.RatingScale(win=win, name='cuchara', marker='triangle', size=1.0, pos=[-0.5, -0.30], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.5, choices = ['Siempre \nderecha', 'Usualmente \nderecha', 'Ambas \npor igual', 'Usualmente \nizquierda', 'Siempre \nizquierda'], scale='', singleClick=True, showAccept=False)

broom = visual.TextStim(win=win, name='broom',
    text='escoba (mano superior)',
    font='Arial',
    pos=(0.37, -0.08), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

escoba = visual.RatingScale(win=win, name='escoba', marker='triangle', size=1.0, pos=[0.5, -0.30], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.5, choices = ['Siempre \nderecha', 'Usualmente \nderecha', 'Ambas \npor igual', 'Usualmente \nizquierda', 'Siempre \nizquierda'], scale='', singleClick=True, showAccept=False)

match= visual.TextStim(win=win, name='match',
    text='encender un fósforo (fósforo)',
    font='Arial',
    pos=(-0.37, -0.25), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

fosforo = visual.RatingScale(win=win, name='fosforo', marker='triangle', size=1.0, pos=[-0.5, -0.65], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.5, choices = ['Siempre \nderecha', 'Usualmente \nderecha', 'Ambas \npor igual', 'Usualmente \nizquierda', 'Siempre \nizquierda'], scale='', singleClick=True, showAccept=False)

box = visual.TextStim(win=win, name='box',
    text='abrir una caja (tapa)',
    font='Arial',
    pos=(0.37, -0.25), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

caja = visual.RatingScale(win=win, name='caja', marker='triangle', size=1.0, pos=[0.5, -0.65], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.5, choices = ['Siempre \nderecha', 'Usualmente \nderecha', 'Ambas \npor igual', 'Usualmente \nizquierda', 'Siempre \nizquierda'], scale='', singleClick=True, showAccept=False)


instr_2 = visual.TextStim(win=win, name='instr_2',
    text='Presiona la tecla de espacio cuando hayas terminado de contestar',
    font='Arial',
    pos=(0, -0.45), height=0.03, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instr_2 = keyboard.Keyboard()

# Initialize components for Routine "fin"
finClock = core.Clock()
gracias = visual.TextStim(win=win, name='gracias',
    text='\n\n¡Muchas gracias por tu respuesta!\n\n\n\n\n\nPresiona la tecla espacio para salir',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instrucciones"-------
# update component parameters for each repeat
key_resp_instr.keys = []
key_resp_instr.rt = []
# keep track of which components have finished
instruccionesComponents = [instr, key_resp_instr]
for thisComponent in instruccionesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruccionesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instrucciones"-------
while continueRoutine:
    # get current time
    t = instruccionesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruccionesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr* updates
    if instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr.frameNStart = frameN  # exact frame index
        instr.tStart = t  # local t and not account for scr refresh
        instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr, 'tStartRefresh')  # time at next scr refresh
        instr.setAutoDraw(True)
    
    # *key_resp_instr* updates
    waitOnFlip = False
    if key_resp_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instr.frameNStart = frameN  # exact frame index
        key_resp_instr.tStart = t  # local t and not account for scr refresh
        key_resp_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instr, 'tStartRefresh')  # time at next scr refresh
        key_resp_instr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instr.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instr.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_instr.keys = theseKeys.name  # just the last key pressed
            key_resp_instr.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruccionesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrucciones"-------
for thisComponent in instruccionesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_instr.keys in ['', [], None]:  # No response was made
    key_resp_instr.keys = None
thisExp.addData('key_resp_instr.keys',key_resp_instr.keys)
if key_resp_instr.keys != None:  # we had a response
    thisExp.addData('key_resp_instr.rt', key_resp_instr.rt)
thisExp.nextEntry()
# the Routine "instrucciones" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Edinburgh_Handedness_Inventory"-------
# update component parameters for each repeat
escribir.reset()
dibujar.reset()
key_resp_instr_2.keys = []
key_resp_instr_2.rt = []
# keep track of which components have finished
Edinburgh_Handedness_InventoryComponents = [writing, escribir, draw, dibujar, throw, lanzar, scissors, tijeras, toothbrush, cepillo, knife, cuchillo, spoon, cuchara, broom, escoba, match, fosforo, box, caja, instr_2, key_resp_instr_2]
for thisComponent in Edinburgh_Handedness_InventoryComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Edinburgh_Handedness_InventoryClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Edinburgh_Handedness_Inventory"-------
while continueRoutine:
    # get current time
    t = Edinburgh_Handedness_InventoryClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Edinburgh_Handedness_InventoryClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *writing* updates
    if writing.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        writing.frameNStart = frameN  # exact frame index
        writing.tStart = t  # local t and not account for scr refresh
        writing.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(writing, 'tStartRefresh')  # time at next scr refresh
        writing.setAutoDraw(True)
    
    # *escribir* updates
    if escribir.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        escribir.frameNStart = frameN  # exact frame index
        escribir.tStart = t  # local t and not account for scr refresh
        escribir.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(escribir, 'tStartRefresh')  # time at next scr refresh
        escribir.setAutoDraw(True)
        
    # *draw* updates
    if draw.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        draw.frameNStart = frameN  # exact frame index
        draw.tStart = t  # local t and not account for scr refresh
        draw.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(draw, 'tStartRefresh')  # time at next scr refresh
        draw.setAutoDraw(True)

    # *dibujar* updates
    if dibujar.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        dibujar.frameNStart = frameN  # exact frame index
        dibujar.tStart = t  # local t and not account for scr refresh
        dibujar.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dibujar, 'tStartRefresh')  # time at next scr refresh
        dibujar.setAutoDraw(True)
        
    # *throw* updates
    if throw.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        throw.frameNStart = frameN  # exact frame index
        throw.tStart = t  # local t and not account for scr refresh
        throw.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(throw, 'tStartRefresh')  # time at next scr refresh
        throw.setAutoDraw(True)

    # *lanzar* updates
    if lanzar.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        lanzar.frameNStart = frameN  # exact frame index
        lanzar.tStart = t  # local t and not account for scr refresh
        lanzar.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lanzar, 'tStartRefresh')  # time at next scr refresh
        lanzar.setAutoDraw(True)

    # *scissors* updates
    if scissors.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        scissors.frameNStart = frameN  # exact frame index
        scissors.tStart = t  # local t and not account for scr refresh
        scissors.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(throw, 'tStartRefresh')  # time at next scr refresh
        scissors.setAutoDraw(True)

    # *tijeras* updates
    if tijeras.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tijeras.frameNStart = frameN  # exact frame index
        tijeras.tStart = t  # local t and not account for scr refresh
        tijeras.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tijeras, 'tStartRefresh')  # time at next scr refresh
        tijeras.setAutoDraw(True)
        
     # *toothbrush* updates
    if toothbrush.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        toothbrush.frameNStart = frameN  # exact frame index
        toothbrush.tStart = t  # local t and not account for scr refresh
        toothbrush.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(toothbrush, 'tStartRefresh')  # time at next scr refresh
        toothbrush.setAutoDraw(True)

    # *cepillo* updates
    if cepillo.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cepillo.frameNStart = frameN  # exact frame index
        cepillo.tStart = t  # local t and not account for scr refresh
        cepillo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cepillo, 'tStartRefresh')  # time at next scr refresh
        cepillo.setAutoDraw(True)

    # *spoon* updates
    if spoon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spoon.frameNStart = frameN  # exact frame index
        spoon.tStart = t  # local t and not account for scr refresh
        spoon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spoon, 'tStartRefresh')  # time at next scr refresh
        spoon.setAutoDraw(True)

    # *cuchara* updates
    if cuchara.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cuchara.frameNStart = frameN  # exact frame index
        cuchara.tStart = t  # local t and not account for scr refresh
        cuchara.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cuchara, 'tStartRefresh')  # time at next scr refresh
        cuchara.setAutoDraw(True)
        
     # *knife* updates
    if knife.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        knife.frameNStart = frameN  # exact frame index
        knife.tStart = t  # local t and not account for scr refresh
        knife.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(knife, 'tStartRefresh')  # time at next scr refresh
        knife.setAutoDraw(True)

    # *cuchillo* updates
    if cuchillo.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cuchillo.frameNStart = frameN  # exact frame index
        cuchillo.tStart = t  # local t and not account for scr refresh
        cuchillo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cuchillo, 'tStartRefresh')  # time at next scr refresh
        cuchillo.setAutoDraw(True)

    # *broom* updates
    if broom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        broom.frameNStart = frameN  # exact frame index
        broom.tStart = t  # local t and not account for scr refresh
        broom.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(broom, 'tStartRefresh')  # time at next scr refresh
        broom.setAutoDraw(True)

    # *escoba* updates
    if escoba.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        escoba.frameNStart = frameN  # exact frame index
        escoba.tStart = t  # local t and not account for scr refresh
        escoba.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(escoba, 'tStartRefresh')  # time at next scr refresh
        escoba.setAutoDraw(True)
        
    # *match* updates
    if match.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        match.frameNStart = frameN  # exact frame index
        match.tStart = t  # local t and not account for scr refresh
        match.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(match, 'tStartRefresh')  # time at next scr refresh
        match.setAutoDraw(True)

    # *fosforo* updates
    if fosforo.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fosforo.frameNStart = frameN  # exact frame index
        fosforo.tStart = t  # local t and not account for scr refresh
        fosforo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fosforo, 'tStartRefresh')  # time at next scr refresh
        fosforo.setAutoDraw(True)
        
    # *box* updates
    if box.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        box.frameNStart = frameN  # exact frame index
        box.tStart = t  # local t and not account for scr refresh
        box.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(box, 'tStartRefresh')  # time at next scr refresh
        box.setAutoDraw(True)

    # *caja* updates
    if caja.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        caja.frameNStart = frameN  # exact frame index
        caja.tStart = t  # local t and not account for scr refresh
        caja.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(caja, 'tStartRefresh')  # time at next scr refresh
        caja.setAutoDraw(True)

    # *instr_2* updates
    if instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_2.frameNStart = frameN  # exact frame index
        instr_2.tStart = t  # local t and not account for scr refresh
        instr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_2, 'tStartRefresh')  # time at next scr refresh
        instr_2.setAutoDraw(True)
    
    # *key_resp_instr_2* updates
    waitOnFlip = False
    if key_resp_instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instr_2.frameNStart = frameN  # exact frame index
        key_resp_instr_2.tStart = t  # local t and not account for scr refresh
        key_resp_instr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instr_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_instr_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instr_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instr_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instr_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instr_2.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_instr_2.keys = theseKeys.name  # just the last key pressed
            key_resp_instr_2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Edinburgh_Handedness_InventoryComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Edinburgh_Handedness_Inventory"-------
for thisComponent in Edinburgh_Handedness_InventoryComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('escribir.response', escribir.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('dibujar.response', dibujar.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('lanzar.response', lanzar.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('tijeras.response', tijeras.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('cepillo.response', cepillo.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('cuchillo.response', cuchillo.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('cuchara.response', cuchara.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('escoba.response', escoba.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('fosforo.response', fosforo.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('caja.response', caja.getRating())
thisExp.nextEntry()

# check responses
if key_resp_instr_2.keys in ['', [], None]:  # No response was made
    key_resp_instr_2.keys = None
thisExp.addData('key_resp_instr_2.keys',key_resp_instr_2.keys)
if key_resp_instr_2.keys != None:  # we had a response
    thisExp.addData('key_resp_instr_2.rt', key_resp_instr_2.rt)
thisExp.nextEntry()
# the Routine "Edinburgh_Handedness_Inventory" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fin"-------
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
# keep track of which components have finished
finComponents = [gracias, key_resp_3]
for thisComponent in finComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "fin"-------
while continueRoutine:
    # get current time
    t = finClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *gracias* updates
    if gracias.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gracias.frameNStart = frameN  # exact frame index
        gracias.tStart = t  # local t and not account for scr refresh
        gracias.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gracias, 'tStartRefresh')  # time at next scr refresh
        gracias.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_3.keys = theseKeys.name  # just the last key pressed
            key_resp_3.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fin"-------
for thisComponent in finComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('gracias.started', gracias.tStartRefresh)
thisExp.addData('gracias.stopped', gracias.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "fin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
