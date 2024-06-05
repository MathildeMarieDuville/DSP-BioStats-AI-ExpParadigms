#Here, a Graphical User Interface (GUI) is designed in which the user can interact with (1) the keyboard to change the screen, '
#(2) the mouse to answer psychometric scales, or (3) to check boxes to inform the answer. All responses are stored in .txt and .csv files
#and are stored in a folder named "data" that is automatically created within the directory where this code is located. 
#To reduce computation time, the number of repetitions has been reduced to 2. To adjust it, change the variable "nReps" at line 520. 

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
expName = 'ScalesCheckBoxesAndKeyBoard'
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
    originPath='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\ScalesCheckBoxesAndKeyBoard.py',
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
    size=(1920, 1080), fullscr=True, screen=0, 
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
    text='¡Hola! Gracias por haber aceptado participar en este estudio. \n\nA continuación, varias series de palabras te serán presentadas. \nDespués de cada serie, por favor, úsa las escalas para evaluar: \n\n- la naturalidad,\n- la inteligibilidad,\n- la valencia, \n- la alerta, \n- la emoción \n\nAntes de empezar, asegúrate de no tener ninguna duda. Puedes preguntar lo que necesites al investigador principal. \n\nPresiona la tecla de espacio para comenzar.\n ',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instr = keyboard.Keyboard()

# Initialize components for Routine "escuchar"
escucharClock = core.Clock()
cruz = visual.ImageStim(
    win=win,
    name='cruz', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\cruz.png', mask=None,
    ori=0, pos=(0, 0), size=(0.6, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text = visual.TextStim(win=win, name='text',
    text='Presiona la tecla espacio cuando se haya acabado la serie de palabras\n',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "escalas1"
escalas1Clock = core.Clock()
robot = visual.ImageStim(
    win=win,
    name='robot', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\robot.png', mask=None,
    ori=0, pos=(0.20, 0.05), size=(0.07, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
cyborg = visual.ImageStim(
    win=win,
    name='cyborg', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\cyborg.jpg', mask=None,
    ori=0, pos=(0.44, 0.05), size=(0.07, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
human = visual.ImageStim(
    win=win,
    name='human', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\human.png', mask=None,
    ori=0, pos=(0.68, 0.05), size=(0.07, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
naturalidad = visual.TextStim(win=win, name='naturalidad',
    text='naturalidad',
    font='Arial',
    pos=(0.45, 0.15), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
nat = visual.RatingScale(win=win, name='nat', marker='triangle', size=0.9, pos=[0.5, -0.05], low=1, high=5, labels=[''], scale='', singleClick=True, showAccept=False)
tick = visual.ImageStim(
    win=win,
    name='tick', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\tick.png', mask=None,
    ori=0, pos=(-0.20, 0.05), size=(0.07, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
int2 = visual.ImageStim(
    win=win,
    name='int2', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\int2.png', mask=None,
    ori=0, pos=(-0.44, 0.05), size=(0.07, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
int1 = visual.ImageStim(
    win=win,
    name='int1', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\x.png', mask=None,
    ori=0, pos=(-0.68, 0.05), size=(0.07, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
inteligibilidad = visual.TextStim(win=win, name='inteligibilidad',
    text='inteligibilidad',
    font='Arial',
    pos=(-0.44, 0.15), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
int = visual.RatingScale(win=win, name='int', marker='triangle', size=0.9, pos=[-0.5, -0.05], low=1, high=5, labels=[''], scale='', singleClick=True, showAccept=False)
valencia = visual.TextStim(win=win, name='valencia',
    text='valencia',
    font='Arial',
    pos=(0.44, 0.45), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
val = visual.RatingScale(win=win, name='val', marker='triangle', size=0.9, pos=[0.5, 0.55], low=1, high=9, labels= [''], scale='', singleClick=True, showAccept=False)
val1 = visual.ImageStim(
    win=win,
    name='val1', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\valencia1.jpg', mask=None,
    ori=0, pos=(0.68, 0.35), size=(0.07, 0.07), 
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
val2 = visual.ImageStim(
    win=win,
    name='val2', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\valencia2.jpg', mask=None,
    ori=0, pos=(0.56, 0.35), size=(0.07, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
val3 = visual.ImageStim(
    win=win,
    name='val3', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\valencia3.jpg', mask=None,
    ori=0, pos=(0.44, 0.35), size=(0.07, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
val4 = visual.ImageStim(
    win=win,
    name='val4', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\valencia4.jpg', mask=None,
    ori=0, pos=(0.32, 0.35), size=(0.07, 0.07), 
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
val5 = visual.ImageStim(
    win=win,
    name='val5', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\valencia5.jpg', mask=None,
    ori=0, pos=(0.20, 0.35), size=(0.07, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
alerta = visual.TextStim(win=win, name='alerta',
    text='alerta',
    font='Arial',
    pos=(-0.44, 0.45), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
alert = visual.RatingScale(win=win, name='alert', marker='triangle', size=0.9, pos=[-0.5, 0.55], low=1, high=9, labels=[''], scale='', singleClick=True, showAccept=False)
alert1 = visual.ImageStim(
    win=win,
    name='alert1', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\alerta1.jpg', mask=None,
    ori=0, pos=(-0.20, 0.35), size=(0.07, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
alert2 = visual.ImageStim(
    win=win,
    name='alert2', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\alerta2.jpg', mask=None,
    ori=0, pos=(-0.32, 0.35), size=(0.07, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
alert3 = visual.ImageStim(
    win=win,
    name='alert3', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\alerta3.jpg', mask=None,
    ori=0, pos=(-0.44, 0.35), size=(0.07, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
alert4 = visual.ImageStim(
    win=win,
    name='alert4', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\alerta4.jpg', mask=None,
    ori=0, pos=(-0.56, 0.35), size=(0.07, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
alert5 = visual.ImageStim(
    win=win,
    name='alert5', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\alerta5.jpg', mask=None,
    ori=0, pos=(-0.68, 0.35), size=(0.07, 0.07),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
enojo = visual.Rect(
    win=win, name='enojo',
    width=(0.06, 0.06)[0], height=(0.06, 0.06)[1],
    ori=0, pos=(-0.33, -0.32),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-27.0, interpolate=True)
anger = visual.ImageStim(
    win=win,
    name='anger', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\enojo.jpg', mask=None,
    ori=0, pos=(-0.33, -0.23), size=(0.08, 0.08),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-28.0)
colère = visual.TextStim(win=win, name='colère',
    text='enojo',
    font='Arial',
    pos=(-0.33, -0.38), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-29.0);
disgusto = visual.Rect(
    win=win, name='disgusto',
    width=(0.06, 0.06)[0], height=(0.06, 0.06)[1],
    ori=0, pos=(0.55, -0.32),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-39.0, interpolate=True)
disgust = visual.ImageStim(
    win=win,
    name='happiness', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\disgusto.jpg', mask=None,
    ori=0, pos=(0.55, -0.23), size=(0.08, 0.08),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-40.0)
dégoût = visual.TextStim(win=win, name='dégoût',
    text='disgusto',
    font='Arial',
    pos=(0.55, -0.38), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-41.0);
miedo = visual.Rect(
    win=win, name='miedo',
    width=(0.06, 0.06)[0], height=(0.06, 0.06)[1],
    ori=0, pos=(0.11, -0.32),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-33.0, interpolate=True)
fear = visual.ImageStim(
    win=win,
    name='fear', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\miedo.jpg', mask=None,
    ori=0, pos=(0.11, -0.23), size=(0.08, 0.08),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-34.0)
peur = visual.TextStim(win=win, name='peur',
    text='miedo',
    font='Arial',
    pos=(0.11, -0.38), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-35.0);
felicidad = visual.Rect(
    win=win, name='felicidad',
    width=(0.06, 0.06)[0], height=(0.06, 0.06)[1],
    ori=0, pos=(0.33, -0.32),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-36.0, interpolate=True)
happiness = visual.ImageStim(
    win=win,
    name='happiness', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\felicidad.jpg', mask=None,
    ori=0, pos=(0.33, -0.23), size=(0.08, 0.08),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-37.0)
joie = visual.TextStim(win=win, name='joie',
    text='felicidad',
    font='Arial',
    pos=(0.33, -0.38), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-38.0);
tristeza = visual.Rect(
    win=win, name='tristeza',
    width=(0.06, 0.06)[0], height=(0.06, 0.06)[1],
    ori=0, pos=(-0.11, -0.32),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-30.0, interpolate=True)
sadness = visual.ImageStim(
    win=win,
    name='sadness', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\tristeza.jpg', mask=None,
    ori=0, pos=(-0.11, -0.23), size=(0.08, 0.08),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-31.0)
tristesse = visual.TextStim(win=win, name='tristesse',
    text='tristeza',
    font='Arial',
    pos=(-0.11, -0.38), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-32.0);
neutro = visual.Rect(
    win=win, name='neutro',
    width=(0.06, 0.06)[0], height=(0.06, 0.06)[1],
    ori=0, pos=(-0.55, -0.32),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-24.0, interpolate=True)
neutral = visual.ImageStim(
    win=win,
    name='neutro', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\GitHub\\PsychoPy\\ScalesCheckBoxesAndKeyBoard\\neutro.jpg', mask=None,
    ori=0, pos=(-0.55, -0.23), size=(0.08, 0.08),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)
neutre = visual.TextStim(win=win, name='neutre',
    text='neutro',
    font='Arial',
    pos=(-0.55, -0.38), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-26.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
clicked1 = []


# Initialize components for Routine "fin"
finClock = core.Clock()
gracias = visual.TextStim(win=win, name='gracias',
    text='                Fin de la sesión\n\n¡Muchas gracias por su participación!\n\n\n\n\n\nPresiona la tecla espacio para salir',
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
    #Screen shot
    #win.getMovieFrame()
    #win.saveMovieFrames('1_instrucciones.tif')

# -------Ending Routine "instrucciones"-------
for thisComponent in instruccionesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_instr.keys in ['', [], None]:  # No response was made
    key_resp_instr.keys = None
#thisExp.addData('key_resp_instr.keys',key_resp_instr.keys)
#if key_resp_instr.keys != None:  # we had a response
    #thisExp.addData('key_resp_instr.rt', key_resp_instr.rt)
thisExp.nextEntry()
# the Routine "instrucciones" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "escuchar"-------
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    # keep track of which components have finished
    escucharComponents = [cruz, text, key_resp_2]
    for thisComponent in escucharComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    escucharClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
        
    # -------Run Routine "escuchar"-------
    while continueRoutine:
        # get current time
        t = escucharClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=escucharClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cruz* updates
        if cruz.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cruz.frameNStart = frameN  # exact frame index
            cruz.tStart = t  # local t and not account for scr refresh
            cruz.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cruz, 'tStartRefresh')  # time at next scr refresh
            cruz.setAutoDraw(True)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_2.keys = theseKeys.name  # just the last key pressed
                key_resp_2.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in escucharComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "escuchar"-------
    for thisComponent in escucharComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #trials.addData('cruz.started', cruz.tStartRefresh)
    #trials.addData('cruz.stopped', cruz.tStopRefresh)
    #trials.addData('text.started', text.tStartRefresh)
    #trials.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    #trials.addData('key_resp_2.keys',key_resp_2.keys)
    #if key_resp_2.keys != None:  # we had a response
        #trials.addData('key_resp_2.rt', key_resp_2.rt)
    #trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    #trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "escuchar" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "escalas1"-------
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    nat.reset()
    int.reset()
    val.reset()
    alert.reset()
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    checkboxes = [enojo, disgusto, miedo, felicidad, tristeza, neutro]
    clicked1 = clicked1
    nb = 1
    
    
    # keep track of which components have finished
    escalas1Components = [robot, cyborg, human, naturalidad, nat, tick, int2, int1, inteligibilidad, int, valencia, val, val1, val2, val3, val4, val5, alerta, alert, alert1, alert2, alert3, alert4, alert5, enojo, anger, colère, disgusto, disgust, dégoût, miedo, fear, peur, felicidad, happiness, joie, tristeza, sadness, tristesse, neutro, neutral, neutre, mouse]
    for thisComponent in escalas1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    escalas1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    #Screen shot
    #win.getMovieFrame()
    #win.saveMovieFrames('1_escuchar.tif')

    
    # -------Run Routine "escalas1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = escalas1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=escalas1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *robot* updates
        if robot.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            robot.frameNStart = frameN  # exact frame index
            robot.tStart = t  # local t and not account for scr refresh
            robot.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(robot, 'tStartRefresh')  # time at next scr refresh
            robot.setAutoDraw(True)
        if robot.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > robot.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                robot.tStop = t  # not accounting for scr refresh
                robot.frameNStop = frameN  # exact frame index
                win.timeOnFlip(robot, 'tStopRefresh')  # time at next scr refresh
                robot.setAutoDraw(False)
        
        # *cyborg* updates
        if cyborg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cyborg.frameNStart = frameN  # exact frame index
            cyborg.tStart = t  # local t and not account for scr refresh
            cyborg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cyborg, 'tStartRefresh')  # time at next scr refresh
            cyborg.setAutoDraw(True)
        if cyborg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cyborg.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                cyborg.tStop = t  # not accounting for scr refresh
                cyborg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cyborg, 'tStopRefresh')  # time at next scr refresh
                cyborg.setAutoDraw(False)
        
        # *human* updates
        if human.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            human.frameNStart = frameN  # exact frame index
            human.tStart = t  # local t and not account for scr refresh
            human.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(human, 'tStartRefresh')  # time at next scr refresh
            human.setAutoDraw(True)
        if human.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > human.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                human.tStop = t  # not accounting for scr refresh
                human.frameNStop = frameN  # exact frame index
                win.timeOnFlip(human, 'tStopRefresh')  # time at next scr refresh
                human.setAutoDraw(False)
        
        # *naturalidad* updates
        if naturalidad.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            naturalidad.frameNStart = frameN  # exact frame index
            naturalidad.tStart = t  # local t and not account for scr refresh
            naturalidad.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(naturalidad, 'tStartRefresh')  # time at next scr refresh
            naturalidad.setAutoDraw(True)
        if naturalidad.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > naturalidad.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                naturalidad.tStop = t  # not accounting for scr refresh
                naturalidad.frameNStop = frameN  # exact frame index
                win.timeOnFlip(naturalidad, 'tStopRefresh')  # time at next scr refresh
                naturalidad.setAutoDraw(False)
        # *nat* updates
        if nat.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nat.frameNStart = frameN  # exact frame index
            nat.tStart = t  # local t and not account for scr refresh
            nat.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nat, 'tStartRefresh')  # time at next scr refresh
            nat.setAutoDraw(True)
        
        # *tick* updates
        if tick.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tick.frameNStart = frameN  # exact frame index
            tick.tStart = t  # local t and not account for scr refresh
            tick.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tick, 'tStartRefresh')  # time at next scr refresh
            tick.setAutoDraw(True)
        if tick.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tick.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                tick.tStop = t  # not accounting for scr refresh
                tick.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tick, 'tStopRefresh')  # time at next scr refresh
                tick.setAutoDraw(False)
        
        # *int2* updates
        if int2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            int2.frameNStart = frameN  # exact frame index
            int2.tStart = t  # local t and not account for scr refresh
            int2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(int2, 'tStartRefresh')  # time at next scr refresh
            int2.setAutoDraw(True)
        if int2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > int2.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                int2.tStop = t  # not accounting for scr refresh
                int2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(int2, 'tStopRefresh')  # time at next scr refresh
                int2.setAutoDraw(False)
        
        # *int1* updates
        if int1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            int1.frameNStart = frameN  # exact frame index
            int1.tStart = t  # local t and not account for scr refresh
            int1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(int1, 'tStartRefresh')  # time at next scr refresh
            int1.setAutoDraw(True)
        if int1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > int1.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                int1.tStop = t  # not accounting for scr refresh
                int1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(int1, 'tStopRefresh')  # time at next scr refresh
                int1.setAutoDraw(False)
        
        # *inteligibilidad* updates
        if inteligibilidad.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inteligibilidad.frameNStart = frameN  # exact frame index
            inteligibilidad.tStart = t  # local t and not account for scr refresh
            inteligibilidad.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inteligibilidad, 'tStartRefresh')  # time at next scr refresh
            inteligibilidad.setAutoDraw(True)
        if inteligibilidad.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > inteligibilidad.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                inteligibilidad.tStop = t  # not accounting for scr refresh
                inteligibilidad.frameNStop = frameN  # exact frame index
                win.timeOnFlip(inteligibilidad, 'tStopRefresh')  # time at next scr refresh
                inteligibilidad.setAutoDraw(False)
        # *int* updates
        if int.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            int.frameNStart = frameN  # exact frame index
            int.tStart = t  # local t and not account for scr refresh
            int.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(int, 'tStartRefresh')  # time at next scr refresh
            int.setAutoDraw(True)
        
        # *valencia* updates
        if valencia.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            valencia.frameNStart = frameN  # exact frame index
            valencia.tStart = t  # local t and not account for scr refresh
            valencia.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(valencia, 'tStartRefresh')  # time at next scr refresh
            valencia.setAutoDraw(True)
        if valencia.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > valencia.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                valencia.tStop = t  # not accounting for scr refresh
                valencia.frameNStop = frameN  # exact frame index
                win.timeOnFlip(valencia, 'tStopRefresh')  # time at next scr refresh
                valencia.setAutoDraw(False)
        # *val* updates
        if val.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            val.frameNStart = frameN  # exact frame index
            val.tStart = t  # local t and not account for scr refresh
            val.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(val, 'tStartRefresh')  # time at next scr refresh
            val.setAutoDraw(True)
        
        # *val1* updates
        if val1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            val1.frameNStart = frameN  # exact frame index
            val1.tStart = t  # local t and not account for scr refresh
            val1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(val1, 'tStartRefresh')  # time at next scr refresh
            val1.setAutoDraw(True)
        if val1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > val1.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                val1.tStop = t  # not accounting for scr refresh
                val1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(val1, 'tStopRefresh')  # time at next scr refresh
                val1.setAutoDraw(False)
        
        # *val2* updates
        if val2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            val2.frameNStart = frameN  # exact frame index
            val2.tStart = t  # local t and not account for scr refresh
            val2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(val2, 'tStartRefresh')  # time at next scr refresh
            val2.setAutoDraw(True)
        if val2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > val2.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                val2.tStop = t  # not accounting for scr refresh
                val2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(val2, 'tStopRefresh')  # time at next scr refresh
                val2.setAutoDraw(False)
        
        # *val3* updates
        if val3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            val3.frameNStart = frameN  # exact frame index
            val3.tStart = t  # local t and not account for scr refresh
            val3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(val3, 'tStartRefresh')  # time at next scr refresh
            val3.setAutoDraw(True)
        if val3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > val3.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                val3.tStop = t  # not accounting for scr refresh
                val3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(val3, 'tStopRefresh')  # time at next scr refresh
                val3.setAutoDraw(False)
        
        # *val4* updates
        if val4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            val4.frameNStart = frameN  # exact frame index
            val4.tStart = t  # local t and not account for scr refresh
            val4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(val4, 'tStartRefresh')  # time at next scr refresh
            val4.setAutoDraw(True)
        if val4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > val4.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                val4.tStop = t  # not accounting for scr refresh
                val4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(val4, 'tStopRefresh')  # time at next scr refresh
                val4.setAutoDraw(False)
        
        # *val5* updates
        if val5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            val5.frameNStart = frameN  # exact frame index
            val5.tStart = t  # local t and not account for scr refresh
            val5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(val5, 'tStartRefresh')  # time at next scr refresh
            val5.setAutoDraw(True)
        if val5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > val5.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                val5.tStop = t  # not accounting for scr refresh
                val5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(val5, 'tStopRefresh')  # time at next scr refresh
                val5.setAutoDraw(False)
        
        # *alerta* updates
        if alerta.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            alerta.frameNStart = frameN  # exact frame index
            alerta.tStart = t  # local t and not account for scr refresh
            alerta.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alerta, 'tStartRefresh')  # time at next scr refresh
            alerta.setAutoDraw(True)
        if alerta.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > alerta.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                alerta.tStop = t  # not accounting for scr refresh
                alerta.frameNStop = frameN  # exact frame index
                win.timeOnFlip(alerta, 'tStopRefresh')  # time at next scr refresh
                alerta.setAutoDraw(False)
        # *alert* updates
        if alert.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            alert.frameNStart = frameN  # exact frame index
            alert.tStart = t  # local t and not account for scr refresh
            alert.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alert, 'tStartRefresh')  # time at next scr refresh
            alert.setAutoDraw(True)
        
        # *alert1* updates
        if alert1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            alert1.frameNStart = frameN  # exact frame index
            alert1.tStart = t  # local t and not account for scr refresh
            alert1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alert1, 'tStartRefresh')  # time at next scr refresh
            alert1.setAutoDraw(True)
        if alert1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > alert1.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                alert1.tStop = t  # not accounting for scr refresh
                alert1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(alert1, 'tStopRefresh')  # time at next scr refresh
                alert1.setAutoDraw(False)
        
        # *alert2* updates
        if alert2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            alert2.frameNStart = frameN  # exact frame index
            alert2.tStart = t  # local t and not account for scr refresh
            alert2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alert2, 'tStartRefresh')  # time at next scr refresh
            alert2.setAutoDraw(True)
        if alert2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > alert2.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                alert2.tStop = t  # not accounting for scr refresh
                alert2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(alert2, 'tStopRefresh')  # time at next scr refresh
                alert2.setAutoDraw(False)
        
        # *alert3* updates
        if alert3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            alert3.frameNStart = frameN  # exact frame index
            alert3.tStart = t  # local t and not account for scr refresh
            alert3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alert3, 'tStartRefresh')  # time at next scr refresh
            alert3.setAutoDraw(True)
        if alert3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > alert3.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                alert3.tStop = t  # not accounting for scr refresh
                alert3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(alert3, 'tStopRefresh')  # time at next scr refresh
                alert3.setAutoDraw(False)
        
        # *alert4* updates
        if alert4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            alert4.frameNStart = frameN  # exact frame index
            alert4.tStart = t  # local t and not account for scr refresh
            alert4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alert4, 'tStartRefresh')  # time at next scr refresh
            alert4.setAutoDraw(True)
        if alert4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > alert4.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                alert4.tStop = t  # not accounting for scr refresh
                alert4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(alert4, 'tStopRefresh')  # time at next scr refresh
                alert4.setAutoDraw(False)
        
        # *alert5* updates
        if alert5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            alert5.frameNStart = frameN  # exact frame index
            alert5.tStart = t  # local t and not account for scr refresh
            alert5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alert5, 'tStartRefresh')  # time at next scr refresh
            alert5.setAutoDraw(True)
        if alert5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > alert5.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                alert5.tStop = t  # not accounting for scr refresh
                alert5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(alert5, 'tStopRefresh')  # time at next scr refresh
                alert5.setAutoDraw(False)
        
        # *enojo* updates
        if enojo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enojo.frameNStart = frameN  # exact frame index
            enojo.tStart = t  # local t and not account for scr refresh
            enojo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enojo, 'tStartRefresh')  # time at next scr refresh
            enojo.setAutoDraw(True)
        if enojo.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enojo.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                enojo.tStop = t  # not accounting for scr refresh
                enojo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enojo, 'tStopRefresh')  # time at next scr refresh
                enojo.setAutoDraw(False)
        
        # *anger* updates
        if anger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            anger.frameNStart = frameN  # exact frame index
            anger.tStart = t  # local t and not account for scr refresh
            anger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(anger, 'tStartRefresh')  # time at next scr refresh
            anger.setAutoDraw(True)
        if anger.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > anger.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                anger.tStop = t  # not accounting for scr refresh
                anger.frameNStop = frameN  # exact frame index
                win.timeOnFlip(anger, 'tStopRefresh')  # time at next scr refresh
                anger.setAutoDraw(False)
        
        # *colère* updates
        if colère.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            colère.frameNStart = frameN  # exact frame index
            colère.tStart = t  # local t and not account for scr refresh
            colère.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(colère, 'tStartRefresh')  # time at next scr refresh
            colère.setAutoDraw(True)
        if colère.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > colère.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                colère.tStop = t  # not accounting for scr refresh
                colère.frameNStop = frameN  # exact frame index
                win.timeOnFlip(colère, 'tStopRefresh')  # time at next scr refresh
                colère.setAutoDraw(False)
        
        # *disgusto* updates
        if disgusto.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            disgusto.frameNStart = frameN  # exact frame index
            disgusto.tStart = t  # local t and not account for scr refresh
            disgusto.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(disgusto, 'tStartRefresh')  # time at next scr refresh
            disgusto.setAutoDraw(True)
        if disgusto.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > disgusto.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                disgusto.tStop = t  # not accounting for scr refresh
                disgusto.frameNStop = frameN  # exact frame index
                win.timeOnFlip(disgusto, 'tStopRefresh')  # time at next scr refresh
                disgusto.setAutoDraw(False)
        
        # *disgust* updates
        if disgust.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            disgust.frameNStart = frameN  # exact frame index
            disgust.tStart = t  # local t and not account for scr refresh
            disgust.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(disgust, 'tStartRefresh')  # time at next scr refresh
            disgust.setAutoDraw(True)
        if disgust.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > disgust.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                disgust.tStop = t  # not accounting for scr refresh
                disgust.frameNStop = frameN  # exact frame index
                win.timeOnFlip(disgust, 'tStopRefresh')  # time at next scr refresh
                disgust.setAutoDraw(False)
        
        # *dégoût* updates
        if dégoût.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dégoût.frameNStart = frameN  # exact frame index
            dégoût.tStart = t  # local t and not account for scr refresh
            dégoût.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dégoût, 'tStartRefresh')  # time at next scr refresh
            dégoût.setAutoDraw(True)
        if dégoût.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dégoût.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                dégoût.tStop = t  # not accounting for scr refresh
                dégoût.frameNStop = frameN  # exact frame index
                win.timeOnFlip(dégoût, 'tStopRefresh')  # time at next scr refresh
                dégoût.setAutoDraw(False)
        
        # *miedo* updates
        if miedo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            miedo.frameNStart = frameN  # exact frame index
            miedo.tStart = t  # local t and not account for scr refresh
            miedo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(miedo, 'tStartRefresh')  # time at next scr refresh
            miedo.setAutoDraw(True)
        if miedo.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > miedo.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                miedo.tStop = t  # not accounting for scr refresh
                miedo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(miedo, 'tStopRefresh')  # time at next scr refresh
                miedo.setAutoDraw(False)
        
        # *fear* updates
        if fear.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fear.frameNStart = frameN  # exact frame index
            fear.tStart = t  # local t and not account for scr refresh
            fear.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fear, 'tStartRefresh')  # time at next scr refresh
            fear.setAutoDraw(True)
        if fear.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fear.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                fear.tStop = t  # not accounting for scr refresh
                fear.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fear, 'tStopRefresh')  # time at next scr refresh
                fear.setAutoDraw(False)
        
        # *peur* updates
        if peur.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            peur.frameNStart = frameN  # exact frame index
            peur.tStart = t  # local t and not account for scr refresh
            peur.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(peur, 'tStartRefresh')  # time at next scr refresh
            peur.setAutoDraw(True)
        if peur.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > peur.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                peur.tStop = t  # not accounting for scr refresh
                peur.frameNStop = frameN  # exact frame index
                win.timeOnFlip(peur, 'tStopRefresh')  # time at next scr refresh
                peur.setAutoDraw(False)
        
        # *felicidad* updates
        if felicidad.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            felicidad.frameNStart = frameN  # exact frame index
            felicidad.tStart = t  # local t and not account for scr refresh
            felicidad.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(felicidad, 'tStartRefresh')  # time at next scr refresh
            felicidad.setAutoDraw(True)
        if felicidad.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > felicidad.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                felicidad.tStop = t  # not accounting for scr refresh
                felicidad.frameNStop = frameN  # exact frame index
                win.timeOnFlip(felicidad, 'tStopRefresh')  # time at next scr refresh
                felicidad.setAutoDraw(False)
        
        # *happiness* updates
        if happiness.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            happiness.frameNStart = frameN  # exact frame index
            happiness.tStart = t  # local t and not account for scr refresh
            happiness.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(happiness, 'tStartRefresh')  # time at next scr refresh
            happiness.setAutoDraw(True)
        if happiness.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > happiness.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                happiness.tStop = t  # not accounting for scr refresh
                happiness.frameNStop = frameN  # exact frame index
                win.timeOnFlip(happiness, 'tStopRefresh')  # time at next scr refresh
                happiness.setAutoDraw(False)
        
        # *joie* updates
        if joie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            joie.frameNStart = frameN  # exact frame index
            joie.tStart = t  # local t and not account for scr refresh
            joie.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(joie, 'tStartRefresh')  # time at next scr refresh
            joie.setAutoDraw(True)
        if joie.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > joie.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                joie.tStop = t  # not accounting for scr refresh
                joie.frameNStop = frameN  # exact frame index
                win.timeOnFlip(joie, 'tStopRefresh')  # time at next scr refresh
                joie.setAutoDraw(False)
        
        # *tristeza* updates
        if tristeza.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tristeza.frameNStart = frameN  # exact frame index
            tristeza.tStart = t  # local t and not account for scr refresh
            tristeza.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tristeza, 'tStartRefresh')  # time at next scr refresh
            tristeza.setAutoDraw(True)
        if tristeza.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tristeza.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                tristeza.tStop = t  # not accounting for scr refresh
                tristeza.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tristeza, 'tStopRefresh')  # time at next scr refresh
                tristeza.setAutoDraw(False)
        
        # *sadness* updates
        if sadness.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sadness.frameNStart = frameN  # exact frame index
            sadness.tStart = t  # local t and not account for scr refresh
            sadness.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sadness, 'tStartRefresh')  # time at next scr refresh
            sadness.setAutoDraw(True)
        if sadness.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sadness.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                sadness.tStop = t  # not accounting for scr refresh
                sadness.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sadness, 'tStopRefresh')  # time at next scr refresh
                sadness.setAutoDraw(False)
        
        # *tristesse* updates
        if tristesse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tristesse.frameNStart = frameN  # exact frame index
            tristesse.tStart = t  # local t and not account for scr refresh
            tristesse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tristesse, 'tStartRefresh')  # time at next scr refresh
            tristesse.setAutoDraw(True)
        if tristesse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tristesse.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                tristesse.tStop = t  # not accounting for scr refresh
                tristesse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tristesse, 'tStopRefresh')  # time at next scr refresh
                tristesse.setAutoDraw(False)
        
        # *neutro* updates
        if neutro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            neutro.frameNStart = frameN  # exact frame index
            neutro.tStart = t  # local t and not account for scr refresh
            neutro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(neutro, 'tStartRefresh')  # time at next scr refresh
            neutro.setAutoDraw(True)
        if neutro.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > neutro.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                neutro.tStop = t  # not accounting for scr refresh
                neutro.frameNStop = frameN  # exact frame index
                win.timeOnFlip(neutro, 'tStopRefresh')  # time at next scr refresh
                neutro.setAutoDraw(False)
        
        # *neutral* updates
        if neutral.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            neutral.frameNStart = frameN  # exact frame index
            neutral.tStart = t  # local t and not account for scr refresh
            neutral.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(neutral, 'tStartRefresh')  # time at next scr refresh
            neutral.setAutoDraw(True)
        if neutral.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > neutral.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                neutral.tStop = t  # not accounting for scr refresh
                neutral.frameNStop = frameN  # exact frame index
                win.timeOnFlip(neutral, 'tStopRefresh')  # time at next scr refresh
                neutral.setAutoDraw(False)
        
        # *neutre* updates
        if neutre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            neutre.frameNStart = frameN  # exact frame index
            neutre.tStart = t  # local t and not account for scr refresh
            neutre.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(neutre, 'tStartRefresh')  # time at next scr refresh
            neutre.setAutoDraw(True)
        if neutre.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > neutre.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                neutre.tStop = t  # not accounting for scr refresh
                neutre.frameNStop = frameN  # exact frame index
                win.timeOnFlip(neutre, 'tStopRefresh')  # time at next scr refresh
                neutre.setAutoDraw(False)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                mouse.tStop = t  # not accounting for scr refresh
                mouse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse, 'tStopRefresh')  # time at next scr refresh
                mouse.status = FINISHED
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [enojo]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
        for box in checkboxes:
            if mouse.isPressedIn(box) and nb==1:
                box.color = "yellow"
                clicked1.append(box.name)
                nb = 0
        #win.getMovieFrame(buffer='back') 
       
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in escalas1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "escalas1"-------
    for thisComponent in escalas1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #trials.addData('robot.started', robot.tStartRefresh)
    #trials.addData('robot.stopped', robot.tStopRefresh)
    #trials.addData('cyborg.started', cyborg.tStartRefresh)
    #trials.addData('cyborg.stopped', cyborg.tStopRefresh)
    #trials.addData('human.started', human.tStartRefresh)
    #trials.addData('human.stopped', human.tStopRefresh)
    #trials.addData('naturalidad.started', naturalidad.tStartRefresh)
    #trials.addData('naturalidad.stopped', naturalidad.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('nat.response', nat.getRating())
    #trials.addData('tick.started', tick.tStartRefresh)
    #trials.addData('tick.stopped', tick.tStopRefresh)
    #trials.addData('int2.started', int2.tStartRefresh)
    #trials.addData('int2.stopped', int2.tStopRefresh)
    #trials.addData('int1.started', int1.tStartRefresh)
    #trials.addData('int1.stopped', int1.tStopRefresh)
    #trials.addData('inteligibilidad.started', inteligibilidad.tStartRefresh)
    #trials.addData('inteligibilidad.stopped', inteligibilidad.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('int.response', int.getRating())
    #trials.addData('int.started', int.tStart)
    #trials.addData('int.stopped', int.tStop)
    #trials.addData('valencia.started', valencia.tStartRefresh)
    #trials.addData('valencia.stopped', valencia.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('val.response', val.getRating())
    #trials.addData('val.started', val.tStart)
    #trials.addData('val.stopped', val.tStop)
    #trials.addData('val1.started', val1.tStartRefresh)
    #trials.addData('val1.stopped', val1.tStopRefresh)
    #trials.addData('val2.started', val2.tStartRefresh)
    #trials.addData('val2.stopped', val2.tStopRefresh)
    #trials.addData('val3.started', val3.tStartRefresh)
    #trials.addData('val3.stopped', val3.tStopRefresh)
    #trials.addData('val4.started', val4.tStartRefresh)
    #trials.addData('val4.stopped', val4.tStopRefresh)
    #trials.addData('val5.started', val5.tStartRefresh)
    #trials.addData('val5.stopped', val5.tStopRefresh)
    #trials.addData('alerta.started', alerta.tStartRefresh)
    #trials.addData('alerta.stopped', alerta.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('alert.response', alert.getRating())
    #trials.addData('alert.started', alert.tStart)
    #trials.addData('alert.stopped', alert.tStop)
    #trials.addData('alert1.started', alert1.tStartRefresh)
    #trials.addData('alert1.stopped', alert1.tStopRefresh)
    #trials.addData('alert2.started', alert2.tStartRefresh)
    #trials.addData('alert2.stopped', alert2.tStopRefresh)
    #trials.addData('alert3.started', alert3.tStartRefresh)
    #trials.addData('alert3.stopped', alert3.tStopRefresh)
    #trials.addData('alert4.started', alert4.tStartRefresh)
    #trials.addData('alert4.stopped', alert4.tStopRefresh)
    #trials.addData('alert5.started', alert5.tStartRefresh)
    #trials.addData('alert5.stopped', alert5.tStopRefresh)
    #trials.addData('anger.started', anger.tStartRefresh)
    #trials.addData('anger.stopped', anger.tStopRefresh)
    #trials.addData('colère.started', colère.tStartRefresh)
    #trials.addData('colère.stopped', colère.tStopRefresh)
    #trials.addData('disgust.started', disgust.tStartRefresh)
    #trials.addData('disgust.stopped', disgust.tStopRefresh)
    #trials.addData('dégoût.started', dégoût.tStartRefresh)
    #trials.addData('dégoût.stopped', dégoût.tStopRefresh)
    #trials.addData('fear.started', fear.tStartRefresh)
    #trials.addData('fear.stopped', fear.tStopRefresh)
    #trials.addData('peur.started', peur.tStartRefresh)
    #trials.addData('peur.stopped', peur.tStopRefresh)
    #trials.addData('happiness.started', happiness.tStartRefresh)
    #trials.addData('happiness.stopped', happiness.tStopRefresh)
    #trials.addData('joie.started', joie.tStartRefresh)
    #trials.addData('joie.stopped', joie.tStopRefresh)
    #trials.addData('sadness.started', sadness.tStartRefresh)
    #trials.addData('sadness.stopped', sadness.tStopRefresh)
    #trials.addData('tristesse.started', tristesse.tStartRefresh)
    #trials.addData('tristesse.stopped', tristesse.tStopRefresh)
    #trials.addData('neutral.started', neutral.tStartRefresh)
    #trials.addData('neutral.stopped', neutral.tStopRefresh)
    #trials.addData('neutre.started', neutre.tStartRefresh)
    #trials.addData('neutre.stopped', neutre.tStopRefresh)
    # store data for trials (TrialHandler)
    #trials.addData('mouse.x', mouse.x)
    #trials.addData('mouse.y', mouse.y)
    #trials.addData('mouse.leftButton', mouse.leftButton)
    #trials.addData('mouse.midButton', mouse.midButton)
    #trials.addData('mouse.rightButton', mouse.rightButton)
    #trials.addData('mouse.time', mouse.time)
    #trials.addData('mouse.clicked_name', mouse.clicked_name)
    for box in checkboxes:
        box.color = "grey"
        if nb == 1:
            clicked1.append('none')
            nb = 0

    thisExp.nextEntry()

    #win.saveMovieFrames(fileName='1_video.mp4')
    #Screen shot
    #win.getMovieFrame()
    #win.saveMovieFrames('1_escalas.tif')

    
# completed 2 repeats of 'trials'


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
#thisExp.addData('gracias.started', gracias.tStartRefresh)
#thisExp.addData('gracias.stopped', gracias.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
#thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
#thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "fin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
data = [clicked1]

np.savetxt(filename+'-checkboxes.txt', data, delimiter = "\n", fmt= "%s", encoding='utf-8')

#Screen shot
#win.getMovieFrame()
#win.saveMovieFrames('1_fin.tif')

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'-scales.csv')
#thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()