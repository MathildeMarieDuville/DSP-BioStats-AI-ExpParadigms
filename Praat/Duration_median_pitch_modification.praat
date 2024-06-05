#Changes the duration and median pitch of audio files in directory
#A time domain PSOLA (Pitch Synchronous Overlap and Add) method is applied.
#Please, refer to the PowerPoint slide dedicated to it for details about this method (TheoreticalExplanations.pdf).
#The Praat Vocal Toolkit must be installed (see: https://www.praatvocaltoolkit.com/download-installation.html) and #its functions must be reachable from your path.
#This code is a modification of the root code suggested by this toolkit
#The new audio file appears as an object in Praat after running the code.
#Use the script named "save_wav_files" suggested in this folder to save it as a .wav file in your directory


form Enter Full Path + \ 
    sentence directory C:\
endform

#Sets up array of files to run batch process on
Create Strings as file list...  list 'directory$'*.wav
number_files = Get number of strings
  for j from 1 to number_files
     select Strings list
     current_token$ = Get string... 'j'
     name$ = current_token$ - ".wav"
     Read from file... 'directory$''current_token$'

writeInfoLine: "Median pitch and duration:"

#Indicate the variable of change "c" from the original audio files to the newly created one. The new file will be created following: new = original-c
#Pitch
diff# = {-16.2, 2.3}
select Sound 'name$'

include minmaxf0.praat
To Pitch: 0.01, minF0, maxF0
f0 = Get quantile: 0, 0, 0.50, "Hertz"
new_pitch_median = max(f0-diff# [j], 0)

#Duration
diffd# = {-0.3, 0.2}
select Sound 'name$'

original_dur = Get total duration
new_duration = max(original_dur-diffd# [j], 0)

appendInfoLine: new_pitch_median
appendInfoLine: f0
appendInfoLine: new_duration
appendInfoLine: original_dur
appendInfoLine: number_files

select all
minus Strings list

formant_shift_ratio = 1

type$ = extractWord$(selected$(), "")

if type$ = "Manipulation"
	manipulation = selected("Manipulation")

	selectObject: "Table changepitchmedian_data"
	f0 = Get value: 1, "f0"
	original_dur = Get value: 1, "original_dur"
	dur = Get value: 1, "dur"
	rdur = Get value: 1, "rdur"
	duration_factor = Get value: 1, "durationfactor"
	new_dur = Get value: 1, "newdur"
	Remove

	selectObject: manipulation
	@manipulate
else
include batch.praat
endif

procedure action
	s = selected("Sound")
	s$ = selected$("Sound")
	original_dur = Get total duration

	if new_pitch_median <> 0 or (new_duration <> 0 and new_duration <> object[s].xmax - object[s].xmin)
		runScript: "workpre.praat"
		wrk = selected("Sound")
		dur = Get total duration
		
		if new_duration = 0
			new_dur = dur
		else
			new_dur = new_duration + 0.025 + 0.025
			original_dur = new_duration
		endif
		duration_factor = new_dur / dur

		if formant_shift_ratio > 1
			rdur = formant_shift_ratio
		elsif formant_shift_ratio < 1
			rdur = 1 / (1 - formant_shift_ratio + 1)
		elsif formant_shift_ratio = 1
			rdur = 1
		endif


		if rdur * duration_factor > 3
			wrk2 = Extract part: 0, new_dur, "rectangular", 1, "no"
			dur = new_dur
		else
			wrk2 = Copy: "wrk2"
		endif

include minmaxf0.praat

		pitch = noprogress To Pitch: 0.01, minF0, maxF0
		f0 = Get quantile: 0, 0, 0.50, "Hertz"


		if f0 <> undefined
			if number(fixed$(f0, 2)) <> number(fixed$(new_pitch_median, 2))
				plusObject: wrk
				manipulation = noprogress To Manipulation
				@manipulate
			else
				selectObject: s
				Copy: "tmp"
			endif
		else
			selectObject: s
			Copy: "tmp"
		endif

		removeObject: wrk, pitch
	else
		Copy: "tmp"
	endif

	Rename: s$ + "-newpitchmedian_" + string$(new_pitch_median)+ "-newduration_" + string$(new_duration)
endproc

procedure manipulate
	.pitchtier = Extract pitch tier
	
	selectObject: .pitchtier
	if new_pitch_median <> 0
		.f0_f = new_pitch_median / f0
		Formula: "self * .f0_f"
	endif


	plusObject: manipulation
	Replace pitch tier

	.durationtier = Create DurationTier: "tmp", 0, dur
	Add point: 0, rdur * duration_factor
	plusObject: manipulation
	Replace duration tier

	selectObject: manipulation
	.res = Get resynthesis (overlap-add)

	.dur2 = Get total duration
	if .dur2 <> new_dur
		.tmp = Extract part: 0, new_dur, "rectangular", 1, "no"
	endif

	runScript: "workpost.praat", original_dur

	removeObject: manipulation, .pitchtier, .durationtier, .res

	if .dur2 <> new_dur
		removeObject: .tmp
	endif

endproc
endfor