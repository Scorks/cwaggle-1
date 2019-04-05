from ConfigEditor import *
import os

'''
Description: Experiment 2 - Comparing original OC algorithm with RL (learned policy)
'''
file1 = 'rl_config1.txt'
file2 = 'rl_config2.txt'
file3 = 'rl_config3.txt'
file4 = 'rl_config4.txt'
file5 = 'rl_config5.txt'
file6 = 'rl_config6.txt'

os.system("touch " + file1)
os.system("touch " + file2)
os.system("touch " + file3)
os.system("touch " + file4)
os.system("touch " + file5)
os.system("touch " + file6)

exp1 = ConfigEditor(file1)
exp2 = ConfigEditor(file2)
exp3 = ConfigEditor(file3)
exp4 = ConfigEditor(file4)
exp5 = ConfigEditor(file5)
exp6 = ConfigEditor(file6)

exp1.writeNewFile()
exp2.writeNewFile()
exp3.writeNewFile()
exp4.writeNewFile()
exp5.writeNewFile()
exp6.writeNewFile()

# OC Learn------------------------------------------------------------

exp1.editValue('numRobots', '8')
exp1.editValue('RLAction', '1')
exp1.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp1.editValue('savePolicy', '100000 gnuplot/q_master.txt')
exp1.editValue('qLearning', '1')
exp1.editValue('maxTimeSteps', '50000000')
exp1.editValue('resultsDir', 'results/')
exp1.editValue('epsilon', '0.0')

# OC Learn------------------------------------------------------------

exp2.editValue('numRobots', '8')
exp2.editValue('RLAction', '1')
exp2.editValue('loadPolicy', '1 gnuplot/q_master.txt')
exp2.editValue('savePolicy', '100000 gnuplot/q_out2.txt')
exp2.editValue('qLearning', '0')
exp2.editValue('maxTimeSteps', '10000000')
exp2.editValue('resultsDir', 'results/EXP2/')
exp2.editValue('epsilon', '0.02')

# OC Learn------------------------------------------------------------

exp3.editValue('numRobots', '8')
exp3.editValue('RLAction', '1')
exp3.editValue('loadPolicy', '1 gnuplot/q_master.txt')
exp3.editValue('savePolicy', '100000 gnuplot/q_out3.txt')
exp3.editValue('qLearning', '0')
exp3.editValue('maxTimeSteps', '10000000')
exp3.editValue('resultsDir', 'results/EXP2/')
exp3.editValue('epsilon', '0.02')

# OC Learn------------------------------------------------------------

exp4.editValue('numRobots', '8')
exp4.editValue('RLAction', '1')
exp4.editValue('loadPolicy', '1 gnuplot/q_master.txt')
exp4.editValue('savePolicy', '100000 gnuplot/q_out4.txt')
exp4.editValue('qLearning', '0')
exp4.editValue('maxTimeSteps', '10000000')
exp4.editValue('resultsDir', 'results/EXP2/')
exp4.editValue('epsilon', '0.02')

# OC Learn------------------------------------------------------------

exp5.editValue('numRobots', '8')
exp5.editValue('RLAction', '1')
exp5.editValue('loadPolicy', '1 gnuplot/q_master.txt')
exp5.editValue('savePolicy', '100000 gnuplot/q_out5.txt')
exp5.editValue('qLearning', '0')
exp5.editValue('maxTimeSteps', '10000000')
exp5.editValue('resultsDir', 'results/EXP2/')
exp5.editValue('epsilon', '0.02')

# OC Learn------------------------------------------------------------

exp6.editValue('numRobots', '8')
exp6.editValue('RLAction', '1')
exp6.editValue('loadPolicy', '1 gnuplot/q_master.txt')
exp6.editValue('savePolicy', '100000 gnuplot/q_out5.txt')
exp6.editValue('qLearning', '0')
exp6.editValue('maxTimeSteps', '10000000')
exp6.editValue('resultsDir', 'results/EXP2/')
exp6.editValue('epsilon', '0.02')

os.system("./cwaggle_rl rl_config1.txt")
os.system("./cwaggle_rl rl_config2.txt & ./cwaggle_rl rl_config3.txt & ./cwaggle_rl rl_config4.txt & ./cwaggle_rl rl_config5.txt & ./cwaggle_rl rl_config6.txt")