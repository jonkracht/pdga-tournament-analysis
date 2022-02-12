import pdgaTournamentPlotterFunctions as plotfuncts
import matplotlib.pyplot as plt
import pandas as pd

baseFilePath = './tournament-data/pdgaEvent'

eventID = 40638

eventInfo, eventData = plotfuncts.loadData(baseFilePath + str(eventID) + '.json')

df = plotfuncts.makeDataFrame(eventData)

plt.scatter(df['Score 1'], df['Rating 1'])
plt.show()

print('Finished')


### Code snippets from initial work


'''
# Fit data
PDGA_fit, best_fit = np.zeros([n_rounds, 2]) , np.zeros([n_rounds, 2])

for rd in range(0,n_rounds):
    PDGA_fit[rd, :] = np.polyfit(round_scores[:, rd], round_ratings[: , rd], 1)
    best_fit[rd, :] = np.polyfit(round_scores[:, rd], player_ratings[:, 0], 1)

print('Data fits:')
print(PDGA_fit)
print(best_fit)




# Plots

# Notes & outstanding questions:
# How to determine if rounds are similar-enough, how to create plots simultaneously,
# outlier removal

# colors = [b,g,r,c,m,y,k,w];  markers = [- -- -. : . , o v ^ < > 1-4 s p h H * + x D d l _]
line_styles = ['bs','rv', 'gx', 'mo']

legend_str = []
for rd in range(0,n_rounds):
    legend_str.append('Round ' + str(rd + 1))

# Plot player rating against their round score
plt.figure()
for rd in range(0,n_rounds):
    plt.plot(round_scores[:, rd], player_ratings, line_styles[rd])
plt.legend(legend_str)
plt.ylabel('PDGA player rating')
plt.xlabel('Round score [strokes]')
plt.title(tourn_name)
plt.show()

# Plot the round scores against the PDGA-computed rating
plt.figure()
for rd in range(0,n_rounds):
    plt.plot(round_scores[:,rd],round_ratings[:,rd], line_styles[rd])
plt.legend(legend_str)
plt.xlabel('Round score [strokes]')
plt.ylabel('PDGA-computed round rating')
plt.title(tourn_name)
plt.show()

# Plot round score against PDGA rating and best-fit rating
vector = np.linspace(50, 100, 25)
for rd in range(0,n_rounds):
    plt.figure()
    plt.plot(round_scores[:,rd], player_ratings, line_styles[rd],
             vector, PDGA_fit[rd, 0] * vector + PDGA_fit[rd,1],'k--',
             vector, best_fit[rd, 0] * vector + best_fit[rd, 1], 'k:')
    plt.title(str(tourn_name) + ':  Round ' + str(rd + 1))
    plt.legend(['Player scores','PDGA fit','Best-fit line'])
    plt.xlabel('Round score [strokes]')
    plt.ylabel('Rating')
    plt.show()
    
    
'''