from ConfigEditor import *
import os

'''
Description: Experiment 1 - Comparing original OC algorithm with RL (after learning)
'''

file6 = 'rl_config6.txt'
file7 = 'rl_config7.txt'
file8 = 'rl_config8.txt'
file9 = 'rl_config9.txt'
file10 = 'rl_config10.txt'

os.system("touch " + file6)
os.system("touch " + file7)
os.system("touch " + file8)
os.system("touch " + file9)
os.system("touch " + file10)

exp6 = ConfigEditor(file6)
exp7 = ConfigEditor(file7)
exp8 = ConfigEditor(file8)
exp9 = ConfigEditor(file9)
exp10 = ConfigEditor(file10)

exp6.writeNewFile()
exp7.writeNewFile()
exp8.writeNewFile()
exp9.writeNewFile()
exp10.writeNewFile()

# RL Learn------------------------------------------------------------

exp6.editValue('numRobots', '8')
exp6.editValue('qLearning', '0')
exp6.editValue('maxTimeSteps', '5000000')
exp6.editValue('loadPolicy', '0 gnuplot/q_out_6.txt')
exp6.editValue('resultsDir', 'results/exp1/learned/')
exp6.editValue('epsilon', '0.01')
exp6.editValue('savePolicy', '100000 gnuplot/q_out6.txt')

# RL Learn------------------------------------------------------------

exp7.editValue('numRobots', '8')
exp7.editValue('qLearning', '0')
exp7.editValue('maxTimeSteps', '5000000')
exp7.editValue('loadPolicy', '0 gnuplot/q_out_7.txt')
exp7.editValue('resultsDir', 'results/exp1/learned/')
exp7.editValue('epsilon', '0.01')
exp7.editValue('savePolicy', '100000 gnuplot/q_out7.txt')

# RL Learn------------------------------------------------------------

exp8.editValue('numRobots', '8')
exp8.editValue('qLearning', '0')
exp8.editValue('maxTimeSteps', '5000000')
exp8.editValue('loadPolicy', '0 gnuplot/q_out_8.txt')
exp8.editValue('resultsDir', 'results/exp1/learned/')
exp8.editValue('epsilon', '0.01')
exp8.editValue('savePolicy', '100000 gnuplot/q_out8.txt')

# RL Learn------------------------------------------------------------

exp9.editValue('numRobots', '8')
exp9.editValue('qLearning', '0')
exp9.editValue('maxTimeSteps', '5000000')
exp9.editValue('loadPolicy', '0 gnuplot/q_out_9.txt')
exp9.editValue('resultsDir', 'results/exp1/learned/')
exp9.editValue('epsilon', '0.01')
exp9.editValue('savePolicy', '100000 gnuplot/q_out9.txt')

# RL Learn------------------------------------------------------------

exp10.editValue('numRobots', '8')
exp10.editValue('qLearning', '0')
exp10.editValue('maxTimeSteps', '5000000')
exp10.editValue('loadPolicy', '1 gnuplot/q_out_10.txt')
exp10.editValue('resultsDir', 'results/exp1/learned/')
exp10.editValue('epsilon', '0.01')
exp10.editValue('savePolicy', '100000 gnuplot/q_out10.txt')


# os.system("./cwaggle_rl rl_config1.txt & ./cwaggle_rl rl_config3.txt & ./cwaggle_rl rl_config5.txt & ./cwaggle_rl rl_config7.txt & ./cwaggle_rl rl_config9.txt & ./cwaggle_rl rl_config2.txt & ./cwaggle_rl rl_config4.txt & ./cwaggle_rl rl_config6.txt & ./cwaggle_rl rl_config8.txt & ./cwaggle_rl rl_config10.txt")
