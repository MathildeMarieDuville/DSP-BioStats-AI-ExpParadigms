#Computes formants and their bandwidths from audio files in directory

form Enter Full Path + \ 
    sentence directory C:\
endform

#Sets up Data File - erases existing file with same name
filedelete 'directory$''name$'F1-5-B1-5.csv
header_row$ = "Filename" + "," + "F1" + "," + "F2" + "," + "F3" + "," + "F4" + "," + "F5" + "," + "B1" + "," + "B2" + "," + "B3" + "," + "B4" + "," + "B5" + "," + newline$ 
header_row$ > 'directory$'F1-5-B1-5.csv

#Sets up array of files to run batch process on
Create Strings as file list...  list 'directory$'*.wav
number_files = Get number of strings
  for j from 1 to number_files
     select Strings list
     current_token$ = Get string... 'j'
     name$ = current_token$ - ".wav"
     Read from file... 'directory$''current_token$'

#F1, F2, F3
#Create the Formant Object
select Sound 'name$'
#Arguments: time step, maximum number of formants, maximum formant, window length, pre-emphasis from (Hz)
#5000 for men, 5500 for women and 8000 for children
To Formant (burg)... 0.0 5 5500 0.025 50 
select Formant 'name$'
onset = Get start time
offset = Get end time
f1 = Get mean... 1 onset offset Hertz
f2 = Get mean... 2 onset offset Hertz
f3 = Get mean... 3 onset offset Hertz
f4 = Get mean... 4 onset offset Hertz
f5 = Get mean... 5 onset offset Hertz

#Formants bandwidths 
dur2 = Get total duration
center = onset + dur2/2
#Arguments: formant number, time, units (Hertz or Bark), interpolation
b1 = Get bandwidth at time... 1 center Hertz Linear
b2 = Get bandwidth at time... 2 center Hertz Linear
b3 = Get bandwidth at time... 3 center Hertz Linear
b4 = Get bandwidth at time... 4 center Hertz Linear
b5 = Get bandwidth at time... 5 center Hertz Linear


fileappend "'directory$'F1-5-B1-5.csv" 'current_token$' ',' 'f1' ',' 'f2' ',' 'f3' ',' 'f4' ',' 'f5' ',' 'b1' ',' 'b2' ',' 'b3' ',' 'b4' ',' 'b5' ',' 'newline$'
     select all
minus Strings list
Remove
endfor

