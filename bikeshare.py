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
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True:
        # Get user input for city
        city = input('Please enter the name of the city to analyze (Chicago, New York City, or Washington): ').lower()
        if city not in CITY_DATA:
            print('Invalid input. Please enter a valid city name.')
            continue
        else:
            break
    
    while True:
        # Get user input for month
        month = input('Please enter the month to filter by (January, February, March, April, May, June), or type "all" to apply no month filter: ').title()
        if month != 'All' and month not in ['January', 'February', 'March', 'April', 'May', 'June']:
            print('Invalid input. Please enter a valid month name or "all".')
            continue
        else:
            break
    
    while True:
        # Get user input for day
        day = input('Please enter the day of the week to filter by (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday), or type "all" to apply no day filter: ').title()
        if day != 'All' and day not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            print('Invalid input. Please enter a valid day name or "all".')
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day"""
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day of Week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'All':
        df = df[df['Month'] == month]

    # Filter by day of week if applicable
    if day != 'All':
        df = df[df['Day of Week'] == day]
        
        display_data(df)
        
    return df

def display_data(df):
    """Displays data in increments of 5 rows as per user input.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day"""
    start_loc = 0
    while True:
        view_data = input('\nDo you want to see 5 rows of data? Enter yes or no.\n')
        if view_data.lower() != 'yes':
            break
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].value_counts().index[0]
    print('Most Common Month of Travel:', common_month)

    # TO DO: display the most common day of week
    common_day = df['Day of Week'].value_counts().index[0]
    print('Most Common Day of Travel:', common_day)

    # TO DO: display the most common start hour
    print('\nCalculating The Most Common Start Hour of Travel...\n')
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

# TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().index[0]
    print('Most Common Start Station:',     common_start_station)

# TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().index[0]
    print('Most Common End Station:', common_end_station)

# TO DO: display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'] + ' - ' + df['End Station']
    common_start_end_station = df['Start End'].value_counts().index[0]
    print('Most Frequent Combination Station:', common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Trip Duration:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print(user_counts)

    # TO DO: Display counts of gender
    if df.columns.isin(['Gender']).any():
        gender_counts = df['Gender'].value_counts()
        print('Gender Counts:\n', gender_counts)
    else:
        print('Gender data is not available for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    
    if df.columns.isin(['Birth Year']).any():
        earliest_birth = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print('Earliest Birth Year:', earliest_birth)
        print('Most Recent Birth Year:', most_recent_year)
        print('Most Common Birth Year:', most_common_year)
    else:
        print('Birth year data is not available for this city.')
    
    
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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
