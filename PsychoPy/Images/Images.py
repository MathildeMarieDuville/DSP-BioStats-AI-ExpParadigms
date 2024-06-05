#Here, images from the International Affective Picture System (IAPS) are presented 
#on a black background with size 20 × 20 degrees of visual angle.
#Each image stays on screen for 5 s before the following picture appears. This scenario lasts 9 minutes.

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
expName = 'Images'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images.py',
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
    winType='pyglet', allowGUI=False, allowStencil=False,
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

# Initialize components for Routine "Instrucciones"
InstruccionesClock = core.Clock()
instr = visual.TextStim(win=win, name='instr',
    text='A continuación, verás una serie de imágenes en la pantalla.\n\nPor favor, obsérvalas fijamente. \n\n\n                        ¡Mucha suerte!\n\n\nPresiona la barra de espacio para comenzar.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instr = keyboard.Keyboard()

# Initialize components for Routine "Imagenes_1"
Imagenes_1Clock = core.Clock()
imagen_7211 = visual.ImageStim(
    win=win,
    name='imagen_7211', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7211.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
imagen_7620 = visual.ImageStim(
    win=win,
    name='imagen_7620', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7620.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
imagen_7092 = visual.ImageStim(
    win=win,
    name='imagen_7092', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7092.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
imagen_9472 = visual.ImageStim(
    win=win,
    name='imagen_9472', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\9472.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
imagen_7188 = visual.ImageStim(
    win=win,
    name='imagen_7188', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7188.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
imagen_5395 = visual.ImageStim(
    win=win,
    name='imagen_5395', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5395.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
imagen_7632 = visual.ImageStim(
    win=win,
    name='imagen_7632', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7632.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
imagen_8211 = visual.ImageStim(
    win=win,
    name='imagen_8211', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\8211.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
imagen_5455 = visual.ImageStim(
    win=win,
    name='imagen_5455', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5455.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
imagen_7496 = visual.ImageStim(
    win=win,
    name='imagen_7496', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7496.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
imagen_7402 = visual.ImageStim(
    win=win,
    name='imagen_7402', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7402.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
imagen_6900 = visual.ImageStim(
    win=win,
    name='imagen_6900', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\6900.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
imagen_5661 = visual.ImageStim(
    win=win,
    name='imagen_5661', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5661.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
imagen_6910 = visual.ImageStim(
    win=win,
    name='imagen_6910', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\6910.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
imagen_5535 = visual.ImageStim(
    win=win,
    name='imagen_5535', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5535.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
imagen_7476 = visual.ImageStim(
    win=win,
    name='imagen_7476', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7476.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
imagen_5900 = visual.ImageStim(
    win=win,
    name='imagen_5900', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5900.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
imagen_7013 = visual.ImageStim(
    win=win,
    name='imagen_7013', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7013.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
imagen_7820 = visual.ImageStim(
    win=win,
    name='imagen_7820', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7820.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
imagen_7830 = visual.ImageStim(
    win=win,
    name='imagen_7830', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7830.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
imagen_7504 = visual.ImageStim(
    win=win,
    name='imagen_7504', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7504.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
imagen_9422 = visual.ImageStim(
    win=win,
    name='imagen_9422', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\9422.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
imagen_7560 = visual.ImageStim(
    win=win,
    name='imagen_7560', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7560.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
imagen_7247 = visual.ImageStim(
    win=win,
    name='imagen_7247', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7247.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
imagen_7248 = visual.ImageStim(
    win=win,
    name='imagen_7248', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7248.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-24.0)
imagen_7077 = visual.ImageStim(
    win=win,
    name='imagen_7077', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7248.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)
imagen_9468 = visual.ImageStim(
    win=win,
    name='imagen_9468', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\9468.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-26.0)
imagen_7365 = visual.ImageStim(
    win=win,
    name='imagen_7365', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7365.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-27.0)
imagen_3005 = visual.ImageStim(
    win=win,
    name='imagen_3005', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\3005.2.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-28.0)
imagen_8325 = visual.ImageStim(
    win=win,
    name='imagen_8325', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\8325.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-29.0)
imagen_7487 = visual.ImageStim(
    win=win,
    name='imagen_7487', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7487.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-30.0)
imagen_7054 = visual.ImageStim(
    win=win,
    name='imagen_7054', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7054.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-31.0)
imagen_7461 = visual.ImageStim(
    win=win,
    name='imagen_7461', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7461.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-32.0)

# Initialize components for Routine "Imagenes_2"
Imagenes_2Clock = core.Clock()
Imagen_3005 = visual.ImageStim(
    win=win,
    name='Imagen_3005', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\3005.2.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Imagen_7632 = visual.ImageStim(
    win=win,
    name='Imagen_7632', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7632.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Imagen_7211 = visual.ImageStim(
    win=win,
    name='Imagen_7211', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7211.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Imagen_9472 = visual.ImageStim(
    win=win,
    name='Imagen_9472', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\9472.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Imagen_7830 = visual.ImageStim(
    win=win,
    name='Imagen_7830', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7830.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
Imagen_7560 = visual.ImageStim(
    win=win,
    name='Imagen_7560', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7560.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
Imagen_5900 = visual.ImageStim(
    win=win,
    name='Imagen_5900', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5900.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
Imagen_7820 = visual.ImageStim(
    win=win,
    name='Imagen_7820', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7820.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
Imagen_9422 = visual.ImageStim(
    win=win,
    name='Imagen_9422', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\9422.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
Imagen_7496 = visual.ImageStim(
    win=win,
    name='Imagen_7496', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7496.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
Imagen_7188 = visual.ImageStim(
    win=win,
    name='Imagen_7188', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7188.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
Imagen_6900 = visual.ImageStim(
    win=win,
    name='Imagen_6900', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\6900.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
Imagen_5535 = visual.ImageStim(
    win=win,
    name='Imagen_5535', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5535.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
Imagen_8325 = visual.ImageStim(
    win=win,
    name='Imagen_8325', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\8325.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
Imagen_7402 = visual.ImageStim(
    win=win,
    name='Imagen_7402', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7402.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
Imagen_7013 = visual.ImageStim(
    win=win,
    name='Imagen_7013', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7013.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
Imagen_9468 = visual.ImageStim(
    win=win,
    name='Imagen_9468', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\9468.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
Imagen_7077 = visual.ImageStim(
    win=win,
    name='Imagen_7077', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7077.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
Imagen_5395 = visual.ImageStim(
    win=win,
    name='Imagen_5395', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5395.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
Imagen_7487 = visual.ImageStim(
    win=win,
    name='Imagen_7487', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7487.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
Imagen_5661 = visual.ImageStim(
    win=win,
    name='Imagen_5661', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5661.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
Imagen_7248 = visual.ImageStim(
    win=win,
    name='Imagen_7248', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7248.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
Imagen_8211 = visual.ImageStim(
    win=win,
    name='Imagen_8211', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\8211.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
Imagen_7092 = visual.ImageStim(
    win=win,
    name='Imagen_7092', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7092.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
Imagen_5455 = visual.ImageStim(
    win=win,
    name='Imagen_5455', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5455.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-24.0)
Imagen_7054 = visual.ImageStim(
    win=win,
    name='Imagen_7054', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7054.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)
Imagen_7247 = visual.ImageStim(
    win=win,
    name='Imagen_7247', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7247.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-26.0)
Imagen_7461 = visual.ImageStim(
    win=win,
    name='Imagen_7461', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7461.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-27.0)
Imagen_7504 = visual.ImageStim(
    win=win,
    name='Imagen_7504', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7504.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-28.0)
Imagen_7476 = visual.ImageStim(
    win=win,
    name='Imagen_7476', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7476.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-29.0)
Imagen_6910 = visual.ImageStim(
    win=win,
    name='Imagen_6910', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\6910.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-30.0)
Imagen_7620 = visual.ImageStim(
    win=win,
    name='Imagen_7620', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7620.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-31.0)
Imagen_7365 = visual.ImageStim(
    win=win,
    name='Imagen_7365', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7365.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-32.0)

# Initialize components for Routine "Imagenes_3"
Imagenes_3Clock = core.Clock()
Image_7092 = visual.ImageStim(
    win=win,
    name='Image_7092', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7092.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Image_7620 = visual.ImageStim(
    win=win,
    name='Image_7620', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7620.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Image_9422 = visual.ImageStim(
    win=win,
    name='Image_9422', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\9422.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Image_7476 = visual.ImageStim(
    win=win,
    name='Image_7476', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7476.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Image_7504 = visual.ImageStim(
    win=win,
    name='Image_7504', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7504.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
Image_7054 = visual.ImageStim(
    win=win,
    name='Image_7054', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7054.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
Image_5455 = visual.ImageStim(
    win=win,
    name='Image_5455', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5455.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
Image_5535 = visual.ImageStim(
    win=win,
    name='Image_5535', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5535.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
Image_7365 = visual.ImageStim(
    win=win,
    name='Image_7365', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7365.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
Image_5661 = visual.ImageStim(
    win=win,
    name='Image_5661', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5661.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
Image_7077 = visual.ImageStim(
    win=win,
    name='Image_7077', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7077.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
Image_7248 = visual.ImageStim(
    win=win,
    name='Image_7248', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7248.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
Image_7013 = visual.ImageStim(
    win=win,
    name='Image_7013', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7013.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
Image_7211 = visual.ImageStim(
    win=win,
    name='Image_7211', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7211.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
Image_7461 = visual.ImageStim(
    win=win,
    name='Image_7461', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7461.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
Image_3005 = visual.ImageStim(
    win=win,
    name='Image_3005', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\3005.2.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
Image_7188 = visual.ImageStim(
    win=win,
    name='Image_7188', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7188.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
Image_8211 = visual.ImageStim(
    win=win,
    name='Image_8211', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\8211.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
Image_7247 = visual.ImageStim(
    win=win,
    name='Image_7247', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7247.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
Image_7496 = visual.ImageStim(
    win=win,
    name='Image_7496', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7496.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
Image_5900 = visual.ImageStim(
    win=win,
    name='Image_5900', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5900.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-20.0)
Image_9468 = visual.ImageStim(
    win=win,
    name='Image_9468', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\9468.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-21.0)
Image_7402 = visual.ImageStim(
    win=win,
    name='Image_7402', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7402.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-22.0)
Image_7487 = visual.ImageStim(
    win=win,
    name='Image_7487', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7487.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-23.0)
Image_5395 = visual.ImageStim(
    win=win,
    name='Image_5395', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5395.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-24.0)
Image_6910 = visual.ImageStim(
    win=win,
    name='Image_6910', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\6910.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-25.0)
Image_6900 = visual.ImageStim(
    win=win,
    name='Image_6900', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\6900.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-26.0)
Image_7560 = visual.ImageStim(
    win=win,
    name='Image_7560', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7560.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-27.0)
Image_7830 = visual.ImageStim(
    win=win,
    name='Image_7830', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7830.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-28.0)
Image_8325 = visual.ImageStim(
    win=win,
    name='Image_8325', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\8325.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-29.0)
Image_7820 = visual.ImageStim(
    win=win,
    name='Image_7820', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7820.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-30.0)
Image_9472 = visual.ImageStim(
    win=win,
    name='Image_9472', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\9472.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-31.0)
Image_7632 = visual.ImageStim(
    win=win,
    name='Image_7632', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7632.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-32.0)
    
    


# Initialize components for Routine "Imagenes_4"

Imagenes_4Clock = core.Clock()
Imagen_3005 = visual.ImageStim(
    win=win,
    name='Imagen_5535', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5535.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Imagen_8211 = visual.ImageStim(
    win=win,
    name='Imagen_8211', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\8211.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Imagen_7402 = visual.ImageStim(
    win=win,
    name='Imagen_7402', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7402.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Imagen_5395 = visual.ImageStim(
    win=win,
    name='Imagen_5395', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5395.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Imagen_7092 = visual.ImageStim(
    win=win,
    name='Imagen_7092', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7092.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
Imagen_7487 = visual.ImageStim(
    win=win,
    name='Imagen_7487', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7487.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
Imagen_7188 = visual.ImageStim(
    win=win,
    name='Imagen_7188', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7188.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
Imagen_7820 = visual.ImageStim(
    win=win,
    name='Imagen_7820', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7820.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
Imagen_5900 = visual.ImageStim(
    win=win,
    name='Imagen_5900', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\5900.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
Imagen_7476 = visual.ImageStim(
    win=win,
    name='Imagen_7476', 
    image='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\Images\\Images\\7476.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)




# Initialize components for Routine "fin"
finClock = core.Clock()
gracias = visual.TextStim(win=win, name='gracias',
    text='\n               ¡Muchas gracias!\n\n\n\n\n\nPresiona la tecla de espacio para salir',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instrucciones"-------
# update component parameters for each repeat
key_resp_instr.keys = []
key_resp_instr.rt = []
# keep track of which components have finished
InstruccionesComponents = [instr, key_resp_instr]
for thisComponent in InstruccionesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstruccionesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instrucciones"-------
while continueRoutine:
    # get current time
    t = InstruccionesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstruccionesClock)
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
    for thisComponent in InstruccionesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instrucciones"-------
for thisComponent in InstruccionesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr.started', instr.tStartRefresh)
thisExp.addData('instr.stopped', instr.tStopRefresh)
# check responses
if key_resp_instr.keys in ['', [], None]:  # No response was made
    key_resp_instr.keys = None
thisExp.addData('key_resp_instr.keys',key_resp_instr.keys)
if key_resp_instr.keys != None:  # we had a response
    thisExp.addData('key_resp_instr.rt', key_resp_instr.rt)
thisExp.addData('key_resp_instr.started', key_resp_instr.tStartRefresh)
thisExp.addData('key_resp_instr.stopped', key_resp_instr.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instrucciones" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Imagenes_1"-------
routineTimer.add(165.000000)
# update component parameters for each repeat
# keep track of which components have finished
Imagenes_1Components = [imagen_7211, imagen_7620, imagen_7092, imagen_9472, imagen_7188, imagen_5395, imagen_7632, imagen_8211, imagen_5455, imagen_7496, imagen_7402, imagen_6900, imagen_5661, imagen_6910, imagen_5535, imagen_7476, imagen_5900, imagen_7013, imagen_7820, imagen_7830, imagen_7504, imagen_9422, imagen_7560, imagen_7247, imagen_7248, imagen_7077, imagen_9468, imagen_7365, imagen_3005, imagen_8325, imagen_7487, imagen_7054, imagen_7461]
for thisComponent in Imagenes_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Imagenes_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Imagenes_1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Imagenes_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Imagenes_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *imagen_7211* updates
    if imagen_7211.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7211.frameNStart = frameN  # exact frame index
        imagen_7211.tStart = t  # local t and not account for scr refresh
        imagen_7211.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7211, 'tStartRefresh')  # time at next scr refresh
        imagen_7211.setAutoDraw(True)
    if imagen_7211.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7211.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7211.tStop = t  # not accounting for scr refresh
            imagen_7211.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7211, 'tStopRefresh')  # time at next scr refresh
            imagen_7211.setAutoDraw(False)
    
    # *imagen_7620* updates
    if imagen_7620.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7620.frameNStart = frameN  # exact frame index
        imagen_7620.tStart = t  # local t and not account for scr refresh
        imagen_7620.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7620, 'tStartRefresh')  # time at next scr refresh
        imagen_7620.setAutoDraw(True)
    if imagen_7620.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7620.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7620.tStop = t  # not accounting for scr refresh
            imagen_7620.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7620, 'tStopRefresh')  # time at next scr refresh
            imagen_7620.setAutoDraw(False)
    
    # *imagen_7092* updates
    if imagen_7092.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7092.frameNStart = frameN  # exact frame index
        imagen_7092.tStart = t  # local t and not account for scr refresh
        imagen_7092.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7092, 'tStartRefresh')  # time at next scr refresh
        imagen_7092.setAutoDraw(True)
    if imagen_7092.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7092.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7092.tStop = t  # not accounting for scr refresh
            imagen_7092.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7092, 'tStopRefresh')  # time at next scr refresh
            imagen_7092.setAutoDraw(False)
    
    # *imagen_9472* updates
    if imagen_9472.status == NOT_STARTED and tThisFlip >= 15.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_9472.frameNStart = frameN  # exact frame index
        imagen_9472.tStart = t  # local t and not account for scr refresh
        imagen_9472.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_9472, 'tStartRefresh')  # time at next scr refresh
        imagen_9472.setAutoDraw(True)
    if imagen_9472.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_9472.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_9472.tStop = t  # not accounting for scr refresh
            imagen_9472.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_9472, 'tStopRefresh')  # time at next scr refresh
            imagen_9472.setAutoDraw(False)
    
    # *imagen_7188* updates
    if imagen_7188.status == NOT_STARTED and tThisFlip >= 20.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7188.frameNStart = frameN  # exact frame index
        imagen_7188.tStart = t  # local t and not account for scr refresh
        imagen_7188.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7188, 'tStartRefresh')  # time at next scr refresh
        imagen_7188.setAutoDraw(True)
    if imagen_7188.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7188.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7188.tStop = t  # not accounting for scr refresh
            imagen_7188.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7188, 'tStopRefresh')  # time at next scr refresh
            imagen_7188.setAutoDraw(False)
    
    # *imagen_5395* updates
    if imagen_5395.status == NOT_STARTED and tThisFlip >= 25.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_5395.frameNStart = frameN  # exact frame index
        imagen_5395.tStart = t  # local t and not account for scr refresh
        imagen_5395.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_5395, 'tStartRefresh')  # time at next scr refresh
        imagen_5395.setAutoDraw(True)
    if imagen_5395.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_5395.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_5395.tStop = t  # not accounting for scr refresh
            imagen_5395.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_5395, 'tStopRefresh')  # time at next scr refresh
            imagen_5395.setAutoDraw(False)
    
    # *imagen_7632* updates
    if imagen_7632.status == NOT_STARTED and tThisFlip >= 30.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7632.frameNStart = frameN  # exact frame index
        imagen_7632.tStart = t  # local t and not account for scr refresh
        imagen_7632.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7632, 'tStartRefresh')  # time at next scr refresh
        imagen_7632.setAutoDraw(True)
    if imagen_7632.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7632.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7632.tStop = t  # not accounting for scr refresh
            imagen_7632.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7632, 'tStopRefresh')  # time at next scr refresh
            imagen_7632.setAutoDraw(False)
    
    # *imagen_8211* updates
    if imagen_8211.status == NOT_STARTED and tThisFlip >= 35.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_8211.frameNStart = frameN  # exact frame index
        imagen_8211.tStart = t  # local t and not account for scr refresh
        imagen_8211.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_8211, 'tStartRefresh')  # time at next scr refresh
        imagen_8211.setAutoDraw(True)
    if imagen_8211.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_8211.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_8211.tStop = t  # not accounting for scr refresh
            imagen_8211.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_8211, 'tStopRefresh')  # time at next scr refresh
            imagen_8211.setAutoDraw(False)
    
    # *imagen_5455* updates
    if imagen_5455.status == NOT_STARTED and tThisFlip >= 40.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_5455.frameNStart = frameN  # exact frame index
        imagen_5455.tStart = t  # local t and not account for scr refresh
        imagen_5455.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_5455, 'tStartRefresh')  # time at next scr refresh
        imagen_5455.setAutoDraw(True)
    if imagen_5455.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_5455.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_5455.tStop = t  # not accounting for scr refresh
            imagen_5455.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_5455, 'tStopRefresh')  # time at next scr refresh
            imagen_5455.setAutoDraw(False)
    
    # *imagen_7496* updates
    if imagen_7496.status == NOT_STARTED and tThisFlip >= 45.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7496.frameNStart = frameN  # exact frame index
        imagen_7496.tStart = t  # local t and not account for scr refresh
        imagen_7496.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7496, 'tStartRefresh')  # time at next scr refresh
        imagen_7496.setAutoDraw(True)
    if imagen_7496.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7496.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7496.tStop = t  # not accounting for scr refresh
            imagen_7496.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7496, 'tStopRefresh')  # time at next scr refresh
            imagen_7496.setAutoDraw(False)
    
    # *imagen_7402* updates
    if imagen_7402.status == NOT_STARTED and tThisFlip >= 50.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7402.frameNStart = frameN  # exact frame index
        imagen_7402.tStart = t  # local t and not account for scr refresh
        imagen_7402.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7402, 'tStartRefresh')  # time at next scr refresh
        imagen_7402.setAutoDraw(True)
    if imagen_7402.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7402.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7402.tStop = t  # not accounting for scr refresh
            imagen_7402.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7402, 'tStopRefresh')  # time at next scr refresh
            imagen_7402.setAutoDraw(False)
    
    # *imagen_6900* updates
    if imagen_6900.status == NOT_STARTED and tThisFlip >= 55.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_6900.frameNStart = frameN  # exact frame index
        imagen_6900.tStart = t  # local t and not account for scr refresh
        imagen_6900.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_6900, 'tStartRefresh')  # time at next scr refresh
        imagen_6900.setAutoDraw(True)
    if imagen_6900.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_6900.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_6900.tStop = t  # not accounting for scr refresh
            imagen_6900.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_6900, 'tStopRefresh')  # time at next scr refresh
            imagen_6900.setAutoDraw(False)
    
    # *imagen_5661* updates
    if imagen_5661.status == NOT_STARTED and tThisFlip >= 60.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_5661.frameNStart = frameN  # exact frame index
        imagen_5661.tStart = t  # local t and not account for scr refresh
        imagen_5661.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_5661, 'tStartRefresh')  # time at next scr refresh
        imagen_5661.setAutoDraw(True)
    if imagen_5661.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_5661.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_5661.tStop = t  # not accounting for scr refresh
            imagen_5661.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_5661, 'tStopRefresh')  # time at next scr refresh
            imagen_5661.setAutoDraw(False)
    
    # *imagen_6910* updates
    if imagen_6910.status == NOT_STARTED and tThisFlip >= 65.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_6910.frameNStart = frameN  # exact frame index
        imagen_6910.tStart = t  # local t and not account for scr refresh
        imagen_6910.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_6910, 'tStartRefresh')  # time at next scr refresh
        imagen_6910.setAutoDraw(True)
    if imagen_6910.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_6910.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_6910.tStop = t  # not accounting for scr refresh
            imagen_6910.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_6910, 'tStopRefresh')  # time at next scr refresh
            imagen_6910.setAutoDraw(False)
    
    # *imagen_5535* updates
    if imagen_5535.status == NOT_STARTED and tThisFlip >= 70.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_5535.frameNStart = frameN  # exact frame index
        imagen_5535.tStart = t  # local t and not account for scr refresh
        imagen_5535.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_5535, 'tStartRefresh')  # time at next scr refresh
        imagen_5535.setAutoDraw(True)
    if imagen_5535.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_5535.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_5535.tStop = t  # not accounting for scr refresh
            imagen_5535.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_5535, 'tStopRefresh')  # time at next scr refresh
            imagen_5535.setAutoDraw(False)
    
    # *imagen_7476* updates
    if imagen_7476.status == NOT_STARTED and tThisFlip >= 75.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7476.frameNStart = frameN  # exact frame index
        imagen_7476.tStart = t  # local t and not account for scr refresh
        imagen_7476.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7476, 'tStartRefresh')  # time at next scr refresh
        imagen_7476.setAutoDraw(True)
    if imagen_7476.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7476.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7476.tStop = t  # not accounting for scr refresh
            imagen_7476.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7476, 'tStopRefresh')  # time at next scr refresh
            imagen_7476.setAutoDraw(False)
    
    # *imagen_5900* updates
    if imagen_5900.status == NOT_STARTED and tThisFlip >= 80.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_5900.frameNStart = frameN  # exact frame index
        imagen_5900.tStart = t  # local t and not account for scr refresh
        imagen_5900.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_5900, 'tStartRefresh')  # time at next scr refresh
        imagen_5900.setAutoDraw(True)
    if imagen_5900.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_5900.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_5900.tStop = t  # not accounting for scr refresh
            imagen_5900.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_5900, 'tStopRefresh')  # time at next scr refresh
            imagen_5900.setAutoDraw(False)
    
    # *imagen_7013* updates
    if imagen_7013.status == NOT_STARTED and tThisFlip >= 85.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7013.frameNStart = frameN  # exact frame index
        imagen_7013.tStart = t  # local t and not account for scr refresh
        imagen_7013.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7013, 'tStartRefresh')  # time at next scr refresh
        imagen_7013.setAutoDraw(True)
    if imagen_7013.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7013.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7013.tStop = t  # not accounting for scr refresh
            imagen_7013.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7013, 'tStopRefresh')  # time at next scr refresh
            imagen_7013.setAutoDraw(False)
    
    # *imagen_7820* updates
    if imagen_7820.status == NOT_STARTED and tThisFlip >= 90.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7820.frameNStart = frameN  # exact frame index
        imagen_7820.tStart = t  # local t and not account for scr refresh
        imagen_7820.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7820, 'tStartRefresh')  # time at next scr refresh
        imagen_7820.setAutoDraw(True)
    if imagen_7820.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7820.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7820.tStop = t  # not accounting for scr refresh
            imagen_7820.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7820, 'tStopRefresh')  # time at next scr refresh
            imagen_7820.setAutoDraw(False)
    
    # *imagen_7830* updates
    if imagen_7830.status == NOT_STARTED and tThisFlip >= 95.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7830.frameNStart = frameN  # exact frame index
        imagen_7830.tStart = t  # local t and not account for scr refresh
        imagen_7830.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7830, 'tStartRefresh')  # time at next scr refresh
        imagen_7830.setAutoDraw(True)
    if imagen_7830.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7830.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7830.tStop = t  # not accounting for scr refresh
            imagen_7830.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7830, 'tStopRefresh')  # time at next scr refresh
            imagen_7830.setAutoDraw(False)
    
    # *imagen_7504* updates
    if imagen_7504.status == NOT_STARTED and tThisFlip >= 100.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7504.frameNStart = frameN  # exact frame index
        imagen_7504.tStart = t  # local t and not account for scr refresh
        imagen_7504.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7504, 'tStartRefresh')  # time at next scr refresh
        imagen_7504.setAutoDraw(True)
    if imagen_7504.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7504.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7504.tStop = t  # not accounting for scr refresh
            imagen_7504.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7504, 'tStopRefresh')  # time at next scr refresh
            imagen_7504.setAutoDraw(False)
    
    # *imagen_9422* updates
    if imagen_9422.status == NOT_STARTED and tThisFlip >= 105.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_9422.frameNStart = frameN  # exact frame index
        imagen_9422.tStart = t  # local t and not account for scr refresh
        imagen_9422.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_9422, 'tStartRefresh')  # time at next scr refresh
        imagen_9422.setAutoDraw(True)
    if imagen_9422.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_9422.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_9422.tStop = t  # not accounting for scr refresh
            imagen_9422.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_9422, 'tStopRefresh')  # time at next scr refresh
            imagen_9422.setAutoDraw(False)
    
    # *imagen_7560* updates
    if imagen_7560.status == NOT_STARTED and tThisFlip >= 110.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7560.frameNStart = frameN  # exact frame index
        imagen_7560.tStart = t  # local t and not account for scr refresh
        imagen_7560.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7560, 'tStartRefresh')  # time at next scr refresh
        imagen_7560.setAutoDraw(True)
    if imagen_7560.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7560.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7560.tStop = t  # not accounting for scr refresh
            imagen_7560.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7560, 'tStopRefresh')  # time at next scr refresh
            imagen_7560.setAutoDraw(False)
    
    # *imagen_7247* updates
    if imagen_7247.status == NOT_STARTED and tThisFlip >= 115.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7247.frameNStart = frameN  # exact frame index
        imagen_7247.tStart = t  # local t and not account for scr refresh
        imagen_7247.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7247, 'tStartRefresh')  # time at next scr refresh
        imagen_7247.setAutoDraw(True)
    if imagen_7247.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7247.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7247.tStop = t  # not accounting for scr refresh
            imagen_7247.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7247, 'tStopRefresh')  # time at next scr refresh
            imagen_7247.setAutoDraw(False)
    
    # *imagen_7248* updates
    if imagen_7248.status == NOT_STARTED and tThisFlip >= 120.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7248.frameNStart = frameN  # exact frame index
        imagen_7248.tStart = t  # local t and not account for scr refresh
        imagen_7248.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7248, 'tStartRefresh')  # time at next scr refresh
        imagen_7248.setAutoDraw(True)
    if imagen_7248.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7248.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7248.tStop = t  # not accounting for scr refresh
            imagen_7248.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7248, 'tStopRefresh')  # time at next scr refresh
            imagen_7248.setAutoDraw(False)
    
    # *imagen_7077* updates
    if imagen_7077.status == NOT_STARTED and tThisFlip >= 125.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7077.frameNStart = frameN  # exact frame index
        imagen_7077.tStart = t  # local t and not account for scr refresh
        imagen_7077.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7077, 'tStartRefresh')  # time at next scr refresh
        imagen_7077.setAutoDraw(True)
    if imagen_7077.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7077.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7077.tStop = t  # not accounting for scr refresh
            imagen_7077.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7077, 'tStopRefresh')  # time at next scr refresh
            imagen_7077.setAutoDraw(False)
    
    # *imagen_9468* updates
    if imagen_9468.status == NOT_STARTED and tThisFlip >= 130.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_9468.frameNStart = frameN  # exact frame index
        imagen_9468.tStart = t  # local t and not account for scr refresh
        imagen_9468.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_9468, 'tStartRefresh')  # time at next scr refresh
        imagen_9468.setAutoDraw(True)
    if imagen_9468.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_9468.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_9468.tStop = t  # not accounting for scr refresh
            imagen_9468.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_9468, 'tStopRefresh')  # time at next scr refresh
            imagen_9468.setAutoDraw(False)
    
    # *imagen_7365* updates
    if imagen_7365.status == NOT_STARTED and tThisFlip >= 135.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7365.frameNStart = frameN  # exact frame index
        imagen_7365.tStart = t  # local t and not account for scr refresh
        imagen_7365.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7365, 'tStartRefresh')  # time at next scr refresh
        imagen_7365.setAutoDraw(True)
    if imagen_7365.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7365.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7365.tStop = t  # not accounting for scr refresh
            imagen_7365.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7365, 'tStopRefresh')  # time at next scr refresh
            imagen_7365.setAutoDraw(False)
    
    # *imagen_3005* updates
    if imagen_3005.status == NOT_STARTED and tThisFlip >= 140.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_3005.frameNStart = frameN  # exact frame index
        imagen_3005.tStart = t  # local t and not account for scr refresh
        imagen_3005.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_3005, 'tStartRefresh')  # time at next scr refresh
        imagen_3005.setAutoDraw(True)
    if imagen_3005.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_3005.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_3005.tStop = t  # not accounting for scr refresh
            imagen_3005.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_3005, 'tStopRefresh')  # time at next scr refresh
            imagen_3005.setAutoDraw(False)
    
    # *imagen_8325* updates
    if imagen_8325.status == NOT_STARTED and tThisFlip >= 145.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_8325.frameNStart = frameN  # exact frame index
        imagen_8325.tStart = t  # local t and not account for scr refresh
        imagen_8325.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_8325, 'tStartRefresh')  # time at next scr refresh
        imagen_8325.setAutoDraw(True)
    if imagen_8325.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_8325.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_8325.tStop = t  # not accounting for scr refresh
            imagen_8325.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_8325, 'tStopRefresh')  # time at next scr refresh
            imagen_8325.setAutoDraw(False)
    
    # *imagen_7487* updates
    if imagen_7487.status == NOT_STARTED and tThisFlip >= 150.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7487.frameNStart = frameN  # exact frame index
        imagen_7487.tStart = t  # local t and not account for scr refresh
        imagen_7487.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7487, 'tStartRefresh')  # time at next scr refresh
        imagen_7487.setAutoDraw(True)
    if imagen_7487.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7487.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7487.tStop = t  # not accounting for scr refresh
            imagen_7487.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7487, 'tStopRefresh')  # time at next scr refresh
            imagen_7487.setAutoDraw(False)
    
    # *imagen_7054* updates
    if imagen_7054.status == NOT_STARTED and tThisFlip >= 155.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7054.frameNStart = frameN  # exact frame index
        imagen_7054.tStart = t  # local t and not account for scr refresh
        imagen_7054.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7054, 'tStartRefresh')  # time at next scr refresh
        imagen_7054.setAutoDraw(True)
    if imagen_7054.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7054.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7054.tStop = t  # not accounting for scr refresh
            imagen_7054.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7054, 'tStopRefresh')  # time at next scr refresh
            imagen_7054.setAutoDraw(False)
    
    # *imagen_7461* updates
    if imagen_7461.status == NOT_STARTED and tThisFlip >= 160.0-frameTolerance:
        # keep track of start time/frame for later
        imagen_7461.frameNStart = frameN  # exact frame index
        imagen_7461.tStart = t  # local t and not account for scr refresh
        imagen_7461.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagen_7461, 'tStartRefresh')  # time at next scr refresh
        imagen_7461.setAutoDraw(True)
    if imagen_7461.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > imagen_7461.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            imagen_7461.tStop = t  # not accounting for scr refresh
            imagen_7461.frameNStop = frameN  # exact frame index
            win.timeOnFlip(imagen_7461, 'tStopRefresh')  # time at next scr refresh
            imagen_7461.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Imagenes_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Imagenes_1"-------
for thisComponent in Imagenes_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Imagenes_2"-------
routineTimer.add(165.000000)
# update component parameters for each repeat
# keep track of which components have finished
Imagenes_2Components = [Imagen_3005, Imagen_7632, Imagen_7211, Imagen_9472, Imagen_7830, Imagen_7560, Imagen_5900, Imagen_7820, Imagen_9422, Imagen_7496, Imagen_7188, Imagen_6900, Imagen_5535, Imagen_8325, Imagen_7402, Imagen_7013, Imagen_9468, Imagen_7077, Imagen_5395, Imagen_7487, Imagen_5661, Imagen_7248, Imagen_8211, Imagen_7092, Imagen_5455, Imagen_7054, Imagen_7247, Imagen_7461, Imagen_7504, Imagen_7476, Imagen_6910, Imagen_7620, Imagen_7365]
for thisComponent in Imagenes_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Imagenes_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Imagenes_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Imagenes_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Imagenes_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Imagen_3005* updates
    if Imagen_3005.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_3005.frameNStart = frameN  # exact frame index
        Imagen_3005.tStart = t  # local t and not account for scr refresh
        Imagen_3005.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_3005, 'tStartRefresh')  # time at next scr refresh
        Imagen_3005.setAutoDraw(True)
    if Imagen_3005.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_3005.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_3005.tStop = t  # not accounting for scr refresh
            Imagen_3005.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_3005, 'tStopRefresh')  # time at next scr refresh
            Imagen_3005.setAutoDraw(False)
    
    # *Imagen_7632* updates
    if Imagen_7632.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7632.frameNStart = frameN  # exact frame index
        Imagen_7632.tStart = t  # local t and not account for scr refresh
        Imagen_7632.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7632, 'tStartRefresh')  # time at next scr refresh
        Imagen_7632.setAutoDraw(True)
    if Imagen_7632.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7632.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7632.tStop = t  # not accounting for scr refresh
            Imagen_7632.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7632, 'tStopRefresh')  # time at next scr refresh
            Imagen_7632.setAutoDraw(False)
    
    # *Imagen_7211* updates
    if Imagen_7211.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7211.frameNStart = frameN  # exact frame index
        Imagen_7211.tStart = t  # local t and not account for scr refresh
        Imagen_7211.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7211, 'tStartRefresh')  # time at next scr refresh
        Imagen_7211.setAutoDraw(True)
    if Imagen_7211.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7211.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7211.tStop = t  # not accounting for scr refresh
            Imagen_7211.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7211, 'tStopRefresh')  # time at next scr refresh
            Imagen_7211.setAutoDraw(False)
    
    # *Imagen_9472* updates
    if Imagen_9472.status == NOT_STARTED and tThisFlip >= 15.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_9472.frameNStart = frameN  # exact frame index
        Imagen_9472.tStart = t  # local t and not account for scr refresh
        Imagen_9472.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_9472, 'tStartRefresh')  # time at next scr refresh
        Imagen_9472.setAutoDraw(True)
    if Imagen_9472.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_9472.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_9472.tStop = t  # not accounting for scr refresh
            Imagen_9472.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_9472, 'tStopRefresh')  # time at next scr refresh
            Imagen_9472.setAutoDraw(False)
    
    # *Imagen_7830* updates
    if Imagen_7830.status == NOT_STARTED and tThisFlip >= 20.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7830.frameNStart = frameN  # exact frame index
        Imagen_7830.tStart = t  # local t and not account for scr refresh
        Imagen_7830.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7830, 'tStartRefresh')  # time at next scr refresh
        Imagen_7830.setAutoDraw(True)
    if Imagen_7830.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7830.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7830.tStop = t  # not accounting for scr refresh
            Imagen_7830.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7830, 'tStopRefresh')  # time at next scr refresh
            Imagen_7830.setAutoDraw(False)
    
    # *Imagen_7560* updates
    if Imagen_7560.status == NOT_STARTED and tThisFlip >= 25.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7560.frameNStart = frameN  # exact frame index
        Imagen_7560.tStart = t  # local t and not account for scr refresh
        Imagen_7560.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7560, 'tStartRefresh')  # time at next scr refresh
        Imagen_7560.setAutoDraw(True)
    if Imagen_7560.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7560.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7560.tStop = t  # not accounting for scr refresh
            Imagen_7560.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7560, 'tStopRefresh')  # time at next scr refresh
            Imagen_7560.setAutoDraw(False)
    
    # *Imagen_5900* updates
    if Imagen_5900.status == NOT_STARTED and tThisFlip >= 30.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_5900.frameNStart = frameN  # exact frame index
        Imagen_5900.tStart = t  # local t and not account for scr refresh
        Imagen_5900.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_5900, 'tStartRefresh')  # time at next scr refresh
        Imagen_5900.setAutoDraw(True)
    if Imagen_5900.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_5900.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_5900.tStop = t  # not accounting for scr refresh
            Imagen_5900.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_5900, 'tStopRefresh')  # time at next scr refresh
            Imagen_5900.setAutoDraw(False)
    
    # *Imagen_7820* updates
    if Imagen_7820.status == NOT_STARTED and tThisFlip >= 35.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7820.frameNStart = frameN  # exact frame index
        Imagen_7820.tStart = t  # local t and not account for scr refresh
        Imagen_7820.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7820, 'tStartRefresh')  # time at next scr refresh
        Imagen_7820.setAutoDraw(True)
    if Imagen_7820.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7820.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7820.tStop = t  # not accounting for scr refresh
            Imagen_7820.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7820, 'tStopRefresh')  # time at next scr refresh
            Imagen_7820.setAutoDraw(False)
    
    # *Imagen_9422* updates
    if Imagen_9422.status == NOT_STARTED and tThisFlip >= 40.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_9422.frameNStart = frameN  # exact frame index
        Imagen_9422.tStart = t  # local t and not account for scr refresh
        Imagen_9422.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_9422, 'tStartRefresh')  # time at next scr refresh
        Imagen_9422.setAutoDraw(True)
    if Imagen_9422.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_9422.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_9422.tStop = t  # not accounting for scr refresh
            Imagen_9422.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_9422, 'tStopRefresh')  # time at next scr refresh
            Imagen_9422.setAutoDraw(False)
    
    # *Imagen_7496* updates
    if Imagen_7496.status == NOT_STARTED and tThisFlip >= 45.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7496.frameNStart = frameN  # exact frame index
        Imagen_7496.tStart = t  # local t and not account for scr refresh
        Imagen_7496.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7496, 'tStartRefresh')  # time at next scr refresh
        Imagen_7496.setAutoDraw(True)
    if Imagen_7496.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7496.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7496.tStop = t  # not accounting for scr refresh
            Imagen_7496.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7496, 'tStopRefresh')  # time at next scr refresh
            Imagen_7496.setAutoDraw(False)
    
    # *Imagen_7188* updates
    if Imagen_7188.status == NOT_STARTED and tThisFlip >= 50.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7188.frameNStart = frameN  # exact frame index
        Imagen_7188.tStart = t  # local t and not account for scr refresh
        Imagen_7188.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7188, 'tStartRefresh')  # time at next scr refresh
        Imagen_7188.setAutoDraw(True)
    if Imagen_7188.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7188.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7188.tStop = t  # not accounting for scr refresh
            Imagen_7188.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7188, 'tStopRefresh')  # time at next scr refresh
            Imagen_7188.setAutoDraw(False)
    
    # *Imagen_6900* updates
    if Imagen_6900.status == NOT_STARTED and tThisFlip >= 55.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_6900.frameNStart = frameN  # exact frame index
        Imagen_6900.tStart = t  # local t and not account for scr refresh
        Imagen_6900.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_6900, 'tStartRefresh')  # time at next scr refresh
        Imagen_6900.setAutoDraw(True)
    if Imagen_6900.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_6900.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_6900.tStop = t  # not accounting for scr refresh
            Imagen_6900.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_6900, 'tStopRefresh')  # time at next scr refresh
            Imagen_6900.setAutoDraw(False)
    
    # *Imagen_5535* updates
    if Imagen_5535.status == NOT_STARTED and tThisFlip >= 60.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_5535.frameNStart = frameN  # exact frame index
        Imagen_5535.tStart = t  # local t and not account for scr refresh
        Imagen_5535.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_5535, 'tStartRefresh')  # time at next scr refresh
        Imagen_5535.setAutoDraw(True)
    if Imagen_5535.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_5535.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_5535.tStop = t  # not accounting for scr refresh
            Imagen_5535.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_5535, 'tStopRefresh')  # time at next scr refresh
            Imagen_5535.setAutoDraw(False)
    
    # *Imagen_8325* updates
    if Imagen_8325.status == NOT_STARTED and tThisFlip >= 65.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_8325.frameNStart = frameN  # exact frame index
        Imagen_8325.tStart = t  # local t and not account for scr refresh
        Imagen_8325.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_8325, 'tStartRefresh')  # time at next scr refresh
        Imagen_8325.setAutoDraw(True)
    if Imagen_8325.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_8325.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_8325.tStop = t  # not accounting for scr refresh
            Imagen_8325.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_8325, 'tStopRefresh')  # time at next scr refresh
            Imagen_8325.setAutoDraw(False)
    
    # *Imagen_7402* updates
    if Imagen_7402.status == NOT_STARTED and tThisFlip >= 70.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7402.frameNStart = frameN  # exact frame index
        Imagen_7402.tStart = t  # local t and not account for scr refresh
        Imagen_7402.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7402, 'tStartRefresh')  # time at next scr refresh
        Imagen_7402.setAutoDraw(True)
    if Imagen_7402.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7402.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7402.tStop = t  # not accounting for scr refresh
            Imagen_7402.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7402, 'tStopRefresh')  # time at next scr refresh
            Imagen_7402.setAutoDraw(False)
    
    # *Imagen_7013* updates
    if Imagen_7013.status == NOT_STARTED and tThisFlip >= 75.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7013.frameNStart = frameN  # exact frame index
        Imagen_7013.tStart = t  # local t and not account for scr refresh
        Imagen_7013.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7013, 'tStartRefresh')  # time at next scr refresh
        Imagen_7013.setAutoDraw(True)
    if Imagen_7013.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7013.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7013.tStop = t  # not accounting for scr refresh
            Imagen_7013.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7013, 'tStopRefresh')  # time at next scr refresh
            Imagen_7013.setAutoDraw(False)
    
    # *Imagen_9468* updates
    if Imagen_9468.status == NOT_STARTED and tThisFlip >= 80.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_9468.frameNStart = frameN  # exact frame index
        Imagen_9468.tStart = t  # local t and not account for scr refresh
        Imagen_9468.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_9468, 'tStartRefresh')  # time at next scr refresh
        Imagen_9468.setAutoDraw(True)
    if Imagen_9468.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_9468.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_9468.tStop = t  # not accounting for scr refresh
            Imagen_9468.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_9468, 'tStopRefresh')  # time at next scr refresh
            Imagen_9468.setAutoDraw(False)
    
    # *Imagen_7077* updates
    if Imagen_7077.status == NOT_STARTED and tThisFlip >= 85.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7077.frameNStart = frameN  # exact frame index
        Imagen_7077.tStart = t  # local t and not account for scr refresh
        Imagen_7077.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7077, 'tStartRefresh')  # time at next scr refresh
        Imagen_7077.setAutoDraw(True)
    if Imagen_7077.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7077.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7077.tStop = t  # not accounting for scr refresh
            Imagen_7077.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7077, 'tStopRefresh')  # time at next scr refresh
            Imagen_7077.setAutoDraw(False)
    
    # *Imagen_5395* updates
    if Imagen_5395.status == NOT_STARTED and tThisFlip >= 90.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_5395.frameNStart = frameN  # exact frame index
        Imagen_5395.tStart = t  # local t and not account for scr refresh
        Imagen_5395.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_5395, 'tStartRefresh')  # time at next scr refresh
        Imagen_5395.setAutoDraw(True)
    if Imagen_5395.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_5395.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_5395.tStop = t  # not accounting for scr refresh
            Imagen_5395.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_5395, 'tStopRefresh')  # time at next scr refresh
            Imagen_5395.setAutoDraw(False)
    
    # *Imagen_7487* updates
    if Imagen_7487.status == NOT_STARTED and tThisFlip >= 95.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7487.frameNStart = frameN  # exact frame index
        Imagen_7487.tStart = t  # local t and not account for scr refresh
        Imagen_7487.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7487, 'tStartRefresh')  # time at next scr refresh
        Imagen_7487.setAutoDraw(True)
    if Imagen_7487.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7487.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7487.tStop = t  # not accounting for scr refresh
            Imagen_7487.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7487, 'tStopRefresh')  # time at next scr refresh
            Imagen_7487.setAutoDraw(False)
    
    # *Imagen_5661* updates
    if Imagen_5661.status == NOT_STARTED and tThisFlip >= 100.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_5661.frameNStart = frameN  # exact frame index
        Imagen_5661.tStart = t  # local t and not account for scr refresh
        Imagen_5661.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_5661, 'tStartRefresh')  # time at next scr refresh
        Imagen_5661.setAutoDraw(True)
    if Imagen_5661.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_5661.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_5661.tStop = t  # not accounting for scr refresh
            Imagen_5661.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_5661, 'tStopRefresh')  # time at next scr refresh
            Imagen_5661.setAutoDraw(False)
    
    # *Imagen_7248* updates
    if Imagen_7248.status == NOT_STARTED and tThisFlip >= 105.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7248.frameNStart = frameN  # exact frame index
        Imagen_7248.tStart = t  # local t and not account for scr refresh
        Imagen_7248.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7248, 'tStartRefresh')  # time at next scr refresh
        Imagen_7248.setAutoDraw(True)
    if Imagen_7248.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7248.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7248.tStop = t  # not accounting for scr refresh
            Imagen_7248.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7248, 'tStopRefresh')  # time at next scr refresh
            Imagen_7248.setAutoDraw(False)
    
    # *Imagen_8211* updates
    if Imagen_8211.status == NOT_STARTED and tThisFlip >= 110.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_8211.frameNStart = frameN  # exact frame index
        Imagen_8211.tStart = t  # local t and not account for scr refresh
        Imagen_8211.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_8211, 'tStartRefresh')  # time at next scr refresh
        Imagen_8211.setAutoDraw(True)
    if Imagen_8211.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_8211.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_8211.tStop = t  # not accounting for scr refresh
            Imagen_8211.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_8211, 'tStopRefresh')  # time at next scr refresh
            Imagen_8211.setAutoDraw(False)
    
    # *Imagen_7092* updates
    if Imagen_7092.status == NOT_STARTED and tThisFlip >= 115.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7092.frameNStart = frameN  # exact frame index
        Imagen_7092.tStart = t  # local t and not account for scr refresh
        Imagen_7092.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7092, 'tStartRefresh')  # time at next scr refresh
        Imagen_7092.setAutoDraw(True)
    if Imagen_7092.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7092.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7092.tStop = t  # not accounting for scr refresh
            Imagen_7092.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7092, 'tStopRefresh')  # time at next scr refresh
            Imagen_7092.setAutoDraw(False)
    
    # *Imagen_5455* updates
    if Imagen_5455.status == NOT_STARTED and tThisFlip >= 120.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_5455.frameNStart = frameN  # exact frame index
        Imagen_5455.tStart = t  # local t and not account for scr refresh
        Imagen_5455.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_5455, 'tStartRefresh')  # time at next scr refresh
        Imagen_5455.setAutoDraw(True)
    if Imagen_5455.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_5455.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_5455.tStop = t  # not accounting for scr refresh
            Imagen_5455.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_5455, 'tStopRefresh')  # time at next scr refresh
            Imagen_5455.setAutoDraw(False)
    
    # *Imagen_7054* updates
    if Imagen_7054.status == NOT_STARTED and tThisFlip >= 125.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7054.frameNStart = frameN  # exact frame index
        Imagen_7054.tStart = t  # local t and not account for scr refresh
        Imagen_7054.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7054, 'tStartRefresh')  # time at next scr refresh
        Imagen_7054.setAutoDraw(True)
    if Imagen_7054.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7054.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7054.tStop = t  # not accounting for scr refresh
            Imagen_7054.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7054, 'tStopRefresh')  # time at next scr refresh
            Imagen_7054.setAutoDraw(False)
    
    # *Imagen_7247* updates
    if Imagen_7247.status == NOT_STARTED and tThisFlip >= 130.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7247.frameNStart = frameN  # exact frame index
        Imagen_7247.tStart = t  # local t and not account for scr refresh
        Imagen_7247.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7247, 'tStartRefresh')  # time at next scr refresh
        Imagen_7247.setAutoDraw(True)
    if Imagen_7247.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7247.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7247.tStop = t  # not accounting for scr refresh
            Imagen_7247.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7247, 'tStopRefresh')  # time at next scr refresh
            Imagen_7247.setAutoDraw(False)
    
    # *Imagen_7461* updates
    if Imagen_7461.status == NOT_STARTED and tThisFlip >= 135.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7461.frameNStart = frameN  # exact frame index
        Imagen_7461.tStart = t  # local t and not account for scr refresh
        Imagen_7461.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7461, 'tStartRefresh')  # time at next scr refresh
        Imagen_7461.setAutoDraw(True)
    if Imagen_7461.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7461.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7461.tStop = t  # not accounting for scr refresh
            Imagen_7461.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7461, 'tStopRefresh')  # time at next scr refresh
            Imagen_7461.setAutoDraw(False)
    
    # *Imagen_7504* updates
    if Imagen_7504.status == NOT_STARTED and tThisFlip >= 140.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7504.frameNStart = frameN  # exact frame index
        Imagen_7504.tStart = t  # local t and not account for scr refresh
        Imagen_7504.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7504, 'tStartRefresh')  # time at next scr refresh
        Imagen_7504.setAutoDraw(True)
    if Imagen_7504.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7504.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7504.tStop = t  # not accounting for scr refresh
            Imagen_7504.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7504, 'tStopRefresh')  # time at next scr refresh
            Imagen_7504.setAutoDraw(False)
    
    # *Imagen_7476* updates
    if Imagen_7476.status == NOT_STARTED and tThisFlip >= 145.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7476.frameNStart = frameN  # exact frame index
        Imagen_7476.tStart = t  # local t and not account for scr refresh
        Imagen_7476.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7476, 'tStartRefresh')  # time at next scr refresh
        Imagen_7476.setAutoDraw(True)
    if Imagen_7476.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7476.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7476.tStop = t  # not accounting for scr refresh
            Imagen_7476.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7476, 'tStopRefresh')  # time at next scr refresh
            Imagen_7476.setAutoDraw(False)
    
    # *Imagen_6910* updates
    if Imagen_6910.status == NOT_STARTED and tThisFlip >= 150.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_6910.frameNStart = frameN  # exact frame index
        Imagen_6910.tStart = t  # local t and not account for scr refresh
        Imagen_6910.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_6910, 'tStartRefresh')  # time at next scr refresh
        Imagen_6910.setAutoDraw(True)
    if Imagen_6910.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_6910.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_6910.tStop = t  # not accounting for scr refresh
            Imagen_6910.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_6910, 'tStopRefresh')  # time at next scr refresh
            Imagen_6910.setAutoDraw(False)
    
    # *Imagen_7620* updates
    if Imagen_7620.status == NOT_STARTED and tThisFlip >= 155.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7620.frameNStart = frameN  # exact frame index
        Imagen_7620.tStart = t  # local t and not account for scr refresh
        Imagen_7620.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7620, 'tStartRefresh')  # time at next scr refresh
        Imagen_7620.setAutoDraw(True)
    if Imagen_7620.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7620.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7620.tStop = t  # not accounting for scr refresh
            Imagen_7620.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7620, 'tStopRefresh')  # time at next scr refresh
            Imagen_7620.setAutoDraw(False)
    
    # *Imagen_7365* updates
    if Imagen_7365.status == NOT_STARTED and tThisFlip >= 160.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7365.frameNStart = frameN  # exact frame index
        Imagen_7365.tStart = t  # local t and not account for scr refresh
        Imagen_7365.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7365, 'tStartRefresh')  # time at next scr refresh
        Imagen_7365.setAutoDraw(True)
    if Imagen_7365.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7365.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7365.tStop = t  # not accounting for scr refresh
            Imagen_7365.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7365, 'tStopRefresh')  # time at next scr refresh
            Imagen_7365.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Imagenes_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Imagenes_2"-------
for thisComponent in Imagenes_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Imagenes_3"-------
routineTimer.add(165.000000)
# update component parameters for each repeat
# keep track of which components have finished
Imagenes_3Components = [Image_7092, Image_7620, Image_9422, Image_7476, Image_7504, Image_7054, Image_5455, Image_5535, Image_7365, Image_5661, Image_7077, Image_7248, Image_7013, Image_7211, Image_7461, Image_3005, Image_7188, Image_8211, Image_7247, Image_7496, Image_5900, Image_9468, Image_7402, Image_7487, Image_5395, Image_6910, Image_6900, Image_7560, Image_7830, Image_8325, Image_7820, Image_9472, Image_7632]
for thisComponent in Imagenes_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Imagenes_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Imagenes_3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Imagenes_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Imagenes_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Image_7092* updates
    if Image_7092.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7092.frameNStart = frameN  # exact frame index
        Image_7092.tStart = t  # local t and not account for scr refresh
        Image_7092.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7092, 'tStartRefresh')  # time at next scr refresh
        Image_7092.setAutoDraw(True)
    if Image_7092.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7092.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7092.tStop = t  # not accounting for scr refresh
            Image_7092.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7092, 'tStopRefresh')  # time at next scr refresh
            Image_7092.setAutoDraw(False)
    
    # *Image_7620* updates
    if Image_7620.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7620.frameNStart = frameN  # exact frame index
        Image_7620.tStart = t  # local t and not account for scr refresh
        Image_7620.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7620, 'tStartRefresh')  # time at next scr refresh
        Image_7620.setAutoDraw(True)
    if Image_7620.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7620.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7620.tStop = t  # not accounting for scr refresh
            Image_7620.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7620, 'tStopRefresh')  # time at next scr refresh
            Image_7620.setAutoDraw(False)
    
    # *Image_9422* updates
    if Image_9422.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        Image_9422.frameNStart = frameN  # exact frame index
        Image_9422.tStart = t  # local t and not account for scr refresh
        Image_9422.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_9422, 'tStartRefresh')  # time at next scr refresh
        Image_9422.setAutoDraw(True)
    if Image_9422.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_9422.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_9422.tStop = t  # not accounting for scr refresh
            Image_9422.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_9422, 'tStopRefresh')  # time at next scr refresh
            Image_9422.setAutoDraw(False)
    
    # *Image_7476* updates
    if Image_7476.status == NOT_STARTED and tThisFlip >= 15.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7476.frameNStart = frameN  # exact frame index
        Image_7476.tStart = t  # local t and not account for scr refresh
        Image_7476.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7476, 'tStartRefresh')  # time at next scr refresh
        Image_7476.setAutoDraw(True)
    if Image_7476.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7476.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7476.tStop = t  # not accounting for scr refresh
            Image_7476.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7476, 'tStopRefresh')  # time at next scr refresh
            Image_7476.setAutoDraw(False)
    
    # *Image_7504* updates
    if Image_7504.status == NOT_STARTED and tThisFlip >= 20.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7504.frameNStart = frameN  # exact frame index
        Image_7504.tStart = t  # local t and not account for scr refresh
        Image_7504.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7504, 'tStartRefresh')  # time at next scr refresh
        Image_7504.setAutoDraw(True)
    if Image_7504.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7504.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7504.tStop = t  # not accounting for scr refresh
            Image_7504.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7504, 'tStopRefresh')  # time at next scr refresh
            Image_7504.setAutoDraw(False)
    
    # *Image_7054* updates
    if Image_7054.status == NOT_STARTED and tThisFlip >= 25.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7054.frameNStart = frameN  # exact frame index
        Image_7054.tStart = t  # local t and not account for scr refresh
        Image_7054.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7054, 'tStartRefresh')  # time at next scr refresh
        Image_7054.setAutoDraw(True)
    if Image_7054.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7054.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7054.tStop = t  # not accounting for scr refresh
            Image_7054.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7054, 'tStopRefresh')  # time at next scr refresh
            Image_7054.setAutoDraw(False)
    
    # *Image_5455* updates
    if Image_5455.status == NOT_STARTED and tThisFlip >= 30.0-frameTolerance:
        # keep track of start time/frame for later
        Image_5455.frameNStart = frameN  # exact frame index
        Image_5455.tStart = t  # local t and not account for scr refresh
        Image_5455.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_5455, 'tStartRefresh')  # time at next scr refresh
        Image_5455.setAutoDraw(True)
    if Image_5455.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_5455.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_5455.tStop = t  # not accounting for scr refresh
            Image_5455.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_5455, 'tStopRefresh')  # time at next scr refresh
            Image_5455.setAutoDraw(False)
    
    # *Image_5535* updates
    if Image_5535.status == NOT_STARTED and tThisFlip >= 35.0-frameTolerance:
        # keep track of start time/frame for later
        Image_5535.frameNStart = frameN  # exact frame index
        Image_5535.tStart = t  # local t and not account for scr refresh
        Image_5535.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_5535, 'tStartRefresh')  # time at next scr refresh
        Image_5535.setAutoDraw(True)
    if Image_5535.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_5535.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_5535.tStop = t  # not accounting for scr refresh
            Image_5535.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_5535, 'tStopRefresh')  # time at next scr refresh
            Image_5535.setAutoDraw(False)
    
    # *Image_7365* updates
    if Image_7365.status == NOT_STARTED and tThisFlip >= 40.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7365.frameNStart = frameN  # exact frame index
        Image_7365.tStart = t  # local t and not account for scr refresh
        Image_7365.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7365, 'tStartRefresh')  # time at next scr refresh
        Image_7365.setAutoDraw(True)
    if Image_7365.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7365.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7365.tStop = t  # not accounting for scr refresh
            Image_7365.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7365, 'tStopRefresh')  # time at next scr refresh
            Image_7365.setAutoDraw(False)
    
    # *Image_5661* updates
    if Image_5661.status == NOT_STARTED and tThisFlip >= 45.0-frameTolerance:
        # keep track of start time/frame for later
        Image_5661.frameNStart = frameN  # exact frame index
        Image_5661.tStart = t  # local t and not account for scr refresh
        Image_5661.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_5661, 'tStartRefresh')  # time at next scr refresh
        Image_5661.setAutoDraw(True)
    if Image_5661.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_5661.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_5661.tStop = t  # not accounting for scr refresh
            Image_5661.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_5661, 'tStopRefresh')  # time at next scr refresh
            Image_5661.setAutoDraw(False)
    
    # *Image_7077* updates
    if Image_7077.status == NOT_STARTED and tThisFlip >= 50.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7077.frameNStart = frameN  # exact frame index
        Image_7077.tStart = t  # local t and not account for scr refresh
        Image_7077.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7077, 'tStartRefresh')  # time at next scr refresh
        Image_7077.setAutoDraw(True)
    if Image_7077.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7077.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7077.tStop = t  # not accounting for scr refresh
            Image_7077.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7077, 'tStopRefresh')  # time at next scr refresh
            Image_7077.setAutoDraw(False)
    
    # *Image_7248* updates
    if Image_7248.status == NOT_STARTED and tThisFlip >= 55.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7248.frameNStart = frameN  # exact frame index
        Image_7248.tStart = t  # local t and not account for scr refresh
        Image_7248.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7248, 'tStartRefresh')  # time at next scr refresh
        Image_7248.setAutoDraw(True)
    if Image_7248.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7248.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7248.tStop = t  # not accounting for scr refresh
            Image_7248.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7248, 'tStopRefresh')  # time at next scr refresh
            Image_7248.setAutoDraw(False)
    
    # *Image_7013* updates
    if Image_7013.status == NOT_STARTED and tThisFlip >= 60.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7013.frameNStart = frameN  # exact frame index
        Image_7013.tStart = t  # local t and not account for scr refresh
        Image_7013.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7013, 'tStartRefresh')  # time at next scr refresh
        Image_7013.setAutoDraw(True)
    if Image_7013.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7013.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7013.tStop = t  # not accounting for scr refresh
            Image_7013.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7013, 'tStopRefresh')  # time at next scr refresh
            Image_7013.setAutoDraw(False)
    
    # *Image_7211* updates
    if Image_7211.status == NOT_STARTED and tThisFlip >= 65.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7211.frameNStart = frameN  # exact frame index
        Image_7211.tStart = t  # local t and not account for scr refresh
        Image_7211.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7211, 'tStartRefresh')  # time at next scr refresh
        Image_7211.setAutoDraw(True)
    if Image_7211.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7211.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7211.tStop = t  # not accounting for scr refresh
            Image_7211.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7211, 'tStopRefresh')  # time at next scr refresh
            Image_7211.setAutoDraw(False)
    
    # *Image_7461* updates
    if Image_7461.status == NOT_STARTED and tThisFlip >= 70.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7461.frameNStart = frameN  # exact frame index
        Image_7461.tStart = t  # local t and not account for scr refresh
        Image_7461.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7461, 'tStartRefresh')  # time at next scr refresh
        Image_7461.setAutoDraw(True)
    if Image_7461.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7461.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7461.tStop = t  # not accounting for scr refresh
            Image_7461.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7461, 'tStopRefresh')  # time at next scr refresh
            Image_7461.setAutoDraw(False)
    
    # *Image_3005* updates
    if Image_3005.status == NOT_STARTED and tThisFlip >= 75.0-frameTolerance:
        # keep track of start time/frame for later
        Image_3005.frameNStart = frameN  # exact frame index
        Image_3005.tStart = t  # local t and not account for scr refresh
        Image_3005.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_3005, 'tStartRefresh')  # time at next scr refresh
        Image_3005.setAutoDraw(True)
    if Image_3005.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_3005.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_3005.tStop = t  # not accounting for scr refresh
            Image_3005.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_3005, 'tStopRefresh')  # time at next scr refresh
            Image_3005.setAutoDraw(False)
    
    # *Image_7188* updates
    if Image_7188.status == NOT_STARTED and tThisFlip >= 80.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7188.frameNStart = frameN  # exact frame index
        Image_7188.tStart = t  # local t and not account for scr refresh
        Image_7188.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7188, 'tStartRefresh')  # time at next scr refresh
        Image_7188.setAutoDraw(True)
    if Image_7188.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7188.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7188.tStop = t  # not accounting for scr refresh
            Image_7188.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7188, 'tStopRefresh')  # time at next scr refresh
            Image_7188.setAutoDraw(False)
    
    # *Image_8211* updates
    if Image_8211.status == NOT_STARTED and tThisFlip >= 85.0-frameTolerance:
        # keep track of start time/frame for later
        Image_8211.frameNStart = frameN  # exact frame index
        Image_8211.tStart = t  # local t and not account for scr refresh
        Image_8211.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_8211, 'tStartRefresh')  # time at next scr refresh
        Image_8211.setAutoDraw(True)
    if Image_8211.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_8211.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_8211.tStop = t  # not accounting for scr refresh
            Image_8211.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_8211, 'tStopRefresh')  # time at next scr refresh
            Image_8211.setAutoDraw(False)
    
    # *Image_7247* updates
    if Image_7247.status == NOT_STARTED and tThisFlip >= 90.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7247.frameNStart = frameN  # exact frame index
        Image_7247.tStart = t  # local t and not account for scr refresh
        Image_7247.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7247, 'tStartRefresh')  # time at next scr refresh
        Image_7247.setAutoDraw(True)
    if Image_7247.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7247.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7247.tStop = t  # not accounting for scr refresh
            Image_7247.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7247, 'tStopRefresh')  # time at next scr refresh
            Image_7247.setAutoDraw(False)
    
    # *Image_7496* updates
    if Image_7496.status == NOT_STARTED and tThisFlip >= 95.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7496.frameNStart = frameN  # exact frame index
        Image_7496.tStart = t  # local t and not account for scr refresh
        Image_7496.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7496, 'tStartRefresh')  # time at next scr refresh
        Image_7496.setAutoDraw(True)
    if Image_7496.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7496.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7496.tStop = t  # not accounting for scr refresh
            Image_7496.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7496, 'tStopRefresh')  # time at next scr refresh
            Image_7496.setAutoDraw(False)
    
    # *Image_5900* updates
    if Image_5900.status == NOT_STARTED and tThisFlip >= 100.0-frameTolerance:
        # keep track of start time/frame for later
        Image_5900.frameNStart = frameN  # exact frame index
        Image_5900.tStart = t  # local t and not account for scr refresh
        Image_5900.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_5900, 'tStartRefresh')  # time at next scr refresh
        Image_5900.setAutoDraw(True)
    if Image_5900.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_5900.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_5900.tStop = t  # not accounting for scr refresh
            Image_5900.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_5900, 'tStopRefresh')  # time at next scr refresh
            Image_5900.setAutoDraw(False)
    
    # *Image_9468* updates
    if Image_9468.status == NOT_STARTED and tThisFlip >= 105.0-frameTolerance:
        # keep track of start time/frame for later
        Image_9468.frameNStart = frameN  # exact frame index
        Image_9468.tStart = t  # local t and not account for scr refresh
        Image_9468.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_9468, 'tStartRefresh')  # time at next scr refresh
        Image_9468.setAutoDraw(True)
    if Image_9468.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_9468.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_9468.tStop = t  # not accounting for scr refresh
            Image_9468.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_9468, 'tStopRefresh')  # time at next scr refresh
            Image_9468.setAutoDraw(False)
    
    # *Image_7402* updates
    if Image_7402.status == NOT_STARTED and tThisFlip >= 110.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7402.frameNStart = frameN  # exact frame index
        Image_7402.tStart = t  # local t and not account for scr refresh
        Image_7402.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7402, 'tStartRefresh')  # time at next scr refresh
        Image_7402.setAutoDraw(True)
    if Image_7402.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7402.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7402.tStop = t  # not accounting for scr refresh
            Image_7402.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7402, 'tStopRefresh')  # time at next scr refresh
            Image_7402.setAutoDraw(False)
    
    # *Image_7487* updates
    if Image_7487.status == NOT_STARTED and tThisFlip >= 115.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7487.frameNStart = frameN  # exact frame index
        Image_7487.tStart = t  # local t and not account for scr refresh
        Image_7487.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7487, 'tStartRefresh')  # time at next scr refresh
        Image_7487.setAutoDraw(True)
    if Image_7487.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7487.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7487.tStop = t  # not accounting for scr refresh
            Image_7487.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7487, 'tStopRefresh')  # time at next scr refresh
            Image_7487.setAutoDraw(False)
    
    # *Image_5395* updates
    if Image_5395.status == NOT_STARTED and tThisFlip >= 120.0-frameTolerance:
        # keep track of start time/frame for later
        Image_5395.frameNStart = frameN  # exact frame index
        Image_5395.tStart = t  # local t and not account for scr refresh
        Image_5395.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_5395, 'tStartRefresh')  # time at next scr refresh
        Image_5395.setAutoDraw(True)
    if Image_5395.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_5395.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_5395.tStop = t  # not accounting for scr refresh
            Image_5395.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_5395, 'tStopRefresh')  # time at next scr refresh
            Image_5395.setAutoDraw(False)
    
    # *Image_6910* updates
    if Image_6910.status == NOT_STARTED and tThisFlip >= 125.0-frameTolerance:
        # keep track of start time/frame for later
        Image_6910.frameNStart = frameN  # exact frame index
        Image_6910.tStart = t  # local t and not account for scr refresh
        Image_6910.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_6910, 'tStartRefresh')  # time at next scr refresh
        Image_6910.setAutoDraw(True)
    if Image_6910.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_6910.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_6910.tStop = t  # not accounting for scr refresh
            Image_6910.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_6910, 'tStopRefresh')  # time at next scr refresh
            Image_6910.setAutoDraw(False)
    
    # *Image_6900* updates
    if Image_6900.status == NOT_STARTED and tThisFlip >= 130.0-frameTolerance:
        # keep track of start time/frame for later
        Image_6900.frameNStart = frameN  # exact frame index
        Image_6900.tStart = t  # local t and not account for scr refresh
        Image_6900.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_6900, 'tStartRefresh')  # time at next scr refresh
        Image_6900.setAutoDraw(True)
    if Image_6900.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_6900.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_6900.tStop = t  # not accounting for scr refresh
            Image_6900.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_6900, 'tStopRefresh')  # time at next scr refresh
            Image_6900.setAutoDraw(False)
    
    # *Image_7560* updates
    if Image_7560.status == NOT_STARTED and tThisFlip >= 135.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7560.frameNStart = frameN  # exact frame index
        Image_7560.tStart = t  # local t and not account for scr refresh
        Image_7560.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7560, 'tStartRefresh')  # time at next scr refresh
        Image_7560.setAutoDraw(True)
    if Image_7560.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7560.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7560.tStop = t  # not accounting for scr refresh
            Image_7560.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7560, 'tStopRefresh')  # time at next scr refresh
            Image_7560.setAutoDraw(False)
    
    # *Image_7830* updates
    if Image_7830.status == NOT_STARTED and tThisFlip >= 140.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7830.frameNStart = frameN  # exact frame index
        Image_7830.tStart = t  # local t and not account for scr refresh
        Image_7830.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7830, 'tStartRefresh')  # time at next scr refresh
        Image_7830.setAutoDraw(True)
    if Image_7830.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7830.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7830.tStop = t  # not accounting for scr refresh
            Image_7830.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7830, 'tStopRefresh')  # time at next scr refresh
            Image_7830.setAutoDraw(False)
    
    # *Image_8325* updates
    if Image_8325.status == NOT_STARTED and tThisFlip >= 145.0-frameTolerance:
        # keep track of start time/frame for later
        Image_8325.frameNStart = frameN  # exact frame index
        Image_8325.tStart = t  # local t and not account for scr refresh
        Image_8325.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_8325, 'tStartRefresh')  # time at next scr refresh
        Image_8325.setAutoDraw(True)
    if Image_8325.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_8325.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_8325.tStop = t  # not accounting for scr refresh
            Image_8325.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_8325, 'tStopRefresh')  # time at next scr refresh
            Image_8325.setAutoDraw(False)
    
    # *Image_7820* updates
    if Image_7820.status == NOT_STARTED and tThisFlip >= 150.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7820.frameNStart = frameN  # exact frame index
        Image_7820.tStart = t  # local t and not account for scr refresh
        Image_7820.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7820, 'tStartRefresh')  # time at next scr refresh
        Image_7820.setAutoDraw(True)
    if Image_7820.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7820.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7820.tStop = t  # not accounting for scr refresh
            Image_7820.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7820, 'tStopRefresh')  # time at next scr refresh
            Image_7820.setAutoDraw(False)
    
    # *Image_9472* updates
    if Image_9472.status == NOT_STARTED and tThisFlip >= 155.0-frameTolerance:
        # keep track of start time/frame for later
        Image_9472.frameNStart = frameN  # exact frame index
        Image_9472.tStart = t  # local t and not account for scr refresh
        Image_9472.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_9472, 'tStartRefresh')  # time at next scr refresh
        Image_9472.setAutoDraw(True)
    if Image_9472.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_9472.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_9472.tStop = t  # not accounting for scr refresh
            Image_9472.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_9472, 'tStopRefresh')  # time at next scr refresh
            Image_9472.setAutoDraw(False)
    
    # *Image_7632* updates
    if Image_7632.status == NOT_STARTED and tThisFlip >= 160.0-frameTolerance:
        # keep track of start time/frame for later
        Image_7632.frameNStart = frameN  # exact frame index
        Image_7632.tStart = t  # local t and not account for scr refresh
        Image_7632.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image_7632, 'tStartRefresh')  # time at next scr refresh
        Image_7632.setAutoDraw(True)
    if Image_7632.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Image_7632.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Image_7632.tStop = t  # not accounting for scr refresh
            Image_7632.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Image_7632, 'tStopRefresh')  # time at next scr refresh
            Image_7632.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Imagenes_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Imagenes_3"-------
for thisComponent in Imagenes_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        
        
# ------Prepare to start Routine "Imagenes_4"-------
routineTimer.add(165.000000)
# update component parameters for each repeat
# keep track of which components have finished
Imagenes_4Components = [Imagen_5535, Imagen_8211, Imagen_7402, Imagen_5395, Imagen_7092, Imagen_7487, Imagen_7188, Imagen_7820, Imagen_5900, Imagen_7476]
for thisComponent in Imagenes_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Imagenes_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Imagenes_4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Imagenes_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Imagenes_4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Imagen_5535* updates
    if Imagen_5535.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_5535.frameNStart = frameN  # exact frame index
        Imagen_5535.tStart = t  # local t and not account for scr refresh
        Imagen_5535.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_5535, 'tStartRefresh')  # time at next scr refresh
        Imagen_5535.setAutoDraw(True)
    if Imagen_5535.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_5535.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_5535.tStop = t  # not accounting for scr refresh
            Imagen_5535.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_5535, 'tStopRefresh')  # time at next scr refresh
            Imagen_5535.setAutoDraw(False)
    
    # *Imagen_8211* updates
    if Imagen_8211.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_8211.frameNStart = frameN  # exact frame index
        Imagen_8211.tStart = t  # local t and not account for scr refresh
        Imagen_8211.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_8211, 'tStartRefresh')  # time at next scr refresh
        Imagen_8211.setAutoDraw(True)
    if Imagen_8211.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_8211.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_8211.tStop = t  # not accounting for scr refresh
            Imagen_8211.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_8211, 'tStopRefresh')  # time at next scr refresh
            Imagen_8211.setAutoDraw(False)
    
    # *Imagen_7402* updates
    if Imagen_7402.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7402.frameNStart = frameN  # exact frame index
        Imagen_7402.tStart = t  # local t and not account for scr refresh
        Imagen_7402.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7402, 'tStartRefresh')  # time at next scr refresh
        Imagen_7402.setAutoDraw(True)
    if Imagen_7402.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7402.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7402.tStop = t  # not accounting for scr refresh
            Imagen_7402.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7402, 'tStopRefresh')  # time at next scr refresh
            Imagen_7402.setAutoDraw(False)
    
    # *Imagen_5395* updates
    if Imagen_5395.status == NOT_STARTED and tThisFlip >= 15.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_5395.frameNStart = frameN  # exact frame index
        Imagen_5395.tStart = t  # local t and not account for scr refresh
        Imagen_5395.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_5395, 'tStartRefresh')  # time at next scr refresh
        Imagen_5395.setAutoDraw(True)
    if Imagen_5395.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_5395.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_5395.tStop = t  # not accounting for scr refresh
            Imagen_5395.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_5395, 'tStopRefresh')  # time at next scr refresh
            Imagen_5395.setAutoDraw(False)
    
    # *Imagen_7092* updates
    if Imagen_7092.status == NOT_STARTED and tThisFlip >= 20.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7092.frameNStart = frameN  # exact frame index
        Imagen_7092.tStart = t  # local t and not account for scr refresh
        Imagen_7092.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7092, 'tStartRefresh')  # time at next scr refresh
        Imagen_7092.setAutoDraw(True)
    if Imagen_7092.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7092.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7092.tStop = t  # not accounting for scr refresh
            Imagen_7092.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7092, 'tStopRefresh')  # time at next scr refresh
            Imagen_7092.setAutoDraw(False)
    
    # *Imagen_7487* updates
    if Imagen_7487.status == NOT_STARTED and tThisFlip >= 25.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7487.frameNStart = frameN  # exact frame index
        Imagen_7487.tStart = t  # local t and not account for scr refresh
        Imagen_7487.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7487, 'tStartRefresh')  # time at next scr refresh
        Imagen_7487.setAutoDraw(True)
    if Imagen_7487.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7487.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7487.tStop = t  # not accounting for scr refresh
            Imagen_7487.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7487, 'tStopRefresh')  # time at next scr refresh
            Imagen_7487.setAutoDraw(False)
    
    # *Imagen_7188* updates
    if Imagen_7188.status == NOT_STARTED and tThisFlip >= 30.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7188.frameNStart = frameN  # exact frame index
        Imagen_7188.tStart = t  # local t and not account for scr refresh
        Imagen_7188.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7188, 'tStartRefresh')  # time at next scr refresh
        Imagen_7188.setAutoDraw(True)
    if Imagen_7188.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7188.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7188.tStop = t  # not accounting for scr refresh
            Imagen_7188.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7188, 'tStopRefresh')  # time at next scr refresh
            Imagen_7188.setAutoDraw(False)
    
    # *Imagen_7820* updates
    if Imagen_7820.status == NOT_STARTED and tThisFlip >= 35.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7820.frameNStart = frameN  # exact frame index
        Imagen_7820.tStart = t  # local t and not account for scr refresh
        Imagen_7820.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7820, 'tStartRefresh')  # time at next scr refresh
        Imagen_7820.setAutoDraw(True)
    if Imagen_7820.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7820.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7820.tStop = t  # not accounting for scr refresh
            Imagen_7820.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7820, 'tStopRefresh')  # time at next scr refresh
            Imagen_7820.setAutoDraw(False)
    
    # *Imagen_5900* updates
    if Imagen_5900.status == NOT_STARTED and tThisFlip >= 40.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_5900.frameNStart = frameN  # exact frame index
        Imagen_5900.tStart = t  # local t and not account for scr refresh
        Imagen_5900.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_5900, 'tStartRefresh')  # time at next scr refresh
        Imagen_5900.setAutoDraw(True)
    if Imagen_5900.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_5900.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_5900.tStop = t  # not accounting for scr refresh
            Imagen_5900.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_5900, 'tStopRefresh')  # time at next scr refresh
            Imagen_5900.setAutoDraw(False)
    
    # *Imagen_7476* updates
    if Imagen_7476.status == NOT_STARTED and tThisFlip >= 45.0-frameTolerance:
        # keep track of start time/frame for later
        Imagen_7476.frameNStart = frameN  # exact frame index
        Imagen_7476.tStart = t  # local t and not account for scr refresh
        Imagen_7476.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Imagen_7476, 'tStartRefresh')  # time at next scr refresh
        Imagen_7476.setAutoDraw(True)
    if Imagen_7476.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Imagen_7476.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Imagen_7476.tStop = t  # not accounting for scr refresh
            Imagen_7476.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Imagen_7476, 'tStopRefresh')  # time at next scr refresh
            Imagen_7476.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Imagenes_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Imagenes_4"-------
for thisComponent in Imagenes_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)        


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
