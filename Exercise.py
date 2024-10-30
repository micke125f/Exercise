
import argparse
""" 
Execution:

python3 Exercise.py


---Values by console: 
when you finish to capture the values on the console press double enter to continue.
Example:

python3 Exercise.py

Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0


---Values by a file:
Example:

python3 Exercise.py -f pathfile
"""

#read file
def readCommandLine():
    teams = []
    
    print("Introduce the teams once captured press double enter to continue: \n")
    while True:
        line = input()
        if line.strip() == "":
            break
        teams.append(line)

    processTeams(teams)

#read command line
def readCommandLineFile(file):
    teams = []
    with open(file, 'r') as f:
    	lines =f.readlines()
    for line in lines:
    	teams.append(line)
    for i in teams:
    	print(i)
    processTeams(teams)

def processTeams(teams):
    dpts = {}
    #separate the values by team and number
    for teams in teams:
        team1, team2 = teams.split(',')
        team1 = team1.lstrip()
        team2 = team2.lstrip()

        nomTeam1, resTeam1 = team1.rsplit(" ", 1)
        nomTeam2, resTeam2 = team2.rsplit(" ", 1)
	
	#compare if tie or win
        if int(resTeam1) == int(resTeam2):
            ptsTeam1 = 1
            ptsTeam2 = 1
        elif int(resTeam1) > int(resTeam2):
            ptsTeam1 = 3
            ptsTeam2 = 0
        elif int(resTeam1) < int(resTeam2):
            ptsTeam1 = 0
            ptsTeam2 = 3
	
	#assign team and point to the dictionary
        if nomTeam1 not in dpts:
            dpts[nomTeam1] = ptsTeam1
        else:
            dpts[nomTeam1] += ptsTeam1

        if nomTeam2 not in dpts:
            dpts[nomTeam2] = ptsTeam2
        else:
            dpts[nomTeam2] += ptsTeam2
    
    #order dictionary by value and key
    dpts = dict(sorted(dpts.items(), key=lambda item: (- item[1], item[0])))
    i = 1
    
    #print dictionary
    for team, pts in dpts.items():
        print(f"{i}. {team}, {pts} pts")
        i += 1
    
    #save dictionary into a file
    saveFile(dpts)
    print("File saved")

def saveFile(dpts):
    i = 1
    with open('processedData.txt','w') as f:
    	for team, pts in dpts.items():
        	f.write(f"{i}. {team}, {pts} pts")
        	f.write("\n")
        	i += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejemplo de argumentos")
    parser.add_argument("-f", type=str, help="Argument with file")
    args = parser.parse_args()
    
    #check if contain arguments
    if args.f != None:
    	readCommandLineFile(args.f)
    else:
    	readCommandLine()
