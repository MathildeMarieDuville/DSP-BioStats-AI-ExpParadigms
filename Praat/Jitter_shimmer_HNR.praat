#Computes jitter, shimmer, and harmonics-to-noise ratio

form Enter Full Path + \ 
    sentence directory C:\
endform


#Sets up Data File - erases existing file with same name
filedelete 'directory$''name$'Jitter_shimmer_HNR.csv
header_row$ = "Filename" + "," + "Jitter local" + "," + "Jitter local absolute (sec)" + "," + "Jitter rap" + "," + "Jitter ppq5" + "," + "Jitter ddp" + "," + "Shimmer local" + "," + "Shimmer local (dB)" + "," + "Shimmer rapq3" + "," + "Shimmer rapq5" + "," + "Shimmer rapq11" + "," + "Shimmer dda" + "," + "Mean HNR (dB)" + "," + "SD HNR" + "," + "Min HNR (dB)" + "," + "Max HNR (dB)" + "," + newline$ 
header_row$ > 'directory$'Jitter_shimmer_HNR.csv

#Sets up array of files to run batch process on
Create Strings as file list...  list 'directory$'*.wav
number_files = Get number of strings
  for j from 1 to number_files
     select Strings list
     current_token$ = Get string... 'j'
     name$ = current_token$ - ".wav"
     Read from file... 'directory$''current_token$'
 

#Jitter & shimmer
select Sound 'name$'
#Point process: sequence of points t in time defined on time domain [tmin, tmax]
#Acoustic periodicity contour
To PointProcess (periodic, cc)... 75 600
#Arguments: time range, period floor, period ceiling, maximum period floor 
jitterlocal = Get jitter (local)... 0 0 0.0001 0.02 1.3
jitterlocalabsolute = Get jitter (local, absolute)... 0 0 0.0001 0.02 1.3
jitterrap = Get jitter (rap)... 0 0 0.0001 0.02 1.3
jitterppq5 = Get jitter (ppq5)... 0 0 0.0001 0.02 1.3
jitterddp = Get jitter (ddp)... 0 0 0.0001 0.02 1.3


select Sound 'name$'
plus PointProcess 'name$'
#Arguments: time range, period floor, period ceiling, maximum period floor 
shimmerlocal =  Get shimmer (local)... 0 0 0.0001 0.02 1.3 1.6
shimmerlocaldb = Get shimmer (local_dB)... 0 0 0.0001 0.02 1.3 1.6
shimmerapq3 = Get shimmer (apq3)... 0 0 0.0001 0.02 1.3 1.6
shimmerapq5 = Get shimmer (apq5)... 0 0 0.0001 0.02 1.3 1.6
shimmerapq11 =  Get shimmer (apq11)... 0 0 0.0001 0.02 1.3 1.6
shimmerdda = Get shimmer (dda)... 0 0 0.0001 0.02 1.3 1.6
       

#Harmonics to noise ratio
select Sound 'name$'
#Arguments: time step, minimum pitch, silence threshold, number of periods per window
To Harmonicity (cc)... 0.01 75 0.1 4.5
select Harmonicity 'name$'
onset = Get start time
offset = Get end time
meanHNR = Get mean... 0 0
sdHNR = Get standard deviation... 0 0
#Arguments: time range, interpolation
min_HNR = Get minimum... onset offset Parabolic
max_HNR = Get maximum... onset offset Parabolic

fileappend "'directory$'Jitter_shimmer_HNR.csv" 'current_token$' ','  'jitterlocal' ',' 'jitterlocalabsolute' ',' 'jitterrap' ',' 'jitterppq5' ',' 'jitterddp' ',' 'shimmerlocal' ',' 'shimmerlocaldb' ',' 'shimmerapq3' ',' 'shimmerapq5' ',' 'shimmerapq11' ',' 'shimmerdda' ',' 'meanHNR' ',' 'sdHNR' ',' 'min_HNR' ',' 'max_HNR' ',' 'newline$'
     select all
minus Strings list
Remove
endfor

