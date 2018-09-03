# "Spectral Convoluter"
# Authors: Jonathan E. Barnsley, Joshua Sutton, Keith C. Gordon - University of Otago, New Zealand
# Input files must be a single value (intensity/extinction co-efficient/transmittance) value per line
# Match resolution, start wavelength below

# Set working directory to C14-20_Convolution.py location, realitive locations will now work

import os

abspath = os.path.abspath("C14-20_C14H-20H_Convolution.py")
dname = os.path.dirname(abspath)
os.chdir(dname)

# Jono's part

Resolution = 96 # 300-780 nm, 1nm/px resolution
StartWavelength = 300 # starting wavelength
ListEntries = 95 # resolution-1 for accessing list values (starts at 0)
ContributionSize = 1 # contribution step size: 1 and 0 

# Read in reference spectra to C14-C20, place in C<number>List

C14 = open("ReferenceSpectra\C14_Calc_UV-Vis.txt", "r")

C14List = []

for line in C14:
    C14List.append(float(line))

C16 = open("ReferenceSpectra\C16_Calc_UV-Vis.txt", "r")

C16List = []

for line in C16:
    C16List.append(float(line))
    
C18 = open("ReferenceSpectra\C18_Calc_UV-Vis.txt", "r")

C18List = []

for line in C18:
    C18List.append(float(line))

C20 = open("ReferenceSpectra\C20_Calc_UV-Vis.txt", "r")

C20List = []

for line in C20:
    C20List.append(float(line))

# Read in reference spectra to C14H-C20H, place in place in C<number>H+List

C14H = open("ReferenceSpectra\C14H_Calc_UV-Vis.txt", "r")

C14HList = []

for line in C14H:
    C14HList.append(float(line))

C16H = open("ReferenceSpectra\C16H_Calc_UV-Vis.txt", "r")

C16HList = []

for line in C16H:
    C16HList.append(float(line))
    
C18H = open("ReferenceSpectra\C18H_Calc_UV-Vis.txt", "r")

C18HList = []

for line in C18H:
    C18HList.append(float(line))

C20H = open("ReferenceSpectra\C20H_Calc_UV-Vis.txt", "r")

C20HList = []

for line in C20H:
    C20HList.append(float(line))

C14.close()
C16.close()
C18.close()
C20.close() # Close all input reference aldehyde spectra files
C14H.close()
C16H.close()
C18H.close()
C20H.close() # Close all input reference protonated spectra files

ContributionC14 = int(0) # initial contributions set to zero - will have one blank spectrum as result
ContributionC16 = int(0)
ContributionC18 = int(0)
ContributionC20 = int(0)
ContributionC14H = int(0) # initial contributions set to zero - will have one blank spectrum as result
ContributionC16H = int(0)
ContributionC18H = int(0)
ContributionC20H = int(0)

i = 0 # set iteration/address value for lists
Length = len(C14List) # get length of input lists
while ContributionC14 <= 1:
	while ContributionC16 <= 1:
		while ContributionC18 <= 1:
			while ContributionC20 <= 1: # iterate through the possible contributions
				while ContributionC14H <= 1:
					while ContributionC16H <= 1:
						while ContributionC18H <= 1:
							while ContributionC20H <= 1: # iterate through the possible contributions
								FileName = str(ContributionC14) + "_" + str(ContributionC16) + "_"  + str(ContributionC18) + "_"  + str(ContributionC20) + "_" + str(ContributionC14H) + "_" + str(ContributionC16H) + "_"  + str(ContributionC18H) + "_"  + str(ContributionC20H)
								OutputFile = open("OutputSpectra\ " + FileName + ".txt", "w")
								Wavelength = StartWavelength # set wavelength for output file to starting wavelength
								while i < Length : # iterate through the lists
									if (ContributionC14 + ContributionC16 + ContributionC18 + ContributionC20 + ContributionC14H + ContributionC16H + ContributionC18H + ContributionC20H) == 0: # hamfisted fix to devide by zero error for molecular contributions
										MolarContribution = 1
									else: 
										MolarContribution = 1 / (ContributionC14 + ContributionC16 + ContributionC18 + ContributionC20 + ContributionC14H + ContributionC16H + ContributionC18H + ContributionC20H) # Accounts for the 'overall' molar contribution
									print ((C14List[i] * ContributionC14 + C16List[i] * ContributionC16 + C18List[i] * ContributionC18 + C20List[i] * ContributionC20 + C14HList[i] * ContributionC14H + C16HList[i] * ContributionC16H + C18HList[i] * ContributionC18H + C20HList[i] * ContributionC20H) * MolarContribution)
									OutputFile.write(str(Wavelength) + '\t' + str((C14List[i] * ContributionC14 + C16List[i] * ContributionC16 + C18List[i] * ContributionC18 + C20List[i] * ContributionC20 + C14HList[i] * ContributionC14H + C16HList[i] * ContributionC16H + C18HList[i] * ContributionC18H + C20HList[i] * ContributionC20H) * MolarContribution) + '\n') 
									Wavelength = Wavelength + 5
									i = i + 1 # increase list address
								Wavelength = StartWavelength # reset wavelength
								OutputFile.close() # close output text file for the given contributions
								i = 0 # reset inner loop counter
								ContributionC20H = ContributionC20H + ContributionSize
							ContributionC20H = int(0)
							ContributionC18H = ContributionC18H + ContributionSize
						ContributionC18H = int(0)
						ContributionC16H = ContributionC16H + ContributionSize
					ContributionC16H = int(0) # reset inner loop counters
					ContributionC14H = ContributionC14H + ContributionSize # increase contribtuion value stepwise
				ContributionC14H = int(0) # reset inner loop counters
				ContributionC20 = ContributionC20 + ContributionSize
			ContributionC20 = int(0)
			ContributionC18 = ContributionC18 + ContributionSize
		ContributionC18 = int(0)
		ContributionC16 = ContributionC16 + ContributionSize
	ContributionC16 = int(0) # reset inner loop counters
	ContributionC14 = ContributionC14 + ContributionSize # 

print (ContributionC14, ContributionC16, ContributionC18, ContributionC20, ContributionC14H, ContributionC16H, ContributionC18H, ContributionC20H)

#C14List[listentrys]
