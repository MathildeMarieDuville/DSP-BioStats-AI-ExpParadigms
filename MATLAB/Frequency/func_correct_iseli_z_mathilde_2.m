function corr = func_correct_iseli_z_mathilde_2(H, f, Fx1, Bx1, Fx2, Bx2, Fs)
% Inverse-filtering of vocal tract resonance (formant). 
%Correction is in dB, and dependent on Fs
% H   [dB]: the intensity of the harmonic to be corrected
% f   [Hz]: the frequency of the harmonic of interest
% Fx1 [Hz]: frequency of the fisrt formant to be corrected for 
% Bx1 [Hz]: bandwidth of the fisrt formant to be corrected for 
% Fx2 [Hz]: frequency of the second formant to be corrected for 
% Bx2 [Hz]: bandwidth of the second formant to be corrected for 
% Fs  [Hz]: sampling frequency
%
% Reference papers: 
%Iseli, M., & Alwan, A. (2004). An improved correction formula for the estimation of harmonic magnitudes and its application to open quotient estimation. 2004 IEEE International Conference on Acoustics, Speech, and Signal Processing, 1, I-669–672. https://doi.org/10.1109/ICASSP.2004.1326074
%Iseli, M., Yen-Liang Shue, & Alwan, A. (2006). Age-and Gender-Dependent Analysis of Voice Source Characteristics. 2006 IEEE International Conference on Acoustics Speed and Signal Processing Proceedings, 1, I-389-I–392. https://doi.org/10.1109/ICASSP.2006.1660039
%Iseli, Markus, Shue, Y.-L., & Alwan, A. (2007). Age, sex, and vowel dependencies of acoustic measures related to the voice sourcea). J. Acoust. Soc. Am., 121(4), 13.

%correction for the effect of Fx1
r1 = exp(-pi*Bx1/Fs);
omega_x1 = 2*pi*Fx1/Fs;
omega  = 2*pi*f/Fs;

num1 = r1.^2 + 1 - 2*r1.*cos(omega_x1); 

a1 = r1.^2 + 1 - 2*r1.*cos(omega_x1 + omega);
b1 = r1.^2 + 1 - 2*r1.*cos(omega_x1 - omega);

%correction for the effect of Fx2

r2 = exp(-pi*Bx2/Fs);
omega_x2 = 2*pi*Fx2/Fs;
omega  = 2*pi*f/Fs;

num2 = r2.^2 + 1 - 2*r2.*cos(omega_x2); 

a2 = r2.^2 + 1 - 2*r2.*cos(omega_x2 + omega);
b2 = r2.^2 + 1 - 2*r2.*cos(omega_x2 - omega);

j = 10*log10((num1)/(a1*b1));
k = 10*log10((num2)/(a2*b2));
corr = H-(j + k);


