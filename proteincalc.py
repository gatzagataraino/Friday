#!/usr/bin/python
#Javier Alegria

ProteinSeq = raw_input("Enter a protein sequence: ")#this function will allow to input data


ProteinSeq = ProteinSeq.upper()#becomes everything in uppercase letters so that the program can still read it (the opposite would be lower()"

AminoDict = {#this is a dictionary of the aminoacids and the mollecular weight
'A':89.09,
'R':174.20,
'N':132.12,
'D':133.10,
'C':121.15,
'Q':146.15,
'E':147.13,
'G':75.07,
'H':155.16,
'I':131.17,
'L':131.17,
'K':146.19,
'M':149.21,
'F':165.19,
'P':115.13,
'S':105.09,
'T':119.12,
'W':204.23,
'Y':181.19,
'V':117.15,
'X':0.0,
'-':0.0,
'*':0.0}


MolWeight = 0
for AminoAcid in ProteinSeq:#this loop will treat proteinSeq as a list. It steps through each letter of the string and assings it to AminoAcid in turn. So each time you loop is as if you write Aminoacid = [ 'F' ] before the print statement.
	MolWeight = MolWeight + AminoDict[AminoAcid]#here, for each value assigned by the loop it will look for the value assigned to it in the dictionary (AminoDict[AminoAcid]) and add it to the value of molWeight.

print "Protein: ", ProteinSeq
print "Molecular weight: %.1f" % (MolWeight)






















