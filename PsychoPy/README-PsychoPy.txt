The codes shared here have been designed on PsychoPy® version 3.2.4.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Depending on the size of the screen, it may be necessary to adjust dimensions within the following line code: 

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')


Also, as a consequence, the position of the elements (e.g., text, images) may be biased. Please, adjust their position to be adequate for your screen. 

You can adjust any variable that affects the dimensions of the discs, text or square in the code for Multiple Object Tracking (MOT) to be adequate to the dimensions of your screen. 
For instance, the area occupied by the instructions at the beginning of the task can be adjust by variable "instructionDimension = [40, 30] # x, y, in deg".

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


The answers of the Autism Spectrum Rating Scales (ASRS) saved within an Excel file (.csv) will be used to compute Standardized scores and generate a report of the patient's behavior.
Please refer to the corresponding Matlab code that uses this Excel file as input to generate the report. 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
