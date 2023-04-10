import time
import pandas as pd
import numpy as np
import datetime
import statistics
from statistics import mode
#Help From https://statisticsglobe.com/mode-function-statistics-module-python

#Lizzi Deneen
#2023

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str( input("Input Your City ") )
    while True:
        if city.lower() in [ 'chicago' ,'new york city'  ,'washington']:
            break
        else:
          city = str( input("Input Your City ") )       
        continue
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = str( input("Input Your Month "))
    while True:
        if month.lower() in [ 'all', 'january', 'february' ,'march' ,'april' ,'may', 'june' ,'july', 'august' ,'september', 'november', 'december']:
            break
        else:
           month = str( input("Input Your Month "))  
        continue
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str( input("Input Your Day "))
    while True:
        if day.lower() in ['all', 'monday' ,'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
           day = str( input("Input Your Day ")) 
        continue
    
        
    return city, month, day




def load_data(filteredcity, filteredmonth, filteredday):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    f = open(filteredcity.replace(" ", "_") + '.csv', 'r')
    df =pd.read_csv(f)
    f.close()
    print('Filters In Place:')
    print(filteredcity)
    print(filteredmonth)
    print(filteredday)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y-%m-%d %H:%M:%S')
    df['month'] = pd.to_datetime(df['Start Time']).dt.strftime('%B')
    df['day'] = pd.to_datetime(df['Start Time']).dt.strftime('%A')
    df['hour'] = pd.to_datetime(df['Start Time']).dt.strftime('%I')
    df['combined']=df.apply(lambda x:'%s_%s' % (x['Start Station'],x['End Station']),axis=1)
    
    # Help From: https://www.geeksforgeeks.org/python-strftime-function/
    
    if filteredmonth != 'All':
 
      filtered_df = df.loc[df['month'].isin([filteredmonth])]
      filtered_df =filtered_df.loc[df['day'].isin([filteredday])]  
     
    elif filteredday != 'All':
      filtered_df =filtered_df.loc[df['day'].isin([filteredday])]  
    
    else:
      filtered_df = df

    
    return filtered_df







def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    month_counter = {}

    for word in df['month']:
        month_counter[word] = month_counter.get(word, 0) + 1
    print('Most Common Month Of Travel:')
    print(max(month_counter))

    # TO DO: display the most common day of week
    day_counter = {}

    for word in df['day']:
        day_counter[word] = day_counter.get(word, 0) + 1

    print('Most Common Day Of Travel:')
    print(max(day_counter))

    # TO DO: display the most common start hour
    hour_counter = {}

    for word in df['hour']:
        hour_counter[word] = hour_counter.get(word, 0) + 1
    print('Most Common Start Hour:')
    print(max(hour_counter))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station_counter = {}

    for word in df['Start Station']:
        start_station_counter[word] = start_station_counter.get(word, 0) + 1
    print('Most Frequest Start Station:')
    print(max(start_station_counter))


    # display most commonly used end station
    
    end_station_counter = {}

    for word in df['End Station']:
        end_station_counter[word] = end_station_counter.get(word, 0) + 1
    print('Most Frequest End Station:')
    print(max(end_station_counter))


    # display most frequent combination of start station and end station trip
    combined_station_counter = {}

    for word in df['combined']:
        combined_station_counter[word] = combined_station_counter.get(word, 0) + 1
    print('Most Frequest Trip:')
    print(max(combined_station_counter))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total Travel Time:')
    print(df['Trip Duration'].sum())

    # display mean travel time
    print('Mean Travel Time:')
    print(df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def user_stats(df,filteredcity, filteredmonth, filteredday):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counter = {}
    
    for word in df['User Type']:
        user_counter[word] = user_counter.get(word, 0) + 1
    print('Counts By User Type:')
    print(user_counter)



    # TO DO: Display counts of gender
    if filteredcity != 'Washington':
      print('This Information is not available for this city')
    else:
        gender_counter = {}

        for word in df['Gender']:
            gender_counter[word] = gender_counter.get(word, 0) + 1

        print('Counts By Gender:')
        print(gender_counter)
        print(type(gender_counter))
   


    # TO DO: Display earliest, most recent, and most common year of birth
    if filteredcity != 'Washington':
      print('This Information is not available for this city')
    else:
        birthyear_counter = {}

        for word in df['Birth Year']:
            birthyear_counter[word] = birthyear_counter.get(word, 0) + 1

        print(' This is the most common birth year:')
        print(max(birthyear_counter))
        print(' This is the most recent birth year:')
        print (df['Birth Year'].max())
        print(' This is the earliest birth year:')
        print(df['Birth Year'].min())
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df, filteredcity, filteredmonth, filteredday):
    pd.set_option('display.max_columns', None)
    answer = str( input("Do You Want To See the first 5 rows of data? Yes/No") ).lower()
    start_loc = 0
    while answer in ['yes']:
        end_loc = start_loc + 5
        print(df.iloc[start_loc: end_loc, :])
        start_loc += 5
        answer = str( input("Do You Want To See the next 5 rows of data? Yes/No") ).lower()
        
   
                 
 
    



def main():
    while True:
        filteredmonth = 'reset'
        filteredcity = 'reset'
        filteredday = 'reset'
        day = 'reset'
        month = 'reset'
        city = 'reset'
       
        filters = get_filters()
        filteredcity = filters[0]
        filteredmonth =   filters[1]
        filteredday =  filters[2]
        filteredmonth = filteredmonth.capitalize()
        filteredday = filteredday.capitalize()

        df = load_data(filteredcity, filteredmonth, filteredday)
        
        time_stats(df)
        df = load_data(filteredcity, filteredmonth ,filteredday)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, filteredcity, filteredmonth, filteredday)
            
        display_data(df, filteredcity, filteredmonth, filteredday)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
