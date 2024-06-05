Read the .xml files within the OpenVibe Designer. 

Please, adjust the paths to the one corresponding to your computer, so that OpenVibe could read the audio and Lua files. 

You can run the OpenVibe scenario without connecting an EEG device by setting the Generic Oscillator onto the Acquisition Server. Random EEG signal will be generated.

Channels can be referenced by loading the "24channel" file into the Driver Properties, after indicating 24 sensors.

You can see the stimulation labels in real time on the EEG data. Stimulation codes are available at: https://openvibe.inria.fr/stimulation-codes/

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The scenarios have been created on OpenVibe version 3.4.0. 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

KeyBoardAndVisualStimuli.xml: 

This scenario has been designed for demonstration purposes only in the context of a workshop with students. 

A clock stimulator is sending the image of a microglia every 2 seconds (we can see its label on the EEG signal in real time). However, the stimulation filter is rejecting the information of the image between seconds 10 and 20. During this interval, its label is not appearing anymore in the EEG signal. You can make the image disappear by pressing then letter "q" on the keyboard. Be careful, because if you press the letter "s", the scenario stops. Another clock stimulator is sending a label to the EEG signal every 1.5 seconds. This labels only counts time and does not correspond to any stimulus. Overall, the EEG signal is written in a GDF file. The EEG signal along with the stimulation information is also written into a binary file (.ov) via the Generic Stream Writer (see the "TopographicMaps.xml" file to discover how to read a generic stream). On the other hand, for visualization only, the signal is filtered between 1 and 20 Hz and can be observed within a second signal display window. 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TopographicMaps.xml: 
The EEG signal is read from binary .ov file via the Generic stream reader. The data is re-referenced to the Nz sensor and bandpass filtered between 8 and 12 Hz. A 2D and a 3D topographic map is shown in real time. Also, the EEG data is display both before and after bandpass filtering. The non-filtered data is written in a GDF file.




