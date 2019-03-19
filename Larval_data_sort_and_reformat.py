#!C:/Users/Wei/AppData/Local/Programs/Python/Python36
import os
#This is the directory of python


#Change directory to the folder the files are in
os.chdir('/Users/Wei/Desktop/YSP/Data processing folder/')

#The files will have to be renamed to match the code (Denticle_belt_positions_as_percentages_final.txt for the percentages file
#and Denticle_belt_positions.txt for the positions file)


#This section takes a percentages file and removes all incomplete data
percentages_original = open('Denticle_belt_positions_as_percentages.txt', 'r')
percentages = open('Denticle_belt_positions_as_percentages_final.txt', 'a')
percentages_lines = percentages_original.readlines()
print len(percentages_lines)

count = 0
for filename in range(0, len(percentages_lines)/4):
	anterior = [splits for splits in percentages_lines[filename*4+1].split("\t") if (splits != "\n" and splits != "")]
	posterior = [splits for splits in percentages_lines[filename*4+2].split("\t") if (splits != "\n" and splits != "")]
	if len(anterior) == 8 and len(posterior) == 8:
		percentages.write(percentages_lines[filename*4])
		percentages.write(percentages_lines[filename*4+1])
		percentages.write(percentages_lines[filename*4+2])
		percentages.write("\n")


#This section takes a hand-edited percentages file and a  much longer, non-edited positions file
#and creates a new file only with the position values that match the percentages
percentages = open('Denticle_belt_positions_as_percentages_final.txt', 'r')
positions_original = open('Denticle_belt_positions.txt', 'r')
positions = open('Denticle_belt_positions_final.txt', 'a')

percentages_lines = percentages.readlines()
positions_lines = positions_original.readlines()
#print len(percentages_lines)
#print len(positions_lines)

count = 0
for filename in range(0, (len(positions_lines))/4):
	#print count
	if (filename-count)*4 < len(percentages_lines) and percentages_lines[(filename-count)*4] == positions_lines[filename*4]:
		positions.write(positions_lines[(filename)*4])
		positions.write(positions_lines[(filename)*4+1])
		positions.write(positions_lines[(filename)*4+2])
		positions.write('\n')
		continue
	count+=1


#This takes two matching percentages and positions files and creates two files, one with
#reformatted percentages and one with reformatted positions
percentages = open('Denticle_belt_positions_as_percentages_final.txt', 'r')
positions = open('Denticle_belt_positions_final.txt', 'r')
denticle_belt_formatted = open('Denticle_belt_formatted.txt', 'a')
body_length_formatted = open('Body_length_formatted.txt', 'a')
species = "name"
count = 0

percentages_lines = percentages.readlines()
positions_lines = positions.readlines()

#print len(percentages_lines)
#print len(positions_lines)
denticle_belt_formatted.write("species" + "\t" + "larva" + "\t" + "segment" + "\t" + "anterior" + "\t" + "posterior" + "\t" + "denticle.width" + "\n")
body_length_formatted.write("species" + "\t" + "larva" + "\t" + "body.length" + "\n")

for file in range(0, (len(percentages_lines))/4):
	count+=1
	anterior = percentages_lines[file*4+1].split("\t")
	posterior = percentages_lines[file*4+2].split("\t")
	for belt_count in range(0, 8):
		denticle_belt_formatted.write(species + "\t" + str(count) + "\t" + "A" + str(belt_count+1) + "\t" + anterior[belt_count] + "\t" + posterior[belt_count] + "\t" + str((float(posterior[belt_count]) - float(anterior[belt_count]))) + "\n")
count = 0
#print (len(percentages_lines))
#print (len(positions_lines))

for file in range(0, (len(positions_lines))/4):
	count+=1
	line = positions_lines[file*4+1].split("\t")
	body_length_formatted.write(species + "\t" + str(count) + "\t" + line[9])
