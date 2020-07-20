import time
import pandas as pd
import numpy as np

CITY_DATA = { 1: 'chicago.csv',
              2: 'new_york_city.csv',
              3: 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (integer) month - name of the month to filter by, or "all" to apply no month filter
        (integer) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while 1:
        try:
            city=int(input('Which city do you want to explore?\n Chicago([1] \n NY[2] \n Washington[3]'))
            if city in (1, 2, 3):
                print(f'\nYou selected city.{city}' )
                break
            else:
                print('\nPlease, you must enter one of the three cities in the promp as it is written')   
          
        except ValueError:
            print('Not valid-Enter a #1,2,3')
        except KeyboardInterrupt:
            print('attempt')
            break
        
        
        
        
      # get user input for filter: month, day or all
    while 1:
        try:
            filter=int(input('filter by month[0], day[1] or all[2]'))
            if filter in (0, 1, 2):
                print('\nYou selected {}.'.format(filter))
                break
            else:
                print('\nPlease, you must enter one of the three filters')  
        except ValueError:
            print('Not valid-Enter a #0,1,2')
        except KeyboardInterrupt:
            print('attempt')
            break
          
          
        

    # get user input for month (all, january, february, ... , june)
    while 1 and filter == 0:
        try:
            month=int(input('Which month?\n Jan([1] \n Feb[2] \n Mar[3] \n Apr[4] \n May[5] \n Jun[6]'))
            day=2 
            if month in (1, 2, 3,4,5,6):
                print(f'\nYou selected {month}.')  
                break
            else:
                print('\nPlease, you must enter one of the six months')
        except ValueError:
            print('Not valid-Enter a #1,2,3..')
        except KeyboardInterrupt:
            print('attempt')
            break
           
        

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while 1 and filter == 1:
        try:
            day=int(input('Which day?\n Sun([0] \n M[1] \n T[2] \n W[3] \n Th[4] \n F[5] \n Sat[6]'))
            month=2
            if day in (0,1,2,3,4,5,6):
                print('\nYou selected {}.'.format(day))
                break
            else:
                print('\nPlease, you must enter one of the seven days')
        except ValueError:
            print('Not valid-Enter a #0,1,2,3..')
        except KeyboardInterrupt:
            print('attempt')
            break
            
        
        
    # select all -number 2 is equivalent to the filter choice "all" 
    if filter == 2:
        month=2
        day=2
                
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday
    
    # filter by month if applicable,2 is the all choice
    if month != 2:
        
        # use the index of the months list to get the corresponding int
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
        # filter by day of week if applicable
    if day != 2:
        # filter by day of week to create the new dataframe
        df = df[df['day']== day]    
    
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('common month:', common_month)
    
    # display the most common day of week
    df['day'] = df['Start Time'].dt.day
    common_day = df['day'].mode()[0]
    print('common day:', common_day)

    # display the most common start hour
    

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    start_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    
    common_start = df['Start Station'].mode()[0]
    print(' common start station:\n', common_start)
    

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('\n common end station:\n', common_end)

    # display most frequent combination of start station and end station trip
    combo=(df['Start Station'] +' to '+ df['End Station']).mode()[0]
    print('\n most freq combo start and end station:\n',combo)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    TripDuration = df['Trip Duration'].describe()[0]
    print('TripDuration:', TripDuration)

    # display mean travel time
    TripDuration = df['Trip Duration'].mean(axis = 0, skipna = True)
    print('mean:', TripDuration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # Display counts of gender
    
    if 'Gender' in df.columns:
        user_gender = df['Gender'].value_counts()
        print(user_gender)
        
        nan_num = df['Gender'].isnull().sum()
        print('{} people did not specify their gender'.format(int(nan_num)))
    else:
        print('This city does not have gender data.')
    
    # Display earliest, most recent, and most common year of birth   
    if 'Birth Year' in df.columns:
        print('\nThe birth year statistics:\n')
        print('The most recent birth year on the record is {}.'.format(int(df['Birth Year'].max())))
        print('The earliest recent birth year on the record is {}.'.format(int(df['Birth Year'].min())))
        print('The common recent birth year on the record is {}.'.format(int(df['Birth Year'].mode()[0])))
    else:
        print('There is no Birth Year data')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        i = 0
        raw = input("\nWould you like to see first 5 rows of raw data; type 'y' or 'n'?\n").lower()
        pd.set_option('display.max_columns',200)
        while True:            
            if raw == 'n':
                break
            print(df.iloc[i:i+5])
            raw = input('\nWould you like to see next rows of raw data? y/n \n').lower()
            i += 5   
        
        
        
        restart = input('\nWould you like to restart? Enter y or n.\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
