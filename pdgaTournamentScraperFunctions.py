import requests
from bs4 import BeautifulSoup

def queryEventId(baseURL):
    '''Query user for index of tournament number of interest.  Check with number matches tournament name.'''

    while True:
        eventID = input('Enter index of tournament for which data is to be scraped:\n> ')

        url = baseURL + eventID

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        tournamentName = soup.find(id='page-title').get_text()
        tournamentDate = soup.find(class_='event-info info-list').find(class_='tournament-date').get_text().split()[1]

        printBanner(f'Details for event number {eventID}')
        print(f'Name: {tournamentName}\nDate: {tournamentDate}')
        print('\nIs this the event of interest?  (\'y\' for yes)')

        response = input('> ')

        if response == 'y':
            break

    return eventID


def printBanner(text):
    '''Standardized method to print text to std out.'''

    char, width, gap = '*', 80, 3

    leftFill = int((width - len(text) - 2 * gap) / 2)
    rightFill = width - leftFill - len(text) - 2 * gap

    print('\n' + width * char)
    print(leftFill * char + gap * ' ' + text + gap * ' ' + rightFill * char)
    print(width * char)

    return


def scrapePdgaData(url):
    '''Function that takes in a PDGA tournament url and outputs two lists:  tournament description and propagator information'''
    import re
    printBanner('Scraping Data')

    # Pull html from website
    r = requests.get(url)

    # Format html
    soup = BeautifulSoup(r.text, 'html.parser')

    # Details of the event
    eventInfo = {}

    eventInfo['Name'] = soup.find("meta", property='og:title')['content']

    # Locate tag in html which contains tournament eventInfo
    infoTag = soup.find(class_='event-info info-list')

    eventInfo['Date'] = infoTag.find(class_='tournament-date').text.split(' ', 1)[1]
    eventInfo['Location'] = infoTag.find(class_='tournament-location').text.split(' ', 1)[1]
    eventInfo['TD'] = infoTag.find(class_='tournament-director').text.split(' ', 2)[2]
    eventInfo['nRounds'] = int(list(soup.findAll('th', text=re.compile('Rd'))[-1].text)[-1])

    eventData = {}

    # Examine all table rows in the document;
    for tag in soup.select('tbody > tr'):
        # Check whether table row include player info
        if tag.find(class_='player')!=None:
            name = tag.find(class_='player').text

            # Handle missing information (PDGA numbers or ratings)
            try:
                pdgaNumber = tag.find(class_='pdga-number').text
            except:
                pdgaNumber = None

            try:
                playerRating = tag.find(class_='player-rating').text
            except:
                playerRating = None

            if tag.find(class_='propagator') == None:
                isPropagator = 0
            else:
                isPropagator = 1

            # Input round scores and ratings
            roundScores, roundRatings = [], []
            for r in tag.findAll(class_='round'):
                roundScores.append(r.text)
                roundRatings.append(r.findNext(class_='round-rating').text)

            # Store info in a dictionary
            playerInfoDict = {}
            playerInfoDict['PDGA Number'] = pdgaNumber
            playerInfoDict['Player Rating'] = playerRating
            playerInfoDict['Propagator'] = isPropagator
            playerInfoDict['Round Scores'] = roundScores
            playerInfoDict['Round Ratings'] = roundRatings

            eventData[name] = playerInfoDict

    print('\nCompleted scraping.')

    return eventInfo, eventData


def printData(data, info):
    '''Prints event info and data to stdout.'''

    # Query user if data is to be printed to debug
    view = str(input('\nWould you like to view the data?  (Type \'y\' for yes.)  '))

    if view == 'y':
        printBanner('Event Details')

        for key, val in info.items():
            print(f"{key+':':<35} {val}")

        printBanner('Event Data')

        for key, val in data.items():
            print(f"{key+ ':':<25}{list(val.values())}")

    return


def saveData(data, info, eventNumber):
    '''Save scraped data via json'''

    import json

    # Create dictionary with two keys:  (event) info and data
    newDict = {}
    newDict['info'] = info
    newDict['data'] = data

    savename = 'pdgaEvent' + str(eventNumber)
    outpath = './tournament-data/' + savename + '.json'

    with open(outpath, "w") as f:
        f.write(json.dumps(newDict))

    print('Data saved to ' + outpath)

    return


if __name__ == '__main__':
    '''A few function calls to test behavior'''

    baseURL = 'https://www.pdga.com/tour/event/'

    #ID = queryEventId(baseURL)

    scrapePdgaData(baseURL + '40638')

    #sampInfo = {'Name': 'Sellersville FISH Bowl', 'Date': '20-Jul-2019', 'Location': 'Sellersville, Pennsylvania, United States', 'TD': 'Dustin Leatherman'}
    #sampData = {'Andrew Fish': {'PDGA Number': '58320', 'Propagator': True, 'Round Scores': ['51', '54'], 'Round Ratings': ['1058', '1059']}, 'Devin Frederick': {'PDGA Number': '16287', 'Propagator': True, 'Round Scores': ['55', '59'], 'Round Ratings': ['1019', '1018']}}
    #printData(sampData, sampInfo)

    print('Finished')