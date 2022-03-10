import time
import pandas as pd
import numpy as np
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
    print('Hello! Let\'s explore some US bikeshare data! \n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print ("Please enter the city name (chicago, new york city , or washington )")
    city = input ().lower()
    
    # To guarantee a correct city name
    while (city != "chicago" and city != 'new york city' and city !='washington') :
        print ('Worng name please enter a valid city name ')
        city = input ().lower() 


    # TO DO: get user input for month (all, january, february, ... , june)
    
    print ('What month would you like to filter by (enter all for not filtering)')
    month = input().lower()
    
    # To guarantee a correct month name
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while (month not in months) :
        print ('worng name please enter a valid month name (january, february , ....)')
        month = input ().lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print ('What day would you like to filter by (enter all for not filtering)?')
    day = input().lower()
    
     # To guarantee a correct day name
    days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while (day not in days) :
        print ('worng name please enter a valid day name (sunday, monday, ...)')
        day = input ().lower()

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
    df= pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # Filtering if possible
    if month != 'all' : 
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        month = months.index(month)+1
        df = df[df['month']==month]
    if day != 'all' :
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    if (df['month'].min() != df['month'].max()): # To skip in case of filtring 
        common_month = df['month'].value_counts().idxmax()
        print (common_month)
    


    # TO DO: display the most common day of week
    if (df['day_of_week'].min() != df['day_of_week'].max()): # To skip in case of filtring
        print ("The most common day is : ")
        common_day = df['day_of_week'].value_counts().idxmax() 
        print (common_day)

    # TO DO: display the most common start hour
    print ('The most common start hour is : ')
    print (df['Start Time'].dt.hour.value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print ('The most common start station is : ')
    print (df['Start Station'].value_counts().idxmax())


    # TO DO: display most commonly used end station
    print ('The most common end station is : ')
    print (df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    print ('The most frequent combination of start station and end station trip is : ')
    print (df[['Start Station', 'End Station']].mode())
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print ('The total travel time is :')
    print (df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print ('The average travel time is :')
    print (df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print ('The counts of user types : \n')
    print (df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if ('Gender' in df ) : # To skip in case of Washington
        print ('The counts of gender : \n')
        print (df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Birth Year' in df ) :  # To skip in case of Washington
        print ('The earliest year of brith is : ', df['Birth Year'].min())
        print ('The most recent year of brith is : ', df['Birth Year'].max())
        print ('The most common year of brith is : ', df['Birth Year'].value_counts().idxmax())



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        x=True
        start_loc = 0
        print ('Do you want to see the first 5 row data ? Yes or No')
        y=input().lower()
        if (y=='no'):
            x=False
        while x :
            print (df.iloc[start_loc:start_loc+5])
            start_loc += 5
            print ('Do you want to see the next 5  row data ? Yes or No')
            y=input().lower()
            if (y=='no'):
                break
            print (df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
