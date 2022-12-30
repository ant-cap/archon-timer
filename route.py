# goatpov note: this is unfinished
import csv

LEVELS = ["Cruelty Squad Headquarters", "Pharmakokinetiks", "Paradise", "Sin Space Engineering", "Androgen Assault",
					"Mall Madness", "Apartment Atrocity", "Seaside Shock", "Bog Business", "Casino Catastrophe", "Idiot Party",
					"Office", "Archon Grid", "Darkworld", "Alpine Hospitality", "Miner's Miracle", "Neuron Activator", "House",
					"Trauma Loop"]

try:
	infile = open("routes.csv", "r", encoding="utf8")
	reader = csv.reader(infile)
	D = {}
	for l in reader:
		D[l[0]] = []
		for i in range(1, len(l)):
			D[l[0]].append(l[i])
	infile.close()
except FileNotFoundError:
	trauma = [1, 2, 3, 3, 0, 0, 0, 0, 0, 0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 10, 16, 16, 16, 8, 15, 2, 13, 7, 14, 17, 18]
	archon = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	D = {"Archon": archon, "Trauma": trauma}
	outfile = open("routes.csv", "w", newline='', encoding="utf8")
	writer = csv.writer(outfile)
	for key in D:
		writer.writerow([key]+D[key])
	outfile.close()



