def loadData(pathToFile):
    '''Load scraped data from json file'''
    import json

    with open(pathToFile) as open_file:
        data = json.load(open_file)

    return data['info'], data['data']


def makeDataFrame(dict):
    '''Convert scraped data structure (nested dictionary) into a Pandas DataFrame for easier plotting and analysis.'''
    import pandas as pd
    import numpy as np

    missingDataValue = np.nan

    # Determine column labels
    numRounds = len(list(dict[list(dict.keys())[0]].values())[3])

    columnLabels = ['Name', 'PDGA#', 'Player Rating', 'Propagator']

    for n in range(numRounds):
        columnLabels.append('Score ' + str(n+1))

    for n in range(numRounds):
        columnLabels.append('Rating ' + str(n+1))

    # Create data frame, row by row
    newrow = []

    for key, val in dict.items():
        dataRow = []

        # Add player name
        dataRow.append(key)

        for key2, val2 in val.items():
            if key2 in ['PDGA Number', 'Player Rating']:
                if val2 == '':
                    dataRow.append(missingDataValue)
                else:
                    dataRow.append(int(val2))
            elif key2 == 'Propagator':
                dataRow.append(bool(key2))
            else:
                for v in val2:
                    if v == '':
                        dataRow.append(missingDataValue)
                    else:
                        dataRow.append(int(v))



        newrow.append(dataRow)

    df = pd.DataFrame(newrow, columns=columnLabels)

    # Convert columns to the desired variable types


    return df

if __name__ == '__main__':

    eventID = 40638
    sampleInfo, sampleData = loadData('./tournament-data/pdgaEvent' + str(eventID) + '.json')

    df = makeDataFrame(sampleData)

    print('Done.')