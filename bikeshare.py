from ssl import SSLSocket
import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # In this block, get what a user should do for input.
    # city month day, In the very same format, lower it, check it whether it's valid
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while 1:
        city = input("tap in the city you are interested in").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("wrong input for city")
    # TO DO: get user input for month (all, january, february, ... , june)
    while 1:
        month = input("tap in the month you are interested in").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("wrong input for month")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while 1:
        day = input("tap in the day_of_week you are interested in").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("wrong input for day_of_week")
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
    #
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime,format it for use
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['city'] = city

    # filter by month if applicable, month is an input para
    if month != 'all':
        # use the index of the months list to get the corresponding int, +1 in that index begin with 0
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # it turns month from word to corresponding number

        # filter by month to create the new dataframe, a new df is created by month
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        # again it filter the df by day based on the new df
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month,use the mode() funcion to describe the most common value
    # in a column
    print("The most common month is ", df['month'].mode()[0])
    print("\n")

    # TO DO: display the most common day of week
    print("The most common day is ", df['day'].mode()[0])
    print("\n")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    # get the piriod time
    # make no sense
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Start station and End station is directly given in the .csv file,
    # so just use the mode() to get the result. Take care of the Capital of the column name
    # TO DO: display most commonly used start station
    print("The most commonly used start station is ",
          df['Start Station'].mode()[0])
    print("\n")
    # TO DO: display most commonly used end station
    print("The most commonly used end station is ",
          df['End Station'].mode()[0])
    print("\n")
    # TO DO: display most frequent combination of start station and end station trip
    # Create the column use the string method " " + " " for combining
    df['combination'] = df['Start Station'] + " " + df['End Station']
    # And then goes like above, nothing special
    print("The most frequent combination of start station and end station trip is: ",df['combination'].mode()[0])

    # make no sense
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # Main things, total, average
    # TO DO: display total travel time
    # use sum() to realize the mathematic operation in a column
    print("The total travel time is", df['Trip Duration'].sum(), "\n")

    # TO DO: display mean travel time
    print("The total mean time is", df['Trip Duration'].mean(), "\n")

    # make no sense
    # No need concern
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    # use the value_counts() to operate on column gender
    # value_counts(no need for para)
    user_types = df['User Type'].value_counts()
    print(user_types, "\n")
    # TO DO: Display counts of gender
    city=df['city'].mode()[0]
    if city != "washington":
        gender_count = df['Gender'].value_counts()
        print('The counts of gender is:', gender_count, "\n")
    # TO DO: Display earliest, most recent, and most common year of birth
    # use min max idmax to operate on column Birth Year
    # Also pay attention to the column name's format
    if city != 'Washington':
        print('The earlist year of birth:', df['Birth Year'].min(), "\n")
        print('The most recent year of birth:', df['Birth Year'].max(), "\n")
        birthyear_count = df['Birth Year'].value_counts()
        print('The most common year of birth:', birthyear_count.idxmax(), "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(raw_dataframe):
    """Ask user if want to see the first five rows of raw data and ask him if want to see more rows"""

    user_request = input('Do you want to see the first five rows of raw data? Enter "yes" to go on, or enter "no" to skip')
    # In advance, define iterator i and initialize it as 0 (it always comes like this)
    # i is used for the very beginning of the 5 rows coming out
    i = 0
    # define breaking_flag as a flag, it can indicate the state of loop "go on" or "break"
    # it should be inactive at the very beginning, namely "no"
    breaking_flag = 'no'
    # while loop will print the first five rows of raw data and break when user doesn't need more or all raw data has been printed
    while user_request.strip().title() == 'Yes':
        # use another index "j" to go through every single 5 rows
        # exact times of loop, I'd like to use for loop
        for j in range(5):
            # before print the raws, check if the interator goes out of the limit(with in the df)
            # use shape to get the rows value and index needs to -1
            if (i+j) < raw_dataframe.shape[0] - 1:
                # print the row just checked 
                print(raw_dataframe.loc[i+j,:])
            else:
                # in this else part, it's the one of the two break states
                # it is over range, no data to show
                # so turn the flag to "yes"
                breaking_flag = "yes"
                break
        # the for loop above is in charge of the every 5 rows

        # especially pay attention, if the flag has been turned, there is no need to consider next 5
        if breaking_flag == 'yes':
            break
        user_request = input('Do you want to go on with the next five rows? enter "yes" or "no"')
        i += 5
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        # raw data need to be a variable seperately from the df we dealed with
        raw_dataframe = pd.read_csv(CITY_DATA[city])
        
        display_raw_data(raw_dataframe)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()