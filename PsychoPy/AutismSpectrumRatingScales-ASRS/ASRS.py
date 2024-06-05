#Here, a Graphical User Interface (GUI) is designed in which the user can answer the Spanish version of the 
#parent-report full-length Autism Spectrum Rating Scales (ASRS; Goldstein S, Naglieri J. Autism Spectrum Rating Scales™ (ASRS®). North
#Tonawanda NY Multi-Health Syst. 2013)

#The full-length ASRS was used, which consists of 71
#items to assess autistic behaviors divided into the following scales: (1) Social/Communication (SC), (2) Unusual
#Behaviors (UB), (3) Self-Regulation (SR), (4) Total Score (TOT; SC, UB, SR), (5) DSM-5 criteria, (6) Peer Socialization
#(PS), (7) Adult Socialization (AS), (8) Social/Emotional Reciprocity (SER), (9) Atypical Language (AL),
#(10) Stereotypy (ST), (11) Behavioral Rigidity (BR), (12) Sensory Sensitivity (SS), and (13) Attention (AT). TOT
#is an equally weighted composite of SC, UB and SR. A 4-level scale is presented to specify how often a particular
#behavior is observed (0 = Never, 1 = Rarely, 2 = Occasionally 3 = Frequently, 4 = Very frequently).

#The answers are saved within an Excel file (.csv) that will be used to compute Standardized scores and generate a report of the patient's behavior.
#Please refer to the corresponding Matlab code that uses this Excel file as input to generate the report. 

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
expName = 'ASRS'  # from the Builder filename that created this script
expInfo = {'participant number': '', 'participant name': '', 'participant age': '','session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant number'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\mathi\\OneDrive\\Documents\\Job\\GitHub\\PsychoPy\\AutismSpectrumRatingScales-ASRS\\ASRS.py',
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
    text='Lea cada frase después de la oración: "Durante las útlimas cuatro semanas, con qué frecuencia observó que el niño(a)...,"\nluego marque su respuesta debajo de la palabra que indique la frecuencia con la que usted observó la conducta. \n\nLea cada frase cuidosamente, luego marque con qué frecuencia usted observó la conducta durante la últimas cuatro semanas. \nConteste cada frase sin omitir ninguna.\n\n\nPresione la barra de espacio para empezar.\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instr = keyboard.Keyboard()

# Initialize components for Routine "ASRSa"
ASRSaClock = core.Clock()

P1a = visual.TextStim(win=win, name='P1a',
    text='pareció desorganizado?',
    font='Arial',
    pos=(-0.37, 0.30), height=0.02, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P1b = visual.RatingScale(win=win, name='P1b', marker='triangle', size=1.0, pos=[-0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P2a = visual.TextStim(win=win, name='P2a',
    text='se sintió incómodo(a) con algunas telas o etiquetas en la ropa?',
    font='Arial',
    pos=(0.37, 0.30), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P2b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P3a = visual.TextStim(win=win, name='P3a',
    text='buscó la compañía de otros niños?',
    font='Arial',
    pos=(-0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P3b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[-0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P4a = visual.TextStim(win=win, name='P4a',
    text='demostró poca emoción?',
    font='Arial',
    pos=(0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P4b = visual.RatingScale(win=win, name='P4b', marker='triangle', size=1.0, pos=[0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P5a = visual.TextStim(win=win, name='P5a',
    text='siguió instrucciones que entendió?',
    font='Arial',
    pos=(-0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P5b = visual.RatingScale(win=win, name='P5b', marker='triangle', size=1.0, pos=[-0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P6a = visual.TextStim(win=win, name='P6a',
    text='discutió y peleó con otros niños?',
    font='Arial',
    pos=(0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P6b = visual.RatingScale(win=win, name='P6b', marker='triangle', size=1.0, pos=[0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


P7a = visual.TextStim(win=win, name='P7a',
    text='tuvo dificultad en esperar su turno?',
    font='Arial',
    pos=(-0.37, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P7b = visual.RatingScale(win=win, name='P7b', marker='triangle', size=1.0, pos=[-0.5, -0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


P8a = visual.TextStim(win=win, name='P8a',
    text='compartió en actividades divertidas con otros?',
    font='Arial',
    pos=(0.37, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P8b = visual.RatingScale(win=win, name='P8b', marker='triangle', size=1.0, pos=[0.5, -0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


instr_2 = visual.TextStim(win=win, name='instr_2',
    text='Presione la tecla de espacio para seguir',
    font='Arial',
    pos=(0, -0.40), height=0.03, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instr_2 = keyboard.Keyboard()


instr_3 = visual.TextStim(win=win, name='instr_3',
    text='¿Durante las últimas cuatro semanas, con qué frecuencia observó que el niño(a)...',
    font='Arial',
    pos=(0, 0.40), height=0.025, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "ASRSb"
ASRSbClock = core.Clock()

P9a = visual.TextStim(win=win, name='P1a',
    text='miró a las personas con quien hablaba?',
    font='Arial',
    pos=(-0.37, 0.30), height=0.02, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P9b = visual.RatingScale(win=win, name='P1b', marker='triangle', size=1.0, pos=[-0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P10a = visual.TextStim(win=win, name='P2a',
    text='se envolvió en tarea que requieren esfuerzo continuo?',
    font='Arial',
    pos=(0.37, 0.30), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P10b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P11a = visual.TextStim(win=win, name='P3a',
    text='evitó mirar a personas que le hablaban?',
    font='Arial',
    pos=(-0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P11b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[-0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P12a = visual.TextStim(win=win, name='P4a',
    text='jugó con juguetes en manera apropiada?',
    font='Arial',
    pos=(0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P12b = visual.RatingScale(win=win, name='P4b', marker='triangle', size=1.0, pos=[0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P13a = visual.TextStim(win=win, name='P5a',
    text='reaccionó fuertemente a cualquier cambio en rutina?',
    font='Arial',
    pos=(-0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P13b = visual.RatingScale(win=win, name='P5b', marker='triangle', size=1.0, pos=[-0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P14a = visual.TextStim(win=win, name='P6a',
    text='tuvo dificultad de hablar con otros niños?',
    font='Arial',
    pos=(0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P14b = visual.RatingScale(win=win, name='P6b', marker='triangle', size=1.0, pos=[0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


P15a = visual.TextStim(win=win, name='P7a',
    text='entendió el punto de vista de otros?',
    font='Arial',
    pos=(-0.37, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P15b = visual.RatingScale(win=win, name='P7b', marker='triangle', size=1.0, pos=[-0.5, -0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


P16a = visual.TextStim(win=win, name='P8a',
    text='aprendió tareas sencillas y luego las olvidó rápidamente?',
    font='Arial',
    pos=(0.37, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P16b = visual.RatingScale(win=win, name='P8b', marker='triangle', size=1.0, pos=[0.5, -0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


instr_4 = visual.TextStim(win=win, name='instr_4',
    text='Presione la tecla de espacio para seguir',
    font='Arial',
    pos=(0, -0.40), height=0.03, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instr_4 = keyboard.Keyboard()


instr_5 = visual.TextStim(win=win, name='instr_5',
    text='¿Durante las últimas cuatro semanas, con qué frecuencia observó que el niño(a)...',
    font='Arial',
    pos=(0, 0.40), height=0.025, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);



# Initialize components for Routine "ASRSc"
ASRScClock = core.Clock()

P17a = visual.TextStim(win=win, name='P1a',
    text='utilizó lenguaje que es inmaduro para su edad?',
    font='Arial',
    pos=(-0.37, 0.30), height=0.02, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P17b = visual.RatingScale(win=win, name='P1b', marker='triangle', size=1.0, pos=[-0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P18a = visual.TextStim(win=win, name='P2a',
    text='tuvo problemas con adultos?',
    font='Arial',
    pos=(0.37, 0.30), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P18b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P19a = visual.TextStim(win=win, name='P3a',
    text='tuvo problemas sociales con niños de la misma edad?',
    font='Arial',
    pos=(-0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P19b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[-0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P20a = visual.TextStim(win=win, name='P4a',
    text='tuvo una manera rara de hablar?',
    font='Arial',
    pos=(0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P20b = visual.RatingScale(win=win, name='P4b', marker='triangle', size=1.0, pos=[0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P21a = visual.TextStim(win=win, name='P5a',
    text='repitió ciertas palabras o frases fuera de contexto?',
    font='Arial',
    pos=(-0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P21b = visual.RatingScale(win=win, name='P5b', marker='triangle', size=1.0, pos=[-0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P22a = visual.TextStim(win=win, name='P6a',
    text='se obsesionó con detalles?',
    font='Arial',
    pos=(0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P22b = visual.RatingScale(win=win, name='P6b', marker='triangle', size=1.0, pos=[0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


P23a = visual.TextStim(win=win, name='P7a',
    text='mantuvo una conversación?',
    font='Arial',
    pos=(-0.37, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P23b = visual.RatingScale(win=win, name='P7b', marker='triangle', size=1.0, pos=[-0.5, -0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


P24a = visual.TextStim(win=win, name='P8a',
    text='insistió en hacer cosas de la misma manera cada vez?',
    font='Arial',
    pos=(0.37, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P24b = visual.RatingScale(win=win, name='P8b', marker='triangle', size=1.0, pos=[0.5, -0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


instr_6 = visual.TextStim(win=win, name='instr_6',
    text='Presione la tecla de espacio para seguir',
    font='Arial',
    pos=(0, -0.40), height=0.03, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instr_6 = keyboard.Keyboard()


instr_7 = visual.TextStim(win=win, name='instr_7',
    text='¿Durante las últimas cuatro semanas, con qué frecuencia observó que el niño(a)...',
    font='Arial',
    pos=(0, 0.40), height=0.025, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "ASRSd"
ASRSdClock = core.Clock()

P25a = visual.TextStim(win=win, name='P1a',
    text='reaccionó exageradamente a ser tocado(a)?',
    font='Arial',
    pos=(-0.37, 0.30), height=0.02, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P25b = visual.RatingScale(win=win, name='P1b', marker='triangle', size=1.0, pos=[-0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P26a = visual.TextStim(win=win, name='P2a',
    text='repitió lo que otros dijeron?',
    font='Arial',
    pos=(0.37, 0.30), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P26b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P27a = visual.TextStim(win=win, name='P3a',
    text='olió, probó, y comió objetos no comestibles?',
    font='Arial',
    pos=(-0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P27b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[-0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P28a = visual.TextStim(win=win, name='P4a',
    text='entendió cómo se sentía otra persona',
    font='Arial',
    pos=(0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P28b = visual.RatingScale(win=win, name='P4b', marker='triangle', size=1.0, pos=[0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P29a = visual.TextStim(win=win, name='P5a',
    text='reaccionó exageramente a olores comunes?',
    font='Arial',
    pos=(-0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P29b = visual.RatingScale(win=win, name='P5b', marker='triangle', size=1.0, pos=[-0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P30a = visual.TextStim(win=win, name='P6a',
    text='se distrajó?',
    font='Arial',
    pos=(0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P30b = visual.RatingScale(win=win, name='P6b', marker='triangle', size=1.0, pos=[0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


P31a = visual.TextStim(win=win, name='P7a',
    text='jugó con otros?',
    font='Arial',
    pos=(-0.37, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P31b = visual.RatingScale(win=win, name='P7b', marker='triangle', size=1.0, pos=[-0.5, -0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


P32a = visual.TextStim(win=win, name='P8a',
    text='reconoció señales sociales?',
    font='Arial',
    pos=(0.37, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P32b = visual.RatingScale(win=win, name='P8b', marker='triangle', size=1.0, pos=[0.5, -0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


instr_8 = visual.TextStim(win=win, name='instr_8',
    text='Presione la tecla de espacio para seguir',
    font='Arial',
    pos=(0, -0.40), height=0.03, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instr_8 = keyboard.Keyboard()


instr_9 = visual.TextStim(win=win, name='instr_9',
    text='¿Durante las últimas cuatro semanas, con qué frecuencia observó que el niño(a)...',
    font='Arial',
    pos=(0, 0.40), height=0.025, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);



# Initialize components for Routine "ASRSe"
ASRSeClock = core.Clock()

P33a = visual.TextStim(win=win, name='P1a',
    text='respondió cuando le hablaron los adultos?',
    font='Arial',
    pos=(-0.37, 0.30), height=0.02, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P33b = visual.RatingScale(win=win, name='P1b', marker='triangle', size=1.0, pos=[-0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P34a = visual.TextStim(win=win, name='P2a',
    text='evitó mirar a un adulto cuando había un problema?',
    font='Arial',
    pos=(0.37, 0.30), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P34b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P35a = visual.TextStim(win=win, name='P3a',
    text='tuvo problemas prestando atención al hacer tareas de la escuela o de la casa?',
    font='Arial',
    pos=(-0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P35b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[-0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P36a = visual.TextStim(win=win, name='P4a',
    text='cometió errores por descuido en el trabajo escolar?',
    font='Arial',
    pos=(0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P36b = visual.RatingScale(win=win, name='P4b', marker='triangle', size=1.0, pos=[0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P37a = visual.TextStim(win=win, name='P5a',
    text='habló mucho de cosas que a los adultos no les interesan?',
    font='Arial',
    pos=(-0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P37b = visual.RatingScale(win=win, name='P5b', marker='triangle', size=1.0, pos=[-0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P38a = visual.TextStim(win=win, name='P6a',
    text='resistió ser tocado(a) o abrazado(a)?',
    font='Arial',
    pos=(0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P38b = visual.RatingScale(win=win, name='P6b', marker='triangle', size=1.0, pos=[0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


P39a = visual.TextStim(win=win, name='P7a',
    text='le importó lo que otras personas piensan o sienten?',
    font='Arial',
    pos=(-0.37, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P39b = visual.RatingScale(win=win, name='P7b', marker='triangle', size=1.0, pos=[-0.5, -0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


P40a = visual.TextStim(win=win, name='P8a',
    text='se enfocó demasiado en detalles?',
    font='Arial',
    pos=(0.37, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P40b = visual.RatingScale(win=win, name='P8b', marker='triangle', size=1.0, pos=[0.5, -0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


instr_10 = visual.TextStim(win=win, name='instr_10',
    text='Presione la tecla de espacio para seguir',
    font='Arial',
    pos=(0, -0.40), height=0.03, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instr_10 = keyboard.Keyboard()


instr_11 = visual.TextStim(win=win, name='instr_11',
    text='¿Durante las últimas cuatro semanas, con qué frecuencia observó que el niño(a)...',
    font='Arial',
    pos=(0, 0.40), height=0.025, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ASRSf"
ASRSfClock = core.Clock()

P41a = visual.TextStim(win=win, name='P1a',
    text='no entendió porqué no le cae bien a otros?',
    font='Arial',
    pos=(-0.37, 0.30), height=0.02, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P41b = visual.RatingScale(win=win, name='P1b', marker='triangle', size=1.0, pos=[-0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P42a = visual.TextStim(win=win, name='P2a',
    text='compartió su alegría con otros?',
    font='Arial',
    pos=(0.37, 0.30), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P42b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P43a = visual.TextStim(win=win, name='P3a',
    text='demostró interés en las ideas de otros?',
    font='Arial',
    pos=(-0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P43b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[-0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P44a = visual.TextStim(win=win, name='P4a',
    text='dejó tareas escolares u otras tareas sin completar?',
    font='Arial',
    pos=(0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P44b = visual.RatingScale(win=win, name='P4b', marker='triangle', size=1.0, pos=[0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P45a = visual.TextStim(win=win, name='P5a',
    text='entendió humor/bromas apropiadas para su edad?',
    font='Arial',
    pos=(-0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P45b = visual.RatingScale(win=win, name='P5b', marker='triangle', size=1.0, pos=[-0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P46a = visual.TextStim(win=win, name='P6a',
    text='sacudió las manos cuando se excitó?',
    font='Arial',
    pos=(0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P46b = visual.RatingScale(win=win, name='P6b', marker='triangle', size=1.0, pos=[0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


P47a = visual.TextStim(win=win, name='P7a',
    text='escuchó cuando le hablaban?',
    font='Arial',
    pos=(-0.37, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P47b = visual.RatingScale(win=win, name='P7b', marker='triangle', size=1.0, pos=[-0.5, -0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


P48a = visual.TextStim(win=win, name='P8a',
    text='se enfocó en una sola cosa por mucho tiempo?',
    font='Arial',
    pos=(0.37, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P48b = visual.RatingScale(win=win, name='P8b', marker='triangle', size=1.0, pos=[0.5, -0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


instr_12 = visual.TextStim(win=win, name='instr_12',
    text='Presione la tecla de espacio para seguir',
    font='Arial',
    pos=(0, -0.40), height=0.03, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instr_12 = keyboard.Keyboard()


instr_13 = visual.TextStim(win=win, name='instr_13',
    text='¿Durante las últimas cuatro semanas, con qué frecuencia observó que el niño(a)...',
    font='Arial',
    pos=(0, 0.40), height=0.025, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);



# Initialize components for Routine "ASRSg"
ASRSgClock = core.Clock()

P49a = visual.TextStim(win=win, name='P1a',
    text='necesitó que las cosas sucedieran como lo esperaba?',
    font='Arial',
    pos=(-0.37, 0.30), height=0.02, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P49b = visual.RatingScale(win=win, name='P1b', marker='triangle', size=1.0, pos=[-0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P50a = visual.TextStim(win=win, name='P2a',
    text='habló demasiado de cosas que no les interesan a otros niños?',
    font='Arial',
    pos=(0.37, 0.30), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P50b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P51a = visual.TextStim(win=win, name='P3a',
    text='insistió en seguir ciertas rutinas?',
    font='Arial',
    pos=(-0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P51b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[-0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P52a = visual.TextStim(win=win, name='P4a',
    text='tuvo dificultad en prestar atención en a cosas divertidas?',
    font='Arial',
    pos=(0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P52b = visual.RatingScale(win=win, name='P4b', marker='triangle', size=1.0, pos=[0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P53a = visual.TextStim(win=win, name='P5a',
    text='se fascinó con las partes de objetos?',
    font='Arial',
    pos=(-0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P53b = visual.RatingScale(win=win, name='P5b', marker='triangle', size=1.0, pos=[-0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P54a = visual.TextStim(win=win, name='P6a',
    text='alineó objetos en una fila?',
    font='Arial',
    pos=(0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P54b = visual.RatingScale(win=win, name='P6b', marker='triangle', size=1.0, pos=[0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


P55a = visual.TextStim(win=win, name='P7a',
    text='sonrió en manera apropiada?',
    font='Arial',
    pos=(-0.37, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P55b = visual.RatingScale(win=win, name='P7b', marker='triangle', size=1.0, pos=[-0.5, -0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


P56a = visual.TextStim(win=win, name='P8a',
    text='inició conversaciones con otros?',
    font='Arial',
    pos=(0.37, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P56b = visual.RatingScale(win=win, name='P8b', marker='triangle', size=1.0, pos=[0.5, -0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


instr_14 = visual.TextStim(win=win, name='instr_14',
    text='Presione la tecla de espacio para seguir',
    font='Arial',
    pos=(0, -0.40), height=0.03, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instr_14 = keyboard.Keyboard()


instr_15 = visual.TextStim(win=win, name='instr_15',
    text='¿Durante las últimas cuatro semanas, con qué frecuencia observó que el niño(a)...',
    font='Arial',
    pos=(0, 0.40), height=0.025, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ASRSh"
ASRShClock = core.Clock()

P57a = visual.TextStim(win=win, name='P1a',
    text='no completó tareas?',
    font='Arial',
    pos=(-0.37, 0.30), height=0.02, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P57b = visual.RatingScale(win=win, name='P1b', marker='triangle', size=1.0, pos=[-0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P58a = visual.TextStim(win=win, name='P2a',
    text='hizo preguntas que estaban fuera del tema?',
    font='Arial',
    pos=(0.37, 0.30), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P58b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P59a = visual.TextStim(win=win, name='P3a',
    text='tuvo dificultad de conversar con adultos?',
    font='Arial',
    pos=(-0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P59b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[-0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P60a = visual.TextStim(win=win, name='P4a',
    text='interumpió o importunó a otros?',
    font='Arial',
    pos=(0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P60b = visual.RatingScale(win=win, name='P4b', marker='triangle', size=1.0, pos=[0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P61a = visual.TextStim(win=win, name='P5a',
    text='miró a otros relacionándose con ellos?',
    font='Arial',
    pos=(-0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P61b = visual.RatingScale(win=win, name='P5b', marker='triangle', size=1.0, pos=[-0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P62a = visual.TextStim(win=win, name='P6a',
    text='reaccionó exageradamente a ruidos fuertes?',
    font='Arial',
    pos=(0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P62b = visual.RatingScale(win=win, name='P6b', marker='triangle', size=1.0, pos=[0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


P63a = visual.TextStim(win=win, name='P7a',
    text='se disgustó si las rutinas cambiaban?',
    font='Arial',
    pos=(-0.37, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P63b = visual.RatingScale(win=win, name='P7b', marker='triangle', size=1.0, pos=[-0.5, -0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


P64a = visual.TextStim(win=win, name='P8a',
    text='decidió jugar solo(a)?',
    font='Arial',
    pos=(0.37, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P64b = visual.RatingScale(win=win, name='P8b', marker='triangle', size=1.0, pos=[0.5, -0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


instr_16 = visual.TextStim(win=win, name='instr_16',
    text='Presione la tecla de espacio para seguir',
    font='Arial',
    pos=(0, -0.40), height=0.03, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instr_16 = keyboard.Keyboard()


instr_17 = visual.TextStim(win=win, name='instr_17',
    text='¿Durante las últimas cuatro semanas, con qué frecuencia observó que el niño(a)...',
    font='Arial',
    pos=(0, 0.40), height=0.025, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "ASRSi"
ASRSiClock = core.Clock()

P65a = visual.TextStim(win=win, name='P1a',
    text='insistió en tener ciertos objetos siempre con él/ella?',
    font='Arial',
    pos=(-0.37, 0.30), height=0.02, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P65b = visual.RatingScale(win=win, name='P1b', marker='triangle', size=1.0, pos=[-0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P66a = visual.TextStim(win=win, name='P2a',
    text='tuvo problemas sociales con adultos?',
    font='Arial',
    pos=(0.37, 0.30), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P66b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[0.5, 0.50], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P67a = visual.TextStim(win=win, name='P3a',
    text='giró, dio vueltas, o golpeó objetos?',
    font='Arial',
    pos=(-0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P67b = visual.RatingScale(win=win, name='P3b', marker='triangle', size=1.0, pos=[-0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P68a = visual.TextStim(win=win, name='P4a',
    text='invirtió los pronombres (ej. tú en vez de mí)?',
    font='Arial',
    pos=(0.37, 0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P68b = visual.RatingScale(win=win, name='P4b', marker='triangle', size=1.0, pos=[0.5, 0.20], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P69a = visual.TextStim(win=win, name='P5a',
    text='mostró buenas interacciones con otros de su edad?',
    font='Arial',
    pos=(-0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P69b = visual.RatingScale(win=win, name='P5b', marker='triangle', size=1.0, pos=[-0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)

P70a = visual.TextStim(win=win, name='P6a',
    text='respondió cuando otros niños hablaban?',
    font='Arial',
    pos=(0.37, 0.0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

P70b = visual.RatingScale(win=win, name='P6b', marker='triangle', size=1.0, pos=[0.5, -0.10], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


P71a = visual.TextStim(win=win, name='P7a',
    text='pereció inquieto(a) cuando se le pidió quedarse sentado(a)?',
    font='Arial',
    pos=(-0.37, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-0.0);

P71b = visual.RatingScale(win=win, name='P7b', marker='triangle', size=1.0, pos=[-0.5, -0.40], low=1, high=5, labels=[], stretch = 1.2, textSize = 0.35, choices = ['Nunca', 'Casi nunca (rara vez)', 'Ocasionalmente', 'Frecuentemente', 'Muy frecuentemente'], scale='', singleClick=True, showAccept=False)


instr_18 = visual.TextStim(win=win, name='instr_18',
    text='Presione la tecla de espacio para terminar',
    font='Arial',
    pos=(0, -0.40), height=0.03, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_instr_18 = keyboard.Keyboard()


instr_19 = visual.TextStim(win=win, name='instr_19',
    text='¿Durante las últimas cuatro semanas, con qué frecuencia observó que el niño(a)...',
    font='Arial',
    pos=(0, 0.40), height=0.025, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);



# Initialize components for Routine "fin"
finClock = core.Clock()
gracias = visual.TextStim(win=win, name='gracias',
    text='\n\n¡Muchas gracias por su respuesta!\n\n\n\n\n\nPresione la tecla de espacio para salir',
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
    # update/P2a components on each frame
    
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

# ------Prepare to start Routine "ASRSa"-------
# update component parameters for each repeat
P1b.reset()
P2b.reset()
key_resp_instr_2.keys = []
key_resp_instr_2.rt = []
# keep track of which components have finished
ASRSaComponents = [P1a, P1b, P2a, P2b, P3a, P3b, P4a, P4b, P5a, P5b, P6a, P6b, P7a, P7b, P8a, P8b, instr_2, instr_3, key_resp_instr_2]
for thisComponent in ASRSaComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ASRSaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "ASRSa"-------
while continueRoutine:
    # get current time
    t = ASRSaClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ASRSaClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/P2a components on each frame
    
    # *P1a* updates
    if P1a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P1a.frameNStart = frameN  # exact frame index
        P1a.tStart = t  # local t and not account for scr refresh
        P1a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P1a, 'tStartRefresh')  # time at next scr refresh
        P1a.setAutoDraw(True)
    
    # *P1b* updates
    if P1b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P1b.frameNStart = frameN  # exact frame index
        P1b.tStart = t  # local t and not account for scr refresh
        P1b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P1b, 'tStartRefresh')  # time at next scr refresh
        P1b.setAutoDraw(True)
        
    # *P2a* updates
    if P2a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P2a.frameNStart = frameN  # exact frame index
        P2a.tStart = t  # local t and not account for scr refresh
        P2a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P2a, 'tStartRefresh')  # time at next scr refresh
        P2a.setAutoDraw(True)

    # *P2b* updates
    if P2b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P2b.frameNStart = frameN  # exact frame index
        P2b.tStart = t  # local t and not account for scr refresh
        P2b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P2b, 'tStartRefresh')  # time at next scr refresh
        P2b.setAutoDraw(True)
        
    # *P3a* updates
    if P3a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P3a.frameNStart = frameN  # exact frame index
        P3a.tStart = t  # local t and not account for scr refresh
        P3a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P3a, 'tStartRefresh')  # time at next scr refresh
        P3a.setAutoDraw(True)

    # *P3b* updates
    if P3b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P3b.frameNStart = frameN  # exact frame index
        P3b.tStart = t  # local t and not account for scr refresh
        P3b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P3b, 'tStartRefresh')  # time at next scr refresh
        P3b.setAutoDraw(True)

    # *P4a* updates
    if P4a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P4a.frameNStart = frameN  # exact frame index
        P4a.tStart = t  # local t and not account for scr refresh
        P4a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P3a, 'tStartRefresh')  # time at next scr refresh
        P4a.setAutoDraw(True)

    # *P4b* updates
    if P4b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P4b.frameNStart = frameN  # exact frame index
        P4b.tStart = t  # local t and not account for scr refresh
        P4b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P4b, 'tStartRefresh')  # time at next scr refresh
        P4b.setAutoDraw(True)
        
     # *P5a* updates
    if P5a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P5a.frameNStart = frameN  # exact frame index
        P5a.tStart = t  # local t and not account for scr refresh
        P5a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P5a, 'tStartRefresh')  # time at next scr refresh
        P5a.setAutoDraw(True)

    # *P5b* updates
    if P5b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P5b.frameNStart = frameN  # exact frame index
        P5b.tStart = t  # local t and not account for scr refresh
        P5b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P5b, 'tStartRefresh')  # time at next scr refresh
        P5b.setAutoDraw(True)

    # *P7a* updates
    if P7a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P7a.frameNStart = frameN  # exact frame index
        P7a.tStart = t  # local t and not account for scr refresh
        P7a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P7a, 'tStartRefresh')  # time at next scr refresh
        P7a.setAutoDraw(True)

    # *P7b* updates
    if P7b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P7b.frameNStart = frameN  # exact frame index
        P7b.tStart = t  # local t and not account for scr refresh
        P7b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P7b, 'tStartRefresh')  # time at next scr refresh
        P7b.setAutoDraw(True)
        
     # *P6a* updates
    if P6a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P6a.frameNStart = frameN  # exact frame index
        P6a.tStart = t  # local t and not account for scr refresh
        P6a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P6a, 'tStartRefresh')  # time at next scr refresh
        P6a.setAutoDraw(True)

    # *P6b* updates
    if P6b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P6b.frameNStart = frameN  # exact frame index
        P6b.tStart = t  # local t and not account for scr refresh
        P6b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P6b, 'tStartRefresh')  # time at next scr refresh
        P6b.setAutoDraw(True)

    # *P8a* updates
    if P8a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P8a.frameNStart = frameN  # exact frame index
        P8a.tStart = t  # local t and not account for scr refresh
        P8a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P8a, 'tStartRefresh')  # time at next scr refresh
        P8a.setAutoDraw(True)

    # *P8b* updates
    if P8b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P8b.frameNStart = frameN  # exact frame index
        P8b.tStart = t  # local t and not account for scr refresh
        P8b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P8b, 'tStartRefresh')  # time at next scr refresh
        P8b.setAutoDraw(True)
        
  
    # *instr_2* updates
    if instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_2.frameNStart = frameN  # exact frame index
        instr_2.tStart = t  # local t and not account for scr refresh
        instr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_2, 'tStartRefresh')  # time at next scr refresh
        instr_2.setAutoDraw(True)


    # *instr_3* updates
    if instr_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_3.frameNStart = frameN  # exact frame index
        instr_3.tStart = t  # local t and not account for scr refresh
        instr_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_3, 'tStartRefresh')  # time at next scr refresh
        instr_3.setAutoDraw(True)
    
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
    for thisComponent in ASRSaComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ASRSa"-------
for thisComponent in ASRSaComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('P1b.response', P1b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P2b.response', P2b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P3b.response', P3b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P4b.response', P4b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P5b.response', P5b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P6b.response', P6b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P7b.response', P7b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P8b.response', P8b.getRating())
#thisExp.nextEntry()


# check responses
if key_resp_instr_2.keys in ['', [], None]:  # No response was made
    key_resp_instr_2.keys = None
thisExp.addData('key_resp_instr_2.keys',key_resp_instr_2.keys)
if key_resp_instr_2.keys != None:  # we had a response
    thisExp.addData('key_resp_instr_2.rt', key_resp_instr_2.rt)
thisExp.nextEntry()
# the Routine "ASRSa" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ASRSb"-------
# update component parameters for each repeat
P9b.reset()
P10b.reset()
key_resp_instr_4.keys = []
key_resp_instr_4.rt = []
# keep track of which components have finished
ASRSbComponents = [P9a, P9b, P10a, P10b, P11a, P11b, P12a, P12b, P13a, P13b, P14a, P14b, P15a, P15b, P16a, P16b, instr_4, instr_5, key_resp_instr_4]
for thisComponent in ASRSbComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ASRSbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "ASRSa"-------
while continueRoutine:
    # get current time
    t = ASRSbClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ASRSbClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/P2a components on each frame
    
    # *P9a* updates
    if P9a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P9a.frameNStart = frameN  # exact frame index
        P9a.tStart = t  # local t and not account for scr refresh
        P9a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P9a, 'tStartRefresh')  # time at next scr refresh
        P9a.setAutoDraw(True)
    
    # *P9b* updates
    if P9b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P9b.frameNStart = frameN  # exact frame index
        P9b.tStart = t  # local t and not account for scr refresh
        P9b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P9b, 'tStartRefresh')  # time at next scr refresh
        P9b.setAutoDraw(True)
        
    # *P10a* updates
    if P10a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P10a.frameNStart = frameN  # exact frame index
        P10a.tStart = t  # local t and not account for scr refresh
        P10a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P10a, 'tStartRefresh')  # time at next scr refresh
        P10a.setAutoDraw(True)

    # *P10b* updates
    if P10b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P10b.frameNStart = frameN  # exact frame index
        P10b.tStart = t  # local t and not account for scr refresh
        P10b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P10b, 'tStartRefresh')  # time at next scr refresh
        P10b.setAutoDraw(True)
        
    # *P11a* updates
    if P11a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P11a.frameNStart = frameN  # exact frame index
        P11a.tStart = t  # local t and not account for scr refresh
        P11a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P11a, 'tStartRefresh')  # time at next scr refresh
        P11a.setAutoDraw(True)

    # *P11b* updates
    if P11b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P11b.frameNStart = frameN  # exact frame index
        P11b.tStart = t  # local t and not account for scr refresh
        P11b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P11b, 'tStartRefresh')  # time at next scr refresh
        P11b.setAutoDraw(True)

    # *P12a* updates
    if P12a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P12a.frameNStart = frameN  # exact frame index
        P12a.tStart = t  # local t and not account for scr refresh
        P12a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P3a, 'tStartRefresh')  # time at next scr refresh
        P12a.setAutoDraw(True)

    # *P12b* updates
    if P12b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P12b.frameNStart = frameN  # exact frame index
        P12b.tStart = t  # local t and not account for scr refresh
        P12b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P12b, 'tStartRefresh')  # time at next scr refresh
        P12b.setAutoDraw(True)
        
     # *P13a* updates
    if P13a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P13a.frameNStart = frameN  # exact frame index
        P13a.tStart = t  # local t and not account for scr refresh
        P13a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P13a, 'tStartRefresh')  # time at next scr refresh
        P13a.setAutoDraw(True)

    # *P13b* updates
    if P13b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P13b.frameNStart = frameN  # exact frame index
        P13b.tStart = t  # local t and not account for scr refresh
        P13b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P13b, 'tStartRefresh')  # time at next scr refresh
        P13b.setAutoDraw(True)

    # *P14a* updates
    if P14a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P14a.frameNStart = frameN  # exact frame index
        P14a.tStart = t  # local t and not account for scr refresh
        P14a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P14a, 'tStartRefresh')  # time at next scr refresh
        P14a.setAutoDraw(True)

    # *P14b* updates
    if P14b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P14b.frameNStart = frameN  # exact frame index
        P14b.tStart = t  # local t and not account for scr refresh
        P14b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P14b, 'tStartRefresh')  # time at next scr refresh
        P14b.setAutoDraw(True)
        
     # *P15a* updates
    if P15a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P15a.frameNStart = frameN  # exact frame index
        P15a.tStart = t  # local t and not account for scr refresh
        P15a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P15a, 'tStartRefresh')  # time at next scr refresh
        P15a.setAutoDraw(True)

    # *P15b* updates
    if P15b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P15b.frameNStart = frameN  # exact frame index
        P15b.tStart = t  # local t and not account for scr refresh
        P15b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P15b, 'tStartRefresh')  # time at next scr refresh
        P15b.setAutoDraw(True)

    # *P16a* updates
    if P16a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P16a.frameNStart = frameN  # exact frame index
        P16a.tStart = t  # local t and not account for scr refresh
        P16a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P16a, 'tStartRefresh')  # time at next scr refresh
        P16a.setAutoDraw(True)

    # *P16b* updates
    if P16b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P16b.frameNStart = frameN  # exact frame index
        P16b.tStart = t  # local t and not account for scr refresh
        P16b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P16b, 'tStartRefresh')  # time at next scr refresh
        P16b.setAutoDraw(True)
        
  
    # *instr_4* updates
    if instr_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_4.frameNStart = frameN  # exact frame index
        instr_4.tStart = t  # local t and not account for scr refresh
        instr_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_4, 'tStartRefresh')  # time at next scr refresh
        instr_4.setAutoDraw(True)


    # *instr_5* updates
    if instr_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_5.frameNStart = frameN  # exact frame index
        instr_5.tStart = t  # local t and not account for scr refresh
        instr_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_5, 'tStartRefresh')  # time at next scr refresh
        instr_5.setAutoDraw(True)
    
    # *key_resp_instr_4* updates
    waitOnFlip = False
    if key_resp_instr_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instr_4.frameNStart = frameN  # exact frame index
        key_resp_instr_4.tStart = t  # local t and not account for scr refresh
        key_resp_instr_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instr_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_instr_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instr_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instr_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instr_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instr_4.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_instr_4.keys = theseKeys.name  # just the last key pressed
            key_resp_instr_4.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ASRSbComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ASRSb"-------
for thisComponent in ASRSbComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('P9b.response', P9b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P10b.response', P10b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P11b.response', P11b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P12b.response', P12b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P13b.response', P13b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P14b.response', P14b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P15b.response', P15b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P16b.response', P16b.getRating())
#thisExp.nextEntry()


# check responses
if key_resp_instr_4.keys in ['', [], None]:  # No response was made
    key_resp_instr_4.keys = None
thisExp.addData('key_resp_instr_4.keys',key_resp_instr_4.keys)
if key_resp_instr_4.keys != None:  # we had a response
    thisExp.addData('key_resp_instr_4.rt', key_resp_instr_4.rt)
thisExp.nextEntry()
# the Routine "ASRSb" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# ------Prepare to start Routine "ASRSc"-------
# update component parameters for each repeat
P17b.reset()
P18b.reset()
key_resp_instr_6.keys = []
key_resp_instr_6.rt = []
# keep track of which components have finished
ASRScComponents = [P17a, P17b, P18a, P18b, P19a, P19b, P20a, P20b, P21a, P21b, P22a, P22b, P23a, P23b, P24a, P24b, instr_6, instr_7, key_resp_instr_6]
for thisComponent in ASRScComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ASRScClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "ASRSc"-------
while continueRoutine:
    # get current time
    t = ASRScClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ASRScClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/P2a components on each frame
    
    # *P17a* updates
    if P17a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P17a.frameNStart = frameN  # exact frame index
        P17a.tStart = t  # local t and not account for scr refresh
        P17a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P17a, 'tStartRefresh')  # time at next scr refresh
        P17a.setAutoDraw(True)
    
    # *P17b* updates
    if P17b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P17b.frameNStart = frameN  # exact frame index
        P17b.tStart = t  # local t and not account for scr refresh
        P17b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P17b, 'tStartRefresh')  # time at next scr refresh
        P17b.setAutoDraw(True)
        
    # *P18a* updates
    if P18a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P18a.frameNStart = frameN  # exact frame index
        P18a.tStart = t  # local t and not account for scr refresh
        P18a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P18a, 'tStartRefresh')  # time at next scr refresh
        P18a.setAutoDraw(True)

    # *P18b* updates
    if P18b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P18b.frameNStart = frameN  # exact frame index
        P18b.tStart = t  # local t and not account for scr refresh
        P18b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P18b, 'tStartRefresh')  # time at next scr refresh
        P18b.setAutoDraw(True)
        
    # *P19a* updates
    if P19a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P19a.frameNStart = frameN  # exact frame index
        P19a.tStart = t  # local t and not account for scr refresh
        P19a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P19a, 'tStartRefresh')  # time at next scr refresh
        P19a.setAutoDraw(True)

    # *P19b* updates
    if P19b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P19b.frameNStart = frameN  # exact frame index
        P19b.tStart = t  # local t and not account for scr refresh
        P19b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P19b, 'tStartRefresh')  # time at next scr refresh
        P19b.setAutoDraw(True)

    # *P20a* updates
    if P20a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P20a.frameNStart = frameN  # exact frame index
        P20a.tStart = t  # local t and not account for scr refresh
        P20a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P3a, 'tStartRefresh')  # time at next scr refresh
        P20a.setAutoDraw(True)

    # *P20b* updates
    if P20b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P20b.frameNStart = frameN  # exact frame index
        P20b.tStart = t  # local t and not account for scr refresh
        P20b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P20b, 'tStartRefresh')  # time at next scr refresh
        P20b.setAutoDraw(True)
        
     # *P21a* updates
    if P21a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P21a.frameNStart = frameN  # exact frame index
        P21a.tStart = t  # local t and not account for scr refresh
        P21a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P21a, 'tStartRefresh')  # time at next scr refresh
        P21a.setAutoDraw(True)

    # *P21b* updates
    if P21b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P21b.frameNStart = frameN  # exact frame index
        P21b.tStart = t  # local t and not account for scr refresh
        P21b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P21b, 'tStartRefresh')  # time at next scr refresh
        P21b.setAutoDraw(True)

    # *P22a* updates
    if P22a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P22a.frameNStart = frameN  # exact frame index
        P22a.tStart = t  # local t and not account for scr refresh
        P22a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P22a, 'tStartRefresh')  # time at next scr refresh
        P22a.setAutoDraw(True)

    # *P22b* updates
    if P22b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P22b.frameNStart = frameN  # exact frame index
        P22b.tStart = t  # local t and not account for scr refresh
        P22b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P22b, 'tStartRefresh')  # time at next scr refresh
        P22b.setAutoDraw(True)
        
     # *P23a* updates
    if P23a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P23a.frameNStart = frameN  # exact frame index
        P23a.tStart = t  # local t and not account for scr refresh
        P23a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P23a, 'tStartRefresh')  # time at next scr refresh
        P23a.setAutoDraw(True)

    # *P23b* updates
    if P23b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P23b.frameNStart = frameN  # exact frame index
        P23b.tStart = t  # local t and not account for scr refresh
        P23b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P23b, 'tStartRefresh')  # time at next scr refresh
        P23b.setAutoDraw(True)

    # *P24a* updates
    if P24a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P24a.frameNStart = frameN  # exact frame index
        P24a.tStart = t  # local t and not account for scr refresh
        P24a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P24a, 'tStartRefresh')  # time at next scr refresh
        P24a.setAutoDraw(True)

    # *P24b* updates
    if P24b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P24b.frameNStart = frameN  # exact frame index
        P24b.tStart = t  # local t and not account for scr refresh
        P24b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P24b, 'tStartRefresh')  # time at next scr refresh
        P24b.setAutoDraw(True)
        
  
    # *instr_6* updates
    if instr_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_6.frameNStart = frameN  # exact frame index
        instr_6.tStart = t  # local t and not account for scr refresh
        instr_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_6, 'tStartRefresh')  # time at next scr refresh
        instr_6.setAutoDraw(True)


    # *instr_7* updates
    if instr_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_7.frameNStart = frameN  # exact frame index
        instr_7.tStart = t  # local t and not account for scr refresh
        instr_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_7, 'tStartRefresh')  # time at next scr refresh
        instr_7.setAutoDraw(True)
    
    # *key_resp_instr_6* updates
    waitOnFlip = False
    if key_resp_instr_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instr_6.frameNStart = frameN  # exact frame index
        key_resp_instr_6.tStart = t  # local t and not account for scr refresh
        key_resp_instr_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instr_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_instr_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instr_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instr_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instr_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instr_6.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_instr_6.keys = theseKeys.name  # just the last key pressed
            key_resp_instr_6.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ASRScComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ASRSc"-------
for thisComponent in ASRScComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('P17b.response', P17b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P18b.response', P18b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P19b.response', P19b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P20b.response', P20b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P21b.response', P21b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P22b.response', P22b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P23b.response', P23b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P24b.response', P24b.getRating())
#thisExp.nextEntry()


# check responses
if key_resp_instr_6.keys in ['', [], None]:  # No response was made
    key_resp_instr_6.keys = None
thisExp.addData('key_resp_instr_6.keys',key_resp_instr_6.keys)
if key_resp_instr_6.keys != None:  # we had a response
    thisExp.addData('key_resp_instr_6.rt', key_resp_instr_6.rt)
thisExp.nextEntry()
# the Routine "ASRSc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



# ------Prepare to start Routine "ASRSd"-------
# update component parameters for each repeat
P25b.reset()
P26b.reset()
key_resp_instr_8.keys = []
key_resp_instr_8.rt = []
# keep track of which components have finished
ASRSdComponents = [P25a, P25b, P26a, P26b, P27a, P27b, P28a, P28b, P29a, P29b, P30a, P30b, P31a, P31b, P32a, P32b, instr_8, instr_9, key_resp_instr_8]
for thisComponent in ASRSdComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ASRSdClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True


# -------Run Routine "ASRSd"-------
while continueRoutine:
    # get current time
    t = ASRSdClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ASRSdClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/P2a components on each frame
    
    # *P25a* updates
    if P25a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P25a.frameNStart = frameN  # exact frame index
        P25a.tStart = t  # local t and not account for scr refresh
        P25a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P25a, 'tStartRefresh')  # time at next scr refresh
        P25a.setAutoDraw(True)
    
    # *P25b* updates
    if P25b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P25b.frameNStart = frameN  # exact frame index
        P25b.tStart = t  # local t and not account for scr refresh
        P25b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P25b, 'tStartRefresh')  # time at next scr refresh
        P25b.setAutoDraw(True)
        
    # *P26a* updates
    if P26a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P26a.frameNStart = frameN  # exact frame index
        P26a.tStart = t  # local t and not account for scr refresh
        P26a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P26a, 'tStartRefresh')  # time at next scr refresh
        P26a.setAutoDraw(True)

    # *P26b* updates
    if P26b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P26b.frameNStart = frameN  # exact frame index
        P26b.tStart = t  # local t and not account for scr refresh
        P26b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P26b, 'tStartRefresh')  # time at next scr refresh
        P26b.setAutoDraw(True)
        
    # *P27a* updates
    if P27a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P27a.frameNStart = frameN  # exact frame index
        P27a.tStart = t  # local t and not account for scr refresh
        P27a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P27a, 'tStartRefresh')  # time at next scr refresh
        P27a.setAutoDraw(True)

    # *P27b* updates
    if P27b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P27b.frameNStart = frameN  # exact frame index
        P27b.tStart = t  # local t and not account for scr refresh
        P27b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P27b, 'tStartRefresh')  # time at next scr refresh
        P27b.setAutoDraw(True)

    # *P28a* updates
    if P28a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P28a.frameNStart = frameN  # exact frame index
        P28a.tStart = t  # local t and not account for scr refresh
        P28a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P3a, 'tStartRefresh')  # time at next scr refresh
        P28a.setAutoDraw(True)

    # *P28b* updates
    if P28b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P28b.frameNStart = frameN  # exact frame index
        P28b.tStart = t  # local t and not account for scr refresh
        P28b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P28b, 'tStartRefresh')  # time at next scr refresh
        P28b.setAutoDraw(True)
        
     # *P29a* updates
    if P29a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P29a.frameNStart = frameN  # exact frame index
        P29a.tStart = t  # local t and not account for scr refresh
        P29a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P29a, 'tStartRefresh')  # time at next scr refresh
        P29a.setAutoDraw(True)

    # *P29b* updates
    if P29b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P29b.frameNStart = frameN  # exact frame index
        P29b.tStart = t  # local t and not account for scr refresh
        P29b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P29b, 'tStartRefresh')  # time at next scr refresh
        P29b.setAutoDraw(True)

    # *P30a* updates
    if P30a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P30a.frameNStart = frameN  # exact frame index
        P30a.tStart = t  # local t and not account for scr refresh
        P30a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P30a, 'tStartRefresh')  # time at next scr refresh
        P30a.setAutoDraw(True)

    # *P30b* updates
    if P30b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P30b.frameNStart = frameN  # exact frame index
        P30b.tStart = t  # local t and not account for scr refresh
        P30b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P30b, 'tStartRefresh')  # time at next scr refresh
        P30b.setAutoDraw(True)
        
     # *P31a* updates
    if P31a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P31a.frameNStart = frameN  # exact frame index
        P31a.tStart = t  # local t and not account for scr refresh
        P31a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P31a, 'tStartRefresh')  # time at next scr refresh
        P31a.setAutoDraw(True)

    # *P31b* updates
    if P31b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P31b.frameNStart = frameN  # exact frame index
        P31b.tStart = t  # local t and not account for scr refresh
        P31b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P31b, 'tStartRefresh')  # time at next scr refresh
        P31b.setAutoDraw(True)

    # *P32a* updates
    if P32a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P32a.frameNStart = frameN  # exact frame index
        P32a.tStart = t  # local t and not account for scr refresh
        P32a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P32a, 'tStartRefresh')  # time at next scr refresh
        P32a.setAutoDraw(True)

    # *P32b* updates
    if P32b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P32b.frameNStart = frameN  # exact frame index
        P32b.tStart = t  # local t and not account for scr refresh
        P32b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P32b, 'tStartRefresh')  # time at next scr refresh
        P32b.setAutoDraw(True)
        
  
    # *instr_8* updates
    if instr_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_8.frameNStart = frameN  # exact frame index
        instr_8.tStart = t  # local t and not account for scr refresh
        instr_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_8, 'tStartRefresh')  # time at next scr refresh
        instr_8.setAutoDraw(True)


    # *instr_9* updates
    if instr_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_9.frameNStart = frameN  # exact frame index
        instr_9.tStart = t  # local t and not account for scr refresh
        instr_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_9, 'tStartRefresh')  # time at next scr refresh
        instr_9.setAutoDraw(True)
    
    # *key_resp_instr_8* updates
    waitOnFlip = False
    if key_resp_instr_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instr_8.frameNStart = frameN  # exact frame index
        key_resp_instr_8.tStart = t  # local t and not account for scr refresh
        key_resp_instr_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instr_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_instr_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instr_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instr_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instr_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instr_8.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_instr_8.keys = theseKeys.name  # just the last key pressed
            key_resp_instr_8.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ASRSdComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ASRSd"-------
for thisComponent in ASRSdComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('P25b.response', P25b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P26b.response', P26b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P27b.response', P27b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P28b.response', P28b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P29b.response', P29b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P30b.response', P30b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P31b.response', P31b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P32b.response', P32b.getRating())
#thisExp.nextEntry()


# check responses
if key_resp_instr_8.keys in ['', [], None]:  # No response was made
    key_resp_instr_8.keys = None
thisExp.addData('key_resp_instr_8.keys',key_resp_instr_8.keys)
if key_resp_instr_8.keys != None:  # we had a response
    thisExp.addData('key_resp_instr_8.rt', key_resp_instr_8.rt)
thisExp.nextEntry()
# the Routine "ASRSd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# ------Prepare to start Routine "ASRSe"-------
# update component parameters for each repeat
P33b.reset()
P34b.reset()
key_resp_instr_10.keys = []
key_resp_instr_10.rt = []
# keep track of which components have finished
ASRSeComponents = [P33a, P33b, P34a, P34b, P35a, P35b, P36a, P36b, P37a, P37b, P38a, P38b, P39a, P39b, P40a, P40b, instr_10, instr_11, key_resp_instr_10]
for thisComponent in ASRSeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ASRSeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True


# -------Run Routine "ASRSe"-------
while continueRoutine:
    # get current time
    t = ASRSeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ASRSeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/P2a components on each frame
    
    # *P33a* updates
    if P33a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P33a.frameNStart = frameN  # exact frame index
        P33a.tStart = t  # local t and not account for scr refresh
        P33a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P33a, 'tStartRefresh')  # time at next scr refresh
        P33a.setAutoDraw(True)
    
    # *P33b* updates
    if P33b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P33b.frameNStart = frameN  # exact frame index
        P33b.tStart = t  # local t and not account for scr refresh
        P33b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P33b, 'tStartRefresh')  # time at next scr refresh
        P33b.setAutoDraw(True)
        
    # *P34a* updates
    if P34a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P34a.frameNStart = frameN  # exact frame index
        P34a.tStart = t  # local t and not account for scr refresh
        P34a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P34a, 'tStartRefresh')  # time at next scr refresh
        P34a.setAutoDraw(True)

    # *P34b* updates
    if P34b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P34b.frameNStart = frameN  # exact frame index
        P34b.tStart = t  # local t and not account for scr refresh
        P34b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P34b, 'tStartRefresh')  # time at next scr refresh
        P34b.setAutoDraw(True)
        
    # *P35a* updates
    if P35a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P35a.frameNStart = frameN  # exact frame index
        P35a.tStart = t  # local t and not account for scr refresh
        P35a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P35a, 'tStartRefresh')  # time at next scr refresh
        P35a.setAutoDraw(True)

    # *P35b* updates
    if P35b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P35b.frameNStart = frameN  # exact frame index
        P35b.tStart = t  # local t and not account for scr refresh
        P35b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P35b, 'tStartRefresh')  # time at next scr refresh
        P35b.setAutoDraw(True)

    # *P36a* updates
    if P36a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P36a.frameNStart = frameN  # exact frame index
        P36a.tStart = t  # local t and not account for scr refresh
        P36a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P3a, 'tStartRefresh')  # time at next scr refresh
        P36a.setAutoDraw(True)

    # *P36b* updates
    if P36b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P36b.frameNStart = frameN  # exact frame index
        P36b.tStart = t  # local t and not account for scr refresh
        P36b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P36b, 'tStartRefresh')  # time at next scr refresh
        P36b.setAutoDraw(True)
        
     # *P37a* updates
    if P37a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P37a.frameNStart = frameN  # exact frame index
        P37a.tStart = t  # local t and not account for scr refresh
        P37a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P37a, 'tStartRefresh')  # time at next scr refresh
        P37a.setAutoDraw(True)

    # *P37b* updates
    if P37b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P37b.frameNStart = frameN  # exact frame index
        P37b.tStart = t  # local t and not account for scr refresh
        P37b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P37b, 'tStartRefresh')  # time at next scr refresh
        P37b.setAutoDraw(True)

    # *P38a* updates
    if P38a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P38a.frameNStart = frameN  # exact frame index
        P38a.tStart = t  # local t and not account for scr refresh
        P38a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P38a, 'tStartRefresh')  # time at next scr refresh
        P38a.setAutoDraw(True)

    # *P38b* updates
    if P38b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P38b.frameNStart = frameN  # exact frame index
        P38b.tStart = t  # local t and not account for scr refresh
        P38b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P38b, 'tStartRefresh')  # time at next scr refresh
        P38b.setAutoDraw(True)
        
     # *P39a* updates
    if P39a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P39a.frameNStart = frameN  # exact frame index
        P39a.tStart = t  # local t and not account for scr refresh
        P39a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P39a, 'tStartRefresh')  # time at next scr refresh
        P39a.setAutoDraw(True)

    # *P39b* updates
    if P39b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P39b.frameNStart = frameN  # exact frame index
        P39b.tStart = t  # local t and not account for scr refresh
        P39b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P39b, 'tStartRefresh')  # time at next scr refresh
        P39b.setAutoDraw(True)

    # *P40a* updates
    if P40a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P40a.frameNStart = frameN  # exact frame index
        P40a.tStart = t  # local t and not account for scr refresh
        P40a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P40a, 'tStartRefresh')  # time at next scr refresh
        P40a.setAutoDraw(True)

    # *P40b* updates
    if P40b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P40b.frameNStart = frameN  # exact frame index
        P40b.tStart = t  # local t and not account for scr refresh
        P40b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P40b, 'tStartRefresh')  # time at next scr refresh
        P40b.setAutoDraw(True)
        
  
    # *instr_10* updates
    if instr_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_10.frameNStart = frameN  # exact frame index
        instr_10.tStart = t  # local t and not account for scr refresh
        instr_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_10, 'tStartRefresh')  # time at next scr refresh
        instr_10.setAutoDraw(True)


    # *instr_11* updates
    if instr_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_11.frameNStart = frameN  # exact frame index
        instr_11.tStart = t  # local t and not account for scr refresh
        instr_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_11, 'tStartRefresh')  # time at next scr refresh
        instr_11.setAutoDraw(True)
    
    # *key_resp_instr_10* updates
    waitOnFlip = False
    if key_resp_instr_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instr_10.frameNStart = frameN  # exact frame index
        key_resp_instr_10.tStart = t  # local t and not account for scr refresh
        key_resp_instr_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instr_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_instr_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instr_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instr_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instr_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instr_10.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_instr_10.keys = theseKeys.name  # just the last key pressed
            key_resp_instr_10.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ASRSeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ASRSe"-------
for thisComponent in ASRSeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('P33b.response', P33b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P34b.response', P34b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P35b.response', P35b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P36b.response', P36b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P37b.response', P37b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P38b.response', P38b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P39b.response', P39b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P40b.response', P40b.getRating())
#thisExp.nextEntry()


# check responses
if key_resp_instr_10.keys in ['', [], None]:  # No response was made
    key_resp_instr_10.keys = None
thisExp.addData('key_resp_instr_10.keys',key_resp_instr_10.keys)
if key_resp_instr_10.keys != None:  # we had a response
    thisExp.addData('key_resp_instr_10.rt', key_resp_instr_10.rt)
thisExp.nextEntry()
# the Routine "ASRSe" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ASRSf"-------
# update component parameters for each repeat
P41b.reset()
P42b.reset()
key_resp_instr_12.keys = []
key_resp_instr_12.rt = []
# keep track of which components have finished
ASRSfComponents = [P41a, P41b, P42a, P42b, P43a, P43b, P44a, P44b, P45a, P45b, P46a, P46b, P47a, P47b, P48a, P48b, instr_12, instr_13, key_resp_instr_12]
for thisComponent in ASRSfComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ASRSfClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True


# -------Run Routine "ASRSf"-------
while continueRoutine:
    # get current time
    t = ASRSfClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ASRSfClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/P2a components on each frame
    
    # *P41a* updates
    if P41a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P41a.frameNStart = frameN  # exact frame index
        P41a.tStart = t  # local t and not account for scr refresh
        P41a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P41a, 'tStartRefresh')  # time at next scr refresh
        P41a.setAutoDraw(True)
    
    # *P41b* updates
    if P41b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P41b.frameNStart = frameN  # exact frame index
        P41b.tStart = t  # local t and not account for scr refresh
        P41b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P41b, 'tStartRefresh')  # time at next scr refresh
        P41b.setAutoDraw(True)
        
    # *P42a* updates
    if P42a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P42a.frameNStart = frameN  # exact frame index
        P42a.tStart = t  # local t and not account for scr refresh
        P42a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P42a, 'tStartRefresh')  # time at next scr refresh
        P42a.setAutoDraw(True)

    # *P42b* updates
    if P42b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P42b.frameNStart = frameN  # exact frame index
        P42b.tStart = t  # local t and not account for scr refresh
        P42b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P42b, 'tStartRefresh')  # time at next scr refresh
        P42b.setAutoDraw(True)
        
    # *P43a* updates
    if P43a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P43a.frameNStart = frameN  # exact frame index
        P43a.tStart = t  # local t and not account for scr refresh
        P43a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P43a, 'tStartRefresh')  # time at next scr refresh
        P43a.setAutoDraw(True)

    # *P43b* updates
    if P43b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P43b.frameNStart = frameN  # exact frame index
        P43b.tStart = t  # local t and not account for scr refresh
        P43b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P43b, 'tStartRefresh')  # time at next scr refresh
        P43b.setAutoDraw(True)

    # *P44a* updates
    if P44a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P44a.frameNStart = frameN  # exact frame index
        P44a.tStart = t  # local t and not account for scr refresh
        P44a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P3a, 'tStartRefresh')  # time at next scr refresh
        P44a.setAutoDraw(True)

    # *P44b* updates
    if P44b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P44b.frameNStart = frameN  # exact frame index
        P44b.tStart = t  # local t and not account for scr refresh
        P44b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P44b, 'tStartRefresh')  # time at next scr refresh
        P44b.setAutoDraw(True)
        
     # *P45a* updates
    if P45a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P45a.frameNStart = frameN  # exact frame index
        P45a.tStart = t  # local t and not account for scr refresh
        P45a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P45a, 'tStartRefresh')  # time at next scr refresh
        P45a.setAutoDraw(True)

    # *P45b* updates
    if P45b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P45b.frameNStart = frameN  # exact frame index
        P45b.tStart = t  # local t and not account for scr refresh
        P45b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P45b, 'tStartRefresh')  # time at next scr refresh
        P45b.setAutoDraw(True)

    # *P46a* updates
    if P46a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P46a.frameNStart = frameN  # exact frame index
        P46a.tStart = t  # local t and not account for scr refresh
        P46a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P46a, 'tStartRefresh')  # time at next scr refresh
        P46a.setAutoDraw(True)

    # *P46b* updates
    if P46b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P46b.frameNStart = frameN  # exact frame index
        P46b.tStart = t  # local t and not account for scr refresh
        P46b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P46b, 'tStartRefresh')  # time at next scr refresh
        P46b.setAutoDraw(True)
        
     # *P47a* updates
    if P47a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P47a.frameNStart = frameN  # exact frame index
        P47a.tStart = t  # local t and not account for scr refresh
        P47a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P47a, 'tStartRefresh')  # time at next scr refresh
        P47a.setAutoDraw(True)

    # *P47b* updates
    if P47b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P47b.frameNStart = frameN  # exact frame index
        P47b.tStart = t  # local t and not account for scr refresh
        P47b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P47b, 'tStartRefresh')  # time at next scr refresh
        P47b.setAutoDraw(True)

    # *P48a* updates
    if P48a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P48a.frameNStart = frameN  # exact frame index
        P48a.tStart = t  # local t and not account for scr refresh
        P48a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P48a, 'tStartRefresh')  # time at next scr refresh
        P48a.setAutoDraw(True)

    # *P48b* updates
    if P48b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P48b.frameNStart = frameN  # exact frame index
        P48b.tStart = t  # local t and not account for scr refresh
        P48b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P48b, 'tStartRefresh')  # time at next scr refresh
        P48b.setAutoDraw(True)
        
  
    # *instr_12* updates
    if instr_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_12.frameNStart = frameN  # exact frame index
        instr_12.tStart = t  # local t and not account for scr refresh
        instr_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_12, 'tStartRefresh')  # time at next scr refresh
        instr_12.setAutoDraw(True)


    # *instr_13* updates
    if instr_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_13.frameNStart = frameN  # exact frame index
        instr_13.tStart = t  # local t and not account for scr refresh
        instr_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_13, 'tStartRefresh')  # time at next scr refresh
        instr_13.setAutoDraw(True)
    
    # *key_resp_instr_12* updates
    waitOnFlip = False
    if key_resp_instr_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instr_12.frameNStart = frameN  # exact frame index
        key_resp_instr_12.tStart = t  # local t and not account for scr refresh
        key_resp_instr_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instr_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_instr_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instr_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instr_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instr_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instr_12.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_instr_12.keys = theseKeys.name  # just the last key pressed
            key_resp_instr_12.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ASRSfComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ASRSf"-------
for thisComponent in ASRSfComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('P41b.response', P41b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P42b.response', P42b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P43b.response', P43b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P44b.response', P44b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P45b.response', P45b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P46b.response', P46b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P47b.response', P47b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P48b.response', P48b.getRating())
#thisExp.nextEntry()


# check responses
if key_resp_instr_12.keys in ['', [], None]:  # No response was made
    key_resp_instr_12.keys = None
thisExp.addData('key_resp_instr_12.keys',key_resp_instr_12.keys)
if key_resp_instr_12.keys != None:  # we had a response
    thisExp.addData('key_resp_instr_12.rt', key_resp_instr_12.rt)
thisExp.nextEntry()
# the Routine "ASRSf" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ASRSg"-------
# update component parameters for each repeat
P49b.reset()
P50b.reset()
key_resp_instr_14.keys = []
key_resp_instr_14.rt = []
# keep track of which components have finished
ASRSgComponents = [P49a, P49b, P50a, P50b, P51a, P51b, P52a, P52b, P53a, P53b, P54a, P54b, P55a, P55b, P56a, P56b, instr_14, instr_15, key_resp_instr_14]
for thisComponent in ASRSgComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ASRSgClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True


# -------Run Routine "ASRSg"-------
while continueRoutine:
    # get current time
    t = ASRSgClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ASRSgClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/P2a components on each frame
    
    # *P49a* updates
    if P49a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P49a.frameNStart = frameN  # exact frame index
        P49a.tStart = t  # local t and not account for scr refresh
        P49a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P49a, 'tStartRefresh')  # time at next scr refresh
        P49a.setAutoDraw(True)
    
    # *P49b* updates
    if P49b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P49b.frameNStart = frameN  # exact frame index
        P49b.tStart = t  # local t and not account for scr refresh
        P49b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P49b, 'tStartRefresh')  # time at next scr refresh
        P49b.setAutoDraw(True)
        
    # *P50a* updates
    if P50a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P50a.frameNStart = frameN  # exact frame index
        P50a.tStart = t  # local t and not account for scr refresh
        P50a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P50a, 'tStartRefresh')  # time at next scr refresh
        P50a.setAutoDraw(True)

    # *P50b* updates
    if P50b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P50b.frameNStart = frameN  # exact frame index
        P50b.tStart = t  # local t and not account for scr refresh
        P50b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P50b, 'tStartRefresh')  # time at next scr refresh
        P50b.setAutoDraw(True)
        
    # *P51a* updates
    if P51a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P51a.frameNStart = frameN  # exact frame index
        P51a.tStart = t  # local t and not account for scr refresh
        P51a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P51a, 'tStartRefresh')  # time at next scr refresh
        P51a.setAutoDraw(True)

    # *P51b* updates
    if P51b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P51b.frameNStart = frameN  # exact frame index
        P51b.tStart = t  # local t and not account for scr refresh
        P51b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P51b, 'tStartRefresh')  # time at next scr refresh
        P51b.setAutoDraw(True)

    # *P52a* updates
    if P52a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P52a.frameNStart = frameN  # exact frame index
        P52a.tStart = t  # local t and not account for scr refresh
        P52a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P3a, 'tStartRefresh')  # time at next scr refresh
        P52a.setAutoDraw(True)

    # *P52b* updates
    if P52b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P52b.frameNStart = frameN  # exact frame index
        P52b.tStart = t  # local t and not account for scr refresh
        P52b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P52b, 'tStartRefresh')  # time at next scr refresh
        P52b.setAutoDraw(True)
        
     # *P53a* updates
    if P53a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P53a.frameNStart = frameN  # exact frame index
        P53a.tStart = t  # local t and not account for scr refresh
        P53a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P53a, 'tStartRefresh')  # time at next scr refresh
        P53a.setAutoDraw(True)

    # *P53b* updates
    if P53b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P53b.frameNStart = frameN  # exact frame index
        P53b.tStart = t  # local t and not account for scr refresh
        P53b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P53b, 'tStartRefresh')  # time at next scr refresh
        P53b.setAutoDraw(True)

    # *P54a* updates
    if P54a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P54a.frameNStart = frameN  # exact frame index
        P54a.tStart = t  # local t and not account for scr refresh
        P54a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P54a, 'tStartRefresh')  # time at next scr refresh
        P54a.setAutoDraw(True)

    # *P54b* updates
    if P54b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P54b.frameNStart = frameN  # exact frame index
        P54b.tStart = t  # local t and not account for scr refresh
        P54b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P54b, 'tStartRefresh')  # time at next scr refresh
        P54b.setAutoDraw(True)
        
     # *P55a* updates
    if P55a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P55a.frameNStart = frameN  # exact frame index
        P55a.tStart = t  # local t and not account for scr refresh
        P55a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P55a, 'tStartRefresh')  # time at next scr refresh
        P55a.setAutoDraw(True)

    # *P55b* updates
    if P55b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P55b.frameNStart = frameN  # exact frame index
        P55b.tStart = t  # local t and not account for scr refresh
        P55b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P55b, 'tStartRefresh')  # time at next scr refresh
        P55b.setAutoDraw(True)

    # *P56a* updates
    if P56a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P56a.frameNStart = frameN  # exact frame index
        P56a.tStart = t  # local t and not account for scr refresh
        P56a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P56a, 'tStartRefresh')  # time at next scr refresh
        P56a.setAutoDraw(True)

    # *P56b* updates
    if P56b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P56b.frameNStart = frameN  # exact frame index
        P56b.tStart = t  # local t and not account for scr refresh
        P56b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P56b, 'tStartRefresh')  # time at next scr refresh
        P56b.setAutoDraw(True)
        
  
    # *instr_14* updates
    if instr_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_14.frameNStart = frameN  # exact frame index
        instr_14.tStart = t  # local t and not account for scr refresh
        instr_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_14, 'tStartRefresh')  # time at next scr refresh
        instr_14.setAutoDraw(True)


    # *instr_15* updates
    if instr_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_15.frameNStart = frameN  # exact frame index
        instr_15.tStart = t  # local t and not account for scr refresh
        instr_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_15, 'tStartRefresh')  # time at next scr refresh
        instr_15.setAutoDraw(True)
    
    # *key_resp_instr_14* updates
    waitOnFlip = False
    if key_resp_instr_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instr_14.frameNStart = frameN  # exact frame index
        key_resp_instr_14.tStart = t  # local t and not account for scr refresh
        key_resp_instr_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instr_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_instr_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instr_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instr_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instr_14.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instr_14.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_instr_14.keys = theseKeys.name  # just the last key pressed
            key_resp_instr_14.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ASRSgComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ASRSg"-------
for thisComponent in ASRSgComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('P49b.response', P49b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P50b.response', P50b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P51b.response', P51b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P52b.response', P52b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P53b.response', P53b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P54b.response', P54b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P55b.response', P55b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P56b.response', P56b.getRating())
#thisExp.nextEntry()


# check responses
if key_resp_instr_14.keys in ['', [], None]:  # No response was made
    key_resp_instr_14.keys = None
thisExp.addData('key_resp_instr_14.keys',key_resp_instr_14.keys)
if key_resp_instr_14.keys != None:  # we had a response
    thisExp.addData('key_resp_instr_14.rt', key_resp_instr_14.rt)
thisExp.nextEntry()
# the Routine "ASRSg" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# ------Prepare to start Routine "ASRSh"-------
# update component parameters for each repeat
P57b.reset()
P58b.reset()
key_resp_instr_16.keys = []
key_resp_instr_16.rt = []
# keep track of which components have finished
ASRShComponents = [P57a, P57b, P58a, P58b, P59a, P59b, P60a, P60b, P61a, P61b, P62a, P62b, P63a, P63b, P64a, P64b, instr_16, instr_17, key_resp_instr_16]
for thisComponent in ASRShComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ASRShClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True


# -------Run Routine "ASRSh"-------
while continueRoutine:
    # get current time
    t = ASRShClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ASRShClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/P2a components on each frame
    
    # *P57a* updates
    if P57a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P57a.frameNStart = frameN  # exact frame index
        P57a.tStart = t  # local t and not account for scr refresh
        P57a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P57a, 'tStartRefresh')  # time at next scr refresh
        P57a.setAutoDraw(True)
    
    # *P57b* updates
    if P57b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P57b.frameNStart = frameN  # exact frame index
        P57b.tStart = t  # local t and not account for scr refresh
        P57b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P57b, 'tStartRefresh')  # time at next scr refresh
        P57b.setAutoDraw(True)
        
    # *P58a* updates
    if P58a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P58a.frameNStart = frameN  # exact frame index
        P58a.tStart = t  # local t and not account for scr refresh
        P58a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P58a, 'tStartRefresh')  # time at next scr refresh
        P58a.setAutoDraw(True)

    # *P58b* updates
    if P58b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P58b.frameNStart = frameN  # exact frame index
        P58b.tStart = t  # local t and not account for scr refresh
        P58b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P58b, 'tStartRefresh')  # time at next scr refresh
        P58b.setAutoDraw(True)
        
    # *P59a* updates
    if P59a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P59a.frameNStart = frameN  # exact frame index
        P59a.tStart = t  # local t and not account for scr refresh
        P59a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P59a, 'tStartRefresh')  # time at next scr refresh
        P59a.setAutoDraw(True)

    # *P59b* updates
    if P59b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P59b.frameNStart = frameN  # exact frame index
        P59b.tStart = t  # local t and not account for scr refresh
        P59b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P59b, 'tStartRefresh')  # time at next scr refresh
        P59b.setAutoDraw(True)

    # *P60a* updates
    if P60a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P60a.frameNStart = frameN  # exact frame index
        P60a.tStart = t  # local t and not account for scr refresh
        P60a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P3a, 'tStartRefresh')  # time at next scr refresh
        P60a.setAutoDraw(True)

    # *P60b* updates
    if P60b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P60b.frameNStart = frameN  # exact frame index
        P60b.tStart = t  # local t and not account for scr refresh
        P60b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P60b, 'tStartRefresh')  # time at next scr refresh
        P60b.setAutoDraw(True)
        
     # *P61a* updates
    if P61a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P61a.frameNStart = frameN  # exact frame index
        P61a.tStart = t  # local t and not account for scr refresh
        P61a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P61a, 'tStartRefresh')  # time at next scr refresh
        P61a.setAutoDraw(True)

    # *P61b* updates
    if P61b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P61b.frameNStart = frameN  # exact frame index
        P61b.tStart = t  # local t and not account for scr refresh
        P61b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P61b, 'tStartRefresh')  # time at next scr refresh
        P61b.setAutoDraw(True)

    # *P62a* updates
    if P62a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P62a.frameNStart = frameN  # exact frame index
        P62a.tStart = t  # local t and not account for scr refresh
        P62a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P62a, 'tStartRefresh')  # time at next scr refresh
        P62a.setAutoDraw(True)

    # *P62b* updates
    if P62b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P62b.frameNStart = frameN  # exact frame index
        P62b.tStart = t  # local t and not account for scr refresh
        P62b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P62b, 'tStartRefresh')  # time at next scr refresh
        P62b.setAutoDraw(True)
        
     # *P63a* updates
    if P63a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P63a.frameNStart = frameN  # exact frame index
        P63a.tStart = t  # local t and not account for scr refresh
        P63a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P63a, 'tStartRefresh')  # time at next scr refresh
        P63a.setAutoDraw(True)

    # *P63b* updates
    if P63b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P63b.frameNStart = frameN  # exact frame index
        P63b.tStart = t  # local t and not account for scr refresh
        P63b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P63b, 'tStartRefresh')  # time at next scr refresh
        P63b.setAutoDraw(True)

    # *P64a* updates
    if P64a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P64a.frameNStart = frameN  # exact frame index
        P64a.tStart = t  # local t and not account for scr refresh
        P64a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P64a, 'tStartRefresh')  # time at next scr refresh
        P64a.setAutoDraw(True)

    # *P64b* updates
    if P64b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P64b.frameNStart = frameN  # exact frame index
        P64b.tStart = t  # local t and not account for scr refresh
        P64b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P64b, 'tStartRefresh')  # time at next scr refresh
        P64b.setAutoDraw(True)
        
  
    # *instr_16* updates
    if instr_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_16.frameNStart = frameN  # exact frame index
        instr_16.tStart = t  # local t and not account for scr refresh
        instr_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_16, 'tStartRefresh')  # time at next scr refresh
        instr_16.setAutoDraw(True)


    # *instr_17* updates
    if instr_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_17.frameNStart = frameN  # exact frame index
        instr_17.tStart = t  # local t and not account for scr refresh
        instr_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_17, 'tStartRefresh')  # time at next scr refresh
        instr_17.setAutoDraw(True)
    
    # *key_resp_instr_16* updates
    waitOnFlip = False
    if key_resp_instr_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instr_16.frameNStart = frameN  # exact frame index
        key_resp_instr_16.tStart = t  # local t and not account for scr refresh
        key_resp_instr_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instr_16, 'tStartRefresh')  # time at next scr refresh
        key_resp_instr_16.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instr_16.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instr_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instr_16.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instr_16.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_instr_16.keys = theseKeys.name  # just the last key pressed
            key_resp_instr_16.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ASRShComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ASRSh"-------
for thisComponent in ASRShComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('P57b.response', P57b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P58b.response', P58b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P59b.response', P59b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P60b.response', P60b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P61b.response', P61b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P62b.response', P62b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P63b.response', P63b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P64b.response', P64b.getRating())
#thisExp.nextEntry()


# check responses
if key_resp_instr_16.keys in ['', [], None]:  # No response was made
    key_resp_instr_16.keys = None
thisExp.addData('key_resp_instr_16.keys',key_resp_instr_16.keys)
if key_resp_instr_16.keys != None:  # we had a response
    thisExp.addData('key_resp_instr_16.rt', key_resp_instr_16.rt)
thisExp.nextEntry()
# the Routine "ASRSh" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ASRSi"-------
# update component parameters for each repeat
P65b.reset()
P66b.reset()
key_resp_instr_18.keys = []
key_resp_instr_18.rt = []
# keep track of which components have finished
ASRSiComponents = [P65a, P65b, P66a, P66b, P67a, P67b, P68a, P68b, P69a, P69b, P70a, P70b, P71a, P71b, instr_18, instr_19, key_resp_instr_18]
for thisComponent in ASRSiComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ASRSiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True


# -------Run Routine "ASRSi"-------
while continueRoutine:
    # get current time
    t = ASRSiClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ASRSiClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/P2a components on each frame
    
    # *P65a* updates
    if P65a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P65a.frameNStart = frameN  # exact frame index
        P65a.tStart = t  # local t and not account for scr refresh
        P65a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P65a, 'tStartRefresh')  # time at next scr refresh
        P65a.setAutoDraw(True)
    
    # *P65b* updates
    if P65b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P65b.frameNStart = frameN  # exact frame index
        P65b.tStart = t  # local t and not account for scr refresh
        P65b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P65b, 'tStartRefresh')  # time at next scr refresh
        P65b.setAutoDraw(True)
        
    # *P66a* updates
    if P66a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P66a.frameNStart = frameN  # exact frame index
        P66a.tStart = t  # local t and not account for scr refresh
        P66a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P66a, 'tStartRefresh')  # time at next scr refresh
        P66a.setAutoDraw(True)

    # *P66b* updates
    if P66b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P66b.frameNStart = frameN  # exact frame index
        P66b.tStart = t  # local t and not account for scr refresh
        P66b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P66b, 'tStartRefresh')  # time at next scr refresh
        P66b.setAutoDraw(True)
        
    # *P67a* updates
    if P67a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P67a.frameNStart = frameN  # exact frame index
        P67a.tStart = t  # local t and not account for scr refresh
        P67a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P67a, 'tStartRefresh')  # time at next scr refresh
        P67a.setAutoDraw(True)

    # *P67b* updates
    if P67b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P67b.frameNStart = frameN  # exact frame index
        P67b.tStart = t  # local t and not account for scr refresh
        P67b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P67b, 'tStartRefresh')  # time at next scr refresh
        P67b.setAutoDraw(True)

    # *P68a* updates
    if P68a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P68a.frameNStart = frameN  # exact frame index
        P68a.tStart = t  # local t and not account for scr refresh
        P68a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P3a, 'tStartRefresh')  # time at next scr refresh
        P68a.setAutoDraw(True)

    # *P68b* updates
    if P68b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P68b.frameNStart = frameN  # exact frame index
        P68b.tStart = t  # local t and not account for scr refresh
        P68b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P68b, 'tStartRefresh')  # time at next scr refresh
        P68b.setAutoDraw(True)
        
     # *P69a* updates
    if P69a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P69a.frameNStart = frameN  # exact frame index
        P69a.tStart = t  # local t and not account for scr refresh
        P69a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P69a, 'tStartRefresh')  # time at next scr refresh
        P69a.setAutoDraw(True)

    # *P69b* updates
    if P69b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P69b.frameNStart = frameN  # exact frame index
        P69b.tStart = t  # local t and not account for scr refresh
        P69b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P69b, 'tStartRefresh')  # time at next scr refresh
        P69b.setAutoDraw(True)

    # *P70a* updates
    if P70a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P70a.frameNStart = frameN  # exact frame index
        P70a.tStart = t  # local t and not account for scr refresh
        P70a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P70a, 'tStartRefresh')  # time at next scr refresh
        P70a.setAutoDraw(True)

    # *P70b* updates
    if P70b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P70b.frameNStart = frameN  # exact frame index
        P70b.tStart = t  # local t and not account for scr refresh
        P70b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P70b, 'tStartRefresh')  # time at next scr refresh
        P70b.setAutoDraw(True)
        
     # *P71a* updates
    if P71a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P71a.frameNStart = frameN  # exact frame index
        P71a.tStart = t  # local t and not account for scr refresh
        P71a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P71a, 'tStartRefresh')  # time at next scr refresh
        P71a.setAutoDraw(True)

    # *P71b* updates
    if P71b.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P71b.frameNStart = frameN  # exact frame index
        P71b.tStart = t  # local t and not account for scr refresh
        P71b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P71b, 'tStartRefresh')  # time at next scr refresh
        P71b.setAutoDraw(True)

       
  
    # *instr_18* updates
    if instr_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_18.frameNStart = frameN  # exact frame index
        instr_18.tStart = t  # local t and not account for scr refresh
        instr_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_18, 'tStartRefresh')  # time at next scr refresh
        instr_18.setAutoDraw(True)


    # *instr_19* updates
    if instr_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_19.frameNStart = frameN  # exact frame index
        instr_19.tStart = t  # local t and not account for scr refresh
        instr_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_19, 'tStartRefresh')  # time at next scr refresh
        instr_19.setAutoDraw(True)
    
    # *key_resp_instr_18* updates
    waitOnFlip = False
    if key_resp_instr_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instr_18.frameNStart = frameN  # exact frame index
        key_resp_instr_18.tStart = t  # local t and not account for scr refresh
        key_resp_instr_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instr_18, 'tStartRefresh')  # time at next scr refresh
        key_resp_instr_18.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instr_18.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instr_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instr_18.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instr_18.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_instr_18.keys = theseKeys.name  # just the last key pressed
            key_resp_instr_18.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ASRSiComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ASRSi"-------
for thisComponent in ASRSiComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('P65b.response', P65b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P66b.response', P66b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P67b.response', P67b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P68b.response', P68b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P69b.response', P69b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P70b.response', P70b.getRating())
#thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('P71b.response', P71b.getRating())
#thisExp.nextEntry()

# check responses
if key_resp_instr_18.keys in ['', [], None]:  # No response was made
    key_resp_instr_18.keys = None
thisExp.addData('key_resp_instr_18.keys',key_resp_instr_18.keys)
if key_resp_instr_18.keys != None:  # we had a response
    thisExp.addData('key_resp_instr_18.rt', key_resp_instr_18.rt)
thisExp.nextEntry()
# the Routine "ASRSi" was not non-slip safe, so reset the non-slip timer
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
    # update/P2a components on each frame
    
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