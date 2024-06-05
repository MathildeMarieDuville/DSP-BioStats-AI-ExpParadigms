-- Mathilde Marie Duville 

function initialize(box)

	dofile(box:get_config("${Path_Data}") .. "/plugins/stimulation/lua-stimulator-stim-codes.lua")
	
-- Stimuli
enojo1, enojo2, enojo3, enojo4 = 33024,33026,33028,33030
disgusto1,disgusto2, disgusto3, disgusto4  = 33032,33034, 33036,33038
miedo1, miedo2, miedo3, miedo4 = 33040,33042,33044,33046
felicidad1, felicidad2, felicidad3, felicidad4 = 33048,33050,33052,33054
neutro1, neutro2, neutro3, neutro4 = 0,2, 4,6
tristeza1, tristeza2, tristeza3, tristeza4 = 8,10,12,14

-- Even number : label for play, odd numbers: label for stop
-- OVTK_StimulationId_Label_00                           0x00008100  //  33024  1
-- OVTK_StimulationId_Label_01                           0x00008101  //  33025
-- OVTK_StimulationId_Label_02                           0x00008102  //  33026  2
-- OVTK_StimulationId_Label_03                           0x00008103  //  33027
-- OVTK_StimulationId_Label_04                           0x00008104  //  33028  3
-- OVTK_StimulationId_Label_05                           0x00008105  //  33029
-- OVTK_StimulationId_Label_06                           0x00008106  //  33030  4
-- OVTK_StimulationId_Label_07                           0x00008107  //  33031
-- OVTK_StimulationId_Label_08                           0x00008108  //  33032  5
-- OVTK_StimulationId_Label_09                           0x00008109  //  33033
-- OVTK_StimulationId_Label_0A                           0x0000810a  //  33034  6
-- OVTK_StimulationId_Label_0B                           0x0000810b  //  33035
-- OVTK_StimulationId_Label_0C                           0x0000810c  //  33036  7
-- OVTK_StimulationId_Label_0D                           0x0000810d  //  33037
-- OVTK_StimulationId_Label_0E                           0x0000810e  //  33038  8
-- OVTK_StimulationId_Label_0F                           0x0000810f  //  33039
-- OVTK_StimulationId_Label_10                           0x00008110  //  33040  9
-- OVTK_StimulationId_Label_11                           0x00008111  //  33041
-- OVTK_StimulationId_Label_12                           0x00008112  //  33042  10
-- OVTK_StimulationId_Label_13                           0x00008113  //  33043 
-- OVTK_StimulationId_Label_14                           0x00008114  //  33044  11
-- OVTK_StimulationId_Label_15                           0x00008115  //  33045
-- OVTK_StimulationId_Label_16                           0x00008116  //  33046  12
-- OVTK_StimulationId_Label_17                           0x00008117  //  33047
-- OVTK_StimulationId_Label_18                           0x00008118  //  33048  13
-- OVTK_StimulationId_Label_19                           0x00008119  //  33049
-- OVTK_StimulationId_Label_1A                           0x0000811a  //  33050  14
-- OVTK_StimulationId_Label_1B                           0x0000811b  //  33051
-- OVTK_StimulationId_Label_1C                           0x0000811c  //  33052  15
-- OVTK_StimulationId_Label_1D                           0x0000811d  //  33053
-- OVTK_StimulationId_Label_1E                           0x0000811e  //  33054  16
-- OVTK_StimulationId_Label_1F                           0x0000811f  //  33055
-- OVTK_StimulationId_Number_00                          0x00000000  //  0  17
-- OVTK_StimulationId_Number_01                          0x00000001  //  1
-- OVTK_StimulationId_Number_02                          0x00000002  //  2  18
-- OVTK_StimulationId_Number_03                          0x00000003  //  3
-- OVTK_StimulationId_Number_04                          0x00000004  //  4  19
-- OVTK_StimulationId_Number_05                          0x00000005  //  5
-- OVTK_StimulationId_Number_06                          0x00000006  //  6  20
-- OVTK_StimulationId_Number_07                          0x00000007  //  7
-- OVTK_StimulationId_Number_08                          0x00000008  //  8  21
-- OVTK_StimulationId_Number_09                          0x00000009  //  9
-- OVTK_StimulationId_Number_0A                          0x0000000a  //  10  22
-- OVTK_StimulationId_Number_0B                          0x0000000b  //  11
-- OVTK_StimulationId_Number_0C                          0x0000000c  //  12  23
-- OVTK_StimulationId_Number_0D                          0x0000000d  //  13
-- OVTK_StimulationId_Number_0E                          0x0000000e  //  14  24
-- OVTK_StimulationId_Number_0F                          0x0000000f  //  15

--OVTK_StimulationId_Number_1D                          0x0000001d  //  29 -- Cross image
--OVTK_StimulationId_Number_1E                          0x0000001e  //  30 -- Image of "End of the experiment"
--OVTK_StimulationId_Number_1F                          0x0000001f  //  31 --  End of the experiment

stim = {miedo2,neutro3,tristeza4,tristeza1,disgusto4,felicidad3,miedo1,miedo4,neutro4,disgusto2,disgusto3,felicidad2,disgusto1,tristeza2,neutro2,tristeza3,felicidad4,miedo3,enojo3,enojo4,enojo1,neutro1,enojo2,felicidad1}

estimulos = 24 --Number of stimuli
end

function process(box)
--The scenario starts at t=0

	local t=0
	box:send_stimulation(1, OVTK_StimulationId_ExperimentStart, t, 0)
	t = t + 5 --We wait 5 seconds to start sending the stimuli
	
	box:send_stimulation(1, 29, t, 0) --cross image
	--OVTK_StimulationId_Number_1D                          0x0000001d  //  29
	
	t = t+0.5 -- 0.5 s before the first audio stimulus

		for i = 1, estimulos do -- Loop for all audio stimuli
	
		box:send_stimulation(1, stim[i], t, 0) -- Stimulus
		
		--Break in-between stimuli
		t = t+3.11 
		
		end
		
	--End 
	--OVTK_StimulationId_Number_1E                          0x0000001e  //  30	
	box:send_stimulation(1, 30, t, 0)
	
	t = t+4 -- 4 seconds
	
	-- Send end for completeness
	box:send_stimulation(1, OVTK_GDF_End_Of_Session, t, 0)
	t = t + 0.5

	box:send_stimulation(1, OVTK_StimulationId_Train, t, 0)
	t = t + 0.5
	
	-- Used to cause the acquisition scenario to stop
	box:send_stimulation(1, OVTK_StimulationId_ExperimentStop, t, 0)
	t = t + 0.5
	box:send_stimulation(1, 31, t, 0)

end