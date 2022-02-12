import pdgaTournamentScraperFunctions as functions

def main():
    '''Streamlined method to scrape and save data for any number of events.'''
    baseURL = 'https://www.pdga.com/tour/event/'

    eventIDS = ['40638', '30718', '31742']

    for event in eventIDS:
        print(f'Processing event {event}.')

        eventDetails, eventData = functions.scrapePdgaData(baseURL + event)

        functions.saveData(eventData, eventDetails, event)

    return


if __name__ == '__main__':
    main()