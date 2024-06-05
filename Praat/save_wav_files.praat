dir$ = "C:\Your\Directory\"

n = numberOfSelected("Sound")
for i from 1 to n
s'i' = selected("Sound",'i')
s'i'$ = selected$("Sound",'i')
endfor

for i from 1 to n
n$ = s'i'$
select s'i'
#Save as 24-bit WAV file... 'dir$''n$''i'.wav
Save as 24-bit WAV file... 'dir$''n$'.wav
endfor