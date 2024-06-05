% This function creates a PDF report for ASRS measurements.
% inputs are 1) ASRS ratings as generated in a
% .csv format by the PsychoPy code elaborated by Mathilde Marie Duville,
% 2) probability for T-scores confidence interval computing: must be 90 or 
% 95%, 3) file is name of the .csv file

function t_scoresv2(ratings,CI,file,language, name) 
raw_data = []; raw_data = ratings;
complete_name = []; complete_name = char(table2array(raw_data(1,99)));
age = []; age = table2array(raw_data(1,100)); 
date = []; date =  char(table2array(raw_data(1,102)));
data = []; data = ratings;
data(:,[1,2,11,12,21,22,31,32,41,42,51,52,61,62,71,72,81,82,90:end])= [];
% DATA 
ASRS_part = []; i = []; 
for i = 1:1:size(data,2) %responses
    e = []; e = table2array(data(:,i));
    idx = []; idx = find(cellfun(@isempty,e));
    e(idx) = []; resp = []; resp =convertCharsToStrings(e{1,1});
    ASRS_part = [ASRS_part;resp];
end
% Score 
clc; i =[]; RIGHT = [1,2,4,6,7,11,13,14,16:22,24:27,29,30,34:38,...
   40,41,44,46,48:54,57:60,62:68,71];
for i = RIGHT %from 0 to 4
    e = []; e = ASRS_part(i,1);
    if e == "Nunca"
        ASRS_part(i,2) = 0;
    elseif e == "Casi nunca (rara vez)" 
        ASRS_part(i,2) = 1;
    elseif e == "Ocasionalmente" 
        ASRS_part(i,2) = 2;
    elseif e == "Frecuentemente" 
        ASRS_part(i,2) = 3;
    elseif e == "Muy frecuentemente" 
        ASRS_part(i,2) = 4;
    elseif e == "None" 
        ASRS_part(i,2) = 5; %5 == NONE
    end
end
i =[]; WRONG = [3,5,8:10,12,15,23,28,31:33,39,42,43,45,47,55,56,61,69,70];
for i = WRONG %from 4 to 0
    e = []; e = ASRS_part(i,1);
    if e == "Nunca"
        ASRS_part(i,2) = 4;
    elseif e == "Casi nunca (rara vez)" 
        ASRS_part(i,2) = 3;
    elseif e == "Ocasionalmente" 
        ASRS_part(i,2) = 2;
    elseif e == "Frecuentemente" 
        ASRS_part(i,2) = 1;
    elseif e == "Muy frecuentemente" 
        ASRS_part(i,2) = 0;
    elseif e == "None" 
        ASRS_part(i,2) = 5; %5 == NONE
    end
end

%% Related scales 
%Limited speech
Conv_lim = [];SC_lim = []; UB_lim = []; SR_lim = []; DSM_lim = [];
PS_lim = []; AS_lim = []; SER_lim = [];

SC_lim = [0 1 2 4:8 10:15 17:21 23:27 29:34 36:40 42:46 48:53 55:59 61:65 ...
    67:72 74:76 repmat(76,1,40)];

UB_lim = [0 1 3:5 7:9 11:13 15:17 19:21 23:25 27:29 31:33 ...
    35:37 39:41 43:45 47:49 51:53 55:57 59:61 63:65 67:69 ...
    71:73 75:77 79:81 83:85 87:89 91:93 95:96 repmat(96,1,32)];

SR_lim = [0:7 9:24 26:41 43:58 60:68 repmat(68,1,40)];

DSM_lim = [0 1 3:5 7:10 12:14 16:18 20:22 24:27 29:31 33:35 37:39 ...
    41:44 46:48 50:52 54:56 58:61 63:65 67:69 71:73 75:78 80:82 ...
    84:86 88:90 92:95 97:99 101:103 105:107 109:112 114:116 118:120 ...
    122:124 126:129 131:133 135 136];

PS_lim = [0 1 3:6 8:10 12:15 17:19 21:24 26:28 30:33 35 36 repmat(36,1,76)];

AS_lim = [0 2 3 5 6 8 9 11 12 14 15 17 18 20 21 23 24 repmat(24,1,88)];

SER_lim = [0:5 7:18 20:31 33:44 46:52 repmat(52,1,56)];

Conv_lim = [0:104;SC_lim;UB_lim;SR_lim;DSM_lim;PS_lim;AS_lim;SER_lim ]';

%Social/Communication
SC_tot = []; i = []; SC_sum = []; 
if language == 0
    SC_idx =  [3 4 8 9 12 23 28 31 32 33 39 42 43 45 55 56 61 69 70]; 
    for i = 1:1:size(SC_idx,2)
        SC_tot = [SC_tot; str2num(ASRS_part(SC_idx(i),2))];
    end
    % SC_tot(1:5) = 5;

    if any(SC_tot(:) == 5) %at least one omitted response
        idx = []; idx = find(SC_tot(:) == 5);
        switch size(idx,1)
            case num2cell(1:2)
                SC_tot_om = []; SC_tot_om = SC_tot; SC_tot_om(idx,:) = [];
                raw = []; raw = sum(SC_tot_om); nb_scale = []; nb_scale = size(SC_idx,2);
                nb_res = []; nb_res = nb_scale - size(idx,1);
                SC_sum = round((raw*nb_scale)/nb_res);
                disp(['Social/Communication: ' num2str(size(idx,1))... 
                    ' omitted response - Ok to compute raw score'])
            otherwise 
                disp(['Social/Communication: too much omitted responses'...
                    ' (n = ' num2str(size(idx,1)) ')'... 
                    ' - Threshold = 2'])
        end

    else
        SC_sum = sum(SC_tot);
        disp(['Social/Communication: no omitted response'])
    end
else
    disp(['Social/Communication: prorated score for limited speech'])
    SC_idx =  [3 4 8 12 28 31 32 33 39 42 43 45 55 61 69 70]; 
    for i = 1:1:size(SC_idx,2)
        SC_tot = [SC_tot; str2num(ASRS_part(SC_idx(i),2))];
    end    
    
    if any(SC_tot(:) == 5) 
             disp(['Social/Communication: too much omitted responses'...
                    ' (n = ' num2str(size(idx,1)) ')'... 
                    ' - Threshold = 0 / Prorated from limited speech'])
     else
        SC_sumLim = sum(SC_tot);
        for p = 1:1:size(Conv_lim,1) %Possibilities for conversions
            raw_pro = Conv_lim(p,1);
            try SC_sumLim;
                switch SC_sumLim
                    case raw_pro
                        SC_sum = Conv_lim(p,2); %Second column = SC
                end
            catch
                 disp('Social Communication: unable to compute T-score/too much omitted responses')
                 break
            end
        end
    end
end

% Unusual Behaviours
UB_tot = []; i = []; UB_sum = []; 
if language == 0
    UB_idx =  [2 13 17 20 21 22 24:27 29 38 40 46 48:51 54 62 63 65 67 68]; 
    for i = 1:1:size(UB_idx,2)
        UB_tot = [UB_tot; str2num(ASRS_part(UB_idx(i),2))];
    end

    if any(UB_tot(:) == 5) %at least one omitted response
        idx = []; idx = find(UB_tot(:) == 5);
        switch size(idx,1)
            case num2cell(1:2)
                UB_tot_om = []; UB_tot_om = UB_tot; UB_tot_om(idx,:) = [];
                raw = []; raw = sum(UB_tot_om); nb_scale = []; nb_scale = size(UB_idx,2);
                nb_res = []; nb_res = nb_scale - size(idx,1);
                UB_sum = round((raw*nb_scale)/nb_res);
                disp(['Unusual Behaviours: ' num2str(size(idx,1))... 
                    ' omitted response - Ok to compute raw score'])
            otherwise 
                disp(['Unusual Behaviours: too much omitted responses'...
                    ' (n = ' num2str(size(idx,1)) ')'... 
                    ' - Threshold = 2'])
        end

    else
        UB_sum = sum(UB_tot);
        disp(['Unusual Behaviours: no omitted response'])
    end
else
    disp(['Unusual Behaviours: prorated score for limited speech'])
    UB_idx = [2 13 22 24 25 27 29 38 40 46 48 49 51 54 62 63 65 67]; 
    for i = 1:1:size(UB_idx,2)
        UB_tot = [UB_tot; str2num(ASRS_part(UB_idx(i),2))];
    end    
    
    if any(UB_tot(:) == 5) 
             disp(['Unusual Behaviours: too much omitted responses'...
                    ' (n = ' num2str(size(idx,1)) ')'... 
                    ' - Threshold = 0 / Prorated from limited speech'])
     else
        UB_sumLim = sum(UB_tot);
        for p = 1:1:size(Conv_lim,1) %Possibilities for conversions
            raw_pro = Conv_lim(p,1);
            try UB_sumLim;
                switch UB_sumLim
                    case raw_pro
                        UB_sum = Conv_lim(p,3); %Second column = UB
                end
            catch
                 disp('Unusual Behaviours: unable to compute T-score/too much omitted responses')
                 break
            end
        end
    end
end

%Self Regulation
SR_tot = []; i = []; SR_sum = []; 
SR_idx =  [1 5:7 16 18 30 34:36 44 52 57 58 60 66 71]; 
if language == 0
    for i = 1:1:size(SR_idx,2)
        SR_tot = [SR_tot; str2num(ASRS_part(SR_idx(i),2))];
    end

    if any(SR_tot(:) == 5) %at least one omitted response
        idx = []; idx = find(SR_tot(:) == 5);
        switch size(idx,1)
            case num2cell(1:2)
                SR_tot_om = []; SR_tot_om = SR_tot; SR_tot_om(idx,:) = [];
                raw = []; raw = sum(SR_tot_om); nb_scale = []; nb_scale = size(SR_idx,2);
                nb_res = []; nb_res = nb_scale - size(idx,1);
                SR_sum = round((raw*nb_scale)/nb_res);
                disp(['Self Regulation: ' num2str(size(idx,1))... 
                    ' omitted response - Ok to compute raw score'])
            otherwise 
                disp(['Self Regulation: too much omitted responses'...
                    ' (n = ' num2str(size(idx,1)) ')'... 
                    ' - Threshold = 2'])
        end

    else
        SR_sum = sum(SR_tot);
        disp(['Self Regulation: no omitted response'])
    end
else
    disp(['Self Regulation: prorated score for limited speech'])
    SR_idx = [1 5:7 16 18 30 34:36 44 52 57 60 66 71]; 
    for i = 1:1:size(SR_idx,2)
        SR_tot = [SR_tot; str2num(ASRS_part(SR_idx(i),2))];
    end    
    
    if any(SR_tot(:) == 5) 
             disp(['Self Regulation: too much omitted responses'...
                    ' (n = ' num2str(size(idx,1)) ')'... 
                    ' - Threshold = 0 / Prorated from limited speech'])
     else
        SR_sumLim = sum(SR_tot);
        for p = 1:1:size(Conv_lim,1) %Possibilities for conversions
            raw_pro = Conv_lim(p,1);
            try SR_sumLim;
                switch SR_sumLim
                    case raw_pro
                        SR_sum = Conv_lim(p,4); %Second column = SR
                end
            catch
                 disp('Self Regulation: unable to compute T-score/too much omitted responses')
                 break
            end
        end
    end
end

%DSM
DSM_tot = []; i = []; DSM_sum = []; 
if language == 0
    DSM_idx =  [8 9 11 13 15 19:21 23 24 26 28 31:33 37 39 42 43 46 48:51 53:56 ...
        61 63 65 67 69 70]; 
    for i = 1:1:size(DSM_idx,2)
        DSM_tot = [DSM_tot; str2num(ASRS_part(DSM_idx(i),2))];
    end

    if any(DSM_tot(:) == 5) %at least one omitted response
        idx = []; idx = find(DSM_tot(:) == 5);
        switch size(idx,1)
            case num2cell(1:4)
                DSM_tot_om = []; DSM_tot_om = DSM_tot; DSM_tot_om(idx,:) = [];
                raw = []; raw = sum(DSM_tot_om); nb_scale = []; nb_scale = size(DSM_idx,2);
                nb_res = []; nb_res = nb_scale - size(idx,1);
                DSM_sum = round((raw*nb_scale)/nb_res);
                disp(['DSM-5: ' num2str(size(idx,1))... 
                    ' omitted response - Ok to compute raw score'])
            otherwise 
                disp(['DSM-5: too much omitted responses'...
                    ' (n = ' num2str(size(idx,1)) ')'... 
                    ' - Threshold = 4'])
        end

    else
        DSM_sum = sum(DSM_tot);
        disp(['DSM-5: no omitted response'])
    end
else
    disp(['DSM-5: prorated score for limited speech'])
    DSM_idx =  [8 11 13 15 19 23 24 28 31:33 39 42 43 46 48 49 51 53:55 ...
        61 63 65 67 69 70];  
    for i = 1:1:size(DSM_idx,2)
        DSM_tot = [DSM_tot; str2num(ASRS_part(DSM_idx(i),2))];
    end    
    
    if any(DSM_tot(:) == 5) 
             disp(['DSM-5: too much omitted responses'...
                    ' (n = ' num2str(size(idx,1)) ')'... 
                    ' - Threshold = 0 / Prorated from limited speech'])
     else
        DSM_sumLim = sum(DSM_tot);
        for p = 1:1:size(Conv_lim,1) %Possibilities for conversions
            raw_pro = Conv_lim(p,1);
            try DSM_sumLim;
                switch DSM_sumLim
                    case raw_pro
                        DSM_sum = Conv_lim(p,5); %Second column = DSM
                end
            catch
                 disp('DSM-5: unable to compute T-score/too much omitted responses')
                 break
            end
        end
    end
end

%Peer Socialization
PS_tot = []; i = []; PS_sum = []; 
if language == 0
    PS_idx =  [3 14 19 31 45 50 64 69 70]; 
    for i = 1:1:size(PS_idx,2)
        PS_tot = [PS_tot; str2num(ASRS_part(PS_idx(i),2))];
    end

    if any(PS_tot(:) == 5) %at least one omitted response
        idx = []; idx = find(PS_tot(:) == 5);
        switch size(idx,1)
            case 1
                PS_tot_om = []; PS_tot_om = PS_tot; PS_tot_om(idx,:) = [];
                raw = []; raw = sum(PS_tot_om); nb_scale = []; nb_scale = size(PS_idx,2);
                nb_res = []; nb_res = nb_scale - size(idx,1);
                PS_sum = round((raw*nb_scale)/nb_res);
                disp(['Peer Socialization: ' num2str(size(idx,1))... 
                    ' omitted response - Ok to compute raw score'])
            otherwise 
                disp(['Peer Socialization: too much omitted responses'...
                    ' (n = ' num2str(size(idx,1)) ')'... 
                    ' - Threshold = 1'])
        end

    else
        PS_sum = sum(PS_tot);
        disp(['Peer Socialization: no omitted response'])
    end
else
    disp(['Peer Socialization: prorated score for limited speech'])
    PS_idx =  [3 19 31 45 64 69 70];  
    for i = 1:1:size(PS_idx,2)
        PS_tot = [PS_tot; str2num(ASRS_part(PS_idx(i),2))];
    end    
    
    if any(PS_tot(:) == 5) 
             disp(['Peer Socialization: too much omitted responses'...
                    ' (n = ' num2str(size(idx,1)) ')'... 
                    ' - Threshold = 0 / Prorated from limited speech'])
     else
        PS_sumLim = sum(PS_tot);
        for p = 1:1:size(Conv_lim,1) %Possibilities for conversions
            raw_pro = Conv_lim(p,1);
            try PS_sumLim;
                switch PS_sumLim
                    case raw_pro
                        PS_sum = Conv_lim(p,6); %Second column = PS
                end
            catch
                 disp('Peer Socialization: unable to compute T-score/too much omitted responses')
                 break
            end
        end
    end
end

%Adult Socialization
AS_tot = []; i = []; AS_sum = []; 
if language == 0
    AS_idx =  [18 33 34 37 59 66]; 
    for i = 1:1:size(AS_idx,2)
        AS_tot = [AS_tot; str2num(ASRS_part(AS_idx(i),2))];
    end
    if any(AS_tot(:) == 5) %at least one omitted response
        idx = []; idx = find(AS_tot(:) == 5);
        switch size(idx,1)
            case 1
                AS_tot_om = []; AS_tot_om = AS_tot; AS_tot_om(idx,:) = [];
                raw = []; raw = sum(AS_tot_om); nb_scale = []; nb_scale = size(AS_idx,2);
                nb_res = []; nb_res = nb_scale - size(idx,1);
                AS_sum = round((raw*nb_scale)/nb_res);
                disp(['Adult Socialization: ' num2str(size(idx,1))... 
                    ' omitted response - Ok to compute raw score'])
            otherwise 
                disp(['Adult Socialization: too much omitted responses'...
                    ' (n = ' num2str(size(idx,1)) ')'... 
                    ' - Threshold = 1'])
        end

    else
        AS_sum = sum(AS_tot);
        disp(['Adult Socialization: no omitted response'])
    end
else
    disp(['Adult Socialization: prorated score for limited speech'])
    AS_idx =  [18 33 34 66];   
    for i = 1:1:size(AS_idx,2)
        AS_tot = [AS_tot; str2num(ASRS_part(AS_idx(i),2))];
    end    
    
    if any(AS_tot(:) == 5) 
             disp(['Adult Socialization: too much omitted responses'...
                    ' (n = ' num2str(size(idx,1)) ')'... 
                    ' - Threshold = 0 / Prorated from limited speech'])
     else
        AS_sumLim = sum(AS_tot);
        for p = 1:1:size(Conv_lim,1) %Possibilities for conversions
            raw_pro = Conv_lim(p,1);
            try AS_sumLim;
                switch AS_sumLim
                    case raw_pro
                        AS_sum = Conv_lim(p,7); %Second column = AS
                end
            catch
                 disp('Adult Socialization: unable to compute T-score/too much omitted responses')
                 break
            end
        end
    end
end
    
%Social/Emotional Reprocitivity
SER_tot = []; i = []; SER_sum = []; 
if language == 0
    SER_idx =  [4 8 9 11 15 28 32 39 41:43 55 61]; 
    for i = 1:1:size(SER_idx,2)
        SER_tot = [SER_tot; str2num(ASRS_part(SER_idx(i),2))];
    end

    if any(SER_tot(:) == 5) %at least one omitted response
        idx = []; idx = find(SER_tot(:) == 5);
        switch size(idx,1)
            case 1
                SER_tot_om = []; SER_tot_om = SER_tot; SER_tot_om(idx,:) = [];
                raw = []; raw = sum(SER_tot_om); nb_scale = []; nb_scale = size(SER_idx,2);
                nb_res = []; nb_res = nb_scale - size(idx,1);
                SER_sum = round((raw*nb_scale)/nb_res);
                disp(['Social/Emotional Reprocitivity: ' num2str(size(idx,1))... 
                    ' omitted response - Ok to compute raw score'])
            otherwise 
                disp(['Social/Emotional Reprocitivity: too much omitted responses'...
                    ' (n = ' num2str(size(idx,1)) ')'... 
                    ' - Threshold = 1'])
        end

    else
        SER_sum = sum(SER_tot);
        disp(['Social/Emotional Reprocitivity: no omitted response'])
    end
else
    disp(['Social/Emotional Reprocitivity: prorated score for limited speech'])
    SER_idx =  [4 8 11 15 28 32 39 41:43 55 61]; 
    for i = 1:1:size(SER_idx,2)
        SER_tot = [SER_tot; str2num(ASRS_part(SER_idx(i),2))];
    end    
    
    if any(SER_tot(:) == 5) 
             disp(['Social/Emotional Reprocitivity: too much omitted responses'...
                    ' (n = ' num2str(size(idx,1)) ')'... 
                    ' - Threshold = 0 / Prorated from limited speech'])
     else
        SER_sumLim = sum(SER_tot);
        for p = 1:1:size(Conv_lim,1) %Possibilities for conversions
            raw_pro = Conv_lim(p,1);
            try SER_sumLim;
                switch SER_sumLim
                    case raw_pro
                        SER_sum = Conv_lim(p,7); %Second column = SER
                end
            catch
                 disp('Social/Emotional Reprocitivity: unable to compute T-score/too much omitted responses')
                 break
            end
        end
    end
end

%Atypical Language 
AL_tot = []; i = []; AL_sum = []; 
if language == 0
    AL_idx =  [17 20 21 26 58 68]; 
    for i = 1:1:size(AL_idx,2)
        AL_tot = [AL_tot; str2num(ASRS_part(AL_idx(i),2))];
    end

    if any(AL_tot(:) == 5) %at least one omitted response
        idx = []; idx = find(AL_tot(:) == 5);
        switch size(idx,1)
            case num2cell(1:2)
                AL_tot_om = []; AL_tot_om = AL_tot; AL_tot_om(idx,:) = [];
                raw = []; raw = sum(AL_tot_om); nb_scale = []; nb_scale = size(AL_idx,2);
                nb_res = []; nb_res = nb_scale - size(idx,1);
                AL_sum = round((raw*nb_scale)/nb_res);
                disp(['Atypical Language: ' num2str(size(idx,1))... 
                    ' omitted response - Ok to compute raw score'])
            otherwise 
                disp(['Atypical Language: too much omitted responses'...
                    ' (n = ' num2str(size(idx,1)) ')'... 
                    ' - Threshold = 2'])
        end

    else
        AL_sum = sum(AL_tot);
        disp(['Atypical Language: no omitted response'])
    end
else 
    disp(['Atypical Language: speech too limited to quantify'])
end

%Stereotypy
ST_tot = []; i = []; ST_sum = []; 
ST_idx =  [46 48 53 54 67]; 
for i = 1:1:size(ST_idx,2)
    ST_tot = [ST_tot; str2num(ASRS_part(ST_idx(i),2))];
end

if any(ST_tot(:) == 5) %at least one omitted response
    idx = []; idx = find(ST_tot(:) == 5);
    switch size(idx,1)
        case 1
            ST_tot_om = []; ST_tot_om = ST_tot; ST_tot_om(idx,:) = [];
            raw = []; raw = sum(ST_tot_om); nb_scale = []; nb_scale = size(ST_idx,2);
            nb_res = []; nb_res = nb_scale - size(idx,1);
            ST_sum = round((raw*nb_scale)/nb_res);
            disp(['Stereotypy: ' num2str(size(idx,1))... 
                ' omitted response - Ok to compute raw score'])
        otherwise 
            disp(['Stereotypy: too much omitted responses'...
                ' (n = ' num2str(size(idx,1)) ')'... 
                ' - Threshold = 1'])
    end
            
else
    ST_sum = sum(ST_tot);
    disp(['Stereotypy: no omitted response'])
end

%Behavioural Rigidity
BR_tot = []; i = []; BR_sum = []; 
BR_idx =  [13 22 24 40 49 51 63 65]; 
for i = 1:1:size(BR_idx,2)
    BR_tot = [BR_tot; str2num(ASRS_part(BR_idx(i),2))];
end

if any(BR_tot(:) == 5) %at least one omitted response
    idx = []; idx = find(BR_tot(:) == 5);
    switch size(idx,1)
        case 1
            BR_tot_om = []; BR_tot_om = BR_tot; BR_tot_om(idx,:) = [];
            raw = []; raw = sum(BR_tot_om); nb_scale = []; nb_scale = size(BR_idx,2);
            nb_res = []; nb_res = nb_scale - size(idx,1);
            BR_sum = round((raw*nb_scale)/nb_res);
            disp(['Behavioural Rigidity: ' num2str(size(idx,1))... 
                ' omitted response - Ok to compute raw score'])
        otherwise 
            disp(['Behavioural Rigidity: too much omitted responses'...
                ' (n = ' num2str(size(idx,1)) ')'... 
                ' - Threshold = 1'])
    end
            
else
    BR_sum = sum(BR_tot);
    disp(['Behavioural Rigidity: no omitted response'])
end

%Sensory Sensitivity 
SS_tot = []; i = []; SS_sum = []; 
SS_idx =  [2 25 27 29 38 62]; 
for i = 1:1:size(SS_idx,2)
    SS_tot = [SS_tot; str2num(ASRS_part(SS_idx(i),2))];
end

if any(SS_tot(:) == 5) %at least one omitted response
    idx = []; idx = find(SS_tot(:) == 5);
    switch size(idx,1)
        case 1
            SS_tot_om = []; SS_tot_om = SS_tot; SS_tot_om(idx,:) = [];
            raw = []; raw = sum(SS_tot_om); nb_scale = []; nb_scale = size(SS_idx,2);
            nb_res = []; nb_res = nb_scale - size(idx,1);
            SS_sum = round((raw*nb_scale)/nb_res);
            disp(['Sensory Sensitivity: ' num2str(size(idx,1))... 
                ' omitted response - Ok to compute raw score'])
        otherwise 
            disp(['Sensory Sensitivity: too much omitted responses'...
                ' (n = ' num2str(size(idx,1)) ')'... 
                ' - Threshold = 1'])
    end
            
else
    SS_sum = sum(SS_tot);
    disp(['Sensory Sensitivity: no omitted response'])
end

%Attention
AT_tot = []; i = []; AT_sum = []; 
AT_idx =  [1 5 10 16 30 35 36 44 47 52 57]; 
for i = 1:1:size(AT_idx,2)
    AT_tot = [AT_tot; str2num(ASRS_part(AT_idx(i),2))];
end

if any(AT_tot(:) == 5) %at least one omitted response
    idx = []; idx = find(AT_tot(:) == 5);
    switch size(idx,1)
        case 1
            AT_tot_om = []; AT_tot_om = AT_tot; AT_tot_om(idx,:) = [];
            raw = []; raw = sum(AT_tot_om); nb_scale = []; nb_scale = size(AT_idx,2);
            nb_res = []; nb_res = nb_scale - size(idx,1);
            AT_sum = round((raw*nb_scale)/nb_res);
            disp(['Attention: ' num2str(size(idx,1))... 
                ' omitted response - Ok to compute raw score'])
        otherwise 
            disp(['Attention: too much omitted responses'...
                ' (n = ' num2str(size(idx,1)) ')'... 
                ' - Threshold = 1'])
    end
            
else
    AT_sum = sum(AT_tot);
    disp(['Attention: no omitted response'])
end
%% FOR EACH SCALE : adapt to participant age and omitted responses
%% SC conversion 6-11 years 
SC_conv_611 = [];
SC_conv_611 = [99,85,64,76, "Very Elevated";
   99,84,62,63, "Very Elevated";   99,83,60,61,"Very Elevated";
   99,82,58,59, "Very Elevated";   99,81,56,57, "Very Elevated";
   99,80,54,55, "Very Elevated";   99,79,52,53, "Very Elevated";
   99,78,50,51, "Very Elevated";   99,77,48,49, "Very Elevated";
   99,76,46,47, "Very Elevated";   99,75,45,45, "Very Elevated";
   99,74,44,44, "Very Elevated";   99,73,42,43, "Very Elevated";
   99,72,41,41, "Very Elevated";   98,71,39,40, "Very Elevated";
   98,70,38,38, "Very Elevated";   97,69,37,37, "Elevated";
   97,69,37,37, "Elevated";   96,68,35,36, "Elevated";
   96,67,34,34, "Elevated";   95,66,33,33, "Elevated";
   93,65,32,32, "Elevated";   92,64,31,31, "Slightly Elevated";
   90,63,29,30, "Slightly Elevated";   88,62,28,28, "Slightly Elevated";
   86,61,27,27, "Slightly Elevated";   84,60,26,26, "Slightly Elevated";
   82,59,25,25, "Average";   79,58,24,24, "Average";
   76,57,23,23, "Average";   73,56,22,22, "Average";
   69,55,21,21, "Average";   66,54,20,20, "Average";
   62,53,19,19, "Average";   58,52,18,18, "Average";
   54,51,17,17, "Average";   50,50,16,16, "Average";
   46,49,15,15, "Average";   42,48,14,14, "Average";
   38,47,13,13, "Average";   34,46,12,12, "Average";
   31,45,11,11, "Average";   27,44,10,10, "Average";
   24,43,9,9, "Average";   21,42,8,8, "Average";
   18,41,7,7, "Average";   16,40,6,6, "Average";
   14,39,5,5, "Low";   12,38,4,4, "Low";
   8,36,3,3, "Low";   7,35,2,2, "Low";
   5,34,1,1, "Low";   4,33,0,0, "Low"]; 
%% UB conversion 6-11 years 
UB_conv_611 = [];
UB_conv_611 = [99,83,96,96, "Very Elevated";    99,82,94,95, "Very Elevated";
    99,81,92,93, "Very Elevated";    99,80,90,91, "Very Elevated";
    99,79,88,89, "Very Elevated";    99,78,86,87, "Very Elevated";
    99,77,84,85, "Very Elevated";    99,76,81,83, "Very Elevated";
    99,75,77,80, "Very Elevated";    99,74,72,76, "Very Elevated";
    99,73,66,71, "Very Elevated";    99,72,61,65, "Very Elevated";
    98,71,58,60, "Very Elevated";    98,70,55,57, "Very Elevated";
    97,69,52,54, "Elevated";    96,68,48,51, "Elevated";
    96,67,46,47, "Elevated";    95,66,44,45, "Elevated";
    93,65,42,43, "Elevated";    92,64,40,41, "Slightly Elevated";
    90,63,38,39, "Slightly Elevated";    88,62,36,37, "Slightly Elevated";
    86,61,34,35, "Slightly Elevated";    84,60,32,33, "Slightly Elevated";
    82,59,30,31, "Average";    79,58,27,29, "Average";
    76,57,25,26, "Average";    73,56,24,24, "Average";
    69,55,22,23, "Average";    66,54,21,21, "Average";
    62,53,20,20, "Average";    58,52,18,19, "Average";
    54,51,17,17, "Average";    50,50,16,16, "Average";
    46,49,15,15, "Average";    42,48,14,14, "Average";
    38,47,13,13, "Average";    34,46,12,12, "Average";
    31,45,11,11, "Average";    27,44,10,10, "Average";
    24,43,9,9, "Average";   21,42,8,8, "Average";
    18,41,7,7, "Average";   16,40,6,6, "Average";
    14,39,4,5, "Low";   12,38,3,3, "Low";
    10,37,2,2, "Low";   7,35,1,1, "Low";
    4,33,0,0, "Low"];
%% SR conversion 6-11 years 
SR_conv_611 = [];
SR_conv_611 = [99,82,67,68, "Very Elevated";
    99,81,65,66, "Very Elevated";    99,80,64,64, "Very Elevated";
    99,79,63,63, "Very Elevated";    99,78,61,62, "Very Elevated";
    99,77,59,60, "Very Elevated";    99,76,57,58, "Very Elevated";
    99,75,56,56, "Very Elevated";    99,74,55,55, "Very Elevated";
    99,73,54,54, "Very Elevated";    99,72,53,53, "Very Elevated";
    98,71,52,52, "Very Elevated";    98,70,50,51, "Very Elevated";    
    97,69,49,49, "Elevated";    96,68,47,48, "Elevated";
    96,67,46,46, "Elevated";    95,66,45,45, "Elevated";
    93,65,44,44, "Elevated";    92,64,41,43, "Slightly Elevated";    
    90,63,40,40, "Slightly Elevated";    88,62,37,39, "Slightly Elevated";
    86,61,35,36, "Slightly Elevated";    84,60,33,34, "Slightly Elevated";    
    82,59,32,32, "Average";    79,58,30,31, "Average";
    76,57,29,29, "Average";    73,56,28,28, "Average";
    69,55,27,27, "Average";    66,54,26,26, "Average";
    62,53,24,25, "Average";    58,52,23,23, "Average";
    54,51,22,22, "Average";    50,50,21,21, "Average";
    46,49,20,20, "Average";    42,48,19,19, "Average";
    38,47,18,18, "Average";    34,46,17,17, "Average";
    31,45,16,16, "Average";    27,44,15,15, "Average";
    24,43,14,14, "Average";    21,42,13,13, "Average";
    18,41,12,12, "Average";   14,39,11,11, "Low";   
    12,38,10,10, "Low";   8,36,9,9, "Low";
    7,35,8,8, "Low";    4,33,7,7, "Low";
    4,32,6,6, "Low";    3,31,5,5, "Low";
    2,30,4,4, "Low";    1,28,3,3, "Low";
    1,27,2,2, "Low";    1,26,1,1, "Low";
    1,25,0,0, "Low"];
%% TOT conversion 6-11 years 
TOT_conv_611 = [];
TOT_conv_611 = [99,85,239,250, "Very Elevated"; 99,84,236,238, "Very Elevated"; 
    99,83,233,235,"Very Elevated";     99,82,230,232, "Very Elevated";
    99,81,227,229, "Very Elevated";    99,80,224,226, "Very Elevated";
    99,79,221,223, "Very Elevated";    99,78,218,220, "Very Elevated";
    99,77,215,217, "Very Elevated";    99,76,213,214, "Very Elevated";
    99,75,211,212, "Very Elevated";    99,74,209,210, "Very Elevated";
    99,73,207,208, "Very Elevated";    99,72,205,206, "Very Elevated";
    98,71,203,204, "Very Elevated";    98,70,201,202, "Very Elevated";    
    97,69,199,200, "Elevated";    96,68,198,198, "Elevated";
    96,67,195,197, "Elevated";    95,66,192,194, "Elevated";
    93,65,189,191, "Elevated";    92,64,187,188, "Slightly Elevated";    
    90,63,185,186, "Slightly Elevated";    88,62,182,184, "Slightly Elevated";
    86,61,179,181, "Slightly Elevated";    84,60,175,178, "Slightly Elevated";    
    82,59,172,174, "Average";    79,58,169,171, "Average";
    76,57,167,168, "Average";    73,56,165,166, "Average";
    69,55,162,164, "Average";    66,54,158,161, "Average";
    62,53,155,157, "Average";    58,52,153,154, "Average";
    54,51,150,152, "Average";    50,50,148,149, "Average";
    46,49,145,147, "Average";    42,48,142,144, "Average";
    38,47,139,141, "Average";    34,46,137,138, "Average";
    31,45,134,136, "Average";    27,44,131,133, "Average";
    24,43,129,130, "Average";    21,42,127,128, "Average";
    18,41,125,126, "Average";    16,40,123,124, "Average";
    14,39,121,122, "Low";   12,38,119,120, "Low";   
    10,37,116,118, "Low";   8,36,113,115, "Low";    
    7,35,110,112, "Low";    5,34,107,109, "Low";   
    4,33,105,106, "Low";    4,32,104,104, "Low";    
    3,31,103,103, "Low";    2,30,101,102, "Low";  
    2,29,100,100, "Low";    1,28,98,99, "Low";    
    1,27,96,97, "Low";      1,26,94,95, "Low";    
    1,25,91,93, "Low"];
%% DSM conversion 6-11 years 
DSM_conv_611 = [];
DSM_conv_611 = [99,85,126,160, "Very Elevated"; 99,84,124,125, "Very Elevated"; 
    99,83,122,123,"Very Elevated";     99,82,120,121, "Very Elevated";
    99,81,118,119, "Very Elevated";    99,80,115,117, "Very Elevated";
    99,79,112,114, "Very Elevated";    99,78,109,111, "Very Elevated";
    99,77,106,108, "Very Elevated";    99,76,103,105, "Very Elevated";
    99,75,100,102, "Very Elevated";    99,74,97,99, "Very Elevated";
    99,73,94,96, "Very Elevated";    99,72,91,93, "Very Elevated";
    98,71,88,90, "Very Elevated";    98,70,85,87, "Very Elevated";    
    97,69,82,84, "Elevated";    96,68,79,81, "Elevated";
    96,67,76,78, "Elevated";    95,66,73,75, "Elevated";
    93,65,70,72, "Elevated";    92,64,67,69, "Slightly Elevated";    
    90,63,64,66, "Slightly Elevated";    88,62,60,63, "Slightly Elevated";
    86,61,56,59, "Slightly Elevated";    84,60,52,55, "Slightly Elevated";    
    82,59,49,51, "Average";    79,58,46,48, "Average";
    76,57,43,45, "Average";    73,56,40,42, "Average";
    69,55,37,39, "Average";    66,54,35,36, "Average";
    62,53,33,34, "Average";    58,52,31,32, "Average";
    54,51,30,30, "Average";    50,50,28,29, "Average";
    46,49,26,27, "Average";    42,48,24,25, "Average";
    38,47,22,23, "Average";    34,46,20,21, "Average";
    31,45,18,19, "Average";    27,44,16,17, "Average";
    24,43,14,15, "Average";    21,42,13,13, "Average";
    18,41,11,12, "Average";    16,40,10,10, "Average";
    14,39,9,9, "Low";   12,38,8,8, "Low";   
    10,37,7,7, "Low";   8,36,6,6, "Low";    
    7,35,5,5, "Low";    5,34,4,4, "Low";   
    4,33,3,3, "Low";    4,32,2,2, "Low";    
    3,31,1,1, "Low";    2,30,0,0, "Low"];
%% PS conversion 6-11 years 
PS_conv_611 = [];
PS_conv_611 = [99,85,36,36, "Very Elevated"; 99,84,35,35, "Very Elevated"; 
    99,83,34,34,"Very Elevated";     99,82,33,33, "Very Elevated";
    99,81,32,32, "Very Elevated";    99,80,31,31, "Very Elevated";
    99,79,30,30, "Very Elevated";    99,78,29,29, "Very Elevated";
    99,77,28,28, "Very Elevated";    99,76,27,27, "Very Elevated";
    99,75,25,26, "Very Elevated";    99,74,24,24, "Very Elevated";
    99,73,23,23, "Very Elevated";    99,72,22,22, "Very Elevated";
    98,71,21,21, "Very Elevated";    98,70,20,20, "Very Elevated";    
    97,69,19,19, "Elevated";    96,68,18,18, "Elevated";
    96,67,17,17, "Elevated";    95,66,16,16, "Elevated";
    93,65,15,15, "Elevated";    90,63,14,14, "Slightly Elevated";    
    86,61,13,13, "Slightly Elevated";       
    82,59,12,12, "Average";    79,58,11,11, "Average";
    73,56,10,10, "Average";    66,54,9,9, "Average";    
    54,51,8,8, "Average";     46,49,7,7, "Average";
    38,47,6,6, "Average";    31,45,5,5, "Average"; 
    24,43,4,4, "Average";    16,40,3,3, "Average";
    12,38,2,2, "Low";    8,36,1,1, "Low";    
    5,34,0,0, "Low"];

%% AS conversion 6-11 years 
AS_conv_611 = [];
AS_conv_611 = [99,85,24,24, "Very Elevated"; 99,84,23,23, "Very Elevated"; 
    99,83,22,22,"Very Elevated";     99,82,21,21, "Very Elevated";
    99,80,20,20, "Very Elevated";    99,78,19,19, "Very Elevated";
    99,76,18,18, "Very Elevated";    99,74,17,17, "Very Elevated";
    99,72,16,16, "Very Elevated";    98,70,15,15, "Very Elevated";    
    96,68,14,14, "Elevated";    95,66,13,13, "Elevated";
    92,64,12,12, "Slightly Elevated";    88,62,11,11, "Slightly Elevated";
    84,60,10,10, "Slightly Elevated";    79,58,9,9, "Average";   
    73,56,8,8, "Average";    66,54,7,7, "Average";
    58,52,6,6, "Average";    46,49,5,5, "Average";
    34,46,4,4, "Average";    24,43,3,3, "Average";
    12,38,2,2, "Low";    8,36,1,1, "Low";    
    5,34,0,0, "Low";];
%% SER conversion 6-11 years 
SER_conv_611 = [];
SER_conv_611 = [99,85,45,52, "Very Elevated"; 
    99,83,44,44,"Very Elevated";     99,82,43,43, "Very Elevated";
    99,81,42,42, "Very Elevated";    99,80,40,41, "Very Elevated";
    99,79,38,39, "Very Elevated";    99,78,37,37, "Very Elevated";
    99,77,36,36, "Very Elevated";    99,76,35,35, "Very Elevated";
    99,75,34,34, "Very Elevated";    
    99,73,33,33, "Very Elevated";    99,72,32,32, "Very Elevated";
    98,71,31,31, "Very Elevated";    98,70,30,30, "Very Elevated";    
    97,69,29,29, "Elevated";    96,68,28,28, "Elevated";
    96,67,27,27, "Elevated";    95,66,26,26, "Elevated";
    93,65,25,25, "Elevated";    92,64,24,24, "Slightly Elevated";    
    90,63,23,23, "Slightly Elevated";    88,62,22,22, "Slightly Elevated";
    86,61,21,21, "Slightly Elevated";    84,60,20,20, "Slightly Elevated";    
    82,59,19,19, "Average";    79,58,18,18, "Average";
    76,57,17,17, "Average";    73,56,16,16, "Average";
    69,55,15,15, "Average";    66,54,14,14, "Average";
    62,53,13,13, "Average";    54,51,12,12, "Average";    
    50,50,11,11, "Average";    42,48,10,10, "Average";
    34,46,9,9, "Average";    27,44,8,8, "Average";
    21,42,7,7, "Average";    16,40,6,6, "Average";
    12,38,5,5, "Low";    8,36,4,4, "Low";    
    5,34,3,3, "Low";    4,32,2,2, "Low";    
    2,30,1,1, "Low";    1,28,0,0, "Low"];
%% AL conversion 6-11 years 
AL_conv_611 = [];
AL_conv_611 = [99,82,24,24, "Very Elevated";
    99,81,23,23, "Very Elevated";    99,80,22,22, "Very Elevated";
    99,78,21,21, "Very Elevated";    99,76,20,20, "Very Elevated";
    99,75,19,19, "Very Elevated";    99,74,18,18, "Very Elevated";
    99,73,17,17, "Very Elevated";    99,72,16,16, "Very Elevated";
    98,71,15,15, "Very Elevated";    98,70,14,14, "Very Elevated";    
    97,69,13,13, "Elevated";    96,68,12,12, "Elevated";
    95,66,11,11, "Elevated";    92,64,10,10, "Slightly Elevated";    
    88,62,9,9, "Slightly Elevated";    84,60,8,8, "Slightly Elevated";    
    79,58,7,7, "Average";    73,56,6,6, "Average";
    66,54,5,5, "Average";    58,52,4,4, "Average";
    42,48,3,3, "Average";    27,44,2,2, "Average";
    16,40,1,1, "Average";    8,37,0,0, "Low"];
%% ST conversion 6-11 years 
ST_conv_611 = [];
ST_conv_611 = [99,82,20,20, "Very Elevated"; 99,80,19,19, "Very Elevated";
    99,78,18,18, "Very Elevated";    99,76,17,17, "Very Elevated";
    99,74,16,16, "Very Elevated";    99,72,15,15, "Very Elevated";
    98,70,14,14, "Very Elevated";    96,68,13,13, "Elevated";
    95,66,12,12, "Elevated";    92,64,11,11, "Slightly Elevated";    
    88,62,10,10, "Slightly Elevated";    84,60,9,9, "Slightly Elevated";    
    79,58,8,8, "Average";    73,56,7,7, "Average";
    66,54,6,6, "Average";    58,52,5,5, "Average";
    46,49,4,4, "Average";    38,47,3,3, "Average";
    31,45,2,2, "Average";    16,40,1,1, "Average";
    10,37,0,0, "Low"];
%% BR conversion 6-11 years 
BR_conv_611 = [];
BR_conv_611 = [99,81,32,32, "Very Elevated";    99,80,31,31, "Very Elevated";
    99,79,30,30, "Very Elevated";    99,78,29,29, "Very Elevated";
    99,76,28,28, "Very Elevated";    99,75,27,27, "Very Elevated";    
    99,74,26,26, "Very Elevated";    99,73,25,25, "Very Elevated";    
    99,72,24,24, "Very Elevated";    98,71,23,23, "Very Elevated";    
    98,70,22,22, "Very Elevated";    97,69,21,21, "Elevated";    
    96,68,20,20, "Elevated";    96,67,19,19, "Elevated";    
    95,66,18,18, "Elevated";    93,65,17,17, "Elevated";    
    92,64,16,16, "Slightly Elevated";    88,62,15,15, "Slightly Elevated";
    86,61,14,14, "Slightly Elevated";    82,59,13,13, "Average"; 
    76,57,12,12, "Average";    69,55,11,11, "Average";
    62,53,10,10, "Average";    58,52,9,9, "Average";
    50,50,8,8, "Average";    46,49,7,7, "Average";
    38,47,6,6, "Average";    31,45,5,5, "Average";   
    27,44,4,4, "Average";    21,42,3,3, "Average";
    16,40,2,2, "Average";    14,39,1,1, "Low"; 
    8,36,0,0, "Low"];
%% SS conversion 6-11 years 
SS_conv_611 = [];
SS_conv_611 = [99,85,22,24, "Very Elevated"; 99,84,21,21, "Very Elevated"; 
    99,83,20,20,"Very Elevated";     99,82,19,19, "Very Elevated";
    99,81,18,18, "Very Elevated";    99,80,17,17, "Very Elevated";
    99,79,16,16, "Very Elevated";    99,78,15,15, "Very Elevated";
    99,77,14,14, "Very Elevated";    99,75,13,13, "Very Elevated";
    99,73,12,12, "Very Elevated";    98,71,11,11, "Very Elevated";
    97,69,10,10, "Elevated";    96,67,9,9, "Elevated"; 
    92,64,8,8, "Slightly Elevated";    86,61,7,7, "Slightly Elevated";   
    82,59,6,6, "Average";    73,56,5,5, "Average";  
    62,53,4,4, "Average";    50,50,3,3, "Average";
    38,47,2,2, "Average";    27,44,1,1, "Average";
    14,39,0,0, "Low"];
%% AT conversion 6-11 years 
AT_conv_611 = [];
AT_conv_611 = [99,85,44,44, "Very Elevated"; 99,84,43,43, "Very Elevated"; 
    99,83,42,42,"Very Elevated";     99,82,41,41, "Very Elevated";
    99,81,40,40, "Very Elevated";    99,80,39,39, "Very Elevated";
    99,78,38,38, "Very Elevated";    99,76,37,37, "Very Elevated";
    99,74,36,36, "Very Elevated";    99,72,35,35, "Very Elevated";
    98,71,34,34, "Very Elevated";    98,70,33,33, "Very Elevated";    
    97,69,32,32, "Elevated";    96,68,31,31, "Elevated";
    96,67,30,30, "Elevated";    95,66,29,29, "Elevated";
    93,65,28,28, "Elevated";    92,64,27,27, "Slightly Elevated";    
    90,63,25,26, "Slightly Elevated";    88,62,24,24, "Slightly Elevated";
    86,61,23,23, "Slightly Elevated";    84,60,22,22, "Slightly Elevated";    
    82,59,21,21, "Average";    79,58,20,20, "Average";
    76,57,19,19, "Average";    73,56,18,18, "Average";
    69,55,17,17, "Average";    62,53,16,16, "Average";    
    58,52,15,15, "Average";    50,50,14,14, "Average";
    46,49,13,13, "Average";    42,48,12,12, "Average";
    34,46,11,11, "Average";    27,44,10,10, "Average";
    24,43,9,9, "Average";    
    21,42,8,8, "Average";    16,40,7,7, "Average";    
    10,37,6,6, "Low";   8,36,5,5, "Low";    
    5,34,4,4, "Low";    4,32,3,3, "Low";    
    2,29,2,2, "Low";    1,28,1,1, "Low";    
    1,26,0,0, "Low"];
%% 12-18 - years-olds
%% FOR EACH SCALE : adapt to participant age and omitted responses
% SC conversion 12-18 years
SC_conv_1218 = [];
SC_conv_1218 = [99,85,60,76, "Very Elevated";
   99,84,59,59, "Very Elevated";   99,83,58,58,"Very Elevated";
   99,82,57,57, "Very Elevated";   99,81,56,56, "Very Elevated";
   99,80,55,55, "Very Elevated";   99,79,54,54, "Very Elevated";
   99,78,53,53, "Very Elevated";   99,77,52,52, "Very Elevated";
   99,76,51,51, "Very Elevated";   99,75,50,50, "Very Elevated";
   99,74,49,49, "Very Elevated";   99,73,48,48, "Very Elevated";
   99,72,47,47, "Very Elevated";   98,71,46,46, "Very Elevated";
   98,70,44,45, "Very Elevated";   97,69,43,43, "Elevated";
   96,68,41,42, "Elevated";   96,67,40,40, "Elevated";
   95,65,38,39, "Elevated";  
   93,65,36,37, "Elevated";   92,64,34,35, "Slightly Elevated";
   90,63,33,33, "Slightly Elevated";   88,62,31,32, "Slightly Elevated";
   86,61,29,30, "Slightly Elevated";   84,60,28,28, "Slightly Elevated";
   
   82,59,27,27, "Average";   79,58,26,26, "Average";
   76,57,25,25, "Average";   73,56,24,24, "Average";
   69,55,23,23, "Average";   66,54,22,22, "Average";
   62,53,20,21, "Average";   58,52,19,19, "Average";
   54,51,18,18, "Average";   50,50,17,17, "Average";
   46,49,15,16, "Average";   42,48,14,14, "Average";
   38,47,13,13, "Average";   34,46,12,12, "Average";
   31,45,11,11, "Average";   27,44,10,10, "Average";
   24,43,9,9, "Average";   21,42,8,8, "Average";
   18,41,7,7, "Average";   16,40,6,6, "Average";
   
   12,38,5,5, "Low";   10,37,4,4, "Low";
   7,35,3,3, "Low";   5,34,2,2, "Low";
   3,31,1,1, "Low";   2,29,0,0, "Low"]; 
% UB conversion 12-18 years
UB_conv_1218 = [];
UB_conv_1218 = [99,85,76,96, "Very Elevated";    99,82,74,75, "Very Elevated";
    99,83,72,73, "Very Elevated";    99,82,71,71, "Very Elevated";
    99,81,69,70, "Very Elevated";    99,80,67,68, "Very Elevated";
    99,79,65,66, "Very Elevated";    99,78,63,64, "Very Elevated";
    99,77,61,62, "Very Elevated";    99,76,59,60, "Very Elevated";
    99,75,58,58, "Very Elevated";    99,74,57,57, "Very Elevated";
    99,73,55,56, "Very Elevated";    99,72,53,54, "Very Elevated";
    98,71,51,52, "Very Elevated";    98,70,49,50, "Very Elevated";
    
    97,69,47,48, "Elevated";    96,68,45,46, "Elevated";
    96,67,42,44, "Elevated";    95,66,39,41, "Elevated";
    93,65,36,38, "Elevated";    
    
    92,64,33,35, "Slightly Elevated";
    90,63,31,32, "Slightly Elevated";    88,62,29,30, "Slightly Elevated";
    86,61,27,28, "Slightly Elevated";    84,60,25,26, "Slightly Elevated";
    
    82,59,23,24, "Average";    79,58,22,22, "Average";
    76,57,21,21, "Average";    73,56,20,20, "Average";
    69,55,18,19, "Average";    66,54,16,17, "Average";
    62,53,14,15, "Average";    58,52,12,13, "Average";
    54,51,11,11, "Average";    50,50,10,10, "Average";
    46,49,9,9, "Average";    42,48,8,8, "Average";
    34,46,7,7, "Average"; 27,44,6,6, "Average";
    21,42,5,5, "Average"; 16,40,4,4, "Average";
      
    14,39,3,3, "Low";   
    10,37,2,2, "Low";   7,35,1,1, "Low";
    4,33,0,0, "Low"];

% SR conversion 12-18 years
SR_conv_1218 = [];
SR_conv_1218 = [99,85,67,68, "Very Elevated";    99,84,66,66, "Very Elevated";
    99,83,65,65, "Very Elevated";    99,82,64,64, "Very Elevated";
    99,81,63,63, "Very Elevated";    99,80,62,62, "Very Elevated";
    99,79,61,61, "Very Elevated";    99,78,60,60, "Very Elevated";
    99,77,59,59, "Very Elevated";    99,76,58,58, "Very Elevated";
    99,75,57,57, "Very Elevated";    99,74,56,56, "Very Elevated";
    99,73,55,55, "Very Elevated";    99,72,54,54, "Very Elevated";
    98,71,52,53, "Very Elevated";    98,70,50,51, "Very Elevated"; 
    97,69,48,49, "Elevated";    96,68,46,47, "Elevated";
    96,67,44,45, "Elevated";    95,66,42,43, "Elevated";
    93,65,40,41, "Elevated";      
    92,64,39,39, "Slightly Elevated";    
    90,63,38,38, "Slightly Elevated";    88,62,36,37, "Slightly Elevated";
    86,61,34,35, "Slightly Elevated";    84,60,33,33, "Slightly Elevated";
    82,59,32,32, "Average";    79,58,30,31, "Average";
    76,57,29,29, "Average";    73,56,27,28, "Average";
    69,55,25,26, "Average";    66,54,23,24, "Average";
    62,53,22,22, "Average";    58,52,21,21, "Average";
    54,51,20,20, "Average";    50,50,19,19, "Average";
    46,49,18,18, "Average";    42,48,17,17, "Average";
    38,47,16,16, "Average";    34,46,15,15, "Average";
    31,45,14,14, "Average";    27,44,13,13, "Average";
    24,43,12,12, "Average";    21,42,11,11, "Average";
    18,41,10,10, "Average";    16,40,9,9, "Average";   
    14,39,8,8, "Low";   
    10,37,7,7, "Low";   8,36,6,6, "Low";
    5,34,5,5, "Low";    4,33,4,4, "Low"; 
    3,31,3,3, "Low";    2,29,2,2, "Low";
    1,27,1,1, "Low";    1,25,0,0, "Low"];
% TOT conversion 12-18 years
TOT_conv_1218 = [];
TOT_conv_1218 = [99,85,242,255, "Very Elevated"; 99,84,239,241, "Very Elevated"; 
    99,83,236,238,"Very Elevated";     99,82,233,235, "Very Elevated";
    99,81,230,232, "Very Elevated";    99,80,227,229, "Very Elevated";
    99,79,224,226, "Very Elevated";    99,78,221,223, "Very Elevated";
    99,77,218,220, "Very Elevated";    99,76,215,217, "Very Elevated";
    99,75,212,214, "Very Elevated";    99,74,209,211, "Very Elevated";
    99,73,206,208, "Very Elevated";    99,72,203,205, "Very Elevated";
    98,71,200,202, "Very Elevated";    98,70,198,199, "Very Elevated"; 
    
    97,69,196,197, "Elevated";    96,68,194,195, "Elevated";
    96,67,192,193, "Elevated";    95,66,189,191, "Elevated";
    93,65,186,188, "Elevated";    
    
    92,64,184,185, "Slightly Elevated";    
    90,63,182,183, "Slightly Elevated";    88,62,180,181, "Slightly Elevated";
    86,61,177,179, "Slightly Elevated";    84,60,175,175, "Slightly Elevated";    
    
    82,59,173,174, "Average";    79,58,171,172, "Average";
    76,57,169,170, "Average";    73,56,166,168, "Average";
    69,55,163,165, "Average";    66,54,160,162, "Average";
    62,53,157,159, "Average";    58,52,154,156, "Average";
    54,51,151,153, "Average";    50,50,149,150, "Average";
    46,49,146,148, "Average";    42,48,144,145, "Average";
    38,47,141,143, "Average";    34,46,139,140, "Average";
    31,45,136,138, "Average";    27,44,133,135, "Average";
    24,43,130,132, "Average";    21,42,127,129, "Average";
    18,41,124,126, "Average";    16,40,121,123, "Average";
    
    14,39,118,120, "Low";   12,38,116,117, "Low";   
    10,37,113,115, "Low";   8,36,111,112, "Low";    
    7,35,108,110, "Low";    5,34,106,107, "Low";   
    4,33,104,105, "Low";    4,32,102,103, "Low";    
    3,31,100,101, "Low";    2,30,98,99, "Low";  
    2,29,96,97, "Low";    1,28,94,95, "Low";    
    1,27,92,93, "Low";      1,26,90,91, "Low";    
    1,25,87,89, "Low"];
% DSM conversion 12-18 years
DSM_conv_1218 = [];
DSM_conv_1218 = [99,85,108,160, "Very Elevated"; 99,84,105,107, "Very Elevated"; 
    99,83,102,104,"Very Elevated";     99,82,100,101, "Very Elevated";
    99,81,98,99, "Very Elevated";    99,80,96,97, "Very Elevated";
    99,79,94,95, "Very Elevated";    99,78,92,93 "Very Elevated";
    99,77,90,91, "Very Elevated";    99,76,188,89, "Very Elevated";
    99,75,86,87, "Very Elevated";    99,74,84,85, "Very Elevated";
    99,73,82,81, "Very Elevated";    99,72,80,81, "Very Elevated";
    98,71,78,79, "Very Elevated";    98,70,76,77, "Very Elevated";
    97,69,73,75, "Elevated";    96,68,70,72, "Elevated";
    96,67,68,69, "Elevated";    95,66,65,67, "Elevated";
    93,65,62,64, "Elevated";    
    92,64,59,61, "Slightly Elevated";    
    90,63,57,58, "Slightly Elevated";    88,62,54,56, "Slightly Elevated";
    86,61,51,53, "Slightly Elevated";    84,60,48,50, "Slightly Elevated";
    82,59,46,47, "Average";    79,58,44,45, "Average";
    76,57,43,42, "Average";    73,56,39,41, "Average";
    69,55,37,38, "Average";    66,54,34,36, "Average";
    62,53,31,33, "Average";    58,52,28,30, "Average";
    54,51,25,27, "Average";    50,50,22,24, "Average";
    46,49,19,21, "Average";    42,48,17,18, "Average";
    38,47,16,16, "Average";    34,46,15,15, "Average";
    31,45,14,14, "Average";    27,44,13,13, "Average";
    24,43,12,12, "Average";    21,42,11,11, "Average";
    18,41,10,10, "Average";    16,40,9,9, "Average";
    14,39,8,8, "Low";   12,38,7,7, "Low";   
    10,37,6,6, "Low";   8,36,5,5, "Low";    
    7,35,4,4, "Low";    5,34,3,3, "Low";   
    4,33,1,1, "Low";    4,32,0,0, "Low"];
% PS conversion 12-18 years
PS_conv_1218 = [];
PS_conv_1218 = [99,85,32,36, "Very Elevated"; 99,84,31,31, "Very Elevated"; 
    99,83,30,30,"Very Elevated";     99,82,29,29, "Very Elevated";
    99,81,28,28, "Very Elevated";    
    99,79,27,27, "Very Elevated";    99,78,26,26, "Very Elevated";
    99,77,25,25, "Very Elevated";    99,76,24,24, "Very Elevated";
    99,75,23,23, "Very Elevated";    99,74,22,22, "Very Elevated";
    99,73,21,21, "Very Elevated";    
    98,71,20,20, "Very Elevated";   
    
    97,69,19,19, "Elevated";    96,67,18,18, "Elevated";    
    93,65,17,17, "Elevated";    
    
    90,63,16,16, "Slightly Elevated";  88,62,15,15, "Slightly Elevated";  
    86,61,14,14, "Slightly Elevated";    
    
    82,59,13,13, "Average";    79,58,12,12, "Average"; 76,57,11,11, "Average";
    69,55,10,10, "Average";    66,54,9,9, "Average";    
    58,52,8,8, "Average";     50,50,7,7, "Average";
    42,48,6,6, "Average";    34,46,5,5, "Average"; 
    27,44,4,4, "Average";    21,42,3,3, "Average";
    
    12,38,2,2, "Low";    5,34,1,1, "Low";    
    3,31,0,0, "Low"];
% AS conversion 12-18 years
AS_conv_1218 = [];
AS_conv_1218 = [99,81,24,24, "Very Elevated";
    99,80,23,23, "Very Elevated";    99,79,22,22, "Very Elevated";
    99,78,21,21, "Very Elevated";    99,77,20,20, "Very Elevated";
    99,76,19,19, "Very Elevated";    98,74,18,18, "Very Elevated";
    98,73,17,17, "Very Elevated";    98,72,16,16, "Very Elevated";
    98,71,15,15, "Very Elevated";    
    
    97,69,14,14, "Elevated";    96,67,13,13, "Elevated";
    93,65,12,12, "Elevated";
    
    90,63,11,11, "Slightly Elevated";    86,61,10,10, "Slightly Elevated";
    
    82,59,9,9, "Average";   
    69,55,8,8, "Average";    66,54,7,7, "Average";
    58,52,6,6, "Average";    50,50,5,5, "Average";
    38,47,4,4, "Average";    31,45,3,3, "Average";
    21,42,2,2, "Average";    
    12,38,1,1, "Low"; 3,31,0,0, "Low"];
% SER conversion 12-18 years
SER_conv_1218 = [];
SER_conv_1218 = [99,85,46,52, "Very Elevated"; 99,84,45,45, "Very Elevated"; 
    99,83,44,44,"Very Elevated";     99,82,43,43, "Very Elevated";
    99,81,42,42, "Very Elevated";    99,80,41,41, "Very Elevated";
    99,79,40,40, "Very Elevated";    99,78,39,39, "Very Elevated";
    99,77,38,38, "Very Elevated";    99,76,37,37, "Very Elevated";
    99,75,36,36, "Very Elevated";    99,74,35,35, "Very Elevated"; 
    99,73,34,34, "Very Elevated";    99,72,33,33, "Very Elevated";
    98,71,32,32, "Very Elevated";    98,70,31,31, "Very Elevated";   
    
    97,69,29,30, "Elevated";    96,68,28,28, "Elevated";
    96,67,27,27, "Elevated";    95,66,26,26, "Elevated";
    93,65,25,25, "Elevated";    
    
    92,64,24,24, "Slightly Elevated";    
    90,63,23,23, "Slightly Elevated";    88,62,22,22, "Slightly Elevated";
    86,61,21,21, "Slightly Elevated";    
    
    82,59,20,20, "Average";    79,58,19,19, "Average";
    76,57,18,18, "Average";    73,56,17,17, "Average";
    66,54,16,16, "Average";    
    62,53,15,15, "Average";    58,52,14,14, "Average"; 
    54,51,13,13, "Average";    
    50,50,12,12, "Average";    42,48,11,11, "Average";
    38,47,10,10, "Average";    34,46,9,9, "Average";
    31,45,8,8, "Average";      27,44,7,7, "Average";    
    21,42,6,6, "Average";      16,40,5,5, "Average";
    
    12,38,4,4, "Low";    10,37,3,3, "Low";    
    8,36,2,2, "Low";    5,34,1,1, "Low";    
    2,30,0,0, "Low"];
% AL conversion 12-18 years
AL_conv_1218 = [];
AL_conv_1218 = [99,85,24,24, "Very Elevated";    99,84,23,23, "Very Elevated";
    99,83,22,22, "Very Elevated";    99,81,21,21, "Very Elevated";
    99,80,20,20, "Very Elevated";    99,79,19,19, "Very Elevated";
    99,77,18,18, "Very Elevated";    99,76,17,17, "Very Elevated";
    99,75,16,16, "Very Elevated";    99,74,15,15, "Very Elevated";
    99,73,14,14, "Very Elevated";    99,72,13,13, "Very Elevated";
    98,71,15,15, "Very Elevated";    98,70,12,12, "Very Elevated";  
    
    97,69,11,11, "Elevated";    96,68,10,10, "Elevated";
    95,67,9,9, "Elevated";      93,65,8,8, "Elevated";    
    
    90,63,7,7, "Slightly Elevated";    
    86,61,6,6, "Slightly Elevated";   
    
    79,58,5,5, "Average";    69,55,4,4, "Average";
    62,53,3,3, "Average";   
    42,48,2,2, "Average";    27,44,1,1, "Average";
    
    14,39,0,0, "Average"];

% ST conversion 12-18 years
ST_conv_1218 = [];
ST_conv_1218 = [99,85,19,21, "Very Elevated";
    99,83,18,18, "Very Elevated"; 99,81,17,17, "Very Elevated";
    99,79,16,16, "Very Elevated";    99,78,15,15, "Very Elevated";
    99,76,14,14, "Very Elevated";    99,74,13,13, "Very Elevated";
    99,72,12,12, "Very Elevated";    98,70,11,11, "Very Elevated"; 
    
    96,68,10,10, "Elevated";
    95,66,9,9, "Elevated";     93,65,8,8, "Elevated"; 
    
    90,63,7,7, "Slightly Elevated";    
    86,61,6,6, "Slightly Elevated";    
    
    82,59,5,5, "Average";    76,55,4,4, "Average";
    69,55,3,3, "Average";    58,52,5,5, "Average";
    58,52,2,2, "Average";    27,44,1,1, "Average";
    14,39,0,0, "Low"];
% BR conversion 12-18 years
BR_conv_1218 = [];
BR_conv_1218 = [99,82,32,32, "Very Elevated"; 
    99,81,31,31, "Very Elevated";    99,80,30,30, "Very Elevated";
    99,79,29,29, "Very Elevated";    99,78,28,28, "Very Elevated";
    99,77,27,27, "Very Elevated";
    99,76,26,26, "Very Elevated";    99,75,25,25, "Very Elevated";    
    99,74,24,24, "Very Elevated";    99,73,23,23, "Very Elevated";    
    99,72,22,22, "Very Elevated";    98,71,21,21, "Very Elevated";  
    98,70,20,20, "Very Elevated";    
    
    97,69,19,19, "Elevated";    
    96,68,18,18, "Elevated";    96,67,17,17, "Elevated";    
    93,65,16,16, "Elevated";  
    
    92,64,15,15, "Slightly Elevated";    90,63,14,14, "Slightly Elevated";
    86,61,13,13, "Slightly Elevated";    84,60,12,12, "Slightly Elevated";
    
    82,59,11,11, "Average"; 
    76,57,10,10, "Average";    69,55,9,9, "Average";
    66,54,8,8, "Average";    58,52,7,7, "Average";
    54,51,6,6, "Average";    46,49,5,5, "Average";
    38,47,4,4, "Average";    31,45,3,3, "Average";   
    18,41,2,2, "Average";     12,38,1,1, "Low"; 
    4,33,0,0, "Low"];
% SS conversion 12-18 years
SS_conv_1218 = [];
SS_conv_1218 = [99,85,20,24, "Very Elevated"; 99,84,19,19, "Very Elevated"; 
    99,82,18,18, "Very Elevated";
    99,80,17,17, "Very Elevated";
    99,78,16,16, "Very Elevated";
    99,77,15,15, "Very Elevated";    99,75,14,14, "Very Elevated";
    99,74,13,13, "Very Elevated";
    99,73,12,12, "Very Elevated";    98,71,11,11, "Very Elevated";
    
    97,69,10,10, "Elevated";    96,67,9,9, "Elevated"; 
    93,65,8,8, "Elevated";    
    
    90,63,7,7, "Slightly Elevated";   
    86,61,6,6, "Average";    82,59,5,5, "Average";  
    76,57,4,4, "Average";    66,54,3,3, "Average";
    54,51,2,2, "Average";    31,45,1,1, "Average";
    14,39,0,0, "Low"];
% AT conversion 12-18 years
AT_conv_1218 = [];
AT_conv_1218 = [99,85,44,44, "Very Elevated"; 99,84,43,43, "Very Elevated"; 
    99,83,42,42,"Very Elevated";     99,82,41,41, "Very Elevated";
    99,81,40,40, "Very Elevated";    99,80,39,39, "Very Elevated";
    99,79,38,38, "Very Elevated";    99,77,37,37, "Very Elevated";
    99,75,36,36, "Very Elevated";    99,74,35,35, "Very Elevated";
    98,73,34,34, "Very Elevated";    98,72,33,33, "Very Elevated"; 
    98,71,32,32, "Very Elevated";  
    
    97,69,31,31, "Elevated";    96,68,30,30, "Elevated";
    96,67,29,29, "Elevated";    95,66,28,28, "Elevated";
        
    92,64,27,27, "Slightly Elevated";    
    90,63,26,26, "Slightly Elevated";    88,62,25,25, "Slightly Elevated";
    86,61,24,24, "Slightly Elevated";    84,60,23,23, "Slightly Elevated";
        
    82,59,22,22, "Average";    79,58,21,21, "Average";
    76,57,20,20, "Average";    73,56,19,19, "Average";
    69,55,18,18, "Average";    66,54,17,17, "Average"; 
    62,53,16,16, "Average";    
    58,52,15,15, "Average";    50,50,14,14, "Average";
    46,49,13,13, "Average";    38,47,12,12, "Average";
    34,46,11,11, "Average";    31,45,10,10, "Average";
    27,44,9,9, "Average";    
    21,42,8,8, "Average";    18,41,7,7, "Average"; 
    
    14,39,6,6, "Low";   10,37,5,5, "Low";    
    7,35,4,4, "Low";    4,33,3,3, "Low";    
    3,31,2,2, "Low";    1,28,1,1, "Low";    
    1,25,0,0, "Low"];
%% Compute T-score
part_age = []; part_age = age; 

if part_age >= 6 && part_age <= 11
    disp('6-11 years'); range = []; range = '6 y 11 años';
    T_score_SC = []; i = []; Percentile_Rank_SC = []; Classification_SC = []; 
    for i = 1:1:size(SC_conv_611,1) %Possibilities for conversions
        mini = []; mini = str2num(SC_conv_611(i,3));
        maxi = []; maxi = str2num(SC_conv_611(i,4));
        try SC_sum;
            switch SC_sum %en un ciclo para cada fila de SC_conv_611
            case num2cell(mini:maxi)
                T_score_SC = str2num(SC_conv_611(i,2));
                Percentile_Rank_SC =  str2num(SC_conv_611(i,1));
                Classification_SC =  SC_conv_611(i,5);
                disp(join(['Social Communication:' SC_conv_611(i,5)]))
            end
         catch
             disp('Social Communication: unable to compute T-score/too much omitted responses')
             break
        end
    end
    i = []; T_score_UB = []; i = []; Percentile_Rank_UB = []; Classification_UB = []; 
    for i = 1:1:size(UB_conv_611,1) %Possibilities for conversions
        mini = []; mini = str2num(UB_conv_611(i,3));
        maxi = []; maxi = str2num(UB_conv_611(i,4));
        try UB_sum;
            switch UB_sum %en un ciclo para cada fila de SC_conv_611
                case num2cell(mini:maxi)
                    T_score_UB = str2num(UB_conv_611(i,2));
                    Percentile_Rank_UB =  str2num(UB_conv_611(i,1));
                    Classification_UB =  UB_conv_611(i,5);
                    disp(join(['Unusual Behaviour:' UB_conv_611(i,5)]))
            end
        catch
             disp('Unusual Behaviour: unable to compute T-score/too much omitted responses')
             break
        end
    end
    i = []; T_score_SR = []; i = []; Percentile_Rank_SR = []; Classification_SR = []; 
    for i = 1:1:size(SR_conv_611,1) %Possibilities for conversions
        mini = []; mini = str2num(SR_conv_611(i,3));
        maxi = []; maxi = str2num(SR_conv_611(i,4));
        try SR_sum;
            switch SR_sum %en un ciclo para cada fila de SC_conv_611
                case num2cell(mini:maxi)
                    T_score_SR = str2num(SR_conv_611(i,2));
                    Percentile_Rank_SR =  str2num(SR_conv_611(i,1));
                    Classification_SR =  SR_conv_611(i,5);
                    disp(join(['Self-Regulation:' SR_conv_611(i,5)]))
            end
        catch
            disp('Self-Regulation: unable to compute T-score/too much omitted responses')
            break
        end
    end
    if ~isempty(T_score_SC) && ~isempty(T_score_UB) && ~isempty(T_score_SR)
        TOT = []; TOT = sum([T_score_SC, T_score_UB, T_score_SR]);
    end
    if isempty(T_score_SC)
        disp('Could not compute Total Score because of too much omitted response on Social Communication')
    end
    if isempty(T_score_UB)
        disp('Could not compute Total Score because of too much omitted response on Unusual Behaviours')
    end
    if isempty(T_score_SR)
        disp('Could not compute Total Score because of too much omitted response on Self Regulation')
    end
    i = []; T_score_TOT = []; i = []; Percentile_Rank_TOT = []; Classification_TOT = []; 
    for i = 1:1:size(TOT_conv_611,1) %Possibilities for conversions
        mini = []; mini = str2num(TOT_conv_611(i,3));
        maxi = []; maxi = str2num(TOT_conv_611(i,4));
        try TOT;
            switch TOT %en un ciclo para cada fila de SC_conv_611
                case num2cell(mini:maxi)
                    T_score_TOT = str2num(TOT_conv_611(i,2));
                    Percentile_Rank_TOT =  str2num(TOT_conv_611(i,1));
                    Classification_TOT =  TOT_conv_611(i,5);
                    disp(join(['Total Score:' TOT_conv_611(i,5)]))
            end
        catch
            disp('Total Score: unable to compute T-score/too much omitted responses')
            break
        end
    end
    
    i = []; T_score_DSM = []; i = []; Percentile_Rank_DSM = []; Classification_DSM = []; 
    for i = 1:1:size(DSM_conv_611,1) %Possibilities for conversions
        mini = []; mini = str2num(DSM_conv_611(i,3));
        maxi = []; maxi = str2num(DSM_conv_611(i,4));
        try DSM_sum;
            switch DSM_sum %en un ciclo para cada fila de SC_conv_611
                case num2cell(mini:maxi)
                    T_score_DSM = str2num(DSM_conv_611(i,2));
                    Percentile_Rank_DSM =  str2num(DSM_conv_611(i,1));
                    Classification_DSM =  DSM_conv_611(i,5);
                    disp(join(['DSM-5:' DSM_conv_611(i,5)]))
            end
        catch
            disp('DSM-5: unable to compute T-score/too much omitted responses')
            break
        end
    end
    
    i = []; T_score_PS = []; i = []; Percentile_Rank_PS = []; Classification_PS = []; 
    for i = 1:1:size(PS_conv_611,1) %Possibilities for conversions
        mini = []; mini = str2num(PS_conv_611(i,3));
        maxi = []; maxi = str2num(PS_conv_611(i,4));
        try PS_sum;
            switch PS_sum %en un ciclo para cada fila de SC_conv_611
                case num2cell(mini:maxi)
                    T_score_PS = str2num(PS_conv_611(i,2));
                    Percentile_Rank_PS =  str2num(PS_conv_611(i,1));
                    Classification_PS =  PS_conv_611(i,5);
                    disp(join(['Peer Socialization:' PS_conv_611(i,5)]))
            end
        catch 
            disp('Peer Socialization: unable to compute T-score/too much omitted responses')
            break
        end
    end
    i = []; T_score_AS = []; i = []; Percentile_Rank_AS = []; Classification_AS = [];  
    for i = 1:1:size(AS_conv_611,1) %Possibilities for conversions
        mini = []; mini = str2num(AS_conv_611(i,3));
        maxi = []; maxi = str2num(AS_conv_611(i,4));
        try AS_sum;
            switch AS_sum %en un ciclo para cada fila de SC_conv_611
                case num2cell(mini:maxi)
                    T_score_AS = str2num(AS_conv_611(i,2));
                    Percentile_Rank_AS =  str2num(AS_conv_611(i,1));
                    Classification_AS =  AS_conv_611(i,5);
                    disp(join(['Adult Socialization:' AS_conv_611(i,5)]))
            end
        catch
            disp('Adult Socialization: unable to compute T-score/too much omitted responses')
            break
        end
    end
    i = []; T_score_SER = []; i = []; Percentile_Rank_SER = []; Classification_SER = [];  
    for i = 1:1:size(SER_conv_611,1) %Possibilities for conversions
        mini = []; mini = str2num(SER_conv_611(i,3));
        maxi = []; maxi = str2num(SER_conv_611(i,4));
        try SER_sum;
            switch SER_sum %en un ciclo para cada fila de SC_conv_611
                case num2cell(mini:maxi)
                    T_score_SER = str2num(SER_conv_611(i,2));
                    Percentile_Rank_SER =  str2num(SER_conv_611(i,1));
                    Classification_SER =  SER_conv_611(i,5);
                    disp(join(['Social/Emotional Reciprocity:' SER_conv_611(i,5)]))
            end
        catch
            disp('Social/Emotional Reciprocity: unable to compute T-score/too much omitted responses')
            break
        end
    end
    i = []; T_score_AL = []; i = []; Percentile_Rank_AL = []; Classification_AL = [];  
    for i = 1:1:size(AL_conv_611,1) %Possibilities for conversions
        mini = []; mini = str2num(AL_conv_611(i,3));
        maxi = []; maxi = str2num(AL_conv_611(i,4));
        try AL_sum;
            switch AL_sum %en un ciclo para cada fila de SC_conv_611
                case num2cell(mini:maxi)
                    T_score_AL = str2num(AL_conv_611(i,2));
                    Percentile_Rank_AL =  str2num(AL_conv_611(i,1));
                    Classification_AL =  AL_conv_611(i,5);
                    disp(join(['Atypical Language:' AL_conv_611(i,5)]))
            end
        catch
            if language == 0
                disp('Atypical Language: unable to compute T-score/too much omitted responses')
            else
                disp('Atypical Language: speech too limited')
            end
            break
        end
    end
    i = []; T_score_ST = []; i = []; Percentile_Rank_ST = []; Classification_ST = [];  
    for i = 1:1:size(ST_conv_611,1) %Possibilities for conversions
        mini = []; mini = str2num(ST_conv_611(i,3));
        maxi = []; maxi = str2num(ST_conv_611(i,4));
        try ST_sum;
            switch ST_sum %en un ciclo para cada fila de SC_conv_611
                case num2cell(mini:maxi)
                    T_score_ST = str2num(ST_conv_611(i,2));
                    Percentile_Rank_ST =  str2num(ST_conv_611(i,1));
                    Classification_ST =  ST_conv_611(i,5);
                    disp(join(['Stereotypy:' ST_conv_611(i,5)]))
            end
        catch
            disp('Stereotypy: unable to compute T-score/too much omitted responses')
            break
        end
    end
    i = []; T_score_BR = []; i = []; Percentile_Rank_BR = []; Classification_BR = [];  
    for i = 1:1:size(BR_conv_611,1) %Possibilities for conversions
        mini = []; mini = str2num(BR_conv_611(i,3));
        maxi = []; maxi = str2num(BR_conv_611(i,4));
        try BR_sum;
            switch BR_sum %en un ciclo para cada fila de SC_conv_611
                case num2cell(mini:maxi)
                    T_score_BR = str2num(BR_conv_611(i,2));
                    Percentile_Rank_BR =  str2num(BR_conv_611(i,1));
                    Classification_BR =  BR_conv_611(i,5);
                    disp(join(['Behavioural Rigidity:' BR_conv_611(i,5)]))
            end
        catch 
            disp('Behavioural Rigidity: unable to compute T-score/too much omitted responses')
            break
        end
    end
    i = []; T_score_SS = []; i = []; Percentile_Rank_SS = []; Classification_SS = [];  
    for i = 1:1:size(SS_conv_611,1) %Possibilities for conversions
        mini = []; mini = str2num(SS_conv_611(i,3));
        maxi = []; maxi = str2num(SS_conv_611(i,4));
        try SS_sum;
            switch SS_sum %en un ciclo para cada fila de SC_conv_611
                case num2cell(mini:maxi)
                    T_score_SS = str2num(SS_conv_611(i,2));
                    Percentile_Rank_SS =  str2num(SS_conv_611(i,1));
                    Classification_SS =  SS_conv_611(i,5);
                    disp(join(['Sensory Sensitivity:' SS_conv_611(i,5)]))
            end
        catch 
            disp('Sensory Sensitivity: unable to compute T-score/too much omitted responses')
            break
        end
    end
    i = []; T_score_AT = []; i = []; Percentile_Rank_AT = []; Classification_AT = [];  
    for i = 1:1:size(AT_conv_611,1) %Possibilities for conversions
        mini = []; mini = str2num(AT_conv_611(i,3));
        maxi = []; maxi = str2num(AT_conv_611(i,4));
        try AT_sum;
            switch AT_sum %en un ciclo para cada fila de SC_conv_611
                case num2cell(mini:maxi)
                    T_score_AT = str2num(AT_conv_611(i,2));
                    Percentile_Rank_AT =  str2num(AT_conv_611(i,1));
                    Classification_AT =  AT_conv_611(i,5);
                    disp(join(['Attention:' AT_conv_611(i,5)]))
            end
        catch
            disp('Attention: unable to compute T-score/too much omitted responses')
            break
        end
    end
    
    
elseif part_age >= 12 && part_age <= 18
    disp('12-18 years'); range = []; range = '12 y 18 años';
    T_score_SC = []; i = []; Percentile_Rank_SC = []; Classification_SC = []; 
    for i = 1:1:size(SC_conv_1218,1) %Possibilities for conversions
        mini = []; mini = str2num(SC_conv_1218(i,3));
        maxi = []; maxi = str2num(SC_conv_1218(i,4));
        try SC_sum;
            switch SC_sum %en un ciclo para cada fila de SC_conv_1218
            case num2cell(mini:maxi)
                T_score_SC = str2num(SC_conv_1218(i,2));
                Percentile_Rank_SC =  str2num(SC_conv_1218(i,1));
                Classification_SC =  SC_conv_1218(i,5);
                disp(join(['Social Communication:' SC_conv_1218(i,5)]))
            end
         catch
             disp('Social Communication: unable to compute T-score/too much omitted responses')
             break
        end
    end
    i = []; T_score_UB = []; i = []; Percentile_Rank_UB = []; Classification_UB = []; 
    for i = 1:1:size(UB_conv_1218,1) %Possibilities for conversions
        mini = []; mini = str2num(UB_conv_1218(i,3));
        maxi = []; maxi = str2num(UB_conv_1218(i,4));
        try UB_sum;
            switch UB_sum %en un ciclo para cada fila de SC_conv_1218
                case num2cell(mini:maxi)
                    T_score_UB = str2num(UB_conv_1218(i,2));
                    Percentile_Rank_UB =  str2num(UB_conv_1218(i,1));
                    Classification_UB =  UB_conv_1218(i,5);
                    disp(join(['Unusual Behaviour:' UB_conv_1218(i,5)]))
            end
        catch
             disp('Unusual Behaviour: unable to compute T-score/too much omitted responses')
             break
        end
    end
    i = []; T_score_SR = []; i = []; Percentile_Rank_SR = []; Classification_SR = []; 
    for i = 1:1:size(SR_conv_1218,1) %Possibilities for conversions
        mini = []; mini = str2num(SR_conv_1218(i,3));
        maxi = []; maxi = str2num(SR_conv_1218(i,4));
        try SR_sum;
            switch SR_sum %en un ciclo para cada fila de SC_conv_1218
                case num2cell(mini:maxi)
                    T_score_SR = str2num(SR_conv_1218(i,2));
                    Percentile_Rank_SR =  str2num(SR_conv_1218(i,1));
                    Classification_SR =  SR_conv_1218(i,5);
                    disp(join(['Self-Regulation:' SR_conv_1218(i,5)]))
            end
        catch
            disp('Self-Regulation: unable to compute T-score/too much omitted responses')
            break
        end
    end
    if ~isempty(T_score_SC) && ~isempty(T_score_UB) && ~isempty(T_score_SR)
        TOT = []; TOT = sum([T_score_SC, T_score_UB, T_score_SR]);
    end
    if isempty(T_score_SC)
        disp('Could not compute Total Score because of too much omitted response on Social Communication')
    end
    if isempty(T_score_UB)
        disp('Could not compute Total Score because of too much omitted response on Unusual Behaviours')
    end
    if isempty(T_score_SR)
        disp('Could not compute Total Score because of too much omitted response on Self Regulation')
    end
    i = []; T_score_TOT = []; i = []; Percentile_Rank_TOT = []; Classification_TOT = []; 
    for i = 1:1:size(TOT_conv_1218,1) %Possibilities for conversions
        mini = []; mini = str2num(TOT_conv_1218(i,3));
        maxi = []; maxi = str2num(TOT_conv_1218(i,4));
        try TOT;
            switch TOT %en un ciclo para cada fila de SC_conv_1218
                case num2cell(mini:maxi)
                    T_score_TOT = str2num(TOT_conv_1218(i,2));
                    Percentile_Rank_TOT =  str2num(TOT_conv_1218(i,1));
                    Classification_TOT =  TOT_conv_1218(i,5);
                    disp(join(['Total Score:' TOT_conv_1218(i,5)]))
            end
        catch
            disp('Total Score: unable to compute T-score/too much omitted responses')
            break
        end
    end
    
    i = []; T_score_DSM = []; i = []; Percentile_Rank_DSM = []; Classification_DSM = []; 
    for i = 1:1:size(DSM_conv_1218,1) %Possibilities for conversions
        mini = []; mini = str2num(DSM_conv_1218(i,3));
        maxi = []; maxi = str2num(DSM_conv_1218(i,4));
        try DSM_sum;
            switch DSM_sum %en un ciclo para cada fila de SC_conv_1218
                case num2cell(mini:maxi)
                    T_score_DSM = str2num(DSM_conv_1218(i,2));
                    Percentile_Rank_DSM =  str2num(DSM_conv_1218(i,1));
                    Classification_DSM =  DSM_conv_1218(i,5);
                    disp(join(['DSM-5:' DSM_conv_1218(i,5)]))
            end
        catch
            disp('DSM-5: unable to compute T-score/too much omitted responses')
            break
        end
    end
    
    i = []; T_score_PS = []; i = []; Percentile_Rank_PS = []; Classification_PS = []; 
    for i = 1:1:size(PS_conv_1218,1) %Possibilities for conversions
        mini = []; mini = str2num(PS_conv_1218(i,3));
        maxi = []; maxi = str2num(PS_conv_1218(i,4));
        try PS_sum;
            switch PS_sum %en un ciclo para cada fila de SC_conv_1218
                case num2cell(mini:maxi)
                    T_score_PS = str2num(PS_conv_1218(i,2));
                    Percentile_Rank_PS =  str2num(PS_conv_1218(i,1));
                    Classification_PS =  PS_conv_1218(i,5);
                    disp(join(['Peer Socialization:' PS_conv_1218(i,5)]))
            end
        catch 
            disp('Peer Socialization: unable to compute T-score/too much omitted responses')
            break
        end
    end
    i = []; T_score_AS = []; i = []; Percentile_Rank_AS = []; Classification_AS = [];  
    for i = 1:1:size(AS_conv_1218,1) %Possibilities for conversions
        mini = []; mini = str2num(AS_conv_1218(i,3));
        maxi = []; maxi = str2num(AS_conv_1218(i,4));
        try AS_sum;
            switch AS_sum %en un ciclo para cada fila de SC_conv_1218
                case num2cell(mini:maxi)
                    T_score_AS = str2num(AS_conv_1218(i,2));
                    Percentile_Rank_AS =  str2num(AS_conv_1218(i,1));
                    Classification_AS =  AS_conv_1218(i,5);
                    disp(join(['Adult Socialization:' AS_conv_1218(i,5)]))
            end
        catch
            disp('Adult Socialization: unable to compute T-score/too much omitted responses')
            break
        end
    end
    i = []; T_score_SER = []; i = []; Percentile_Rank_SER = []; Classification_SER = [];  
    for i = 1:1:size(SER_conv_1218,1) %Possibilities for conversions
        mini = []; mini = str2num(SER_conv_1218(i,3));
        maxi = []; maxi = str2num(SER_conv_1218(i,4));
        try SER_sum;
            switch SER_sum %en un ciclo para cada fila de SC_conv_1218
                case num2cell(mini:maxi)
                    T_score_SER = str2num(SER_conv_1218(i,2));
                    Percentile_Rank_SER =  str2num(SER_conv_1218(i,1));
                    Classification_SER =  SER_conv_1218(i,5);
                    disp(join(['Social/Emotional Reciprocity:' SER_conv_1218(i,5)]))
            end
        catch
            disp('Social/Emotional Reciprocity: unable to compute T-score/too much omitted responses')
            break
        end
    end
    i = []; T_score_AL = []; i = []; Percentile_Rank_AL = []; Classification_AL = [];  
    for i = 1:1:size(AL_conv_1218,1) %Possibilities for conversions
        mini = []; mini = str2num(AL_conv_1218(i,3));
        maxi = []; maxi = str2num(AL_conv_1218(i,4));
        try AL_sum;
            switch AL_sum %en un ciclo para cada fila de SC_conv_1218
                case num2cell(mini:maxi)
                    T_score_AL = str2num(AL_conv_1218(i,2));
                    Percentile_Rank_AL =  str2num(AL_conv_1218(i,1));
                    Classification_AL =  AL_conv_1218(i,5);
                    disp(join(['Atypical Language:' AL_conv_1218(i,5)]))
            end
        catch
            if language == 0
                disp('Atypical Language: unable to compute T-score/too much omitted responses')
            else
                disp('Atypical Language: speech too limited')
            end
            break
        end
    end
    i = []; T_score_ST = []; i = []; Percentile_Rank_ST = []; Classification_ST = [];  
    for i = 1:1:size(ST_conv_1218,1) %Possibilities for conversions
        mini = []; mini = str2num(ST_conv_1218(i,3));
        maxi = []; maxi = str2num(ST_conv_1218(i,4));
        try ST_sum;
            switch ST_sum %en un ciclo para cada fila de SC_conv_1218
                case num2cell(mini:maxi)
                    T_score_ST = str2num(ST_conv_1218(i,2));
                    Percentile_Rank_ST =  str2num(ST_conv_1218(i,1));
                    Classification_ST =  ST_conv_1218(i,5);
                    disp(join(['Stereotypy:' ST_conv_1218(i,5)]))
            end
        catch
            disp('Stereotypy: unable to compute T-score/too much omitted responses')
            break
        end
    end
    i = []; T_score_BR = []; i = []; Percentile_Rank_BR = []; Classification_BR = [];  
    for i = 1:1:size(BR_conv_1218,1) %Possibilities for conversions
        mini = []; mini = str2num(BR_conv_1218(i,3));
        maxi = []; maxi = str2num(BR_conv_1218(i,4));
        try BR_sum;
            switch BR_sum %en un ciclo para cada fila de SC_conv_1218
                case num2cell(mini:maxi)
                    T_score_BR = str2num(BR_conv_1218(i,2));
                    Percentile_Rank_BR =  str2num(BR_conv_1218(i,1));
                    Classification_BR =  BR_conv_1218(i,5);
                    disp(join(['Behavioural Rigidity:' BR_conv_1218(i,5)]))
            end
        catch 
            disp('Behavioural Rigidity: unable to compute T-score/too much omitted responses')
            break
        end
    end
    i = []; T_score_SS = []; i = []; Percentile_Rank_SS = []; Classification_SS = [];  
    for i = 1:1:size(SS_conv_1218,1) %Possibilities for conversions
        mini = []; mini = str2num(SS_conv_1218(i,3));
        maxi = []; maxi = str2num(SS_conv_1218(i,4));
        try SS_sum;
            switch SS_sum %en un ciclo para cada fila de SC_conv_1218
                case num2cell(mini:maxi)
                    T_score_SS = str2num(SS_conv_1218(i,2));
                    Percentile_Rank_SS =  str2num(SS_conv_1218(i,1));
                    Classification_SS =  SS_conv_1218(i,5);
                    disp(join(['Sensory Sensitivity:' SS_conv_1218(i,5)]))
            end
        catch 
            disp('Sensory Sensitivity: unable to compute T-score/too much omitted responses')
            break
        end
    end
%
    i = []; T_score_AT = []; i = []; Percentile_Rank_AT = []; Classification_AT = [];  
    for i = 1:1:size(AT_conv_1218,1) %Possibilities for conversions
        mini = []; mini = str2num(AT_conv_1218(i,3));
        maxi = []; maxi = str2num(AT_conv_1218(i,4));
        try AT_sum;
            switch AT_sum %en un ciclo para cada fila de SC_conv_1218
                case num2cell(mini:maxi)
                    T_score_AT = str2num(AT_conv_1218(i,2));
                    Percentile_Rank_AT =  str2num(AT_conv_1218(i,1));
                    Classification_AT =  AT_conv_1218(i,5);
                    disp(join(['Attention:' AT_conv_1218(i,5)]))
            end
        catch
            disp('Attention: unable to compute T-score/too much omitted responses')
            break
        end
    end    
else
    disp('Age is out of range for ASRS (6-18 years old)')
end
%% SC - Compute T-score CI 90% CI 6-11-years
i = []; mini = []; m = []; m = 80:-1:64; m = [m, 64:-1:45]; 
m = [m,45:-1:30];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 87:-1:74; m = [m, 74:-1:55];
m = [m,55:-1:37];
for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:33]';
CI_Tscore_90_SC_611 = []; CI_Tscore_90_SC_611 = [T,mini,maxi];

%% UB - Compute T-score CI 90% CI 6-11-years
i = []; mini = []; m = []; m = 78:-1:64; m = [m, 64:-1:45]; 
m = [m,45:-1:30];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 85:-1:74; m = [m, 74:-1:55];
m = [m,55:-1:37];
for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [83:-1:33]';
CI_Tscore_90_UB_611 = []; CI_Tscore_90_UB_611 = [T,mini,maxi];
%% SR - Compute T-score CI 90% CI 6-11-years
i = []; mini = []; m = []; m = 75:-1:69; m = [m, 69:-1:58]; 
m = [m,58:-1:46]; m = [m,46:-1:35]; m = [m,35:-1:23]; m = [m,23];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 84:-1:77; m = [m, 77:-1:65];
m = [m,65:-1:54]; m = [m,54:-1:42]; m = [m,42:-1:31];
for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [82:-1:25]';
CI_Tscore_90_SR_611 = []; CI_Tscore_90_SR_611 = [T,mini,maxi];
%% TOT - Compute T-score CI 90% CI 6-11-years
i = []; mini = []; m = []; m = 81:-1:78; m = [m, 78:-1:42]; 
m = [m,42:-1:23]; 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 87:-1:58; m = [m, 58:-1:28];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:25]';
CI_Tscore_90_TOT_611 = []; CI_Tscore_90_TOT_611 = [T,mini,maxi];
%% DSM - Compute T-score CI 90% CI 6-11-years
i = []; mini = []; m = []; m = 80:-1:78; m = [m, 78:-1:54]; 
m = [m,54:-1:30]; m = [m,30:-1:27]; 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 87:-1:70; m = [m, 70:-1:46];
m = [m, 46:-1:33];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:29]';
CI_Tscore_90_DSM_611 = []; CI_Tscore_90_DSM_611 = [T,mini,maxi];
%% PS - Compute T-score CI 90% CI 6-11-years
i = []; mini = []; m = [];  m = 75; m = [m,75:-1:68]; m = [m, 68:-1:60]; 
m = [m,60:-1:53]; m = [m,53:-1:46]; m = [m,46:-1:38]; m = [m,38:-1:31]; 
m = [m,31]; 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 86:-1:84; m = [m, 84:-1:76];
m = [m, 76:-1:69]; m = [m, 69:-1:62]; m = [m, 62:-1:54];
m = [m, 54:-1:47]; m = [m, 47:-1:41];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:34]';
CI_Tscore_90_PS_611 = []; CI_Tscore_90_PS_611 = [T,mini,maxi];
%% AS - Compute T-score CI 90% CI 6-11-years
i = []; mini = []; m = [];  m = 69; m = [m,69:-1:68]; m = [m, 68:-1:65]; 
m = [m,65:-1:62]; m = [m,62:-1:59]; m = [m,59:-1:55]; m = [m,55:-1:52]; 
m = [m,52:-1:49]; m = [m,49:-1:45]; m = [m,45:-1:42]; m = [m,42:-1:38];
m = [m,38:-1:35]; m = [m,35:-1:32]; m = [m,32:-1:28]; m = [m,28:-1:27];   
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 85:-1:78; m = [m, 78:-1:75];
m = [m, 75:-1:72]; m = [m, 72:-1:68]; m = [m, 68:-1:65];
m = [m, 65:-1:62]; m = [m, 62:-1:58]; m = [m, 58:-1:55];
m = [m, 55:-1:51]; m = [m, 51:-1:48]; m = [m, 48:-1:45];
m = [m, 45:-1:41]; m = [m, 41];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:29]';
CI_Tscore_90_AS_611 = []; CI_Tscore_90_AS_611 = [T,mini,maxi];
%% SER - Compute T-score CI 90% CI 6-11-years
i = []; mini = []; m = []; m = [m,77:-1:68]; m = [m, 68:-1:59]; 
m = [m,59:-1:50]; m = [m,50:-1:41]; m = [m,41:-1:32]; m = [m,32:-1:25];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 86;  m = [m, 86:-1:77]; m = [m, 77:-1:68];
m = [m, 68:-1:59]; m = [m, 59:-1:50]; m = [m, 50:-1:41];
m = [m, 41:-1:35]; 

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:28]';
CI_Tscore_90_SER_611 = []; CI_Tscore_90_SER_611 = [T,mini,maxi];
%% AL - Compute T-score CI 90% CI 6-11-years
i = []; mini = []; m = [];m = 70; m = [m,70:-1:65]; m = [m, 65:-1:61]; 
m = [m,61:-1:56]; m = [m,56:-1:51]; m = [m,51:-1:46]; m = [m,46:-1:41];
m = [m,41:-1:36]; m = [m,36:-1:33];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 83:-1:78; m = [m, 78:-1:74];
m = [m, 74:-1:69]; m = [m, 69:-1:64]; m = [m, 64:-1:59];
m = [m, 59:-1:54]; m = [m, 54:-1:49]; m = [m, 49:-1:45];  

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [82:-1:37]';
CI_Tscore_90_AL_611 = []; CI_Tscore_90_AL_611 = [T,mini,maxi];
%% ST - Compute T-score CI 90% CI 6-11-years
i = []; mini = []; m = []; m = 69:-1:65; m = [m, 65:-1:61]; 
m = [m,61:-1:58]; m = [m,58:-1:54]; m = [m,54:-1:50]; m = [m,50:-1:46];
m = [m,46:-1:43]; m = [m,43:-1:39]; m = [m,39:-1:35]; m = [m,35:-1:32];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 82:-1:80; m = [m, 80:-1:76];
m = [m, 76:-1:72]; m = [m, 72:-1:69]; m = [m, 69:-1:65];
m = [m, 65:-1:61]; m = [m, 61:-1:57]; m = [m, 57:-1:54]; 
m = [m, 54:-1:50]; m = [m, 50:-1:46]; m = [m, 46];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [82:-1:36]';
CI_Tscore_90_ST_611 = []; CI_Tscore_90_ST_611 = [T,mini,maxi];
%% BR - Compute T-score CI 90% CI 6-11-years
i = []; mini = []; m = []; m = 74:-1:64; m = [m, 64:-1:64]; 
m = [m,64:-1:54]; m = [m,54:-1:43]; m = [m,43:-1:33]; 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 83:-1:77; m = [m, 77:-1:67];
m = [m, 67:-1:57]; m = [m, 57:-1:46]; m = [m, 46:-1:42];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [81:-1:36]';
CI_Tscore_90_BR_611 = []; CI_Tscore_90_BR_611 = [T,mini,maxi];
%% SS - Compute T-score CI 90% CI 6-11-years
i = []; mini = []; m = []; m = 72; m = [m, 72:-1:67]; m = [m, 67:-1:62]; 
m = [m,62:-1:58]; m = [m,58:-1:53]; m = [m,53:-1:49]; m = [m,49:-1:44];
m = [m,44:-1:40]; m = [m,40:-1:35]; m = [m,35];   
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 85:-1:83; m = [m, 83:-1:79];
m = [m, 79:-1:74]; m = [m, 74:-1:69]; m = [m, 69:-1:65]; 
m = [m, 65:-1:60]; m = [m, 60:-1:56]; m = [m, 56:-1:51];
m = [m, 51:-1:47];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:39]';
CI_Tscore_90_SS_611 = []; CI_Tscore_90_SS_611 = [T,mini,maxi];
%% AT - Compute T-score CI 90% CI 6-11-years
i = []; mini = []; m = []; m = 77:-1:73; m = [m, 73:-1:63]; 
m = [m,63:-1:53]; m = [m,53:-1:43]; m = [m,43:-1:33]; m = [m,33:-1:23];
 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 87:-1:77; m = [m, 77:-1:67];
m = [m, 67:-1:57]; m = [m, 57:-1:47]; m = [m, 47:-1:37]; 
m = [m, 37:-1:33]; 

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:26]';
CI_Tscore_90_AT_611 = []; CI_Tscore_90_AT_611 = [T,mini,maxi];
%% SC - Compute T-score CI 90% CI 12-18-years
i = []; mini = []; m = []; m = 79:-1:71; m = [m, 71:-1:56]; 
m = [m, 56:-1:40]; m = [m,40:-1:26];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 87:-1:76; m = [m, 76:-1:60];
m = [m,60:-1:44]; m = [m,44:-1:34];
for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:29]';
CI_Tscore_90_SC_1218 = []; CI_Tscore_90_SC_1218 = [T,mini,maxi];

%% UB - Compute T-score CI 90% CI 12-18-years
i = []; mini = []; m = []; m = 79:-1:72; m = [m, 72:-1:56]; 
m = [m,56:-1:40]; m = [m,40:-1:30];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 87:-1:75; m = [m, 75:-1:60];
m = [m,60:-1:44]; m = [m,44:-1:38];
for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:33]';
CI_Tscore_90_UB_1218 = []; CI_Tscore_90_UB_1218 = [T,mini,maxi];
%% SR - Compute T-score CI 90% CI 12-18-years
i = []; mini = []; m = []; m = 78:-1:77; m = [m, 77:-1:64]; 
m = [m,64:-1:50]; m = [m,50:-1:37];  m = [m,37:-1:24]; m = [m,24:-1:23]; 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 87:-1:76; m = [m, 76:-1:63];
m = [m,63:-1:50]; m = [m,50:-1:36]; m = [m,36:-1:31];
for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
%
T = []; T = [85:-1:25]';
CI_Tscore_90_SR_1218 = []; CI_Tscore_90_SR_1218 = [T,mini,maxi];
%% TOT - Compute T-score CI 90% CI 12-18-years
i = []; mini = []; m = []; m = 81:-1:72; m = [m, 72:-1:39]; 
m = [m,39:-1:23]; 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 87:-1:61; m = [m, 61:-1:28];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:25]';
CI_Tscore_90_TOT_1218 = []; CI_Tscore_90_TOT_1218 = [T,mini,maxi];
%% DSM - Compute T-score CI 90% CI 12-18-years
i = []; mini = []; m = []; m = 80:-1:63; m = [m, 63:-1:44];
m = [m, 44:-1:25]; m = [m, 25];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 87:-1:75; m = [m, 75:-1:56];
m = [m, 56:-1:37]; m = [m, 37:-1:32];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:27]';
CI_Tscore_90_DSM_1218 = []; CI_Tscore_90_DSM_1218 = [T,mini,maxi];
%% PS - Compute T-score CI 90% CI 12-18-years
i = []; mini = []; m = [];  m = 75; m = [m,75:-1:68]; m = [m, 68:-1:61]; 
m = [m,61:-1:53]; m = [m,53:-1:46]; m = [m,46:-1:39]; m = [m,39:-1:31]; 
m = [m,31:-1:28]; 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 86:-1:83; m = [m, 83:-1:76];
m = [m, 76:-1:69]; m = [m, 69:-1:61]; m = [m, 61:-1:54];
m = [m, 54:-1:47]; m = [m, 47:-1:39]; m = [m, 39];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:31]';
CI_Tscore_90_PS_1218 = []; CI_Tscore_90_PS_1218 = [T,mini,maxi];
%% AS - Compute T-score CI 90% CI 12-18-years
i = []; mini = []; m = [];  m = 67; m = [m,67:-1:64]; m = [m, 64:-1:60]; 
m = [m,60:-1:56]; m = [m,56:-1:53]; m = [m,53:-1:49]; m = [m,49:-1:46]; 
m = [m,46:-1:42]; m = [m,42:-1:39]; m = [m,39:-1:35]; m = [m,35:-1:32];
m = [m,32:-1:28];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 81:-1:79; m = [m, 79:-1:75];
m = [m, 75:-1:72]; m = [m, 72:-1:68]; m = [m, 68:-1:65];
m = [m, 65:-1:61]; m = [m, 61:-1:58]; m = [m, 58:-1:54];
m = [m, 54:-1:51]; m = [m, 51:-1:47]; m = [m, 47:-1:44];
m = [m, 44:-1:42]; 

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [81:-1:31]';
CI_Tscore_90_AS_1218 = []; CI_Tscore_90_AS_1218 = [T,mini,maxi];
%% SER - Compute T-score CI 90% CI 12-18-years
i = []; mini = []; m = []; m = [m,77:-1:68]; m = [m, 68:-1:59]; 
m = [m,59:-1:50]; m = [m,50:-1:41]; m = [m,41:-1:32]; m = [m,32:-1:27];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 86;  m = [m, 86:-1:77]; m = [m, 77:-1:68];
m = [m, 68:-1:59]; m = [m, 59:-1:50]; m = [m, 50:-1:41];
m = [m, 41:-1:37]; 

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:30]';
CI_Tscore_90_SER_1218 = []; CI_Tscore_90_SER_1218 = [T,mini,maxi];
%% AL - Compute T-score CI 90% CI 12-18-years
i = []; mini = []; m = [];m = 73; m = [m,73:-1:68]; m = [m, 68:-1:62]; 
m = [m,62:-1:57]; m = [m,57:-1:52]; m = [m,52:-1:47]; m = [m,47:-1:41];
m = [m,41:-1:36]; m = [m,36:-1:35];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 85; m = [m,85:-1:80]; m = [m, 80:-1:74];
m = [m, 74:-1:69]; m = [m, 69:-1:64]; m = [m, 64:-1:59];
m = [m, 59:-1:53]; m = [m, 53:-1:48]; m = [m, 48:-1:47];  

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:39]';
CI_Tscore_90_AL_1218 = []; CI_Tscore_90_AL_1218 = [T,mini,maxi];
%% ST - Compute T-score CI 90% CI 12-18-years
i = []; mini = []; m = []; m = 70:-1:69; m = [m, 69:-1:67]; 
m = [m,67:-1:63]; m = [m,63:-1:60]; m = [m,60:-1:56]; m = [m,56:-1:53];
m = [m,53:-1:49]; m = [m,49:-1:46]; m = [m,46:-1:42]; m = [m,42:-1:38];
m = [m,38:-1:35]; m = [m,35];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 85:-1:79; m = [m, 79:-1:76];
m = [m, 76:-1:72]; m = [m, 72:-1:69]; m = [m, 69:-1:65];
m = [m, 65:-1:62]; m = [m, 62:-1:58]; m = [m, 58:-1:54]; 
m = [m, 54:-1:51]; m = [m, 51:-1:48]; 

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:39]';
CI_Tscore_90_ST_1218 = []; CI_Tscore_90_ST_1218 = [T,mini,maxi];
%% BR - Compute T-score CI 90% CI 12-18-years
i = []; mini = []; m = []; m = 74; m = [m,74:-1:64]; m = [m, 64:-1:54]; 
m = [m,54:-1:43]; m = [m,43:-1:33]; m = [m,33:-1:30]; 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 84:-1:77; m = [m, 77:-1:67];
m = [m, 67:-1:57]; m = [m, 57:-1:46]; m = [m, 46:-1:39];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [82:-1:33]';
CI_Tscore_90_BR_1218 = []; CI_Tscore_90_BR_1218 = [T,mini,maxi];
%% SS - Compute T-score CI 90% CI 12-18-years
i = []; mini = []; m = []; m = 72:-1:68; m = [m, 68:-1:64]; 
m = [m,64:-1:60]; m = [m,60:-1:56]; m = [m,56:-1:52]; m = [m,52:-1:48];
m = [m,48:-1:44]; m = [m,44:-1:40]; m = [m,40:-1:36]; m = [m,36:-1:35];    
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 84; m = [m,84:-1:80]; m = [m, 80:-1:76];
m = [m, 76:-1:72]; m = [m, 72:-1:68]; m = [m, 68:-1:64]; 
m = [m, 64:-1:60]; m = [m, 60:-1:56]; m = [m, 56:-1:52];
m = [m, 52:-1:48]; m = [m, 48];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:39]';
CI_Tscore_90_SS_1218 = []; CI_Tscore_90_SS_1218 = [T,mini,maxi];
%% AT - Compute T-score CI 90% CI 12-18-years
i = []; mini = []; m = []; m = 77:-1:68; m = [m, 68:-1:59]; 
m = [m,59:-1:50]; m = [m,50:-1:41]; m = [m,41:-1:32]; m = [m,32:-1:23];
m = [m,23];
 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 86; m = [m,86:-1:77]; m = [m, 77:-1:68];
m = [m, 68:-1:59]; m = [m, 59:-1:50]; m = [m, 50:-1:41]; 
m = [m, 41:-1:32]; 

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:25]';
CI_Tscore_90_AT_1218 = []; CI_Tscore_90_AT_1218 = [T,mini,maxi];
%% SC - Compute T-score CI 95% CI 6-11-years
i = []; mini = []; m = []; m = 79:-1:69; m = [m, 69:-1:50]; 
m = [m,50:-1:31]; m = [m,31:-1:30];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 88:-1:69; m = [m, 69:-1:50];
m = [m,50:-1:38];
for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:33]';
CI_Tscore_95_SC_611 = []; CI_Tscore_95_SC_611 = [T,mini,maxi];

%% UB - Compute T-score CI 95% CI 6-11-years
i = []; mini = []; m = []; m = 77:-1:69; m = [m, 69:-1:50]; 
m = [m,50:-1:31]; m = [m,31:-1:30];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 86:-1:69; m = [m, 69:-1:50];
m = [m,50:-1:38];
for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [83:-1:33]';
CI_Tscore_95_UB_611 = []; CI_Tscore_95_UB_611 = [T,mini,maxi];
%% SR - Compute T-score CI 95% CI 6-11-years
i = []; mini = []; m = []; m = 74:-1:70; m = [m, 70:-1:58]; 
m = [m,58:-1:47]; m = [m,47:-1:35]; m = [m,35:-1:24]; m = [m,24:-1:22];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 85:-1:76; m = [m, 76:-1:65];
m = [m,65:-1:53]; m = [m,53:-1:42]; m = [m,42:-1:32];
for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [82:-1:25]';
CI_Tscore_95_SR_611 = []; CI_Tscore_95_SR_611 = [T,mini,maxi];
%% TOT - Compute T-score CI 95% CI 6-11-years
i = []; mini = []; m = []; m = 81:-1:59; m = [m, 59:-1:22]; 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 87:-1:77; m = [m, 77:-1:41];
m = [m, 41:-1:29];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:25]';
CI_Tscore_95_TOT_611 = []; CI_Tscore_95_TOT_611 = [T,mini,maxi];
%% DSM - Compute T-score CI 95% CI 6-11-years
i = []; mini = []; m = []; m = 80:-1:63; m = [m, 63:-1:39]; 
m = [m,39:-1:26];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 87:-1:85; m = [m, 85:-1:61];
m = [m, 61:-1:37]; m = [m, 37:-1:34];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:29]';
CI_Tscore_95_DSM_611 = []; CI_Tscore_95_DSM_611 = [T,mini,maxi];
%% PS - Compute T-score CI 95% CI 6-11-years
i = []; mini = []; m = [];  m = 74; m = [m,74:-1:66]; m = [m, 66:-1:59]; 
m = [m,59:-1:52]; m = [m,52:-1:44]; m = [m,44:-1:37]; m = [m,37:-1:30]; 
m = [m,30]; 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 87:-1:85; m = [m, 85:-1:78];
m = [m, 78:-1:70]; m = [m, 70:-1:63]; m = [m, 63:-1:56];
m = [m, 56:-1:48]; m = [m, 48:-1:42];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:34]';
CI_Tscore_95_PS_611 = []; CI_Tscore_95_PS_611 = [T,mini,maxi];
%% AS - Compute T-score CI 95% CI 6-11-years
i = []; mini = []; m = [];  m = 69:-1:66; m = [m, 66:-1:63]; 
m = [m,63:-1:59]; m = [m,59:-1:56]; m = [m,56:-1:53]; m = [m,53:-1:49]; 
m = [m,49:-1:46]; m = [m,46:-1:43]; m = [m,43:-1:39]; m = [m,39:-1:36];
m = [m,36:-1:33]; m = [m,33:-1:29]; m = [m,29:-1:26]; m = [m,26];   
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 85:-1:84; m = [m, 84:-1:81];
m = [m, 81:-1:77]; m = [m, 77:-1:74]; m = [m, 74:-1:71];
m = [m, 71:-1:67]; m = [m, 67:-1:64]; m = [m, 64:-1:61];
m = [m, 61:-1:57]; m = [m, 57:-1:54]; m = [m, 54:-1:51];
m = [m, 51:-1:47]; m = [m, 47:-1:44]; m = [m, 44:-1:42];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:29]';
CI_Tscore_95_AS_611 = []; CI_Tscore_95_AS_611 = [T,mini,maxi];
%% SER - Compute T-score CI 95% CI 6-11-years
i = []; mini = []; m = []; m = [m,76:-1:67]; m = [m, 67:-1:58]; 
m = [m,58:-1:49]; m = [m,49:-1:40]; m = [m,40:-1:31]; m = [m,31:-1:24];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 87;  m = [m, 87:-1:78]; m = [m, 78:-1:69];
m = [m, 69:-1:60]; m = [m, 60:-1:51]; m = [m, 51:-1:42];
m = [m, 42:-1:36]; 

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:28]';
CI_Tscore_95_SER_611 = []; CI_Tscore_95_SER_611 = [T,mini,maxi];
%% AL - Compute T-score CI 95% CI 6-11-years
i = []; mini = []; m = [];m = 69:-1:68; m = [m, 68:-1:63]; 
m = [m,63:-1:59]; m = [m,59:-1:54]; m = [m,54:-1:49]; m = [m,49:-1:44];
m = [m,44:-1:39]; m = [m,39:-1:34]; m = [m,34:-1:32];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 84:-1:81; m = [m, 81:-1:76];
m = [m, 76:-1:71]; m = [m, 71:-1:66]; m = [m, 66:-1:61];
m = [m, 61:-1:56]; m = [m, 56:-1:51]; m = [m, 51:-1:46];  

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [82:-1:37]';
CI_Tscore_95_AL_611 = []; CI_Tscore_95_AL_611 = [T,mini,maxi];
%% ST - Compute T-score CI 95% CI 6-11-years
i = []; mini = []; m = []; m = 67; m = [m,67:-1:63]; m = [m, 63:-1:59]; 
m = [m,59:-1:55]; m = [m,55:-1:52]; m = [m,52:-1:48]; m = [m,48:-1:44];
m = [m,44:-1:40]; m = [m,40:-1:36]; m = [m,36:-1:33]; m = [m,33:-1:31];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 83:-1:82; m = [m, 82:-1:79];
m = [m, 79:-1:75]; m = [m, 75:-1:71]; m = [m, 71:-1:67];
m = [m, 67:-1:64]; m = [m, 64:-1:60]; m = [m, 60:-1:56]; 
m = [m, 56:-1:52]; m = [m, 52:-1:48]; m = [m, 48:-1:47];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [82:-1:36]';
CI_Tscore_95_ST_611 = []; CI_Tscore_95_ST_611 = [T,mini,maxi];
%% BR - Compute T-score CI 95% CI 6-11-years
i = []; mini = []; m = []; m = 73:-1:64; m = [m, 64:-1:53]; 
m = [m,53:-1:43]; m = [m,43:-1:33]; m = [m,33:-1:32]; 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 84:-1:77; m = [m, 77:-1:67];
m = [m, 67:-1:57]; m = [m, 57:-1:47]; m = [m, 47:-1:43];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [81:-1:36]';
CI_Tscore_95_BR_611 = []; CI_Tscore_95_BR_611 = [T,mini,maxi];
%% SS - Compute T-score CI 95% CI 6-11-years
i = []; mini = []; m = []; m = 71:-1:69; m = [m, 69:-1:65]; 
m = [m,65:-1:60]; m = [m,60:-1:56]; m = [m,56:-1:51]; m = [m,51:-1:46];
m = [m,46:-1:42]; m = [m,42:-1:37]; m = [m,37:-1:33];   
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 86:-1:85;  m = [m, 85:-1:81]; m = [m, 81:-1:76];
m = [m, 76:-1:72]; m = [m, 72:-1:67]; m = [m, 67:-1:63]; 
m = [m, 63:-1:58]; m = [m, 58:-1:54]; m = [m, 54:-1:49];
m = [m, 49];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:39]';
CI_Tscore_95_SS_611 = []; CI_Tscore_95_SS_611 = [T,mini,maxi];
%% AT - Compute T-score CI 95% CI 6-11-years
i = []; mini = []; m = []; m = 76:-1:73; m = [m, 73:-1:63]; 
m = [m,63:-1:53]; m = [m,53:-1:43]; m = [m,43:-1:32]; m = [m,32:-1:22];
 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 88:-1:78; m = [m, 78:-1:68];
m = [m, 68:-1:57]; m = [m, 57:-1:47]; m = [m, 47:-1:37]; 
m = [m, 37:-1:34]; 

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:26]';
CI_Tscore_95_AT_611 = []; CI_Tscore_95_AT_611 = [T,mini,maxi];
%% SC - Compute T-score CI 95% CI 12-18-years
i = []; mini = []; m = []; m = 78:-1:74; m = [m, 74:-1:59]; 
m = [m, 59:-1:43]; m = [m,43:-1:27]; m = [m,27:-1:26];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 88:-1:73; m = [m, 73:-1:57];
m = [m,57:-1:41]; m = [m,41:-1:35];
for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:29]';
CI_Tscore_95_SC_1218 = []; CI_Tscore_95_SC_1218 = [T,mini,maxi];

%% UB - Compute T-score CI 95% CI 12-18-years
i = []; mini = []; m = []; m = 78:-1:75; m = [m, 75:-1:59]; 
m = [m,59:-1:43]; m = [m,43:-1:29];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 88:-1:72; m = [m, 72:-1:57];
m = [m,57:-1:41]; m = [m,41:-1:39];
for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:33]';
CI_Tscore_95_UB_1218 = []; CI_Tscore_95_UB_1218 = [T,mini,maxi];
%% SR - Compute T-score CI 95% CI 12-18-years
i = []; mini = []; m = []; m = 78:-1:65; m = [m, 65:-1:52]; 
m = [m,52:-1:39]; m = [m,39:-1:25];  m = [m,25:-1:22]; 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 88:-1:75; m = [m, 75:-1:61];
m = [m,61:-1:48]; m = [m,48:-1:35]; m = [m,35:-1:32];
for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
%
T = []; T = [85:-1:25]';
CI_Tscore_95_SR_1218 = []; CI_Tscore_95_SR_1218 = [T,mini,maxi];
%% TOT - Compute T-score CI 95% CI 12-18-years
i = []; mini = []; m = []; m = 81:-1:54; m = [m, 54:-1:22]; 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 87:-1:80; m = [m, 80:-1:46];
m = [m, 46:-1:29];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:25]';
CI_Tscore_95_TOT_1218 = []; CI_Tscore_95_TOT_1218 = [T,mini,maxi];
%% DSM - Compute T-score CI 95% CI 12-18-years
i = []; mini = []; m = []; m = 79:-1:68; m = [m, 68:-1:49];
m = [m, 49:-1:30]; m = [m, 30:-1:24];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 88:-1:70; m = [m, 70:-1:51];
m = [m, 51:-1:32]; 
for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:27]';
CI_Tscore_95_DSM_1218 = []; CI_Tscore_95_DSM_1218 = [T,mini,maxi];
%% PS - Compute T-score CI 95% CI 12-18-years
i = []; mini = []; m = [];  m = 74; m = [m,74:-1:67]; m = [m, 67:-1:59]; 
m = [m,59:-1:52]; m = [m,52:-1:45]; m = [m,45:-1:37]; m = [m,37:-1:30]; 
m = [m,30:-1:27]; 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 87:-1:85; m = [m, 85:-1:77];
m = [m, 77:-1:70]; m = [m, 70:-1:63]; m = [m, 63:-1:55];
m = [m, 55:-1:48]; m = [m, 48:-1:41]; m = [m, 41:-1:40];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:31]';
CI_Tscore_95_PS_1218 = []; CI_Tscore_95_PS_1218 = [T,mini,maxi];
%% AS - Compute T-score CI 95% CI 12-18-years
i = []; mini = []; m = []; m = 66:-1:65; m = [m, 65:-1:61]; 
m = [m,61:-1:58]; m = [m,58:-1:54]; m = [m,54:-1:50]; m = [m,50:-1:47]; 
m = [m,47:-1:43]; m = [m,43:-1:40]; m = [m,40:-1:36]; m = [m,36:-1:33];
m = [m,33:-1:29]; m = [m,29:-1:27];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 82:-1:81; m = [m, 81:-1:78];
m = [m, 78:-1:74]; m = [m, 74:-1:71]; m = [m, 71:-1:67];
m = [m, 67:-1:64]; m = [m, 64:-1:60]; m = [m, 60:-1:57];
m = [m, 57:-1:53]; m = [m, 53:-1:50]; m = [m, 50:-1:46];
m = [m, 46:-1:43]; 

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [81:-1:31]';
CI_Tscore_95_AS_1218 = []; CI_Tscore_95_AS_1218 = [T,mini,maxi];
%% SER - Compute T-score CI 95% CI 12-18-years
i = []; mini = []; m = []; m = [m,76:-1:68]; m = [m, 68:-1:59]; 
m = [m,59:-1:50]; m = [m,50:-1:41]; m = [m,41:-1:32]; m = [m,32:-1:26];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 87:-1:86; m = [m,86:-1:77]; m = [m, 77:-1:68];
m = [m, 68:-1:59]; m = [m, 59:-1:50]; m = [m, 50:-1:41];
m = [m, 41:-1:38]; 

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:30]';
CI_Tscore_95_SER_1218 = []; CI_Tscore_95_SER_1218 = [T,mini,maxi];
%% AL - Compute T-score CI 95% CI 12-18-years
i = []; mini = []; m = []; m = [m,72:-1:71]; m = [m, 71:-1:65]; 
m = [m,65:-1:60]; m = [m,60:-1:55]; m = [m,55:-1:50]; m = [m,50:-1:44];
m = [m,44:-1:39]; m = [m,39:-1:34]; m = [m,34];
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m  = 87:-1:82; m = [m, 82:-1:77];
m = [m, 77:-1:71]; m = [m, 71:-1:66]; m = [m, 66:-1:61];
m = [m, 61:-1:56]; m = [m, 56:-1:50]; m = [m, 50:-1:48];  

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:39]';
CI_Tscore_95_AL_1218 = []; CI_Tscore_95_AL_1218 = [T,mini,maxi];
%% ST - Compute T-score CI 95% CI 12-18-years
i = []; mini = []; m = []; m = 69:-1:68; m = [m, 68:-1:64]; 
m = [m,64:-1:61]; m = [m,61:-1:57]; m = [m,57:-1:54]; m = [m,54:-1:50];
m = [m,50:-1:47]; m = [m,47:-1:43]; m = [m,43:-1:39]; m = [m,39:-1:36];
m = [m,36:-1:33]; 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 85; m = [m,85:-1:82]; m = [m,82:-1:78];
m = [m, 78:-1:75]; m = [m, 75:-1:71]; m = [m, 71:-1:68];
m = [m, 68:-1:64]; m = [m, 64:-1:61]; m = [m, 61:-1:57]; 
m = [m, 57:-1:53]; m = [m, 53:-1:50]; m = [m, 50]; 

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:39]';
CI_Tscore_95_ST_1218 = []; CI_Tscore_95_ST_1218 = [T,mini,maxi];
%% BR - Compute T-score CI 95% CI 12-18-years
i = []; mini = []; m = []; m = 74:-1:64; m = [m, 64:-1:54]; 
m = [m,54:-1:43]; m = [m,43:-1:33]; m = [m,33:-1:29]; 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 85:-1:77; m = [m, 77:-1:67];
m = [m, 67:-1:57]; m = [m, 57:-1:46]; m = [m, 46:-1:40];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [82:-1:33]';
CI_Tscore_95_BR_1218 = []; CI_Tscore_95_BR_1218 = [T,mini,maxi];
%% SS - Compute T-score CI 95% CI 12-18-years
i = []; mini = []; m = []; m = 70:-1:69; m = [m, 69:-1:65]; 
m = [m,65:-1:61]; m = [m,61:-1:57]; m = [m,57:-1:53]; m = [m,53:-1:49];
m = [m,49:-1:45]; m = [m,45:-1:41]; m = [m,41:-1:37]; m = [m,37:-1:33];    
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 86:-1:83; m = [m, 83:-1:79];
m = [m, 79:-1:75]; m = [m, 75:-1:71]; m = [m, 71:-1:67]; 
m = [m, 67:-1:63]; m = [m, 63:-1:59]; m = [m, 59:-1:55];
m = [m, 55:-1:51]; m = [m, 51:-1:49];

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:39]';
CI_Tscore_95_SS_1218 = []; CI_Tscore_95_SS_1218 = [T,mini,maxi];
%% AT - Compute T-score CI 95% CI 12-18-years
i = []; mini = []; m = []; m = 76:-1:67; m = [m, 67:-1:58]; 
m = [m,58:-1:49]; m = [m,49:-1:40]; m = [m,40:-1:31]; m = [m,31:-1:22];
m = [m,22];
 
for i = m
    mini1 = []; mini1 = i;
    mini = [mini;mini1];
end

i = []; maxi = []; m = []; m = 87; m = [m,87:-1:78]; m = [m, 78:-1:69];
m = [m, 69:-1:60]; m = [m, 60:-1:51]; m = [m, 51:-1:42]; 
m = [m, 42:-1:33]; 

for i = m
    maxi1 = []; maxi1 = i;
    maxi = [maxi;maxi1];
end
T = []; T = [85:-1:25]';
CI_Tscore_95_AT_1218 = []; CI_Tscore_95_AT_1218 = [T,mini,maxi];
%%
CI_d = []; CI_d = CI;
if part_age >= 6 && part_age <= 11
    switch CI_d
        case 90
            i = []; T_score_CI_90_SC = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_SC_611,1)
                T_score = []; T_score = CI_Tscore_90_SC_611(i,1);
                mini = []; mini = CI_Tscore_90_SC_611(i,2);
                maxi = []; maxi =CI_Tscore_90_SC_611(i,3);        
                try T_score_SC;
                    switch T_score_SC
                        case T_score
                            T_score_CI_90_SC = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Social Communication: T-score CI is ' T_score_CI_90_SC])
                    end

                catch
                    disp('Social Communication: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end

            i = []; T_score_CI_90_UB = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_UB_611,1)
                T_score = []; T_score = CI_Tscore_90_UB_611(i,1);
                mini = []; mini = CI_Tscore_90_UB_611(i,2);
                maxi = []; maxi =CI_Tscore_90_UB_611(i,3);        
                try T_score_UB;
                    switch T_score_UB
                        case T_score
                            T_score_CI_90_UB = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Unusual Behaviour: T-score CI is ' T_score_CI_90_UB])
                    end

                catch
                    disp('Unusual Behaviour: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_90_SR = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_SR_611,1)
                T_score = []; T_score = CI_Tscore_90_SR_611(i,1);
                mini = []; mini = CI_Tscore_90_SR_611(i,2);
                maxi = []; maxi =CI_Tscore_90_SR_611(i,3);        
                try T_score_SR;
                    switch T_score_SR
                        case T_score
                            T_score_CI_90_SR = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Self-Regulation: T-score CI is ' T_score_CI_90_SR])
                    end

                catch
                    disp('Self-Regulation: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_90_TOT = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_TOT_611,1)
                T_score = []; T_score = CI_Tscore_90_TOT_611(i,1);
                mini = []; mini = CI_Tscore_90_TOT_611(i,2);
                maxi = []; maxi =CI_Tscore_90_TOT_611(i,3);        
                try T_score_TOT;
                    switch T_score_TOT
                        case T_score
                            T_score_CI_90_TOT = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Total Score: T-score CI is ' T_score_CI_90_TOT])
                    end

                catch
                    disp('Total Score: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_90_DSM = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_DSM_611,1)
                T_score = []; T_score = CI_Tscore_90_DSM_611(i,1);
                mini = []; mini = CI_Tscore_90_DSM_611(i,2);
                maxi = []; maxi =CI_Tscore_90_DSM_611(i,3);        
                try T_score_DSM;
                    switch T_score_DSM
                        case T_score
                            T_score_CI_90_DSM = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['DSM-5: T-score CI is ' T_score_CI_90_DSM])
                    end

                catch
                    disp('DSM-5: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_90_PS = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_PS_611,1)
                T_score = []; T_score = CI_Tscore_90_PS_611(i,1);
                mini = []; mini = CI_Tscore_90_PS_611(i,2);
                maxi = []; maxi =CI_Tscore_90_PS_611(i,3);        
                try T_score_PS;
                    switch T_score_PS
                        case T_score
                            T_score_CI_90_PS = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Peer Socialization: T-score CI is ' T_score_CI_90_PS])
                    end

                catch
                    disp('Peer Socialization: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_90_AS = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_AS_611,1)
                T_score = []; T_score = CI_Tscore_90_AS_611(i,1);
                mini = []; mini = CI_Tscore_90_AS_611(i,2);
                maxi = []; maxi =CI_Tscore_90_AS_611(i,3);        
                try T_score_AS;
                    switch T_score_AS
                        case T_score
                            T_score_CI_90_AS = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Adult Socialization: T-score CI is ' T_score_CI_90_AS])
                    end

                catch
                    disp('Adult Socialization: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_90_SER = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_SER_611,1)
                T_score = []; T_score = CI_Tscore_90_SER_611(i,1);
                mini = []; mini = CI_Tscore_90_SER_611(i,2);
                maxi = []; maxi =CI_Tscore_90_SER_611(i,3);        
                try T_score_SER;
                    switch T_score_SER
                        case T_score
                            T_score_CI_90_SER = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Social/Emotional Reciprocity: T-score CI is ' T_score_CI_90_SER])
                    end

                catch
                    disp('Social/Emotional Reciprocity: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_90_AL = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_AL_611,1)
                T_score = []; T_score = CI_Tscore_90_AL_611(i,1);
                mini = []; mini = CI_Tscore_90_AL_611(i,2);
                maxi = []; maxi =CI_Tscore_90_AL_611(i,3);        
                try T_score_AL;
                    switch T_score_AL
                        case T_score
                            T_score_CI_90_AL = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Atypical Language: T-score CI is ' T_score_CI_90_AL])
                    end

                catch
                    if language == 0
                        disp('Atypical Language: unable to compute T-score/too much omitted responses')
                    else
                        disp('Atypical Language: speech too limited')
                    end
                    break
                end
            end
            i = []; T_score_CI_90_ST = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_ST_611,1)
                T_score = []; T_score = CI_Tscore_90_ST_611(i,1);
                mini = []; mini = CI_Tscore_90_ST_611(i,2);
                maxi = []; maxi =CI_Tscore_90_ST_611(i,3);        
                try T_score_ST;
                    switch T_score_ST
                        case T_score
                            T_score_CI_90_ST = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Stereotypy: T-score CI is ' T_score_CI_90_ST])
                    end

                catch
                    disp('Stereotypy: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end

            i = []; T_score_CI_90_BR = []; %disp('6-11 years');
            for i = 1:1:size(CI_Tscore_90_BR_611,1)
                T_score = []; T_score = CI_Tscore_90_BR_611(i,1);
                mini = []; mini = CI_Tscore_90_BR_611(i,2);
                maxi = []; maxi =CI_Tscore_90_BR_611(i,3);        
                try T_score_BR;
                    switch T_score_BR
                        case T_score
                            T_score_CI_90_BR = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Behavioural Rigidity: T-score CI is ' T_score_CI_90_BR])
                    end

                catch
                    disp('Behavioural Rigidity: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end

            i = []; T_score_CI_90_SS = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_SS_611,1)
                T_score = []; T_score = CI_Tscore_90_SS_611(i,1);
                mini = []; mini = CI_Tscore_90_SS_611(i,2);
                maxi = []; maxi =CI_Tscore_90_SS_611(i,3);        
                try T_score_SS;
                    switch T_score_SS
                        case T_score
                            T_score_CI_90_SS = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Sensory Sensitivity: T-score CI is ' T_score_CI_90_SS])
                    end

                catch
                    disp('Sensory Sensitivity: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_90_AT = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_AT_611,1)
                T_score = []; T_score = CI_Tscore_90_AT_611(i,1);
                mini = []; mini = CI_Tscore_90_AT_611(i,2);
                maxi = []; maxi =CI_Tscore_90_AT_611(i,3);        
                try T_score_AT;
                    switch T_score_AT
                        case T_score
                            T_score_CI_90_AT = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Attention: T-score CI is ' T_score_CI_90_AT])
                    end

                catch
                    disp('Attention: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
        case 95
            i = []; T_score_CI_95_SC = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_SC_611,1)
                T_score = []; T_score = CI_Tscore_95_SC_611(i,1);
                mini = []; mini = CI_Tscore_95_SC_611(i,2);
                maxi = []; maxi =CI_Tscore_95_SC_611(i,3);        
                try T_score_SC;
                    switch T_score_SC
                        case T_score
                            T_score_CI_95_SC = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Social Communication: T-score CI is ' T_score_CI_95_SC])
                    end

                catch
                    disp('Social Communication: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end

            i = []; T_score_CI_95_UB = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_UB_611,1)
                T_score = []; T_score = CI_Tscore_95_UB_611(i,1);
                mini = []; mini = CI_Tscore_95_UB_611(i,2);
                maxi = []; maxi =CI_Tscore_95_UB_611(i,3);        
                try T_score_UB;
                    switch T_score_UB
                        case T_score
                            T_score_CI_95_UB = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Unusual Behaviour: T-score CI is ' T_score_CI_95_UB])
                    end

                catch
                    disp('Unusual Behaviour: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_95_SR = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_SR_611,1)
                T_score = []; T_score = CI_Tscore_95_SR_611(i,1);
                mini = []; mini = CI_Tscore_95_SR_611(i,2);
                maxi = []; maxi =CI_Tscore_95_SR_611(i,3);        
                try T_score_SR;
                    switch T_score_SR
                        case T_score
                            T_score_CI_95_SR = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Self-Regulation: T-score CI is ' T_score_CI_95_SR])
                    end

                catch
                    disp('Self-Regulation: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_95_TOT = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_TOT_611,1)
                T_score = []; T_score = CI_Tscore_95_TOT_611(i,1);
                mini = []; mini = CI_Tscore_95_TOT_611(i,2);
                maxi = []; maxi =CI_Tscore_95_TOT_611(i,3);        
                try T_score_TOT;
                    switch T_score_TOT
                        case T_score
                            T_score_CI_95_TOT = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Total Score: T-score CI is ' T_score_CI_95_TOT])
                    end

                catch
                    disp('Total Score: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_95_DSM = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_DSM_611,1)
                T_score = []; T_score = CI_Tscore_95_DSM_611(i,1);
                mini = []; mini = CI_Tscore_95_DSM_611(i,2);
                maxi = []; maxi =CI_Tscore_95_DSM_611(i,3);        
                try T_score_DSM;
                    switch T_score_DSM
                        case T_score
                            T_score_CI_95_DSM = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['DSM-5: T-score CI is ' T_score_CI_95_DSM])
                    end

                catch
                    disp('DSM-5: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_95_PS = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_PS_611,1)
                T_score = []; T_score = CI_Tscore_95_PS_611(i,1);
                mini = []; mini = CI_Tscore_95_PS_611(i,2);
                maxi = []; maxi =CI_Tscore_95_PS_611(i,3);        
                try T_score_PS;
                    switch T_score_PS
                        case T_score
                            T_score_CI_95_PS = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Peer Socialization: T-score CI is ' T_score_CI_95_PS])
                    end

                catch
                    disp('Peer Socialization: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_95_AS = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_AS_611,1)
                T_score = []; T_score = CI_Tscore_95_AS_611(i,1);
                mini = []; mini = CI_Tscore_95_AS_611(i,2);
                maxi = []; maxi =CI_Tscore_95_AS_611(i,3);        
                try T_score_AS;
                    switch T_score_AS
                        case T_score
                            T_score_CI_95_AS = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Adult Socialization: T-score CI is ' T_score_CI_95_AS])
                    end

                catch
                    disp('Adult Socialization: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_95_SER = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_SER_611,1)
                T_score = []; T_score = CI_Tscore_95_SER_611(i,1);
                mini = []; mini = CI_Tscore_95_SER_611(i,2);
                maxi = []; maxi =CI_Tscore_95_SER_611(i,3);        
                try T_score_SER;
                    switch T_score_SER
                        case T_score
                            T_score_CI_95_SER = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Social/Emotional Reciprocity: T-score CI is ' T_score_CI_95_SER])
                    end

                catch
                    disp('Social/Emotional Reciprocity: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_95_AL = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_AL_611,1)
                T_score = []; T_score = CI_Tscore_95_AL_611(i,1);
                mini = []; mini = CI_Tscore_95_AL_611(i,2);
                maxi = []; maxi =CI_Tscore_95_AL_611(i,3);        
                try T_score_AL;
                    switch T_score_AL
                        case T_score
                            T_score_CI_95_AL = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Atypical Language: T-score CI is ' T_score_CI_95_AL])
                    end

                catch
                    if language == 0
                        disp('Atypical Language: unable to compute T-score/too much omitted responses')
                    else
                        disp('Atypical Language: speech too limited')
                    end
                    break
                end
            end
            i = []; T_score_CI_95_ST = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_ST_611,1)
                T_score = []; T_score = CI_Tscore_95_ST_611(i,1);
                mini = []; mini = CI_Tscore_95_ST_611(i,2);
                maxi = []; maxi =CI_Tscore_95_ST_611(i,3);        
                try T_score_ST;
                    switch T_score_ST
                        case T_score
                            T_score_CI_95_ST = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Stereotypy: T-score CI is ' T_score_CI_95_ST])
                    end

                catch
                    disp('Stereotypy: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end

            i = []; T_score_CI_95_BR = []; %disp('6-11 years');
            for i = 1:1:size(CI_Tscore_95_BR_611,1)
                T_score = []; T_score = CI_Tscore_95_BR_611(i,1);
                mini = []; mini = CI_Tscore_95_BR_611(i,2);
                maxi = []; maxi =CI_Tscore_95_BR_611(i,3);        
                try T_score_BR;
                    switch T_score_BR
                        case T_score
                            T_score_CI_95_BR = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Behavioural Rigidity: T-score CI is ' T_score_CI_95_BR])
                    end

                catch
                    disp('Behavioural Rigidity: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end

            i = []; T_score_CI_95_SS = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_SS_611,1)
                T_score = []; T_score = CI_Tscore_95_SS_611(i,1);
                mini = []; mini = CI_Tscore_95_SS_611(i,2);
                maxi = []; maxi =CI_Tscore_95_SS_611(i,3);        
                try T_score_SS;
                    switch T_score_SS
                        case T_score
                            T_score_CI_95_SS = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Sensory Sensitivity: T-score CI is ' T_score_CI_95_SS])
                    end

                catch
                    disp('Sensory Sensitivity: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_95_AT = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_AT_611,1)
                T_score = []; T_score = CI_Tscore_95_AT_611(i,1);
                mini = []; mini = CI_Tscore_95_AT_611(i,2);
                maxi = []; maxi =CI_Tscore_95_AT_611(i,3);        
                try T_score_AT;
                    switch T_score_AT
                        case T_score
                            T_score_CI_95_AT = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Attention: T-score CI is ' T_score_CI_95_AT])
                    end

                catch
                    disp('Attention: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
        otherwise
            disp(['Confidence Interval for T-score must be 90 or 95. You entered '... 
               num2str(CI_d)] )
    end
       
elseif part_age >= 12 && part_age <= 18
     switch CI_d
        case 90
            i = []; T_score_CI_90_SC = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_SC_1218,1)
                T_score = []; T_score = CI_Tscore_90_SC_1218(i,1);
                mini = []; mini = CI_Tscore_90_SC_1218(i,2);
                maxi = []; maxi =CI_Tscore_90_SC_1218(i,3);        
                try T_score_SC;
                    switch T_score_SC
                        case T_score
                            T_score_CI_90_SC = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Social Communication: T-score CI is ' T_score_CI_90_SC])
                    end

                catch
                    disp('Social Communication: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end

            i = []; T_score_CI_90_UB = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_UB_1218,1)
                T_score = []; T_score = CI_Tscore_90_UB_1218(i,1);
                mini = []; mini = CI_Tscore_90_UB_1218(i,2);
                maxi = []; maxi =CI_Tscore_90_UB_1218(i,3);        
                try T_score_UB;
                    switch T_score_UB
                        case T_score
                            T_score_CI_90_UB = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Unusual Behaviour: T-score CI is ' T_score_CI_90_UB])
                    end

                catch
                    disp('Unusual Behaviour: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_90_SR = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_SR_1218,1)
                T_score = []; T_score = CI_Tscore_90_SR_1218(i,1);
                mini = []; mini = CI_Tscore_90_SR_1218(i,2);
                maxi = []; maxi =CI_Tscore_90_SR_1218(i,3);        
                try T_score_SR;
                    switch T_score_SR
                        case T_score
                            T_score_CI_90_SR = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Self-Regulation: T-score CI is ' T_score_CI_90_SR])
                    end

                catch
                    disp('Self-Regulation: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_90_TOT = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_TOT_1218,1)
                T_score = []; T_score = CI_Tscore_90_TOT_1218(i,1);
                mini = []; mini = CI_Tscore_90_TOT_1218(i,2);
                maxi = []; maxi =CI_Tscore_90_TOT_1218(i,3);        
                try T_score_TOT;
                    switch T_score_TOT
                        case T_score
                            T_score_CI_90_TOT = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Total Score: T-score CI is ' T_score_CI_90_TOT])
                    end

                catch
                    disp('Total Score: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_90_DSM = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_DSM_1218,1)
                T_score = []; T_score = CI_Tscore_90_DSM_1218(i,1);
                mini = []; mini = CI_Tscore_90_DSM_1218(i,2);
                maxi = []; maxi =CI_Tscore_90_DSM_1218(i,3);        
                try T_score_DSM;
                    switch T_score_DSM
                        case T_score
                            T_score_CI_90_DSM = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['DSM-5: T-score CI is ' T_score_CI_90_DSM])
                    end

                catch
                    disp('DSM-5: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_90_PS = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_PS_1218,1)
                T_score = []; T_score = CI_Tscore_90_PS_1218(i,1);
                mini = []; mini = CI_Tscore_90_PS_1218(i,2);
                maxi = []; maxi =CI_Tscore_90_PS_1218(i,3);        
                try T_score_PS;
                    switch T_score_PS
                        case T_score
                            T_score_CI_90_PS = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Peer Socialization: T-score CI is ' T_score_CI_90_PS])
                    end

                catch
                    disp('Peer Socialization: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_90_AS = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_AS_1218,1)
                T_score = []; T_score = CI_Tscore_90_AS_1218(i,1);
                mini = []; mini = CI_Tscore_90_AS_1218(i,2);
                maxi = []; maxi =CI_Tscore_90_AS_1218(i,3);        
                try T_score_AS;
                    switch T_score_AS
                        case T_score
                            T_score_CI_90_AS = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Adult Socialization: T-score CI is ' T_score_CI_90_AS])
                    end

                catch
                    disp('Adult Socialization: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_90_SER = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_SER_1218,1)
                T_score = []; T_score = CI_Tscore_90_SER_1218(i,1);
                mini = []; mini = CI_Tscore_90_SER_1218(i,2);
                maxi = []; maxi =CI_Tscore_90_SER_1218(i,3);        
                try T_score_SER;
                    switch T_score_SER
                        case T_score
                            T_score_CI_90_SER = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Social/Emotional Reciprocity: T-score CI is ' T_score_CI_90_SER])
                    end

                catch
                    disp('Social/Emotional Reciprocity: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_90_AL = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_AL_1218,1)
                T_score = []; T_score = CI_Tscore_90_AL_1218(i,1);
                mini = []; mini = CI_Tscore_90_AL_1218(i,2);
                maxi = []; maxi =CI_Tscore_90_AL_1218(i,3);        
                try T_score_AL;
                    switch T_score_AL
                        case T_score
                            T_score_CI_90_AL = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Atypical Language: T-score CI is ' T_score_CI_90_AL])
                    end

                catch
                    if language == 0
                        disp('Atypical Language: unable to compute T-score/too much omitted responses')
                    else
                        disp('Atypical Language: speech too limited')
                    end
                    break
                end
            end
            i = []; T_score_CI_90_ST = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_ST_1218,1)
                T_score = []; T_score = CI_Tscore_90_ST_1218(i,1);
                mini = []; mini = CI_Tscore_90_ST_1218(i,2);
                maxi = []; maxi =CI_Tscore_90_ST_1218(i,3);        
                try T_score_ST;
                    switch T_score_ST
                        case T_score
                            T_score_CI_90_ST = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Stereotypy: T-score CI is ' T_score_CI_90_ST])
                    end

                catch
                    disp('Stereotypy: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end

            i = []; T_score_CI_90_BR = []; %disp('6-11 years');
            for i = 1:1:size(CI_Tscore_90_BR_1218,1)
                T_score = []; T_score = CI_Tscore_90_BR_1218(i,1);
                mini = []; mini = CI_Tscore_90_BR_1218(i,2);
                maxi = []; maxi =CI_Tscore_90_BR_1218(i,3);        
                try T_score_BR;
                    switch T_score_BR
                        case T_score
                            T_score_CI_90_BR = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Behavioural Rigidity: T-score CI is ' T_score_CI_90_BR])
                    end

                catch
                    disp('Behavioural Rigidity: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end

            i = []; T_score_CI_90_SS = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_SS_1218,1)
                T_score = []; T_score = CI_Tscore_90_SS_1218(i,1);
                mini = []; mini = CI_Tscore_90_SS_1218(i,2);
                maxi = []; maxi =CI_Tscore_90_SS_1218(i,3);        
                try T_score_SS;
                    switch T_score_SS
                        case T_score
                            T_score_CI_90_SS = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Sensory Sensitivity: T-score CI is ' T_score_CI_90_SS])
                    end

                catch
                    disp('Sensory Sensitivity: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_90_AT = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_90_AT_1218,1)
                T_score = []; T_score = CI_Tscore_90_AT_1218(i,1);
                mini = []; mini = CI_Tscore_90_AT_1218(i,2);
                maxi = []; maxi =CI_Tscore_90_AT_1218(i,3);        
                try T_score_AT;
                    switch T_score_AT
                        case T_score
                            T_score_CI_90_AT = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Attention: T-score CI is ' T_score_CI_90_AT])
                    end

                catch
                    disp('Attention: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end

        case 95
            i = []; T_score_CI_95_SC = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_SC_1218,1)
                T_score = []; T_score = CI_Tscore_95_SC_1218(i,1);
                mini = []; mini = CI_Tscore_95_SC_1218(i,2);
                maxi = []; maxi =CI_Tscore_95_SC_1218(i,3);        
                try T_score_SC;
                    switch T_score_SC
                        case T_score
                            T_score_CI_95_SC = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Social Communication: T-score CI is ' T_score_CI_95_SC])
                    end

                catch
                    disp('Social Communication: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end

            i = []; T_score_CI_95_UB = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_UB_1218,1)
                T_score = []; T_score = CI_Tscore_95_UB_1218(i,1);
                mini = []; mini = CI_Tscore_95_UB_1218(i,2);
                maxi = []; maxi =CI_Tscore_95_UB_1218(i,3);        
                try T_score_UB;
                    switch T_score_UB
                        case T_score
                            T_score_CI_95_UB = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Unusual Behaviour: T-score CI is ' T_score_CI_95_UB])
                    end

                catch
                    disp('Unusual Behaviour: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_95_SR = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_SR_1218,1)
                T_score = []; T_score = CI_Tscore_95_SR_1218(i,1);
                mini = []; mini = CI_Tscore_95_SR_1218(i,2);
                maxi = []; maxi =CI_Tscore_95_SR_1218(i,3);        
                try T_score_SR;
                    switch T_score_SR
                        case T_score
                            T_score_CI_95_SR = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Self-Regulation: T-score CI is ' T_score_CI_95_SR])
                    end

                catch
                    disp('Self-Regulation: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_95_TOT = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_TOT_1218,1)
                T_score = []; T_score = CI_Tscore_95_TOT_1218(i,1);
                mini = []; mini = CI_Tscore_95_TOT_1218(i,2);
                maxi = []; maxi =CI_Tscore_95_TOT_1218(i,3);        
                try T_score_TOT;
                    switch T_score_TOT
                        case T_score
                            T_score_CI_95_TOT = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Total Score: T-score CI is ' T_score_CI_95_TOT])
                    end

                catch
                    disp('Total Score: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_95_DSM = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_DSM_1218,1)
                T_score = []; T_score = CI_Tscore_95_DSM_1218(i,1);
                mini = []; mini = CI_Tscore_95_DSM_1218(i,2);
                maxi = []; maxi =CI_Tscore_95_DSM_1218(i,3);        
                try T_score_DSM;
                    switch T_score_DSM
                        case T_score
                            T_score_CI_95_DSM = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['DSM-5: T-score CI is ' T_score_CI_95_DSM])
                    end

                catch
                    disp('DSM-5: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_95_PS = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_PS_1218,1)
                T_score = []; T_score = CI_Tscore_95_PS_1218(i,1);
                mini = []; mini = CI_Tscore_95_PS_1218(i,2);
                maxi = []; maxi =CI_Tscore_95_PS_1218(i,3);        
                try T_score_PS;
                    switch T_score_PS
                        case T_score
                            T_score_CI_95_PS = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Peer Socialization: T-score CI is ' T_score_CI_95_PS])
                    end

                catch
                    disp('Peer Socialization: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_95_AS = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_AS_1218,1)
                T_score = []; T_score = CI_Tscore_95_AS_1218(i,1);
                mini = []; mini = CI_Tscore_95_AS_1218(i,2);
                maxi = []; maxi =CI_Tscore_95_AS_1218(i,3);        
                try T_score_AS;
                    switch T_score_AS
                        case T_score
                            T_score_CI_95_AS = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Adult Socialization: T-score CI is ' T_score_CI_95_AS])
                    end

                catch
                    disp('Adult Socialization: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_95_SER = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_SER_1218,1)
                T_score = []; T_score = CI_Tscore_95_SER_1218(i,1);
                mini = []; mini = CI_Tscore_95_SER_1218(i,2);
                maxi = []; maxi =CI_Tscore_95_SER_1218(i,3);        
                try T_score_SER;
                    switch T_score_SER
                        case T_score
                            T_score_CI_95_SER = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Social/Emotional Reciprocity: T-score CI is ' T_score_CI_95_SER])
                    end

                catch
                    disp('Social/Emotional Reciprocity: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_95_AL = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_AL_1218,1)
                T_score = []; T_score = CI_Tscore_95_AL_1218(i,1);
                mini = []; mini = CI_Tscore_95_AL_1218(i,2);
                maxi = []; maxi =CI_Tscore_95_AL_1218(i,3);        
                try T_score_AL;
                    switch T_score_AL
                        case T_score
                            T_score_CI_95_AL = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Atypical Language: T-score CI is ' T_score_CI_95_AL])
                    end

                catch
                    if language == 0
                        disp('Atypical Language: unable to compute T-score/too much omitted responses')
                    else
                        disp('Atypical Language: speech too limited')
                    end
                    break
                end
            end
            i = []; T_score_CI_95_ST = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_ST_1218,1)
                T_score = []; T_score = CI_Tscore_95_ST_1218(i,1);
                mini = []; mini = CI_Tscore_95_ST_1218(i,2);
                maxi = []; maxi =CI_Tscore_95_ST_1218(i,3);        
                try T_score_ST;
                    switch T_score_ST
                        case T_score
                            T_score_CI_95_ST = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Stereotypy: T-score CI is ' T_score_CI_95_ST])
                    end

                catch
                    disp('Stereotypy: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end

            i = []; T_score_CI_95_BR = []; %disp('6-11 years');
            for i = 1:1:size(CI_Tscore_95_BR_1218,1)
                T_score = []; T_score = CI_Tscore_95_BR_1218(i,1);
                mini = []; mini = CI_Tscore_95_BR_1218(i,2);
                maxi = []; maxi =CI_Tscore_95_BR_1218(i,3);        
                try T_score_BR;
                    switch T_score_BR
                        case T_score
                            T_score_CI_95_BR = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Behavioural Rigidity: T-score CI is ' T_score_CI_95_BR])
                    end

                catch
                    disp('Behavioural Rigidity: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end

            i = []; T_score_CI_95_SS = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_SS_1218,1)
                T_score = []; T_score = CI_Tscore_95_SS_1218(i,1);
                mini = []; mini = CI_Tscore_95_SS_1218(i,2);
                maxi = []; maxi =CI_Tscore_95_SS_1218(i,3);        
                try T_score_SS;
                    switch T_score_SS
                        case T_score
                            T_score_CI_95_SS = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Sensory Sensitivity: T-score CI is ' T_score_CI_95_SS])
                    end

                catch
                    disp('Sensory Sensitivity: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
            i = []; T_score_CI_95_AT = []; %disp('6-11 years'); 
            for i = 1:1:size(CI_Tscore_95_AT_1218,1)
                T_score = []; T_score = CI_Tscore_95_AT_1218(i,1);
                mini = []; mini = CI_Tscore_95_AT_1218(i,2);
                maxi = []; maxi =CI_Tscore_95_AT_1218(i,3);        
                try T_score_AT;
                    switch T_score_AT
                        case T_score
                            T_score_CI_95_AT = [num2str(mini) ' to ' num2str(maxi)];
                            disp(['Attention: T-score CI is ' T_score_CI_95_AT])
                    end

                catch
                    disp('Attention: unable to compute CI on T-score/too much omitted responses')
                    break
                end
            end
         otherwise 
            disp(['Confidence Interval for T-score must be 90 or 95. You entered '... 
               num2str(CI_d)] )
    end
    
else
    disp('Age is out of range for ASRS (6-18 years old)')
end
%% Table Summary 
switch CI_d
    case 90
        if ~isempty(SC_sum)
            SC_Scale = []; SC_Scale = ["Social/Communication (SC - ASRS)",...
                num2str(SC_sum), num2str(T_score_SC), num2str(Percentile_Rank_SC),...
                Classification_SC, T_score_CI_90_SC];
        else
            disp('Could not compute Social/Communication summary/too much omitted responses')
        end
        if ~isempty(UB_sum)
            UB_Scale = []; UB_Scale = ["Unusual Behaviours (UB - ASRS)",...
                num2str(UB_sum), num2str(T_score_UB), num2str(Percentile_Rank_UB),...
                Classification_UB, T_score_CI_90_UB];
         else
            disp('Could not compute Unusual Behaviours summary/too much omitted responses')
        end
        if ~isempty(SR_sum)
            SR_Scale = []; SR_Scale = ["Self-Regulation (SR - ASRS)",...
                num2str(SR_sum), num2str(T_score_SR), num2str(Percentile_Rank_SR),...
                Classification_SR, T_score_CI_90_SR];
        else
            disp('Could not compute Self-Regulation summary/too much omitted responses')
        end
        if ~isempty(SC_sum) && ~isempty(UB_sum) && ~isempty(SR_sum)
            ASRS_scales = array2table(...
                [SC_Scale;UB_Scale;SR_Scale], 'VariableNames', ...
                {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '90% T-Score CI'});
            
        elseif isempty(SC_sum) && ~isempty(UB_sum) && ~isempty(SR_sum)
               ASRS_scales = array2table(...
                    [UB_Scale;SR_Scale], 'VariableNames', ...
                    {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                    'Classification', '90% T-Score CI'});
            
        elseif ~isempty(SC_sum) && isempty(UB_sum) && ~isempty(SR_sum)
               ASRS_scales = array2table(...
                    [SC_Scale;SR_Scale], 'VariableNames', ...
                    {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                    'Classification', '90% T-Score CI'});
                
        elseif ~isempty(SC_sum) && ~isempty(UB_sum) && isempty(SR_sum)
               ASRS_scales = array2table(...
                    [SC_Scale;UB_Scale], 'VariableNames', ...
                    {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                    'Classification', '90% T-Score CI'});
        elseif isempty(SC_sum) && isempty(UB_sum) && ~isempty(SR_sum)
             ASRS_scales = array2table(...
                  SR_Scale, 'VariableNames', ...
                  {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                  'Classification', '90% T-Score CI'});
        elseif isempty(SC_sum) && ~isempty(UB_sum) && isempty(SR_sum)
               ASRS_scales = array2table(...
                    UB_Scale, 'VariableNames', ...
                    {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                    'Classification', '90% T-Score CI'});
        elseif ~isempty(SC_sum) && isempty(UB_sum) && isempty(SR_sum)
               ASRS_scales = array2table(...
                    SC_Scale, 'VariableNames', ...
                    {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                    'Classification', '90% T-Score CI'});
        elseif isempty(SC_sum) && isempty(UB_sum) && isempty(SR_sum)
               disp('Could not compute ASRS Scales because of too much omitted responses on Social/Communication, Unusual Behaviours, and Self-Regulation')
            
        end
        try TOT;
            Total_score_Scale = array2table(["Total Score (ASRS)",...
                num2str(TOT), num2str(T_score_TOT), num2str(Percentile_Rank_TOT),...
                Classification_TOT, T_score_CI_90_TOT],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '90% T-Score CI'});
            Scale_Score_Summary = [ASRS_scales;Total_score_Scale];
        catch
            disp('Could not compute Total Score Scale')
            try ASRS_scales;
                Scale_Score_Summary = ASRS_scales; 
            catch
                disp('Could not compute neither ASRS Scales nor Total Score Scale')
                Scale_Score_Summary = table(); 
            end
        end
        
        if ~isempty(DSM_sum)
            DSM_Scale = array2table(["DSM-5 Scale",...
                num2str(DSM_sum), num2str(T_score_DSM), num2str(Percentile_Rank_DSM),...
                Classification_DSM, T_score_CI_90_DSM],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '90% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;DSM_Scale];
        else
            disp('Could not compute DSM-5 Scale')
        end
        
        if ~isempty(PS_sum)
            PS_Scale = array2table(["Peer Socialization Scale (PS - Treatment Scale)",...
                num2str(PS_sum), num2str(T_score_PS), num2str(Percentile_Rank_PS),...
                Classification_PS, T_score_CI_90_PS],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '90% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;PS_Scale];
        else
            disp('Could not compute Peer Socialization Scale')
        end
        
        if ~isempty(AS_sum)
            AS_Scale = array2table(["Adult Socialization Scale (AS - Treatment Scale)",...
                num2str(AS_sum), num2str(T_score_AS), num2str(Percentile_Rank_AS),...
                Classification_AS, T_score_CI_90_AS],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '90% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;AS_Scale];
        else
            disp('Could not compute Adult Socialization Scale')
        end
        
         if ~isempty(SER_sum)
            SER_Scale = array2table(["Social/Emotional Reciprocity Scale (SER - Treatment Scale)",...
                num2str(SER_sum), num2str(T_score_SER), num2str(Percentile_Rank_SER),...
                Classification_SER, T_score_CI_90_SER],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '90% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;SER_Scale];
        else
            disp('Could not compute Social/Emotional Reciprocity Scale')
        end
        
        if ~isempty(AL_sum)
            AL_Scale = array2table(["Atypical Language Scale (AL - Treatment Scale)",...
                num2str(AL_sum), num2str(T_score_AL), num2str(Percentile_Rank_AL),...
                Classification_AL, T_score_CI_90_AL],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '90% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;AL_Scale];
        else
            disp('Could not compute Atypical Language Scale')
        end
        
        if ~isempty(ST_sum)
            ST_Scale = array2table(["Stereotypy Scale (ST - Treatment Scale)",...
                num2str(ST_sum), num2str(T_score_ST), num2str(Percentile_Rank_ST),...
                Classification_ST, T_score_CI_90_ST],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '90% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;ST_Scale];
        else
            disp('Could not compute Stereotypy Scale')
        end
        
        if ~isempty(BR_sum)
            BR_Scale = array2table(["Behavioural Rigidity Scale (BR  - Treatment Scale)",...
                num2str(BR_sum), num2str(T_score_BR), num2str(Percentile_Rank_BR),...
                Classification_BR, T_score_CI_90_BR],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '90% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;BR_Scale];
        else
            disp('Could not compute Behavioural Rigidity Scale')
        end
        
        if ~isempty(SS_sum)
            SS_Scale = array2table(["Sensory Sensitivity Scale (SS - Treatment Scale)",...
                num2str(SS_sum), num2str(T_score_SS), num2str(Percentile_Rank_SS),...
                Classification_SS, T_score_CI_90_SS],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '90% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;SS_Scale];
        else
            disp('Could not compute Sensory Sensitivity Scale')
        end
        
        if ~isempty(AT_sum)
            AT_Scale = array2table(["Attention Scale (AT - Treatment Scale)",...
                num2str(AT_sum), num2str(T_score_AT), num2str(Percentile_Rank_AT),...
                Classification_AT, T_score_CI_90_AT],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '90% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;AT_Scale];
        else
            disp('Could not compute Attention Scale')
        end     
    case 95
        if ~isempty(SC_sum)
            SC_Scale = []; SC_Scale = ["Social/Communication (SC - ASRS)",...
                num2str(SC_sum), num2str(T_score_SC), num2str(Percentile_Rank_SC),...
                Classification_SC, T_score_CI_95_SC];
        else
            disp('Could not compute Social/Communication summary/too much omitted responses')
        end
        if ~isempty(UB_sum)
            UB_Scale = []; UB_Scale = ["Unusual Behaviours (UB - ASRS)",...
                num2str(UB_sum), num2str(T_score_UB), num2str(Percentile_Rank_UB),...
                Classification_UB, T_score_CI_95_UB];
         else
            disp('Could not compute Unusual Behaviours summary/too much omitted responses')
        end
        if ~isempty(SR_sum)
            SR_Scale = []; SR_Scale = ["Self-Regulation (SR - ASRS)",...
                num2str(SR_sum), num2str(T_score_SR), num2str(Percentile_Rank_SR),...
                Classification_SR, T_score_CI_95_SR];
        else
            disp('Could not compute Self-Regulation summary/too much omitted responses')
        end
        if ~isempty(SC_sum) && ~isempty(UB_sum) && ~isempty(SR_sum)
            ASRS_scales = array2table(...
                [SC_Scale;UB_Scale;SR_Scale], 'VariableNames', ...
                {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '95% T-Score CI'});
            
        elseif isempty(SC_sum) && ~isempty(UB_sum) && ~isempty(SR_sum)
               ASRS_scales = array2table(...
                    [UB_Scale;SR_Scale], 'VariableNames', ...
                    {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                    'Classification', '95% T-Score CI'});
            
        elseif ~isempty(SC_sum) && isempty(UB_sum) && ~isempty(SR_sum)
               ASRS_scales = array2table(...
                    [SC_Scale;SR_Scale], 'VariableNames', ...
                    {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                    'Classification', '95% T-Score CI'});
                
        elseif ~isempty(SC_sum) && ~isempty(UB_sum) && isempty(SR_sum)
               ASRS_scales = array2table(...
                    [SC_Scale;UB_Scale], 'VariableNames', ...
                    {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                    'Classification', '95% T-Score CI'});
        elseif isempty(SC_sum) && isempty(UB_sum) && ~isempty(SR_sum)
             ASRS_scales = array2table(...
                  SR_Scale, 'VariableNames', ...
                  {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                  'Classification', '95% T-Score CI'});
        elseif isempty(SC_sum) && ~isempty(UB_sum) && isempty(SR_sum)
               ASRS_scales = array2table(...
                    UB_Scale, 'VariableNames', ...
                    {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                    'Classification', '95% T-Score CI'});
        elseif ~isempty(SC_sum) && isempty(UB_sum) && isempty(SR_sum)
               ASRS_scales = array2table(...
                    SC_Scale, 'VariableNames', ...
                    {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                    'Classification', '95% T-Score CI'});
        elseif isempty(SC_sum) && isempty(UB_sum) && isempty(SR_sum)
               disp('Could not compute ASRS Scales because of too much omitted responses on Social/Communication, Unusual Behaviours, and Self-Regulation')
            
        end
        try TOT;
            Total_score_Scale = array2table(["Total Score (ASRS)",...
                num2str(TOT), num2str(T_score_TOT), num2str(Percentile_Rank_TOT),...
                Classification_TOT, T_score_CI_95_TOT],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '95% T-Score CI'});
            Scale_Score_Summary = [ASRS_scales;Total_score_Scale];
        catch
            disp('Could not compute Total Score Scale')
            try ASRS_scales;
                Scale_Score_Summary = ASRS_scales; 
            catch
                disp('Could not compute neither ASRS Scales nor Total Score Scale')
                Scale_Score_Summary = table(); 
            end
        end
        
        if ~isempty(DSM_sum)
            DSM_Scale = array2table(["DSM-5 Scale",...
                num2str(DSM_sum), num2str(T_score_DSM), num2str(Percentile_Rank_DSM),...
                Classification_DSM, T_score_CI_95_DSM],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '95% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;DSM_Scale];
        else
            disp('Could not compute DSM-5 Scale')
        end
        
        if ~isempty(PS_sum)
            PS_Scale = array2table(["Peer Socialization Scale (PS - Treatment Scale)",...
                num2str(PS_sum), num2str(T_score_PS), num2str(Percentile_Rank_PS),...
                Classification_PS, T_score_CI_95_PS],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '95% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;PS_Scale];
        else
            disp('Could not compute Peer Socialization Scale')
        end
        
        if ~isempty(AS_sum)
            AS_Scale = array2table(["Adult Socialization Scale (AS - Treatment Scale)",...
                num2str(AS_sum), num2str(T_score_AS), num2str(Percentile_Rank_AS),...
                Classification_AS, T_score_CI_95_AS],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '95% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;AS_Scale];
        else
            disp('Could not compute Adult Socialization Scale')
        end
        
         if ~isempty(SER_sum)
            SER_Scale = array2table(["Social/Emotional Reciprocity Scale (SER - Treatment Scale)",...
                num2str(SER_sum), num2str(T_score_SER), num2str(Percentile_Rank_SER),...
                Classification_SER, T_score_CI_95_SER],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '95% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;SER_Scale];
        else
            disp('Could not compute Social/Emotional Reciprocity Scale')
        end
        
        if ~isempty(AL_sum)
            AL_Scale = array2table(["Atypical Language Scale (AL - Treatment Scale)",...
                num2str(AL_sum), num2str(T_score_AL), num2str(Percentile_Rank_AL),...
                Classification_AL, T_score_CI_95_AL],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '95% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;AL_Scale];
        else
            disp('Could not compute Atypical Language Scale')
        end
        
        if ~isempty(ST_sum)
            ST_Scale = array2table(["Stereotypy Scale (ST - Treatment Scale)",...
                num2str(ST_sum), num2str(T_score_ST), num2str(Percentile_Rank_ST),...
                Classification_ST, T_score_CI_95_ST],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '95% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;ST_Scale];
        else
            disp('Could not compute Stereotypy Scale')
        end
        
        if ~isempty(BR_sum)
            BR_Scale = array2table(["Behavioural Rigidity Scale (BR  - Treatment Scale)",...
                num2str(BR_sum), num2str(T_score_BR), num2str(Percentile_Rank_BR),...
                Classification_BR, T_score_CI_95_BR],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '95% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;BR_Scale];
        else
            disp('Could not compute Behavioural Rigidity Scale')
        end
        
        if ~isempty(SS_sum)
            SS_Scale = array2table(["Sensory Sensitivity Scale (SS - Treatment Scale)",...
                num2str(SS_sum), num2str(T_score_SS), num2str(Percentile_Rank_SS),...
                Classification_SS, T_score_CI_95_SS],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '95% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;SS_Scale];
        else
            disp('Could not compute Sensory Sensitivity Scale')
        end
        
        if ~isempty(AT_sum)
            AT_Scale = array2table(["Attention Scale (AT - Treatment Scale)",...
                num2str(AT_sum), num2str(T_score_AT), num2str(Percentile_Rank_AT),...
                Classification_AT, T_score_CI_95_AT],...
                'VariableNames', {'Scales', 'Raw Score', 'T-Score', 'Percentile Rank',...
                'Classification', '95% T-Score CI'});
            Scale_Score_Summary = [Scale_Score_Summary;AT_Scale];
        else
            disp('Could not compute Attention Scale')
        end  
    otherwise 
        disp('Could not compute summary because CI is neither 90 nor 95')     
        
end
writetable(Scale_Score_Summary, [name(1:14) 'summary.xlsx']);
%% Figures Summary
% Raw scores: can not be interpreted because each scale have different
% number of items --> we need standardized scores (T-scores)
% T-scores are based on a comparison to the normative sample 
% T-scores of each scale have mean of 50 and STD of 10. For instance, a
% T-score of 50 corresponds the the 50th quantile of the normative sample
% Percentile rank is the percentage of children in the normative sample
% who earned a raw score that is the same or lower. For instance, a
% percentile rank of 65 meand that 65% of the children in the normative
% sample earned a raw score that is equal or lower. Percentile ranks are
% usefull describing the relative standing of an individual in the
% normative sample distribution. T-scores are better for comparing a
% youth's scores accross scales on ASRS. 
% Confidence intervals: measurements error. Provide at a specific level of
% probability a range of scores within which the true score is expected to 
% fall. 90% CI is recommended. 

% --> bar graph 
% --> texto explicativo con los sintomas que trabajar 
% Mekkochart para percentiles y tabla para interpretacion 
% https://uk.mathworks.com/help/rptgen/ug/create-a-report-generator.html
% https://uk.mathworks.com/matlabcentral/answers/1642305-how-do-i-export-matlab-plots-and-tables-from-matlab-to-pdf-directly
% https://datavizcatalogue.com/methods/marimekko_chart.html
% https://uk.mathworks.com/matlabcentral/fileexchange/71330-marimekko
% table interpretativa con las preguntas especificas (puntos a mejorar), un bar chart y un
% mekkochart
T_scores_tot = [];
for i = 1:1:size(Scale_Score_Summary,1) %Scales
    x = []; x = str2num(table2array(Scale_Score_Summary(i,3)));
    T_scores_tot = [T_scores_tot,x]; 
end

i = []; e_tot_sp = []; 
for i = 1:1:size(Scale_Score_Summary,1)
     e = []; e = table2array(Scale_Score_Summary(i,1));
     switch e
        case "Social/Communication (SC - ASRS)"
            e2 = "Social/Comunicación (SC)";
            e_tot_sp = [e_tot_sp;e2]; 
         case  "Unusual Behaviours (UB - ASRS)"
            e2 = "Conductas Inusuales (CI)";
            e_tot_sp = [e_tot_sp;e2]; 
         case "Self-Regulation (SR - ASRS)"
              e2 = "Autorregulación (AR)";
              e_tot_sp = [e_tot_sp;e2]; 
         case "Total Score (ASRS)"
              e2 = "Puntuación Total (SC+CI+AR)";
              e_tot_sp = [e_tot_sp;e2]; 
         case "DSM-5 Scale"
              e2 = "DSM-5";
              e_tot_sp = [e_tot_sp;e2]; 
         case "Peer Socialization Scale (PS - Treatment Scale)"
              e2 = "Socialización con Compañeros (SOC)";
              e_tot_sp = [e_tot_sp;e2]; 
         case "Adult Socialization Scale (AS - Treatment Scale)"
              e2 = "Socialización con Adultos (SOA)";
              e_tot_sp = [e_tot_sp;e2]; 
         case "Social/Emotional Reciprocity Scale (SER - Treatment Scale)"
              e2 = "Reciprocidad Social/Emocional (RSE)";
              e_tot_sp = [e_tot_sp;e2]; 
         case "Atypical Language Scale (AL - Treatment Scale)"
              e2 = "Lenguaje Atípico (LA)";
              e_tot_sp = [e_tot_sp;e2];
         case "Stereotypy Scale (ST - Treatment Scale)"
              e2 = "Estereotipia (ET)";
              e_tot_sp = [e_tot_sp;e2];
         case "Behavioural Rigidity Scale (BR  - Treatment Scale)"
              e2 = "Rigidez Conductual (RC)";
              e_tot_sp = [e_tot_sp;e2];
         case "Sensory Sensitivity Scale (SS - Treatment Scale)"
              e2 = "Sensibilidad Sensorial (SS)";
              e_tot_sp = [e_tot_sp;e2];
         case "Attention Scale (AT - Treatment Scale)"
              e2 = "Atención (AT)";
              e_tot_sp = [e_tot_sp;e2];
      end

end
   
y1 = [];
for i = 1:1:size(Scale_Score_Summary,1) %Scales
    x = []; x = convertStringsToChars(e_tot_sp(i,1));
    y1{1,i} = x; 
end

y = []; y = categorical(y1);
y = reordercats(y,y1);
%% Bargraph
figure('WindowState','maximized')
b = []; b = barh(y,T_scores_tot, 0.5,'FaceColor', [0.3010 0.7450 0.9330]);
xlabel('Puntuación estandarizada','fontweight','bold','fontsize',40)
set(get(gca, 'YAxis'), 'FontWeight', 'bold');
% set(gca,'fontweight','bold', 'YDir','reverse');
set(gca,'YDir','reverse');
% xlim([0 max(T_scores_tot)+5])
xlim([0 max(T_scores_tot)+17]) %FOR PDF REPORT
% xtips1 = b(1).YEndPoints + 0.3;
xtips1 = b(1).YEndPoints + 1.2; %FOR PDF REPORT
ytips1 = b(1).XEndPoints; 
labels1 = string(b(1).YData);
% text(xtips1,ytips1,labels1,'VerticalAlignment','middle')
text(xtips1,ytips1,labels1,'VerticalAlignment','middle','FontSize', 45)
% FOR PSDF REPORT

% xtips2 = b(1).YEndPoints + 1.5; 
i = []; labels2 = []; 
xtips2 = b(1).YEndPoints + 4.6; %FOR PDF REPORT
switch CI_d
    case 90
        T_tot = [convertCharsToStrings(T_score_CI_90_SC);
                convertCharsToStrings(T_score_CI_90_UB);
                convertCharsToStrings(T_score_CI_90_SR);
                convertCharsToStrings(T_score_CI_90_TOT);
                convertCharsToStrings(T_score_CI_90_DSM);
                convertCharsToStrings(T_score_CI_90_PS);
                convertCharsToStrings(T_score_CI_90_AS);
                convertCharsToStrings(T_score_CI_90_SER);
                convertCharsToStrings(T_score_CI_90_AL);
                convertCharsToStrings(T_score_CI_90_ST);
                convertCharsToStrings(T_score_CI_90_BR);
                convertCharsToStrings(T_score_CI_90_SS);
                convertCharsToStrings(T_score_CI_90_AT)];
        e_tot = [];
         for i = 1:1:size(T_tot,1)
             e = []; e = T_tot(i,1);
             e2 = join(['(' replace(convertCharsToStrings(e),...
                        ' to ', '-') ')'], '');
             e_tot= [e_tot,e2]; 
         end
        labels2 = []; labels2 = e_tot; 
%         text(xtips2,ytips1,labels2,'VerticalAlignment','middle')
        text(xtips2,ytips1,labels2,'VerticalAlignment','middle',...
            'FontSize', 45) %FOR PDF REPORT
  
    case 95
        T_tot = [convertCharsToStrings(T_score_CI_95_SC);
                convertCharsToStrings(T_score_CI_95_UB);
                convertCharsToStrings(T_score_CI_95_SR);
                convertCharsToStrings(T_score_CI_95_TOT);
                convertCharsToStrings(T_score_CI_95_DSM);
                convertCharsToStrings(T_score_CI_95_PS);
                convertCharsToStrings(T_score_CI_95_AS);
                convertCharsToStrings(T_score_CI_95_SER);
                convertCharsToStrings(T_score_CI_95_AL);
                convertCharsToStrings(T_score_CI_95_ST);
                convertCharsToStrings(T_score_CI_95_BR);
                convertCharsToStrings(T_score_CI_95_SS);
                convertCharsToStrings(T_score_CI_95_AT)];
        e_tot = [];
         for i = 1:1:size(T_tot,1)
             e = []; e = T_tot(i,1);
             e2 = join(['(' replace(convertCharsToStrings(e),...
                        ' to ', '-') ')'], '');
             e_tot= [e_tot,e2]; 
         end
        labels2 = []; labels2 = e_tot; 
%         text(xtips2,ytips1,labels2,'VerticalAlignment','middle')
        text(xtips2,ytips1,labels2,'VerticalAlignment','middle',...
            'FontSize', 45)%FOR PDF REPORT
        
end

title('Severidad de síntomas asociados con el espectro autista',...
    'fontsize',35)
%saveas(b, 'T-score.fig')
% close all
%% Mekkochart
nombre = complete_name; figure('WindowState','maximized');
i = []; class_sp = []; 
for i = 1:1:size(Scale_Score_Summary,1)
     e = []; e = table2array(Scale_Score_Summary(i,5));
     switch e
        case "Average"
            e2 = "Promedio";
            class_sp = [class_sp;e2]; 
         case  "Low"
            e2 = "Bajo";
            class_sp = [class_sp;e2]; 
         case "Slightly Elevated"
              e2 = "Ligeramente Elevado";
              class_sp = [class_sp;e2]; 
         case "Elevated"
              e2 = "Elevado";
              class_sp = [class_sp;e2]; 
         case "Very Elevated"
              e2 = "Muy Elevado";
              class_sp = [class_sp;e2]; 
      end

end
P_tot = []; 
P_tot = [[Percentile_Rank_SC,100-Percentile_Rank_SC]',...
        [Percentile_Rank_UB,100-Percentile_Rank_UB]',...
        [Percentile_Rank_SR,100-Percentile_Rank_SR]',...
        [Percentile_Rank_TOT,100-Percentile_Rank_TOT]',...
        [Percentile_Rank_DSM,100-Percentile_Rank_DSM]',...
        [Percentile_Rank_PS,100-Percentile_Rank_PS]',...
        [Percentile_Rank_AS,100-Percentile_Rank_AS]',...
        [Percentile_Rank_SER,100-Percentile_Rank_SER]',...
        [Percentile_Rank_AL,100-Percentile_Rank_AL]',...
        [Percentile_Rank_ST,100-Percentile_Rank_ST]',...
        [Percentile_Rank_BR,100-Percentile_Rank_BR]',...
        [Percentile_Rank_SS,100-Percentile_Rank_SS]',...
        [Percentile_Rank_AT,100-Percentile_Rank_AT]'];
    
groups = cell(1,size(e_tot_sp,1)); i = []; 
for i = 1:1:size(e_tot_sp,1)
    groups{1,i} = convertStringsToChars(e_tot_sp(i,1));
end
i = []; 
for i = 1:1:size(groups,2)
    e = []; e = groups{1,i};
    switch e
        case 'Socialización con Compañeros (SOC)'
            groups{1,i} = ['Socialización' newline 'con Compañeros (SOC)'];
        case 'Puntuación Total (SC+CI+AR)'
            groups{1,i} = ['Puntuación' newline 'Total (SC+CI+AR)'];
        case 'Socialización con Adultos (SOA)'
            groups{1,i} = ['Socialización' newline 'con Adultos (SOA)'];
        case 'Reciprocidad Social/Emocional (RSE)'
            groups{1,i} = ['Reciprocidad' newline 'Social/Emocional (RSE)'];
    end
end

marimekkoh(P_tot,class_sp(:,1),groups);
xticks([0 .1 .2 .3 .4 .5 .6 .7 .8 .9 10]);
xticklabels({'0','10','20','30','40','50','60', '70', '80', '90', '100'});
yticks(''); yticklabels({''});
% legend(join([nombre ' y niño(a)s con sintomatología igual o menor'],''), ...
%     'Niño(a)s con sintomatología más pronunciada', 'Position', ...
%     [0.129432624113475 0.934269662921348 0.27770390070922 0.0499999999999999],...
%     'FontSize', 11.5);
legend(join([nombre ' y niño(a)s con sintomatología igual o menor'],''), ...
    'Niño(a)s con sintomatología más pronunciada', 'Position', ...
    [0.250221631205674 0.899812734082396 0.561835106382979 0.0919475655430712],...
    'FontSize', 23, 'FontWeight', 'bold'); %FOR PDF REPORT
set(gca,'Units', 'normalized', 'Position', [0.25 0.08 0.74 0.8150] );
mek = []; mek = gcf;

%saveas(mek, 'Percentiles.fig')
close all

%% Peer Socialization (PS)
TG_PS_tot = []; 
if part_age >= 6 && part_age <= 11
    treat_PS = [];
    disp('6-11 years'); range = []; range = '6 y 11 años'; i = [];
    for i = 1:1:size(PS_tot,1)
        e = []; e = PS_tot(i,:);
        if e ~= 5
            switch true
                case e >= 3 && e <= 4 && i == 1
                    TG = []; TG = "Mejorar la capacidad de buscar a otros niños para socializar.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];                 
                case e >= 3 && e <= 4 && i == 2 && language == 0
                    TG = []; TG = "Mejorar la capacidad de mantener una conversación apropiada con otros niños.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];    
                case e >= 3 && e <= 4 && i == 3 && language == 0
                    TG = []; TG = "Mejorar las relaciones sociales con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG]; 
                case e >= 2 && e <= 4 && i == 4 && language == 0
                    TG = []; TG = "Aumentar el tiempo de juego con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG]; 
                case e >= 3 && e <= 4&& i == 5 && language == 0
                    TG = []; TG = "Mejorar la habilidad de entender y responder adecuadamente al humor.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
                case e >= 3 && e <= 4&& i == 6 && language == 0
                    TG = []; TG = "Mejorar la habilidad de encontrar temas apropiados al hablar con otros niños.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
                case e >= 3 && e <= 4&& i == 7 && language == 0
                    TG = []; TG = "Mejorar el juego interactivo con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
                case e >= 2 && e <= 4&& i == 8 && language == 0
                    TG = []; TG = "Mejorar la calidad de las interacciones con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
                case e >= 2 && e <= 4&& i == 9 && language == 0
                    TG = []; TG = "Mejorar la habilidad de responder adecuadamente al hablar con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
                    
   
                case e >= 3 && e <= 4 && i == 2 && language == 1
                    TG = []; TG = "Mejorar las relaciones sociales con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG]; 
                case e >= 2 && e <= 4 && i == 3 && language == 1
                    TG = []; TG = "Aumentar el tiempo de juego con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG]; 
                case e >= 3 && e <= 4&& i == 4 && language == 1
                    TG = []; TG = "Mejorar la habilidad de entender y responder adecuadamente al humor.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
                case e >= 3 && e <= 4&& i == 5 && language == 1
                    TG = []; TG = "Mejorar el juego interactivo con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
                case e >= 2 && e <= 4&& i == 6 && language == 1
                    TG = []; TG = "Mejorar la calidad de las interacciones con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
                case e >= 2 && e <= 4&& i == 7 && language == 1
                    TG = []; TG = "Mejorar la habilidad de responder adecuadamente al hablar con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
            end
        end
    end
    if ~isempty(treat_PS)
        Scale = []; Scale = categorical(repmat(["Socialización con Compañeros (SOC)"], 1,size(treat_PS,1))');
    else
        Scale = []; Scale = categorical(repmat(["Socialización con Compañeros (SOC)"],1,1)');
    end
    if ~isempty(treat_PS)
        TG_PS_tot = array2table([Scale,categorical(convertCharsToStrings(treat_PS))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        TG_PS_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    end
    
elseif part_age >= 12 && part_age <= 18
    treat_PS = [];
    disp('12-18 years'); range = []; range = '12 y 18 años'; i = [];
    for i = 1:1:size(PS_tot,1)
        e = []; e = PS_tot(i,:);
        if e ~= 5
            switch true
                case e >= 3 && e <= 4 && i == 1
                    TG = []; TG = "Mejorar la capacidad de buscar a otros niños para socializar.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];                 
                  case e >= 3 && e <= 4 && i == 2 && language == 0
                    TG = []; TG = "Mejorar la capacidad de mantener una conversación apropiada con otros niños.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];    
                case e >= 3 && e <= 4 && i == 3 && language == 0
                    TG = []; TG = "Mejorar las relaciones sociales con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG]; 
                case e >= 2 && e <= 4 && i == 4 && language == 0
                    TG = []; TG = "Aumentar el tiempo de juego con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG]; 
                case e >= 3 && e <= 4&& i == 5 && language == 0
                    TG = []; TG = "Mejorar la habilidad de entender y responder adecuadamente al humor.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
                case e >= 3 && e <= 4&& i == 6 && language == 0
                    TG = []; TG = "Mejorar la habilidad de encontrar temas apropiados al hablar con otros niños.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
                case e >= 3 && e <= 4&& i == 7 && language == 0
                    TG = []; TG = "Mejorar el juego interactivo con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
                case e >= 2 && e <= 4&& i == 8 && language == 0
                    TG = []; TG = "Mejorar la calidad de las interacciones con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
                case e >= 2 && e <= 4&& i == 9 && language == 0
                    TG = []; TG = "Mejorar la habilidad de responder adecuadamente al hablar con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
                    
   
                case e >= 3 && e <= 4 && i == 2 && language == 1
                    TG = []; TG = "Mejorar las relaciones sociales con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG]; 
                case e >= 2 && e <= 4 && i == 3 && language == 1
                    TG = []; TG = "Aumentar el tiempo de juego con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG]; 
                case e >= 3 && e <= 4&& i == 4 && language == 1
                    TG = []; TG = "Mejorar la habilidad de entender y responder adecuadamente al humor.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
                case e >= 3 && e <= 4&& i == 5 && language == 1
                    TG = []; TG = "Mejorar el juego interactivo con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
                case e >= 2 && e <= 4&& i == 6 && language == 1
                    TG = []; TG = "Mejorar la calidad de las interacciones con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
                case e >= 2 && e <= 4&& i == 7 && language == 1
                    TG = []; TG = "Mejorar la habilidad de responder adecuadamente al hablar con compañeros.";
                    disp(TG) %treatement target
                    treat_PS = [treat_PS;TG];
            end
        end
    end
    if ~isempty(treat_PS)
        Scale = []; Scale = categorical(repmat(["Socialización con Compañeros (SOC)"], 1,size(treat_PS,1))');
    else
        Scale = []; Scale = categorical(repmat(["Socialización con Compañeros (SOC)"],1,1)');
    end
    if ~isempty(treat_PS)
        TG_PS_tot = array2table([Scale,categorical(convertCharsToStrings(treat_PS))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        TG_PS_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    end 

else
    disp('Age is out of range for ASRS (6-18 years old)')
end
% Adult Socialization (AS)
TG_AS_tot = []; 
if part_age >= 6 && part_age <= 11
    treat_AS = [];
    disp('6-11 years'); range = []; range = '6 y 11 años'; i = [];
    for i = 1:1:size(AS_tot,1)
        e = []; e = AS_tot(i,:);
        if e ~= 5
            switch true
                case e >= 3 && e <= 4 && i == 1
                    TG = []; TG = "Reducir la frecuencia de ocurrencia de situaciones problemáticas con adultos.";
                    disp(TG) %treatement target
                    treat_AS = [treat_AS;TG];                 
                case e >= 2 && e <= 4 && i == 2
                    TG = []; TG = "Mejorar la habilidad de responder adecuadademente al hablar con adultos.";
                    disp(TG) %treatement target
                    treat_AS = [treat_AS;TG];    
                case e >= 3 && e <= 4 && i == 3 
                    TG = []; TG = "Mejorar la habilidad de mantener contacto visual durante conversaciones problemáticas con adultos.";
                    disp(TG) %treatement target
                    treat_AS = [treat_AS;TG]; 
                case e >= 3 && e <= 4 && i == 4 && language == 0
                    TG = []; TG = "Mejorar la habilidad de elegir temas de conversaciones apropiados a la hora de conversar con adultos.";
                    disp(TG) %treatement target
                    treat_AS = [treat_AS;TG]; 
                case e >= 3 && e <= 4&& i == 5 && language == 0
                    TG = []; TG = "Mejorar la habilidad de mantener una conversación apropiada con adultos.";
                    disp(TG) %treatement target
                    treat_AS = [treat_AS;TG];
                case e >= 2 && e <= 4&& i == 6 && language == 0
                    TG = []; TG = "Mejorar las relaciones sociales con adultos.";
                    disp(TG) %treatement target
                    treat_AS = [treat_AS;TG];
               
                case e >= 2 && e <= 4&& i == 4 && language == 1
                    TG = []; TG = "Mejorar las relaciones sociales con adultos.";
                    disp(TG) %treatement target
                    treat_AS = [treat_AS;TG];

            end
        end
    end
    if ~isempty(treat_AS)
        Scale = []; Scale = categorical(repmat(["Socialización con Adultos (SOA)"], 1,size(treat_AS,1))');
    else
        Scale = []; Scale = categorical(repmat(["Socialización con Adultos (SOA)"],1,1)');
    end
    if ~isempty(treat_AS)
        TG_AS_tot = array2table([Scale,categorical(convertCharsToStrings(treat_AS))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        TG_AS_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    end
    
elseif part_age >= 12 && part_age <= 18
    treat_AS = [];
    disp('12-18 years'); range = []; range = '12 y 18 años'; i = [];
    for i = 1:1:size(AS_tot,1)
        e = []; e = AS_tot(i,:);
        if e ~= 5
            switch true
                case e >= 3 && e <= 4 && i == 1
                    TG = []; TG = "Reducir la frecuencia de ocurrencia de situaciones problemáticas con adultos.";
                    disp(TG) %treatement target
                    treat_AS = [treat_AS;TG];                 
                case e >= 2 && e <= 4 && i == 2
                    TG = []; TG = "Mejorar la habilidad de responder adecuadademente al hablar con adultos.";
                    disp(TG) %treatement target
                    treat_AS = [treat_AS;TG];    
                case e >= 3 && e <= 4 && i == 3
                    TG = []; TG = "Mejorar la habilidad de mantener contacto visual durante conversaciones problemáticas con adultos.";
                    disp(TG) %treatement target
                    treat_AS = [treat_AS;TG]; 
                case e >= 3 && e <= 4 && i == 4 && language == 0
                    TG = []; TG = "Mejorar la habilidad de elegir temas de conversaciones apropiados a la hora de conversar con adultos.";
                    disp(TG) %treatement target
                    treat_AS = [treat_AS;TG]; 
                case e >= 3 && e <= 4&& i == 5 && language == 0
                    TG = []; TG = "Mejorar la habilidad de mantener una conversación apropiada con adultos.";
                    disp(TG) %treatement target
                    treat_AS = [treat_AS;TG];
                case e >= 2 && e <= 4&& i == 6 && language == 0
                    TG = []; TG = "Mejorar las relaciones sociales con adultos.";
                    disp(TG) %treatement target
                    treat_AS = [treat_AS;TG];
               
                case e >= 2 && e <= 4&& i == 4 && language == 1
                    TG = []; TG = "Mejorar las relaciones sociales con adultos.";
                    disp(TG) %treatement target
                    treat_AS = [treat_AS;TG];
            end
        end
    end
    if ~isempty(treat_AS)
        Scale = []; Scale = categorical(repmat(["Socialización con Adultos (SOA)"], 1,size(treat_AS,1))');
    else
        Scale = []; Scale = categorical(repmat(["Socialización con Adultos (SOA)"],1,1)');
    end
    if ~isempty(treat_AS)
        TG_AS_tot = array2table([Scale,categorical(convertCharsToStrings(treat_AS))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        TG_AS_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    end
else
    disp('Age is out of range for ASRS (6-18 years old)')
end
% Social/Emotional Reciprocity (SER)
TG_SER_tot = []; 
if part_age >= 6 && part_age <= 11
    treat_SER = [];
    disp('6-11 years'); range = []; range = '6 y 11 años'; i = [];
    for i = 1:1:size(SER_tot,1)
        e = []; e = SER_tot(i,:);
        if e ~= 5
            switch true
                case e >= 3 && e <= 4 && i == 1
                    TG = []; TG = "Mejorar las expresiones emocionales apropiadas durante interacciones sociales.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];                 
                case e >= 2 && e <= 4 && i == 2
                    TG = []; TG = "Mejorar la habilidad de compartir experiencias agradables con otros.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];    
                case e >= 2 && e <= 4 && i == 3
                    TG = []; TG = "Mejorar la habilidad de mirar a los demás al conversar con ellos.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG]; 
                case e >= 3 && e <= 4 && i == 4
                    TG = []; TG = "Mejorar la habilidad de mirar a los demás cuando le hablan.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG]; 
                case e >= 3 && e <= 4&& i == 5
                    TG = []; TG = "Mejorar la habilidad de apreciar y entender la opinión de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 6
                    TG = []; TG = "Mejorar la habilidad de entender los sentimientos y las emociones de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 7
                    TG = []; TG = "Mejorar la habilidad de reconocer adecuadamente señales sociales.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 8
                    TG = []; TG = "Desarrollar la habilidad de responder adecuadamente a las ideas y sentimientos de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 9
                    TG = []; TG = "Mejorar la percepción y comprensión de los pensamientos y sentimientos de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 2 && e <= 4&& i == 10
                    TG = []; TG = "Mejorar la habilidad de compartir y expresar placer al interactuar con los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 11
                    TG = []; TG = "Mejorar la habilidad de responder adecuadamente a los intereses de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 2 && e <= 4&& i == 12
                    TG = []; TG = "Mejorar la habilidad de sonreir apropiadamente en situaciones sociales.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 13
                    TG = []; TG = "Mejorar la habilidad de mirar a los demás apropiadamente al interactuar con ellos.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4 && i == 3 && language == 1
                    TG = []; TG = "Mejorar la habilidad de mirar a los demás cuando le hablan.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG]; 
                case e >= 3 && e <= 4&& i == 4 && language == 1
                    TG = []; TG = "Mejorar la habilidad de apreciar y entender la opinión de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 5 && language == 1
                    TG = []; TG = "Mejorar la habilidad de entender los sentimientos y las emociones de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 6 && language == 1
                    TG = []; TG = "Mejorar la habilidad de reconocer adecuadamente señales sociales.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 7 && language == 1
                    TG = []; TG = "Desarrollar la habilidad de responder adecuadamente a las ideas y sentimientos de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 8 && language == 1
                    TG = []; TG = "Mejorar la percepción y comprensión de los pensamientos y sentimientos de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 9 && language == 1
                    TG = []; TG = "Mejorar la habilidad de compartir y expresar placer al interactuar con los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 10 && language == 1
                    TG = []; TG = "Mejorar la habilidad de responder adecuadamente a los intereses de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 2 && e <= 4&& i == 11 && language == 1
                    TG = []; TG = "Mejorar la habilidad de sonreir apropiadamente en situaciones sociales.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                 case e >= 3 && e <= 4&& i == 12 && language == 1
                    TG = []; TG = "Mejorar la habilidad de mirar a los demás apropiadamente al interactuar con ellos.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
            end
        end
    end
    if ~isempty(treat_SER)
        Scale = []; Scale = categorical(repmat(["Reciprocidad Social/Emocional (RSE)"], 1,size(treat_SER,1))');
    else
        Scale = []; Scale = categorical(repmat(["Reciprocidad Social/Emocional (RSE)"],1,1)');
    end
    if ~isempty(treat_SER)
        TG_SER_tot = array2table([Scale,categorical(convertCharsToStrings(treat_SER))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        TG_SER_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    end
    
elseif part_age >= 12 && part_age <= 18
    treat_SER = [];
    disp('12-18 years'); range = []; range = '12 y 18 años'; i = []    
    for i = 1:1:size(SER_tot,1)
        e = []; e = SER_tot(i,:);
        if e ~= 5
            switch true
                case e >= 3 && e <= 4 && i == 1
                    TG = []; TG = "Mejorar las expresiones emocionales apropiadas durante interacciones sociales.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];                 
                case e >= 3 && e <= 4 && i == 2
                    TG = []; TG = "Mejorar la habilidad de compartir experiencias agradables con otros.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];    
                case e >= 2 && e <= 4 && i == 3 && language == 0
                    TG = []; TG = "Mejorar la habilidad de mirar a los demás al conversar con ellos.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG]; 
                case e >= 3 && e <= 4 && i == 4 && language == 0
                    TG = []; TG = "Mejorar la habilidad de mirar a los demás cuando le hablan.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG]; 
                case e >= 3 && e <= 4&& i == 5 && language == 0
                    TG = []; TG = "Mejorar la habilidad de apreciar y entender la opinión de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 6 && language == 0
                    TG = []; TG = "Mejorar la habilidad de entender los sentimientos y las emociones de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 7 && language == 0
                    TG = []; TG = "Mejorar la habilidad de reconocer adecuadamente señales sociales.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 8 && language == 0
                    TG = []; TG = "Desarrollar la habilidad de responder adecuadamente a las ideas y sentimientos de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 9 && language == 0
                    TG = []; TG = "Mejorar la percepción y comprensión de los pensamientos y sentimientos de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 10 && language == 0
                    TG = []; TG = "Mejorar la habilidad de compartir y expresar placer al interactuar con los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 11 && language == 0
                    TG = []; TG = "Mejorar la habilidad de responder adecuadamente a los intereses de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 2 && e <= 4&& i == 12 && language == 0
                    TG = []; TG = "Mejorar la habilidad de sonreir apropiadamente en situaciones sociales.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 13 && language == 0
                    TG = []; TG = "Mejorar la habilidad de mirar a los demás apropiadamente al interactuar con ellos.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                    
                case e >= 3 && e <= 4 && i == 3 && language == 1
                    TG = []; TG = "Mejorar la habilidad de mirar a los demás cuando le hablan.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG]; 
                case e >= 3 && e <= 4&& i == 4 && language == 1
                    TG = []; TG = "Mejorar la habilidad de apreciar y entender la opinión de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 5 && language == 1
                    TG = []; TG = "Mejorar la habilidad de entender los sentimientos y las emociones de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 6 && language == 1
                    TG = []; TG = "Mejorar la habilidad de reconocer adecuadamente señales sociales.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 7 && language == 1
                    TG = []; TG = "Desarrollar la habilidad de responder adecuadamente a las ideas y sentimientos de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 8 && language == 1
                    TG = []; TG = "Mejorar la percepción y comprensión de los pensamientos y sentimientos de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 9 && language == 1
                    TG = []; TG = "Mejorar la habilidad de compartir y expresar placer al interactuar con los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 3 && e <= 4&& i == 10 && language == 1
                    TG = []; TG = "Mejorar la habilidad de responder adecuadamente a los intereses de los demás.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                case e >= 2 && e <= 4&& i == 11 && language == 1
                    TG = []; TG = "Mejorar la habilidad de sonreir apropiadamente en situaciones sociales.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
                 case e >= 3 && e <= 4&& i == 12 && language == 1
                    TG = []; TG = "Mejorar la habilidad de mirar a los demás apropiadamente al interactuar con ellos.";
                    disp(TG) %treatement target
                    treat_SER = [treat_SER;TG];
            end
        end
    end
    if ~isempty(treat_SER)
        Scale = []; Scale = categorical(repmat(["Reciprocidad Social/Emocional (RSE)"], 1,size(treat_SER,1))');
    else
        Scale = []; Scale = categorical(repmat(["Reciprocidad Social/Emocional (RSE)"],1,1)');
    end
    if ~isempty(treat_SER)
        TG_SER_tot = array2table([Scale,categorical(convertCharsToStrings(treat_SER))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        TG_SER_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    end

else
    disp('Age is out of range for ASRS (6-18 years old)')
end
% Atypical Language (AL)
TG_AL_tot = []; 
if part_age >= 6 && part_age <= 11
    treat_AL = [];
    disp('6-11 years'); range = []; range = '6 y 11 años'; i = [];
    for i = 1:1:size(AL_tot,1)
        e = []; e = AL_tot(i,:);
        if e ~= 5
            switch true
                case e >= 3 && e <= 4 && i == 1
                    TG = []; TG = "Mejorar las habilidades de lenguaje hacia un nivel apropiado para su edad.";
                    disp(TG) %treatement target
                    treat_AL = [treat_AL;TG];                 
                case e >= 2 && e <= 4 && i == 2
                    TG = []; TG = "Demostrar tono y ritmo apropiado al hablar.";
                    disp(TG) %treatement target
                    treat_AL = [treat_AL;TG];    
                case e >= 2 && e <= 4 && i == 3
                    TG = []; TG = "Aumentar el lenguaje social apropiado reduciendo la frecuencia de frases repetitivas y fuera de contexto.";
                    disp(TG) %treatement target
                    treat_AL = [treat_AL;TG]; 
                case e >= 3 && e <= 4 && i == 4
                    TG = []; TG = "Reducir la ecolalia.";
                    disp(TG) %treatement target
                    treat_AL = [treat_AL;TG]; 
                case e >= 3 && e <= 4&& i == 5
                    TG = []; TG = "Reducir la frecuencia de preguntas fuera de contexto.";
                    disp(TG) %treatement target
                    treat_AL = [treat_AL;TG];
                case e >= 2 && e <= 4&& i == 6
                    TG = []; TG = "Aumentar el uso apropiado de pronombres.";
                    disp(TG) %treatement target
                    treat_AL = [treat_AL;TG];
            end
        end
    end
    if ~isempty(treat_AL)
        Scale = []; Scale = categorical(repmat(["Lenguaje Atípico (LA)"], 1,size(treat_AL,1))');
    else
        Scale = []; Scale = categorical(repmat(["Lenguaje Atípico (LA)"],1,1)');
    end
    if ~isempty(treat_AL)
        TG_AL_tot = array2table([Scale,categorical(convertCharsToStrings(treat_AL))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        if language == 0
            TG_AL_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                            {'Tipo de síntoma', ['Objetivos para el tratamiento']});
        else
            TG_AL_tot = array2table([Scale,categorical("Nivel de lenguaje demasiado limitado para evaluar objetivos específicos para el tratamiento.")], 'VariableNames', ...
                    {'Tipo de síntoma', ['Objetivos para el tratamiento']});
        end
    end
    
elseif part_age >= 12 && part_age <= 18
    treat_AL = [];
    disp('12-18 years'); range = []; range = '12 y 18 años'; i = [];
    for i = 1:1:size(AL_tot,1)
        e = []; e = AL_tot(i,:);
        if e ~= 5
            switch true
                case e >= 2 && e <= 4 && i == 1
                    TG = []; TG = "Mejorar las habilidades de lenguaje hacia un nivel apropiado para su edad.";
                    disp(TG) %treatement target
                    treat_AL = [treat_AL;TG];                 
                case e >= 2 && e <= 4 && i == 2
                    TG = []; TG = "Demostrar tono y ritmo apropiado al hablar.";
                    disp(TG) %treatement target
                    treat_AL = [treat_AL;TG];    
                case e >= 2 && e <= 4 && i == 3
                    TG = []; TG = "Aumentar el lenguaje social apropiado reduciendo la frecuencia de frases repetitivas y fuera de contexto.";
                    disp(TG) %treatement target
                    treat_AL = [treat_AL;TG]; 
                case e >= 2 && e <= 4 && i == 4
                    TG = []; TG = "Reducir la ecolalia.";
                    disp(TG) %treatement target
                    treat_AL = [treat_AL;TG]; 
                case e >= 3 && e <= 4&& i == 5
                    TG = []; TG = "Reducir la frecuencia de preguntas fuera de contexto.";
                    disp(TG) %treatement target
                    treat_AL = [treat_AL;TG];
                case e >= 2 && e <= 4&& i == 6
                    TG = []; TG = "Aumentar el uso apropiado de pronombres.";
                    disp(TG) %treatement target
                    treat_AL = [treat_AL;TG];
            end
        end
    end

    if ~isempty(treat_AL)
        Scale = []; Scale = categorical(repmat(["Lenguaje Atípico (LA)"], 1,size(treat_AL,1))');
    else
        Scale = []; Scale = categorical(repmat(["Lenguaje Atípico (LA)"],1,1)');
    end
    if ~isempty(treat_AL)
        TG_AL_tot = array2table([Scale,categorical(convertCharsToStrings(treat_AL))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        if language == 0
            TG_AL_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                            {'Tipo de síntoma', ['Objetivos para el tratamiento']});
        else
            TG_AL_tot = array2table([Scale,categorical("Nivel de lenguaje demasiado limitado para evaluar objetivos específicos para el tratamiento.")], 'VariableNames', ...
                    {'Tipo de síntoma', ['Objetivos para el tratamiento']});
        end
    end
else
    disp('Age is out of range for ASRS (6-18 years old)')
end
% Stereotypy (ST)
TG_ST_tot = []; 
if part_age >= 6 && part_age <= 11
    treat_ST = [];
    disp('6-11 years'); range = []; range = '6 y 11 años'; i = [];
    for i = 1:1:size(ST_tot,1)
        e = []; e = ST_tot(i,:);
        if e ~= 5
            switch true
                case e >= 2 && e <= 4 && i == 1
                    TG = []; TG = "Reducir las conductas autoestimulantes (por ejemplo aletear las manos).";
                    disp(TG) %treatement target
                    treat_ST = [treat_ST;TG];                 
                case e >= 3 && e <= 4 && i == 2
                    TG = []; TG = "Adquirir flexibilidad para el cambio y no obsesionarse con un mismo tema.";
                    disp(TG) %treatement target
                    treat_ST = [treat_ST;TG];    
                case e >= 3 && e <= 4 && i == 3
                    TG = []; TG = "Interactuar adecuadamente con juguetes y objetos.";
                    disp(TG) %treatement target
                    treat_ST = [treat_ST;TG]; 
                case e >= 3 && e <= 4 && i == 4
                    TG = []; TG = "Reducir comportamientos de orden excesivo.";
                    disp(TG) %treatement target
                    treat_ST = [treat_ST;TG]; 
                case e >= 3 && e <= 4&& i == 5
                    TG = []; TG = "Reducir el uso inapropiado de objetos.";
                    disp(TG) %treatement target
                    treat_ST = [treat_ST;TG];
            end
        end
    end
    if ~isempty(treat_ST)
        Scale = []; Scale = categorical(repmat(["Estereotipia (ET)"], 1,size(treat_ST,1))');
    else
        Scale = []; Scale = categorical(repmat(["Estereotipia (ET)"],1,1)');
    end
    if ~isempty(treat_ST)
        TG_ST_tot = array2table([Scale,categorical(convertCharsToStrings(treat_ST))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        TG_ST_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    end
    
elseif part_age >= 12 && part_age <= 18
    treat_ST = [];
    disp('12-18 years'); range = []; range = '12 y 18 años'; i = [];
    
     for i = 1:1:size(ST_tot,1)
        e = []; e = ST_tot(i,:);
        if e ~= 5
            switch true
                case e >= 2 && e <= 4 && i == 1
                    TG = []; TG = "Reducir las conductas autoestimulantes (por ejemplo aletear las manos).";
                    disp(TG) %treatement target
                    treat_ST = [treat_ST;TG];                 
                case e >= 3 && e <= 4 && i == 2
                    TG = []; TG = "Adquirir flexibilidad para el cambio y no obsesionarse con un mismo tema.";
                    disp(TG) %treatement target
                    treat_ST = [treat_ST;TG];    
                case e >= 3 && e <= 4 && i == 3
                    TG = []; TG = "Interactuar adecuadamente con juguetes y objetos.";
                    disp(TG) %treatement target
                    treat_ST = [treat_ST;TG]; 
                case e >= 2 && e <= 4 && i == 4
                    TG = []; TG = "Reducir comportamientos de orden excesivo.";
                    disp(TG) %treatement target
                    treat_ST = [treat_ST;TG]; 
                case e >= 2 && e <= 4&& i == 5
                    TG = []; TG = "Reducir el uso inapropiado de objetos.";
                    disp(TG) %treatement target
                    treat_ST = [treat_ST;TG];
            end
        end
    end
    if ~isempty(treat_ST)
        Scale = []; Scale = categorical(repmat(["Estereotipia (ET)"], 1,size(treat_ST,1))');
    else
        Scale = []; Scale = categorical(repmat(["Estereotipia (ET)"],1,1)');
    end
    if ~isempty(treat_ST)
        TG_ST_tot = array2table([Scale,categorical(convertCharsToStrings(treat_ST))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        TG_ST_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    end
    
    
    
else
    disp('Age is out of range for ASRS (6-18 years old)')
end
% Behavioural Rigidity Scale (BR)
TG_BR_tot = []; 
if part_age >= 6 && part_age <= 11
    treat_BR = [];
    disp('6-11 years'); range = []; range = '6 y 11 años'; i = [];
    for i = 1:1:size(BR_tot,1)
        e = []; e = BR_tot(i,:);
        if e ~= 5
            switch true
                case e >= 3 && e <= 4 && i == 1
                    TG = []; TG = "Reducir la intensidad de las reacciones a cambios de rutina.";
                    disp(TG) %treatement target
                    treat_BR = [treat_BR;TG];                 
                case e >= 3 && e <= 4 && i == 2
                    TG = []; TG = "Mejorar la habilidad de considar perspectivas generales y enfocarse menos en detalles.";
                    disp(TG) %treatement target
                    treat_BR = [treat_BR;TG];    
                case e >= 3 && e <= 4 && i == 3
                    TG = []; TG = "Aumentar flexibilidad y reducir rigidez para poder participar a actividades diversas.";
                    disp(TG) %treatement target
                    treat_BR = [treat_BR;TG]; 
                case e >= 3 && e <= 4 && i == 4
                    TG = []; TG = "Desarrollar la habilidad de apreciar y entender perspectivas amplias en situaciones problemáticas.";
                    disp(TG) %treatement target
                    treat_BR = [treat_BR;TG]; 
                case e >= 3 && e <= 4&& i == 5
                    TG = []; TG = "Mejorar la habilidad de lidiar con cambios inesperados.";
                    disp(TG) %treatement target
                    treat_BR = [treat_BR;TG];
                case e >= 3 && e <= 4&& i == 6
                    TG = []; TG = "Reducir la rigidez y la falta de flexibilidad para aceptar cambios de rutina.";
                    disp(TG) %treatement target
                    treat_BR = [treat_BR;TG];
                case e >= 3 && e <= 4&& i == 7
                    TG = []; TG = "Desarrollar la habilidad de manejar con flexibilidad cambios de rutina.";
                    disp(TG) %treatement target
                    treat_BR = [treat_BR;TG];
                case e >= 3 && e <= 4&& i == 8
                    TG = []; TG = "Reducir la necesitad de siempre tener consigo objetos específicos.";
                    disp(TG) %treatement target
                    treat_BR = [treat_BR;TG];
            end
        end
    end
    if ~isempty(treat_BR)
        Scale = []; Scale = categorical(repmat(["Rigidez Conductual (RC)"], 1,size(treat_BR,1))');
    else
        Scale = []; Scale = categorical(repmat(["Rigidez Conductual (RC)"],1,1)');
    end
    if ~isempty(treat_BR)
        TG_BR_tot = array2table([Scale,categorical(convertCharsToStrings(treat_BR))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        TG_BR_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    end
    
elseif part_age >= 12 && part_age <= 18
    treat_BR = [];
    disp('12-18 years'); range = []; range = '12 y 18 años'; i = [];
        for i = 1:1:size(BR_tot,1)
        e = []; e = BR_tot(i,:);
        if e ~= 5
            switch true
                case e >= 3 && e <= 4 && i == 1
                    TG = []; TG = "Reducir la intensidad de las reacciones a cambios de rutina.";
                    disp(TG) %treatement target
                    treat_BR = [treat_BR;TG];                 
                case e >= 3 && e <= 4 && i == 2
                    TG = []; TG = "Mejorar la habilidad de considar perspectivas generales y enfocarse menos en detalles.";
                    disp(TG) %treatement target
                    treat_BR = [treat_BR;TG];    
                case e >= 3 && e <= 4 && i == 3
                    TG = []; TG = "Aumentar flexibilidad y reducir rigidez para poder participar a actividades diversas.";
                    disp(TG) %treatement target
                    treat_BR = [treat_BR;TG]; 
                case e >= 3 && e <= 4 && i == 4
                    TG = []; TG = "Desarrollar la habilidad de apreciar y entender perspectivas amplias en situaciones problemáticas.";
                    disp(TG) %treatement target
                    treat_BR = [treat_BR;TG]; 
                case e >= 3 && e <= 4&& i == 5
                    TG = []; TG = "Mejorar la habilidad de lidiar con cambios inesperados.";
                    disp(TG) %treatement target
                    treat_BR = [treat_BR;TG];
                case e >= 3 && e <= 4&& i == 6
                    TG = []; TG = "Reducir la rigidez y la falta de flexibilidad para aceptar cambios de rutina.";
                    disp(TG) %treatement target
                    treat_BR = [treat_BR;TG];
                case e >= 3 && e <= 4&& i == 7
                    TG = []; TG = "Desarrollar la habilidad de manejar con flexibilidad cambios de rutina.";
                    disp(TG) %treatement target
                    treat_BR = [treat_BR;TG];
                case e >= 2 && e <= 4&& i == 8
                    TG = []; TG = "Reducir la necesitad de siempre tener consigo objetos específicos.";
                    disp(TG) %treatement target
                    treat_BR = [treat_BR;TG];
            end
        end
    end
    if ~isempty(treat_BR)
        Scale = []; Scale = categorical(repmat(["Rigidez Conductual (RC)"], 1,size(treat_BR,1))');
    else
        Scale = []; Scale = categorical(repmat(["Rigidez Conductual (RC)"],1,1)');
    end
    if ~isempty(treat_BR)
        TG_BR_tot = array2table([Scale,categorical(convertCharsToStrings(treat_BR))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        TG_BR_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    end
   
else
    disp('Age is out of range for ASRS (6-18 years old)')
end
% Sensory Sensitivity (SS)
TG_SS_tot = []; 
if part_age >= 6 && part_age <= 11
    treat_SS = [];
    disp('6-11 years'); range = []; range = '6 y 11 años'; i = [];
    for i = 1:1:size(SS_tot,1)
        e = []; e = SS_tot(i,:);
        if e ~= 5
            switch true
                case e >= 3 && e <= 4 && i == 1
                    TG = []; TG = "Reducir la sensibilidad táctil a la ropa.";
                    disp(TG) %treatement target
                    treat_SS = [treat_SS;TG];                 
                case e >= 2 && e <= 4 && i == 2
                    TG = []; TG = "Aumentar respuestas apropiadas a estimulaciones táctiles.";
                    disp(TG) %treatement target
                    treat_SS = [treat_SS;TG];    
                case e >= 2 && e <= 4 && i == 3
                    TG = []; TG = "Reducir la pica (ingestión de objetos no comestibles).";
                    disp(TG) %treatement target
                    treat_SS = [treat_SS;TG]; 
                case e >= 2 && e <= 4 && i == 4
                    TG = []; TG = "Mejorar la habilidad de lidiar con olores comunes.";
                    disp(TG) %treatement target
                    treat_SS = [treat_SS;TG]; 
                case e >= 2 && e <= 4&& i == 5
                    TG = []; TG = "Mejorar la habilidad de tolerar el tacto y contactos físicos normales.";
                    disp(TG) %treatement target
                    treat_SS = [treat_SS;TG];
                case e >= 3 && e <= 4&& i == 6
                    TG = []; TG = "Mejorar la habilidad de reponder adecuadamente a sonidos fuertes.";
                    disp(TG) %treatement target
                    treat_SS = [treat_SS;TG];
            end
        end
    end
    if ~isempty(treat_SS)
        Scale = []; Scale = categorical(repmat(["Sensibilidad Sensorial (SS)"], 1,size(treat_SS,1))');
    else
        Scale = []; Scale = categorical(repmat(["Sensibilidad Sensorial (SS)"],1,1)');
    end
    if ~isempty(treat_SS)
        TG_SS_tot = array2table([Scale,categorical(convertCharsToStrings(treat_SS))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        TG_SS_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    end
    
elseif part_age >= 12 && part_age <= 18
    treat_SS = [];
    disp('12-18 years'); range = []; range = '12 y 18 años'; i = [];
        for i = 1:1:size(SS_tot,1)
        e = []; e = SS_tot(i,:);
        if e ~= 5
            switch true
                case e >= 2 && e <= 4 && i == 1
                    TG = []; TG = "Reducir la sensibilidad táctil a la ropa.";
                    disp(TG) %treatement target
                    treat_SS = [treat_SS;TG];                 
                case e >= 2 && e <= 4 && i == 2
                    TG = []; TG = "Aumentar respuestas apropiadas a estimulaciones táctiles.";
                    disp(TG) %treatement target
                    treat_SS = [treat_SS;TG];    
                case e >= 1 && e <= 4 && i == 3
                    TG = []; TG = "Reducir la pica (ingestión de objetos no comestibles).";
                    disp(TG) %treatement target
                    treat_SS = [treat_SS;TG]; 
                case e >= 2 && e <= 4 && i == 4
                    TG = []; TG = "Mejorar la habilidad de lidiar con olores comunes.";
                    disp(TG) %treatement target
                    treat_SS = [treat_SS;TG]; 
                case e >= 2 && e <= 4&& i == 5
                    TG = []; TG = "Mejorar la habilidad de tolerar el tacto y contactos físicos normales.";
                    disp(TG) %treatement target
                    treat_SS = [treat_SS;TG];
                case e >= 2 && e <= 4&& i == 6
                    TG = []; TG = "Mejorar la habilidad de reponder adecuadamente a sonidos fuertes.";
                    disp(TG) %treatement target
                    treat_SS = [treat_SS;TG];

            end
        end
    end
    if ~isempty(treat_SS)
        Scale = []; Scale = categorical(repmat(["Sensibilidad Sensorial (SS)"], 1,size(treat_SS,1))');
    else
        Scale = []; Scale = categorical(repmat(["Sensibilidad Sensorial (SS)"],1,1)');
    end
    if ~isempty(treat_SS)
        TG_SS_tot = array2table([Scale,categorical(convertCharsToStrings(treat_SS))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        TG_SS_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    end
else
    disp('Age is out of range for ASRS (6-18 years old)')
end
% Atention (AT)
TG_AT_tot = []; 
if part_age >= 6 && part_age <= 11
    treat_AT = [];
    disp('6-11 years'); range = []; range = '6 y 11 años'; i = [];
    for i = 1:1:size(AT_tot,1)
        e = []; e = AT_tot(i,:);
        if e ~= 5
            switch true
                case e >= 3 && e <= 4 && i == 1
                    TG = []; TG = "Desarrollar hablidades de organización más eficientes.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];                 
                case e >= 3 && e <= 4 && i == 2
                    TG = []; TG = "Aumentar la conformidad y el seguimiento adecuado de instrucciones.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];    
                case e >= 3 && e <= 4 && i == 3
                    TG = []; TG = "Aumentar la participación en tareas que requieren un esfuerzo prolongado.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG]; 
                case e >= 3 && e <= 4 && i == 4
                    TG = []; TG = "Mejorar la habilidad de recordar cómo realizar tareas simples.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG]; 
                case e >= 4 && e <= 4&& i == 5
                    TG = []; TG = "Mejorar la habilidad de mantener la atención aún cuando haya distracciones.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];
                case e >= 4 && e <= 4&& i == 6
                    TG = []; TG = "Mejorar la habilidad de mantener la atención al completar tareas escolares, domésticas y otros tipos de actividades exigiridas.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];
                case e >= 4 && e <= 4&& i == 7
                    TG = []; TG = "Reducir errores por descuidado y prisa en tareas escolares.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];
                case e >= 4 && e <= 4&& i == 8
                    TG = []; TG = "Mejorar la habilidad de completar tareas escolares y domésticas exitosamente.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];
                case e >= 3 && e <= 4&& i == 9
                    TG = []; TG = "Mejorar la habilidad de escuchar cuando le hablan.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];
                case e >= 3 && e <= 4&& i == 10
                    TG = []; TG = "Mejorar la habilidad de mantener la atención durante actividades agradables.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];
                case e >= 3 && e <= 4&& i == 11
                    TG = []; TG = "Aumentar la finalización de tareas.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];
            end
        end
    end
    if ~isempty(treat_AT)
        Scale = []; Scale = categorical(repmat(["Atención (AT)"], 1,size(treat_AT,1))');
    else
        Scale = []; Scale = categorical(repmat(["Atención (AT)"],1,1)');
    end
    if ~isempty(treat_AT)
        TG_AT_tot = array2table([Scale,categorical(convertCharsToStrings(treat_AT))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        TG_AT_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    end
    
elseif part_age >= 12 && part_age <= 18
    treat_AT = [];
    disp('12-18 years'); range = []; range = '12 y 18 años'; i = [];
    for i = 1:1:size(AT_tot,1)
        e = []; e = AT_tot(i,:);
        if e ~= 5
            switch true
                case e >= 4 && e <= 4 && i == 1
                    TG = []; TG = "Desarrollar hablidades de organización más eficientes.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];                 
                case e >= 3 && e <= 4 && i == 2
                    TG = []; TG = "Aumentar la conformidad y el seguimiento adecuado de instrucciones.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];    
                case e >= 3 && e <= 4 && i == 3
                    TG = []; TG = "Aumentar la participación en tareas que requieren un esfuerzo prolongado.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG]; 
                case e >= 3 && e <= 4 && i == 4
                    TG = []; TG = "Mejorar la habilidad de recordar cómo realizar tareas simples.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG]; 
                case e >= 4 && e <= 4&& i == 5
                    TG = []; TG = "Mejorar la habilidad de mantener la atención aún cuando haya distracciones.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];
                case e >= 4 && e <= 4&& i == 6
                    TG = []; TG = "Mejorar la habilidad de mantener la atención al completar tareas escolares, domésticas y otros tipos de actividades exigiridas.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];
                case e >= 4 && e <= 4&& i == 7
                    TG = []; TG = "Reducir errores por descuidado y prisa en tareas escolares.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];
                case e >= 4 && e <= 4&& i == 8
                    TG = []; TG = "Mejorar la habilidad de completar tareas escolares y domésticas exitosamente.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];
                case e >= 3 && e <= 4&& i == 9
                    TG = []; TG = "Mejorar la habilidad de escuchar cuando le hablan.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];
                case e >= 2 && e <= 4&& i == 10
                    TG = []; TG = "Mejorar la habilidad de mantener la atención durante actividades agradables.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];
                case e >= 3 && e <= 4&& i == 11
                    TG = []; TG = "Aumentar la finalización de tareas.";
                    disp(TG) %treatement target
                    treat_AT = [treat_AT;TG];
            end
        end
    end
    if ~isempty(treat_AT)
        Scale = []; Scale = categorical(repmat(["Atención (AT)"], 1,size(treat_AT,1))');
    else
        Scale = []; Scale = categorical(repmat(["Atención (AT)"],1,1)');
    end
    if ~isempty(treat_AT)
        TG_AT_tot = array2table([Scale,categorical(convertCharsToStrings(treat_AT))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        TG_AT_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    end
else
    disp('Age is out of range for ASRS (6-18 years old)')
end

% Self-Regulation (SR)
TG_SR_tot = []; 
if part_age >= 6 && part_age <= 11
    treat_SR = [];
    disp('6-11 years'); range = []; range = '6 y 11 años'; i = [];
    if language == 0
        items = [3 4 15 17];
    else 
        items = [3 4 14 16]; %Limited speech
    end
    for i = items
        e = []; e = SR_tot(i,:);
        if e ~= 5
            switch true
                case e >= 3 && e <= 4 && i == 3
                    TG = []; TG = "Desarrollar habilidades para resolver conflictos para reducir peleas y conflictos con otros niños.";
                    disp(TG) %treatement target
                    treat_SR = [treat_SR;TG];                 
                case e >= 3 && e <= 4 && i == 4
                    TG = []; TG = "Mejorar la habilidad de esperar su turno cuando sea necesario.";
                    disp(TG) %treatement target
                    treat_SR = [treat_SR;TG];    
                case e >= 4 && e <= 4 && i == 15  && language == 0
                    TG = []; TG = "Reducir comportamientos intrusivos y/o pertubadores.";
                    disp(TG) %treatement target
                    treat_SR = [treat_SR;TG]; 
                case e >= 3 && e <= 4 && i == 17 && language == 0
                    TG = []; TG = "Desarrollar la habilidad de quedarse quieto cuando sea requerido.";
                    disp(TG) %treatement target
                    treat_SR = [treat_SR;TG]; 
                case e >= 4 && e <= 4 && i == 14  && language == 1
                    TG = []; TG = "Reducir comportamientos intrusivos y/o pertubadores.";
                    disp(TG) %treatement target
                    treat_SR = [treat_SR;TG]; 
                case e >= 3 && e <= 4 && i == 16 && language == 1
                    TG = []; TG = "Desarrollar la habilidad de quedarse quieto cuando sea requerido.";
                    disp(TG) %treatement target
                    treat_SR = [treat_SR;TG]; 
            end
        end
    end
    if ~isempty(treat_SR)
        Scale = []; Scale = categorical(repmat(["Autorregulación (AR)"], 1,size(treat_SR,1))');
    else
        Scale = []; Scale = categorical(repmat(["Autorregulación (AR)"],1,1)');
    end
    if ~isempty(treat_SR)
        TG_SR_tot = array2table([Scale,categorical(convertCharsToStrings(treat_SR))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        TG_SR_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    end
    
elseif part_age >= 12 && part_age <= 18
    treat_SR = [];
    disp('12-18 years'); range = []; range = '12 y 18 años'; i = [];
    if language == 0
        items = [3 4 15 17];
    else 
        items = [3 4 14 16]; %Limited speech
    end
    for i = items
        e = []; e = SR_tot(i,:);
        if e ~= 5
            switch true
                case e >= 3 && e <= 4 && i == 3
                    TG = []; TG = "Desarrollar habilidades para resolver conflictos para reducir peleas y conflictos con otros niños.";
                    disp(TG) %treatement target
                    treat_SR = [treat_SR;TG];                 
                case e >= 3 && e <= 4 && i == 4
                    TG = []; TG = "Mejorar la habilidad de esperar su turno cuando sea necesario.";
                    disp(TG) %treatement target
                    treat_SR = [treat_SR;TG];    
                case e >= 4 && e <= 4 && i == 15  && language == 0
                    TG = []; TG = "Reducir comportamientos intrusivos y/o pertubadores.";
                    disp(TG) %treatement target
                    treat_SR = [treat_SR;TG]; 
                case e >= 3 && e <= 4 && i == 17 && language == 0
                    TG = []; TG = "Desarrollar la habilidad de quedarse quieto cuando sea requerido.";
                    disp(TG) %treatement target
                    treat_SR = [treat_SR;TG]; 
                case e >= 4 && e <= 4 && i == 14  && language == 1
                    TG = []; TG = "Reducir comportamientos intrusivos y/o pertubadores.";
                    disp(TG) %treatement target
                    treat_SR = [treat_SR;TG]; 
                case e >= 3 && e <= 4 && i == 16 && language == 1
                    TG = []; TG = "Desarrollar la habilidad de quedarse quieto cuando sea requerido.";
                    disp(TG) %treatement target
                    treat_SR = [treat_SR;TG]; 
            end
        end
    end
    if ~isempty(treat_SR)
        Scale = []; Scale = categorical(repmat(["Autorregulación (AR)"], 1,size(treat_SR,1))');
    else
        Scale = []; Scale = categorical(repmat(["Autorregulación (AR)"],1,1)');
    end
    if ~isempty(treat_SR)
        TG_SR_tot = array2table([Scale,categorical(convertCharsToStrings(treat_SR))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        TG_SR_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    end
else
    disp('Age is out of range for ASRS (6-18 years old)')
end
% Social/Communication (SC)
TG_SC_tot = []; 
if part_age >= 6 && part_age <= 11
    treat_SC = [];
    disp('6-11 years'); range = []; range = '6 y 11 años'; i = [];
    if language == 0
        items = [6 16];
    else 
        items = []; %Limited speech
    end
    for i = items
        e = []; e = SC_tot(i,:);
        if e ~= 5
            switch true
                case e >= 3 && e <= 4 && i == 6
                    TG = []; TG = "Mejorar la habilidad de mantener conversaciones apropiadas.";
                    disp(TG) %treatement target
                    treat_SC = [treat_SC;TG];                 
                case e >= 3 && e <= 4 && i == 16
                    TG = []; TG = "Mejorar la habilidad de empezar adecuadamente conversaciones.";
                    disp(TG) %treatement target
                    treat_SC = [treat_SC;TG];    
            end
        end
    end
    if ~isempty(treat_SC)
        Scale = []; Scale = categorical(repmat(["Social/Comunicación (SC)"], 1,size(treat_SC,1))');
    else
        Scale = []; Scale = categorical(repmat(["Social/Comunicación (SC)"],1,1)');
    end
    if ~isempty(treat_SC)
        TG_SC_tot = array2table([Scale,categorical(convertCharsToStrings(treat_SC))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        if language == 0
            TG_SC_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                            {'Tipo de síntoma', ['Objetivos para el tratamiento']});
        else
            TG_SC_tot = array2table([Scale,categorical("Nivel de lenguaje demasiado limitado para evaluar objetivos específicos para el tratamiento.")], 'VariableNames', ...
                    {'Tipo de síntoma', ['Objetivos para el tratamiento']});
        end
    end
    
elseif part_age >= 12 && part_age <= 18
    treat_SC = [];
    disp('12-18 years'); range = []; range = '12 y 18 años'; i = [];
    if language == 0
        items = [6 16];
    else 
        items = []; %Limited speech
    end
    for i = items
        e = []; e = SC_tot(i,:);
        if e ~= 5
            switch true
                case e >= 3 && e <= 4 && i == 6
                    TG = []; TG = "Mejorar la habilidad de mantener conversaciones apropiadas.";
                    disp(TG) %treatement target
                    treat_SC = [treat_SC;TG];                 
                case e >= 3 && e <= 4 && i == 16
                    TG = []; TG = "Mejorar la habilidad de empezar adecuadamente conversaciones.";
                    disp(TG) %treatement target
                    treat_SC = [treat_SC;TG];    
            end
        end
    end
    if ~isempty(treat_SC)
        Scale = []; Scale = categorical(repmat(["Social/Comunicación (SC)"], 1,size(treat_SC,1))');
    else
        Scale = []; Scale = categorical(repmat(["Social/Comunicación (SC)"],1,1)');
    end
    if ~isempty(treat_SC)
        TG_SC_tot = array2table([Scale,categorical(convertCharsToStrings(treat_SC))], 'VariableNames', ...
                        {'Tipo de síntoma', ['Objetivos para el tratamiento']});
    else
        if language == 0
            TG_SC_tot = array2table([Scale,categorical("No es un área de preocupación.")], 'VariableNames', ...
                            {'Tipo de síntoma', ['Objetivos para el tratamiento']});
        else
            TG_SC_tot = array2table([Scale,categorical("Nivel de lenguaje demasiado limitado para evaluar objetivos específicos para el tratamiento.")], 'VariableNames', ...
                    {'Tipo de síntoma', ['Objetivos para el tratamiento']});
        end
    end
else
    disp('Age is out of range for ASRS (6-18 years old)')
end
%% Table Tot : all symptoms scales 
Treatment_Tot = table();
Treatment_Tot = [TG_PS_tot; TG_AS_tot;...
    TG_SER_tot;TG_AL_tot; TG_ST_tot;...
    TG_BR_tot;TG_SS_tot;TG_AT_tot; TG_SR_tot; TG_SC_tot]; 
% %% Report
% import mlreportgen.report.* 
% import mlreportgen.dom.* 
% rpt = Report([convertCharsToStrings(file)+ "_CI" + convertCharsToStrings(...
%     num2str(CI_d))],...
%     "pdf");
% tp = TitlePage; 
% tp.Title = ['ASRS - Versión de los Padres (Autism Spectrum Rating Scales/Escalas de Puntuación del Espectro Autista): Reporte de Síntomas y Áreas de Mejora Para el Tratamiento.']; 
% tp.Subtitle = ['Paciente: ' nombre '/' num2str(age) ' años']; 
% tp.Author = 'Investigadora: Estudiante de doctorado Mathilde Marie Duville'; 
% tp.Publisher = ['Fecha y hora de la prueba: ' date];
% tp.Image = 'Logos.png';
% tp.Image = getImageReporter(tp);
% tp.Image.Content.Width = '494px';
% tp.Image.Content.Height =  '161px';
% add(rpt,tp); 
% add(rpt,TableOfContents); 
% 
% sec1 = Section; 
% sec1.Title = 'Breve descripción del ASRS'; 
% para = Paragraph(['Las Escalas de Puntuación del Espectro Autista'...
%     ' o ASRS por sus siglas en Inglés (Autism Spectrum Rating Scales)'...
%     ' han sido diseñadas para evaluar las conductas asociadas con'...
%      ' el espectro autista de niños y niñas entre 2 y 18 años según reportes'...
%      ' de padres o maestros.' newline 'El ASRS ayuda a guiar el'...
%      ' diagnóstico y se puede utilizar para la planeación de tratamientos,'...
%      ' el monitoreo de respuesta a intervenciones y la evaluación de programas clínicos.'...
%      newline ' ']); 
% para.Style = {HAlign('justify')};
%  
% para2 = Paragraph([' EL ASRS se compone de las siguientes escalas de sintomatología: '...
%     ' 1) Social/Comunicación (SC), 2) Conductas Inusuales (CI),'...
%      ' 3) Autorregulación (AR) 4) Puntuación Total (SC+CI+AR)', ...
%      ' 5) DSM-5, 6) Socialización con Compañeros (SOC), 7) Socialización con Adultos (SOA),',...
%      ' 8) Reciprocidad Social/Emocional (RSE), 9) Lenguaje Atípico (LA),'...
%      ' 10) Estereotipia (ET), 11) Rigidez Conductual (RC), 12) Sensibilidad Sensorial (SS) y',...
%      ' 13) Atención (AT). Referirse a la Tabla 1.1 para la interpretación de estas escalas.' ]); 
% para2.Style = {HAlign('justify')};
%  
% para3 =  Paragraph(['     ']);
%  
% Escalas_interp = table();
% Scale_interp = []; Scale_interp = ...
%     categorical(["Social/Comunicación (SC)"; "Conductas Inusuales (CI)";...
%       "Autorregulación (AR)"; "Puntuación Total (SC+CI+AR)"; ...
%       "DSM-5"; "Socialización con Compañeros (SOC)";...
%       "Socialización con Adultos (SOA)";...
%       "Reciprocidad Social/Emocional (RSE)"; ...
%       "Lenguaje Atípico (LA)";...
%       "Estereotipia (ET)"; "Rigidez Conductual (RC)";...
%       "Sensibilidad Sensorial (SS)";...
%       "Atención (AT)"]); 
% Interp_scale = []; Interp_scale = categorical([" Uso inapropiado de comunicación verbal y/o no-verbal para iniciar, involucrarse y mantener el contacto social.";...
%     "Tiene dificultades para tolerar cambios de rutina. Presenta comportamientos sin propósitos y estereotipados. Reacciona exageradamente a estimulaciones sensoriales.";...
%     "Presenta déficit de atención y/o de impulsos/control motor. Tiende a polemizar.";...
%     "Presenta muchas características similares a individuos diagnosticados con Trastornos del Espectro Autista.";...
%     "Presenta muchos síntomas relacionados directamente con el Manual Diagnóstico y Estadístico de los Trastornos Mentales - Quinta edición o DSM-5 por sus siglas en Inglés (Diagnostic and Statistical Manual of Mental Disorders - Fifth Edition).";...
%     "Tiene intereses y capacidades limitados para participar exitosamente en actividades que involucran desarrolar y mantener relaciones sociales con otros niños.";...
%     "Tiene intereses y capacidades limitados para participar exitosamente en actividades que involucran desarrolar y mantener relaciones sociales con adultos.";...
%     "Tiene habilidades limitadas para demostrar respuestas emocionales apropiadas hacia otras personas  en contextos sociales.";...
%     "La comunicación oral puede ser repetitiva, poco convencional y desestructurada.";...
%     "Demuestra movimientos o comportamientos sin propósito, repetitivos y ruidosos.";...
%     "Presenta dificultades para tolerar cambios de rutina, actividades o conductas. Su ambiente no debe cambiar.";...
%     "Reacciona exageradamente a ciertas percepciones táctiles, auditivas, olfactivas, visuales o gustativas.";...
%     "Se le dificulta mantener atención hacia un solo asunto e ignorar distracciones. Demuestra poca organización."]); 
% 
% Escalas_interp=table(Scale_interp, Interp_scale,'VariableNames', ...
%                         {'Escala de síntomas', 'Interpretación'} );
% %
% import mlreportgen.report.* 
% import mlreportgen.dom.* 
% tableStyle = ...
%     { ...
%     Width("100%"), ...
%     Border("solid"), ...
%     RowSep("solid"), ...
%     ColSep("solid") ...
%     };
% 
% tableEntriesStyle = ...
%     { ...
%     HAlign("center"), ...
%     VAlign("middle") ...
%     };
% headerRowStyle = ...
%     { ...
%     InnerMargin("2pt","2pt"), ...
%     BackgroundColor("cyan"), ...
%     Bold(true) ...
%     };
% grps(1) = TableColSpecGroup;
% grps(1).Span = size(Escalas_interp,1);
% 
% specs(1) = TableColSpec;
% specs(1).Span = 1;
% specs(1).Style = {Width("35%")};
% 
% specs(2) = TableColSpec;
% specs(2).Span = 1;
% specs(2).Style = {Width("65%")};
% 
% grps(1).ColSpecs = specs;
% table1 = Table(Escalas_interp);
% table1.ColSpecGroups = grps;
% 
% table1.Style = tableStyle;
% table1.TableEntriesStyle = tableEntriesStyle;
% 
% firstRow = table1.Children(1);
% firstRow.Style = headerRowStyle; 
% 
% add(sec1,para); add(sec1,para2); add(sec1,para3);
% add(sec1,getTableTitle1(convertCharsToStrings(['Características comunes '...
%     'de niños con puntuación alta.'])));
% add(sec1,table1);
% 
% para5 =  Paragraph(['     ']);
% add(sec1,para5);
% 
% para4 =  Paragraph(['Es importante resaltar que criterios adicionales son'...
%     ' necesarios para confirmar con precisión el diagnóstico. Esta prueba'...
%     ' debe ser interpretada a la luz de otras pruebas de diagnóstico que la complementan.'...
%     ' El ASRS describe la tendencias conductuales del niño dentro de'...
%     ' las úlimas 4 semanas por lo que los resultados representan conductas'...
%     ' actuales y no toman en cuenta la evolución previa de los patrones del espectro autista'... 
%     ' desde los primeros meses de vida.']);
% para4.Style = {HAlign('justify')};
% add(sec1,para4);
% add(rpt,sec1) 
% 
% % T-score 
% import mlreportgen.report.* 
% import mlreportgen.dom.* 
% sec2 = Section; 
% sec2.Title = ['Puntuación estandarizada de ' nombre]; 
% if language == 1
%     para0 =  Paragraph(['La evaluación de las habilidades de ' nombre ...
%        ' ha sido ajustada a su nivel de lenguaje. El nivel de lenguaje' ...
%        ' es demasiado limitado para poder evaluar la escala Lenguage Atípico ' ...
%        ' definida en la Tabla 1.1.']);
%     para0.Style = {HAlign('justify')};
%     add(sec2,para0);
% end
% 
% openfig('T-score.fig');
% figT = []; figT = Figure(gcf); 
% ax = gca; ax.FontSize = 50; 
% figT.Scaling = 'custom';
% figT.Height = '65cm'; 
% figT.Width = '95cm'; 
% figT.Snapshot.Caption = sprintf(['La puntuación se basa en la relación entre la severidad de los síntomas del paciente y los patrones autistas observados en niños fuera del espectro autista. A mayor observaciones de conductas atípicas, más alta es la puntuación. Los valores entre paréntesis indican el intervalo de confianza: rango en el cual se encuentra la puntuación verdadera con una probabilidad de ' ...
%     num2str(CI_d) ' por ciento.']); 
% add(sec2,figT)
% add(rpt,sec2)
% 
% close all
% % Percentil
% import mlreportgen.report.* 
% import mlreportgen.dom.* 
% sec3 = Section; 
% sec3.Title = ['Evaluación de los patrones autistas de ' nombre...
%     ' con respecto a niños y niñas fuera del espectro']; 
% openfig('Percentiles.fig');
% figT = []; figT = Figure(gcf); 
% ax = gca; ax.FontSize = 25; 
% figT.Scaling = 'custom';
% figT.Height = '21in'; 
% figT.Width = '19in'; 
% figT.Snapshot.Caption = sprintf(['Percentil y clasificación de la severidad de los síntomas de '...
%     nombre '. Los números describen la representatividad de los síntomas del paciente'...
%     ' dentro de la población fuera del espectro autista (niños y niñas entre ' range ').' ...
%     ' Por ejemplo, una puntuación de 60 por ciento (paciente) '...
%     'significa que 60 por ciento de los niños y niñas fuera del espectro presentan una sintomatología igual o menor a la del paciente.'...
%     ' La clasificación (por ejemplo "Ligeramente elevado") describe el nivel de síntomatología con respecto a niños y niñas fuera del espectro.']); 
% add(sec3,figT)
% add(rpt,sec3)
% close all
% 
% % Treatement Targets
% 
% import mlreportgen.report.* 
% import mlreportgen.dom.* 
% sec4 = Section; 
% sec4.Title = ['Metas para la intervención']; 
% 
% tableStyle = ...
%     { ...
%     Width("100%"), ...
%     Border("solid"), ...
%     RowSep("solid"), ...
%     ColSep("solid") ...
%     };
% 
% tableEntriesStyle = ...
%     { ...
%     HAlign("center"), ...
%     VAlign("middle") ...
%     };
% headerRowStyle = ...
%     { ...
%     InnerMargin("2pt","2pt"), ...
%     BackgroundColor("cyan"), ...
%     Bold(true) ...
%     };
% 
% grps(1) = TableColSpecGroup;
% grps(1).Span = size(TG_AL_tot,1);
% 
% specs(1) = TableColSpec;
% specs(1).Span = 1;
% specs(1).Style = {Width("40%")};
% 
% specs(2) = TableColSpec;
% specs(2).Span = 1;
% specs(2).Style = {Width("60%")};
% 
% grps(1).ColSpecs = specs;
% table1 = table();
% table1 = Table(Treatment_Tot);
% table1.ColSpecGroups = grps;
% 
% table1.Style = tableStyle;
% table1.TableEntriesStyle = tableEntriesStyle;
% 
% firstRow = table1.Children(1);
% firstRow.Style = headerRowStyle; 
% 
% add(sec4,getTableTitle(convertCharsToStrings(['Áreas de mejora de ' nombre])));
% add(sec4,table1);
% add(rpt,sec4); 
% rptview(rpt)
end

