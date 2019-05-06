from ConfigEditor import *
import os

'''
Description: Testing New State Representations
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

exp1.writeNewFileRL('Original_9bit')
exp2.writeNewFileRL('Original_9bit')
exp3.writeNewFileRL('Original_9bit')
exp4.writeNewFileRL('Original_9bit')
exp5.writeNewFileRL('Original_9bit')
exp6.writeNewFileRL('Original_9bit')
exp7.writeNewFileRL('Original_9bit')
exp8.writeNewFileRL('Original_9bit')
exp9.writeNewFileRL('Original_9bit')
exp10.writeNewFileRL('Original_9bit')

# RL Learn------------------------------------------------------------

exp1.editValue('resultsDir', 'results/new_stateReps/Original_9bit/1/')

# RL Learn------------------------------------------------------------

exp2.editValue('resultsDir', 'results/new_stateReps/Original_9bit/2/')

# RL Learn------------------------------------------------------------

exp3.editValue('resultsDir', 'results/new_stateReps/Original_9bit/3/')

# RL Learn------------------------------------------------------------

exp4.editValue('resultsDir', 'results/new_stateReps/Original_9bit/4/')

# RL Learn------------------------------------------------------------

exp5.editValue('resultsDir', 'results/new_stateReps/Original_9bit/5/')

# RL Learn------------------------------------------------------------

exp6.editValue('resultsDir', 'results/new_stateReps/Original_9bit/6/')

# RL Learn------------------------------------------------------------

exp7.editValue('resultsDir', 'results/new_stateReps/Original_9bit/7/')

# RL Learn------------------------------------------------------------

exp8.editValue('resultsDir', 'results/new_stateReps/Original_9bit/8/')

# RL Learn------------------------------------------------------------

exp9.editValue('resultsDir', 'results/new_stateReps/Original_9bit/9/')

# RL Learn------------------------------------------------------------

exp10.editValue('resultsDir', 'results/new_stateReps/Original_9bit/10/')

# os.system("./cwaggle_rl rl_config1.txt & ./cwaggle_rl rl_config2.txt & ./cwaggle_rl rl_config3.txt & ./cwaggle_rl rl_config4.txt & ./cwaggle_rl rl_config5.txt & ./cwaggle_rl rl_config6.txt & ./cwaggle_rl rl_config7.txt & ./cwaggle_rl rl_config8.txt & ./cwaggle_rl rl_config9.txt & ./cwaggle_rl rl_config10.txt & ./cwaggle_rl rl_config11.txt & ./cwaggle_rl rl_config12.txt & ./cwaggle_rl rl_config13.txt & ./cwaggle_rl rl_config14.txt & ./cwaggle_rl rl_config15.txt & ./cwaggle_rl rl_config16.txt & ./cwaggle_rl rl_config17.txt & ./cwaggle_rl rl_config18.txt & ./cwaggle_rl rl_config19.txt & ./cwaggle_rl rl_config20.txt")
