#Computes intensity features from audio files in directory

form Enter Full Path + \ 
    sentence directory C:\
endform

#Sets up Data File - erases existing file with same name
filedelete 'directory$''name$'IntensityFeatures_dB.csv
header_row$ = "Filename" + "," + "Mean intensity (dB)" + "," + "Max intensity (dB)" + "," + "Min intensity (dB)" + "," + "SD intensity (dB)" + newline$ 
header_row$ > 'directory$'IntensityFeatures_dB.csv

#Sets up array of files to run batch process on
Create Strings as file list...  list 'directory$'*.wav
number_files = Get number of strings
  for j from 1 to number_files
     select Strings list
     current_token$ = Get string... 'j'
     name$ = current_token$ - ".wav"
     Read from file... 'directory$''current_token$'
     

#Intensity features
select Sound 'name$'
#Arguments: minimum pitch, time step, average method (time selection)
To Intensity: 100, 0, "yes"
select Intensity 'name$'
onset = Get start time
offset = Get end time
#Arguments: time range, method (energy, dB or sones)
mean_int = Get mean... onset offset dB
sd_int = Get standard deviation... onset offset 
#Arguments: time range, interpolation
min_int = Get minimum... onset offset Parabolic
max_int = Get maximum... onset offset Parabolic

fileappend "'directory$'IntensityFeatures_dB.csv" 'current_token$' ',' 'mean_int' ',' 'max_int' ',' 'min_int' ',' 'sd_int' ',' 'newline$'
     select all
minus Strings list
Remove
endfor

