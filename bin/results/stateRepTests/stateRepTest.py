from ConfigEditor import *
import os

'''
Description: Letter 'X' RL vs OC
'''
file1 = 'rl_config1.txt'
file2 = 'rl_config2.txt'
file3 = 'rl_config3.txt'
file4 = 'rl_config4.txt'
file5 = 'rl_config5.txt'
file6 = 'rl_config6.txt'
file7 = 'rl_config7.txt'
file8 = 'rl_config8.txt'
file9 = 'rl_config9.txt'
file10 = 'rl_config10.txt'
file11 = 'rl_config11.txt'
file12 = 'rl_config12.txt'
file13 = 'rl_config13.txt'
file14 = 'rl_config14.txt'
file15 = 'rl_config15.txt'
file16 = 'rl_config16.txt'
file17 = 'rl_config17.txt'
file18 = 'rl_config18.txt'
file19 = 'rl_config19.txt'
file20 = 'rl_config20.txt'
file21 = 'rl_config21.txt'
file22 = 'rl_config22.txt'
file23 = 'rl_config23.txt'
file24 = 'rl_config24.txt'
file25 = 'rl_config25.txt'
file26 = 'rl_config26.txt'
file27 = 'rl_config27.txt'
file28 = 'rl_config28.txt'
file29 = 'rl_config29.txt'
file30 = 'rl_config30.txt'

os.system("touch " + file1)
os.system("touch " + file2)
os.system("touch " + file3)
os.system("touch " + file4)
os.system("touch " + file5)
os.system("touch " + file6)
os.system("touch " + file7)
os.system("touch " + file8)
os.system("touch " + file9)
os.system("touch " + file10)
os.system("touch " + file11)
os.system("touch " + file12)
os.system("touch " + file13)
os.system("touch " + file14)
os.system("touch " + file15)
os.system("touch " + file16)
os.system("touch " + file17)
os.system("touch " + file18)
os.system("touch " + file19)
os.system("touch " + file20)
os.system("touch " + file21)
os.system("touch " + file22)
os.system("touch " + file23)
os.system("touch " + file24)
os.system("touch " + file25)
os.system("touch " + file26)
os.system("touch " + file27)
os.system("touch " + file28)
os.system("touch " + file29)
os.system("touch " + file30)

exp1 = ConfigEditor(file1)
exp2 = ConfigEditor(file2)
exp3 = ConfigEditor(file3)
exp4 = ConfigEditor(file4)
exp5 = ConfigEditor(file5)
exp6 = ConfigEditor(file6)
exp7 = ConfigEditor(file7)
exp8 = ConfigEditor(file8)
exp9 = ConfigEditor(file9)
exp10 = ConfigEditor(file10)
exp11 = ConfigEditor(file11)
exp12 = ConfigEditor(file12)
exp13 = ConfigEditor(file13)
exp14 = ConfigEditor(file14)
exp15 = ConfigEditor(file15)
exp16 = ConfigEditor(file16)
exp17 = ConfigEditor(file17)
exp18 = ConfigEditor(file18)
exp19 = ConfigEditor(file19)
exp20 = ConfigEditor(file20)
exp21 = ConfigEditor(file21)
exp22 = ConfigEditor(file22)
exp23 = ConfigEditor(file23)
exp24 = ConfigEditor(file24)
exp25 = ConfigEditor(file25)
exp26 = ConfigEditor(file26)
exp27 = ConfigEditor(file27)
exp28 = ConfigEditor(file28)
exp29 = ConfigEditor(file29)
exp30 = ConfigEditor(file30)

exp1.writeNewFileRL('Original')
exp2.writeNewFileRL('Original')
exp3.writeNewFileRL('Original')
exp4.writeNewFileRL('Original')
exp5.writeNewFileRL('Original')
exp6.writeNewFileRL('Original')
exp7.writeNewFileRL('Original')
exp8.writeNewFileRL('Original')
exp9.writeNewFileRL('Original')
exp10.writeNewFileRL('Original')
exp11.writeNewFileRL('PuckMid4')
exp12.writeNewFileRL('PuckMid4')
exp13.writeNewFileRL('PuckMid4')
exp14.writeNewFileRL('PuckMid4')
exp15.writeNewFileRL('PuckMid4')
exp16.writeNewFileRL('PuckMid4')
exp17.writeNewFileRL('PuckMid4')
exp18.writeNewFileRL('PuckMid4')
exp19.writeNewFileRL('PuckMid4')
exp20.writeNewFileRL('PuckMid4')
exp21.writeNewFileRL('PuckMid16')
exp22.writeNewFileRL('PuckMid16')
exp23.writeNewFileRL('PuckMid16')
exp24.writeNewFileRL('PuckMid16')
exp25.writeNewFileRL('PuckMid16')
exp26.writeNewFileRL('PuckMid16')
exp27.writeNewFileRL('PuckMid16')
exp28.writeNewFileRL('PuckMid16')
exp29.writeNewFileRL('PuckMid16')
exp30.writeNewFileRL('PuckMid16')

# RL Learn------------------------------------------------------------

exp1.editValue('resultsDir', 'results/stateRepTests/Original/1/')

# RL Learn------------------------------------------------------------

exp2.editValue('resultsDir', 'results/stateRepTests/Original/2/')

# RL Learn------------------------------------------------------------

exp3.editValue('resultsDir', 'results/stateRepTests/Original/3/')

# RL Learn------------------------------------------------------------

exp4.editValue('resultsDir', 'results/stateRepTests/Original/4/')

# RL Learn------------------------------------------------------------

exp5.editValue('resultsDir', 'results/stateRepTests/Original/5/')

# RL Learn------------------------------------------------------------

exp6.editValue('resultsDir', 'results/stateRepTests/Original/6/')

# RL Learn------------------------------------------------------------

exp7.editValue('resultsDir', 'results/stateRepTests/Original/7/')

# RL Learn------------------------------------------------------------

exp8.editValue('resultsDir', 'results/stateRepTests/Original/8/')

# RL Learn------------------------------------------------------------

exp9.editValue('resultsDir', 'results/stateRepTests/Original/9/')

# RL Learn------------------------------------------------------------

exp10.editValue('resultsDir', 'results/stateRepTests/Original/10/')

# PuckMid16------------------------------------------------------------

exp11.editValue('resultsDir', 'results/stateRepTests/PuckMid4/1/')

exp12.editValue('resultsDir', 'results/stateRepTests/PuckMid4/2/')

exp13.editValue('resultsDir', 'results/stateRepTests/PuckMid4/3/')

exp14.editValue('resultsDir', 'results/stateRepTests/PuckMid4/4/')

exp15.editValue('resultsDir', 'results/stateRepTests/PuckMid4/5/')

exp16.editValue('resultsDir', 'results/stateRepTests/PuckMid4/6/')

exp17.editValue('resultsDir', 'results/stateRepTests/PuckMid4/7/')

exp18.editValue('resultsDir', 'results/stateRepTests/PuckMid4/8/')

exp19.editValue('resultsDir', 'results/stateRepTests/PuckMid4/9/')

exp20.editValue('resultsDir', 'results/stateRepTests/PuckMid4/10/')

# PuckMid16------------------------------------------------------------

exp21.editValue('resultsDir', 'results/stateRepTests/PuckMid16/1/')

exp22.editValue('resultsDir', 'results/stateRepTests/PuckMid16/2/')

exp23.editValue('resultsDir', 'results/stateRepTests/PuckMid16/3/')

exp24.editValue('resultsDir', 'results/stateRepTests/PuckMid16/4/')

exp25.editValue('resultsDir', 'results/stateRepTests/PuckMid16/5/')

exp26.editValue('resultsDir', 'results/stateRepTests/PuckMid16/6/')

exp27.editValue('resultsDir', 'results/stateRepTests/PuckMid16/7/')

exp28.editValue('resultsDir', 'results/stateRepTests/PuckMid16/8/')

exp29.editValue('resultsDir', 'results/stateRepTests/PuckMid16/9/')

exp30.editValue('resultsDir', 'results/stateRepTests/PuckMid16/10/')

# os.system("./cwaggle_rl rl_config1.txt & ./cwaggle_rl rl_config2.txt & ./cwaggle_rl rl_config3.txt & ./cwaggle_rl rl_config4.txt & ./cwaggle_rl rl_config5.txt & ./cwaggle_rl rl_config6.txt & ./cwaggle_rl rl_config7.txt & ./cwaggle_rl rl_config8.txt & ./cwaggle_rl rl_config9.txt & ./cwaggle_rl rl_config10.txt & ./cwaggle_rl rl_config11.txt & ./cwaggle_rl rl_config12.txt & ./cwaggle_rl rl_config13.txt & ./cwaggle_rl rl_config14.txt & ./cwaggle_rl rl_config15.txt & ./cwaggle_rl rl_config16.txt & ./cwaggle_rl rl_config17.txt & ./cwaggle_rl rl_config18.txt & ./cwaggle_rl rl_config19.txt & ./cwaggle_rl rl_config20.txt")
