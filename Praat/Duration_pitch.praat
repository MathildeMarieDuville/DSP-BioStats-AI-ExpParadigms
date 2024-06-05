#Computes median pitch, mean pitch, minimum pitch, maximum pitch, and duration

#Sets the directory where the audio files are located
form Enter Full Path + \ 
    sentence directory C:\
endform

#Sets up Data File - erases existing file with same name
filedelete 'directory$''name$'Duration_pitch.csv
header_row$ = "Filename" + "," + "Median pitch(Hz)" + "," +  "Mean pitch(Hz)" + "," + "Min pitch(Hz)" + "," + "Max pitch(Hz)" + "," + "SD pitch(Hz)" + "," + "Duration (s)" +  newline$ 
header_row$ > 'directory$'Duration_pitch.csv

#Sets up array of files to run batch process on
Create Strings as file list...  list 'directory$'*.wav
number_files = Get number of strings
  for j from 1 to number_files
     select Strings list
     current_token$ = Get string... 'j'
     name$ = current_token$ - ".wav"
     Read from file... 'directory$''current_token$'
     

#Pitch features: change parameters from female to male: 100 for females and 75 for males (200 for children).
select Sound 'name$'
#Arguments = time step, pitch floor, pitch ceiling 

To Pitch: 0.01, 100, 600
# 0 0 = all signal
medianpitch = Get quantile: 0, 0, 0.50, "Hertz"
meanpitch = Get mean... 0 0 Hertz
minpitch = Get minimum... 0 0 Hertz Parabolic
maxpitch = Get maximum... 0 0 Hertz Parabolic
#sd_1 = Get standard deviation: 0, 0, "semitones"
sdpitch = Get standard deviation... 0 0 Hertz

#Total duration
select Sound 'name$'
dur = Get total duration


fileappend "'directory$'Duration_pitch.csv" 'current_token$' ',' 'medianpitch' ',' 'meanpitch' ',' 'minpitch'  ',' 'maxpitch'  ',' 'sdpitch' ',' 'dur', 'newline$'
     select all
minus Strings list
Remove
endfor

