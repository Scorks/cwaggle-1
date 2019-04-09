from ConfigEditor import *
import os

'''
Description: Experiment 3 - Comparing original OC algorithm with RL on L Shape
'''
file1 = 'rl_config1.txt'
file2 = 'rl_config2.txt'

os.system("touch " + file1)
os.system("touch " + file2)

exp1 = ConfigEditor(file1)
exp2 = ConfigEditor(file2)

exp1.writeNewFile()
exp2.writeNewFile()

# OC Learn------------------------------------------------------------

exp1.editValue('numRobots', '8')
exp1.editValue('RLAction', '0')
exp1.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp1.editValue('savePolicy', '100000 gnuplot/q_master.txt')
exp1.editValue('qLearning', '1')
exp1.editValue('maxTimeSteps', '5000000')
exp1.editValue('resultsDir', 'results/EXP3/')
exp1.editValue('epsilon', '0.0')
exp1.editValue('importGrid', '1 images/potential_field_L.png')
exp1.editValue('outieThreshold', '1.0')
exp1.editValue('innieThreshold', '1.0')
exp1.editValue('numPucks', '300')
exp1.editValue('width', '1200')
exp1.editValue('height', '1200')

# RL Learn------------------------------------------------------------

exp2.editValue('numRobots', '8')
exp2.editValue('RLAction', '1')
exp2.editValue('loadPolicy', '0 gnuplot/q_master.txt')
exp2.editValue('savePolicy', '100000 gnuplot/q_out2.txt')
exp2.editValue('qLearning', '1')
exp2.editValue('maxTimeSteps', '5000000')
exp2.editValue('resultsDir', 'results/EXP3/')
exp2.editValue('epsilon', '0.00')
exp2.editValue('importGrid', '1 images/potential_field_L.png')
exp2.editValue('outieThreshold', '1.0')
exp2.editValue('innieThreshold', '1.0')
exp2.editValue('numPucks', '300')
exp2.editValue('width', '1200')
exp2.editValue('height', '1200')

os.system("./cwaggle_rl rl_config1.txt & ./cwaggle_rl rl_config2.txt")
# os.system("./cwaggle_rl rl_config2.txt & ./cwaggle_rl rl_config3.txt & ./cwaggle_rl rl_config4.txt & ./cwaggle_rl rl_config5.txt & ./cwaggle_rl rl_config6.txt")