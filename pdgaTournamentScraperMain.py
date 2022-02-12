import pdgaTournamentScraperFunctions as functions

def main():

    functions.printBanner('Welcome to the PDGA tournament data scraper')

    baseURL = 'https://www.pdga.com/tour/event/'

    # Get tournament event number from user
    eventNumber = functions.queryEventId(baseURL)

    eventURL = baseURL + eventNumber

    eventDetails, eventData = functions.scrapePdgaData(eventURL)

    functions.printData(eventData, eventDetails)

    # Query user if data is to be saved
    save = str(input('\nShall we save the data?  (Type \'y\' for yes.)  '))

    if save == 'y':
        functions.saveData(eventData, eventDetails, eventNumber)
    else:
        print('Data NOT saved.')

    functions.printBanner('Exiting Scraper.  Buh-bye.')

    return


if __name__ == '__main__':
    main()