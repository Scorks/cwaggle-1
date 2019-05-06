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

exp1.writeNewFile()
exp2.writeNewFile()
exp3.writeNewFile()
exp4.writeNewFile()
exp5.writeNewFile()
exp6.writeNewFile()
exp7.writeNewFile()
exp8.writeNewFile()
exp9.writeNewFile()
exp10.writeNewFile()
exp11.writeNewFile()
exp12.writeNewFile()
exp13.writeNewFile()
exp14.writeNewFile()
exp15.writeNewFile()
exp16.writeNewFile()
exp17.writeNewFile()
exp18.writeNewFile()
exp19.writeNewFile()
exp20.writeNewFile()

# RL Learn------------------------------------------------------------

exp1.editValue('numRobots', '8')
exp1.editValue('RLAction', '1')
exp1.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp1.editValue('savePolicy', '0 gnuplot/q_out1.txt')
exp1.editValue('qLearning', '1')
exp1.editValue('maxTimeSteps', '5000000')
exp1.editValue('resultsDir', 'results/Z/RL/1/')
exp1.editValue('epsilon', '0.0')
#exp1.editValue('importGrid', '1 images/potential_field_X.png')

# RL Learn------------------------------------------------------------

exp2.editValue('numRobots', '8')
exp2.editValue('RLAction', '1')
exp2.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp2.editValue('savePolicy', '0 gnuplot/q_out2.txt')
exp2.editValue('qLearning', '1')
exp2.editValue('maxTimeSteps', '5000000')
exp2.editValue('resultsDir', 'results/Z/RL/2/')
exp2.editValue('epsilon', '0.0')
#exp2.editValue('importGrid', '1 images/potential_field_X.png')

# RL Learn------------------------------------------------------------

exp3.editValue('numRobots', '8')
exp3.editValue('RLAction', '1')
exp3.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp3.editValue('savePolicy', '0 gnuplot/q_out3.txt')
exp3.editValue('qLearning', '1')
exp3.editValue('maxTimeSteps', '5000000')
exp3.editValue('resultsDir', 'results/Z/RL/3/')
exp3.editValue('epsilon', '0.0')
#exp3.editValue('importGrid', '1 images/potential_field_X.png')

# RL Learn------------------------------------------------------------

exp4.editValue('numRobots', '8')
exp4.editValue('RLAction', '1')
exp4.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp4.editValue('savePolicy', '0 gnuplot/q_out4.txt')
exp4.editValue('qLearning', '1')
exp4.editValue('maxTimeSteps', '5000000')
exp4.editValue('resultsDir', 'results/Z/RL/4/')
exp4.editValue('epsilon', '0.0')
#exp4.editValue('importGrid', '1 images/potential_field_X.png')

# RL Learn------------------------------------------------------------

exp5.editValue('numRobots', '8')
exp5.editValue('RLAction', '1')
exp5.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp5.editValue('savePolicy', '0 gnuplot/q_out5.txt')
exp5.editValue('qLearning', '1')
exp5.editValue('maxTimeSteps', '5000000')
exp5.editValue('resultsDir', 'results/Z/RL/5/')
exp5.editValue('epsilon', '0.0')
#exp5.editValue('importGrid', '1 images/potential_field_X.png')

# RL Learn------------------------------------------------------------

exp6.editValue('numRobots', '8')
exp6.editValue('RLAction', '1')
exp6.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp6.editValue('savePolicy', '0 gnuplot/q_out6.txt')
exp6.editValue('qLearning', '1')
exp6.editValue('maxTimeSteps', '5000000')
exp6.editValue('resultsDir', 'results/Z/RL/6/')
exp6.editValue('epsilon', '0.0')
#exp6.editValue('importGrid', '1 images/potential_field_X.png')

# RL Learn------------------------------------------------------------

exp7.editValue('numRobots', '8')
exp7.editValue('RLAction', '1')
exp7.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp7.editValue('savePolicy', '0 gnuplot/q_out7.txt')
exp7.editValue('qLearning', '1')
exp7.editValue('maxTimeSteps', '5000000')
exp7.editValue('resultsDir', 'results/Z/RL/7/')
exp7.editValue('epsilon', '0.0')
#exp7.editValue('importGrid', '1 images/potential_field_X.png')

# RL Learn------------------------------------------------------------

exp8.editValue('numRobots', '8')
exp8.editValue('RLAction', '1')
exp8.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp8.editValue('savePolicy', '0 gnuplot/q_out8.txt')
exp8.editValue('qLearning', '1')
exp8.editValue('maxTimeSteps', '5000000')
exp8.editValue('resultsDir', 'results/Z/RL/8/')
exp8.editValue('epsilon', '0.0')
#exp8.editValue('importGrid', '1 images/potential_field_X.png')

# RL Learn------------------------------------------------------------

exp9.editValue('numRobots', '8')
exp9.editValue('RLAction', '1')
exp9.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp9.editValue('savePolicy', '0 gnuplot/q_out9.txt')
exp9.editValue('qLearning', '1')
exp9.editValue('maxTimeSteps', '5000000')
exp9.editValue('resultsDir', 'results/Z/RL/9/')
exp9.editValue('epsilon', '0.0')
#exp9.editValue('importGrid', '1 images/potential_field_X.png')

# RL Learn------------------------------------------------------------

exp10.editValue('numRobots', '8')
exp10.editValue('RLAction', '1')
exp10.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp10.editValue('savePolicy', '0 gnuplot/q_out10.txt')
exp10.editValue('qLearning', '1')
exp10.editValue('maxTimeSteps', '5000000')
exp10.editValue('resultsDir', 'results/Z/RL/10/')
exp10.editValue('epsilon', '0.0')
#exp10.editValue('importGrid', '1 images/potential_field_X.png')

# OC Learn------------------------------------------------------------

exp11.editValue('numRobots', '8')
exp11.editValue('RLAction', '0')
exp11.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp11.editValue('savePolicy', '0 gnuplot/q_out11.txt')
exp11.editValue('qLearning', '0')
exp11.editValue('maxTimeSteps', '5000000')
exp11.editValue('resultsDir', 'results/Z/OC/1/')
exp11.editValue('epsilon', '0.0')
#exp11.editValue('importGrid', '1 images/potential_field_X.png')

# OC Learn------------------------------------------------------------

exp12.editValue('numRobots', '8')
exp12.editValue('RLAction', '0')
exp12.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp12.editValue('savePolicy', '0 gnuplot/q_out11.txt')
exp12.editValue('qLearning', '0')
exp12.editValue('maxTimeSteps', '5000000')
exp12.editValue('resultsDir', 'results/Z/OC/2/')
exp12.editValue('epsilon', '0.0')
#exp12.editValue('importGrid', '1 images/potential_field_X.png')

# OC Learn------------------------------------------------------------

exp13.editValue('numRobots', '8')
exp13.editValue('RLAction', '0')
exp13.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp13.editValue('savePolicy', '0 gnuplot/q_out11.txt')
exp13.editValue('qLearning', '0')
exp13.editValue('maxTimeSteps', '5000000')
exp13.editValue('resultsDir', 'results/Z/OC/3/')
exp13.editValue('epsilon', '0.0')
#exp13.editValue('importGrid', '1 images/potential_field_X.png')

# OC Learn------------------------------------------------------------

exp14.editValue('numRobots', '8')
exp14.editValue('RLAction', '0')
exp14.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp14.editValue('savePolicy', '0 gnuplot/q_out11.txt')
exp14.editValue('qLearning', '0')
exp14.editValue('maxTimeSteps', '5000000')
exp14.editValue('resultsDir', 'results/Z/OC/4/')
exp14.editValue('epsilon', '0.0')
#exp14.editValue('importGrid', '1 images/potential_field_X.png')

# OC Learn------------------------------------------------------------

exp15.editValue('numRobots', '8')
exp15.editValue('RLAction', '0')
exp15.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp15.editValue('savePolicy', '0 gnuplot/q_out11.txt')
exp15.editValue('qLearning', '0')
exp15.editValue('maxTimeSteps', '5000000')
exp15.editValue('resultsDir', 'results/Z/OC/5/')
exp15.editValue('epsilon', '0.0')
#exp15.editValue('importGrid', '1 images/potential_field_X.png')

# OC Learn------------------------------------------------------------

exp16.editValue('numRobots', '8')
exp16.editValue('RLAction', '0')
exp16.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp16.editValue('savePolicy', '0 gnuplot/q_out11.txt')
exp16.editValue('qLearning', '0')
exp16.editValue('maxTimeSteps', '5000000')
exp16.editValue('resultsDir', 'results/Z/OC/6/')
exp16.editValue('epsilon', '0.0')
#exp16.editValue('importGrid', '1 images/potential_field_X.png')

# OC Learn------------------------------------------------------------

exp17.editValue('numRobots', '8')
exp17.editValue('RLAction', '0')
exp17.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp17.editValue('savePolicy', '0 gnuplot/q_out11.txt')
exp17.editValue('qLearning', '0')
exp17.editValue('maxTimeSteps', '5000000')
exp17.editValue('resultsDir', 'results/Z/OC/7/')
exp17.editValue('epsilon', '0.0')
#exp17.editValue('importGrid', '1 images/potential_field_X.png')

# OC Learn------------------------------------------------------------

exp18.editValue('numRobots', '8')
exp18.editValue('RLAction', '0')
exp18.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp18.editValue('savePolicy', '0 gnuplot/q_out11.txt')
exp18.editValue('qLearning', '0')
exp18.editValue('maxTimeSteps', '5000000')
exp18.editValue('resultsDir', 'results/Z/OC/8/')
exp18.editValue('epsilon', '0.0')
#exp18.editValue('importGrid', '1 images/potential_field_X.png')

# OC Learn------------------------------------------------------------

exp19.editValue('numRobots', '8')
exp19.editValue('RLAction', '0')
exp19.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp19.editValue('savePolicy', '0 gnuplot/q_out11.txt')
exp19.editValue('qLearning', '0')
exp19.editValue('maxTimeSteps', '5000000')
exp19.editValue('resultsDir', 'results/Z/OC/9/')
exp19.editValue('epsilon', '0.0')
#exp19.editValue('importGrid', '1 images/potential_field_X.png')

# OC Learn------------------------------------------------------------

exp20.editValue('numRobots', '8')
exp20.editValue('RLAction', '0')
exp20.editValue('loadPolicy', '0 gnuplot/q_out.txt')
exp20.editValue('savePolicy', '0 gnuplot/q_out11.txt')
exp20.editValue('qLearning', '0')
exp20.editValue('maxTimeSteps', '5000000')
exp20.editValue('resultsDir', 'results/Z/OC/10/')
exp20.editValue('epsilon', '0.0')
#exp20.editValue('importGrid', '1 images/potential_field_X.png')

# os.system("./cwaggle_rl rl_config1.txt & ./cwaggle_rl rl_config2.txt & ./cwaggle_rl rl_config3.txt & ./cwaggle_rl rl_config4.txt & ./cwaggle_rl rl_config5.txt & ./cwaggle_rl rl_config6.txt & ./cwaggle_rl rl_config7.txt & ./cwaggle_rl rl_config8.txt & ./cwaggle_rl rl_config9.txt & ./cwaggle_rl rl_config10.txt & ./cwaggle_rl rl_config11.txt & ./cwaggle_rl rl_config12.txt & ./cwaggle_rl rl_config13.txt & ./cwaggle_rl rl_config14.txt & ./cwaggle_rl rl_config15.txt & ./cwaggle_rl rl_config16.txt & ./cwaggle_rl rl_config17.txt & ./cwaggle_rl rl_config18.txt & ./cwaggle_rl rl_config19.txt & ./cwaggle_rl rl_config20.txt")
