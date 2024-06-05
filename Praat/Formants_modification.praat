#Changes the frequency of formants (F1, F2, F3, F4, and/or F5) of audio files in directory
#Linear Predictive Coding (LPC) is applied.
#Please, refer to the PowerPoint slide dedicated to it for details about this method (TheoreticalExplanations.pdf).
#The Praat Vocal Toolkit must be installed (see: https://www.praatvocaltoolkit.com/download-installation.html) and #its functions must be reachable from your path.
#This code is a modification of the root code suggested by this toolkit
#The new audio file appears as an object in Praat after running the code.
#Use the script named "save_wav_files" suggested in this folder to save it as a .wav file in your directory

form Enter Full Path + \ 
    sentence directory C:\
	comment Formant determination
	positive Maximum_formant_(Hz) 5500 (= adult female)
	comment Set 5000 Hz for men, 5500 Hz for women or up to 8000 Hz for children.
	boolean Process_only_voiced_parts 1
	boolean Retrieve_intensity_contour 1
endform

#Sets up array of files to run batch process on
Create Strings as file list...  list 'directory$'*.wav
number_files = Get number of strings
  for j from 1 to number_files
     select Strings list
     current_token$ = Get string... 'j'
     name$ = current_token$ - ".wav"
     Read from file... 'directory$''current_token$'

## New F2 (Hz)
newF2# = {719.57, 865}

## New F3 (Hz)
newF3# = {1283.2, 1450}

##No change
new_F1_mean = 0 
new_F4_mean = 0 
new_F5_mean = 0 

f1 = max(new_F1_mean, 0)
f2 = max(newF2# [j], 0)
f3 = max(newF3# [j], 0)
f4 = max(new_F4_mean, 0)
f5 = max(new_F5_mean, 0)


include batch.praat

procedure action
	s = selected("Sound")
	s$ = selected$("Sound")
	original_dur = Get total duration
	int = Get intensity (dB)

	if int <> undefined
		if process_only_voiced_parts
			@extractUV
			selectObject: extractUV.s_v
			int_v = Get intensity (dB)
			if int_v <> undefined
				int = int_v
			else
				process_only_voiced_parts = 0
				selectObject: s
				removeObject: extractUV.s_u, extractUV.s_v
			endif
		endif

		runScript: "workpre.praat"
		wrk = selected("Sound")
		sf1 = Get sampling frequency

		runScript: "extractvowels.praat", 0, 0
		vow_tmp = selected("Sound")

		runScript: "workpre.praat"
		vow = selected("Sound")

		#formant1 = noprogress nowarn To Formant (robust): 0.005, 5, maximum_formant, 0.025, 50, 1.5, 5, 0.000001
		formant1 = noprogress nowarn To Formant (burg)... 0.0 5 maximum_formant 0.025 50 
		onset = Get start time
		offset = Get end time
		vf1 = Get mean: 1, onset, offset, "hertz"
		vf2 = Get mean: 2, onset, offset, "hertz"
		vf3 = Get mean: 3, onset, offset, "hertz"
		vf4 = Get mean: 4, onset, offset, "hertz"
		vf5 = Get mean: 5, onset, offset, "hertz"
		df1 = f1 - vf1
		df2 = f2 - vf2
		df3 = f3 - vf3
		df4 = f4 - vf4
		df5 = f5 - vf5

		selectObject: wrk
		hf = Filter (pass Hann band): maximum_formant, 0, 100

		selectObject: wrk
		sf2 = maximum_formant * 2
		rs1 = Resample: sf2, 10

		#formant2 = noprogress nowarn To Formant (robust): 0.005, 5, maximum_formant, 0.025, 50, 1.5, 5, 0.000001
		formant2 = noprogress nowarn To Formant (burg)... 0.0 5 maximum_formant 0.025 50 

		lpc1 = noprogress To LPC: sf2
		plusObject: rs1
		source = Filter (inverse)

		selectObject: formant2
		filtr = Copy: "filtr"

		if f1 <> 0 and abs(df1) < 1000
			Formula (frequencies): "if row = 1 then self + df1 else self fi"
		endif
		if f2 <> 0 and abs(df2) < 2500
			Formula (frequencies): "if row = 2 then self + df2 else self fi"
		endif
		if f3 <> 0 and abs(df3) < 2500
			Formula (frequencies): "if row = 3 then self + df3 else self fi"
		endif
		if f4 <> 0 and abs(df4) < 2500
			Formula (frequencies): "if row = 4 then self + df4 else self fi"
		endif
		if f5 <> 0 and abs(df5) < 2500
			Formula (frequencies): "if row = 5 then self + df5 else self fi"
		endif

		lpc2 = noprogress To LPC: sf2
		plusObject: source
		tmp = Filter: "no"

		rs2 = Resample: sf1, 10
		Formula: "self + object[hf]"

		runScript: "workpost.praat", original_dur
		Scale intensity: int
		runScript: "declip.praat"

		if process_only_voiced_parts
			@mixUV
		endif

		if retrieve_intensity_contour
			tmp3 = selected("Sound")
			plusObject: s
			runScript: "copyintensitycontour.praat"
			removeObject: tmp3
		endif
		dur = Get total duration
		if dur > 0.5
			Fade in: 0, 0, 0.005, "yes"
			Fade out: 0, dur, -0.005, "yes"
		endif

		removeObject: wrk, vow_tmp, vow, formant1, hf, rs1, formant2, lpc1, source, filtr, lpc2, tmp, rs2
	else
		Copy: "tmp"
	endif

	Rename: s$ + "-changeformants"
endproc

procedure extractUV
	runScript: "voicedunvoiced.praat", "no"
	select all
	.s_u = selected("Sound", -2)
	.s_v = selected("Sound", -1)
endproc

procedure mixUV
	.sel_tmp = selected("Sound")
	plusObject: extractUV.s_u
	runScript: "copymix.praat", 50, 0, 0
	removeObject: extractUV.s_u, extractUV.s_v, .sel_tmp
endproc
endfor



