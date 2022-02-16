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
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
            city = input("choose a city name from \n 1-Chicago  \n 2-New york city \n 3-Washington \n city name is: ").lower()
            if city in CITY_DATA:
                break
                
                
            else:
                print("\nyou choosed a invalid city , enter a right city name !")
        
            
        # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        months = ["january" , "feburary" , "march" , "april" , "may" , "june" , "all"]
        month = input("\nEnter a month from \n 1-January \n 2-Feburary \n 3-March \n 4-April \n 5-May \n 6-June \n 7-All \n month is : ").lower()

        if month in months:
            break
            

        else:
            print("Sorry , but you must enter a vaild month from january to june or all ")
            
            
        
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        days = ["saturday" , "sunday" , "monday" , "tuesday" , "wednesday" , "thursday" , "friday" , "all"]
        day = input("Enter a day name of the week from \n 1-Saturday \n 2-Sunday \n 3-Monday \n 4-Tuesday \n 5-Wednesday \n 6-Thursday \n 7-Friday \n 8-All \n day is : ").lower()
        
        
        if day in days:
            break
            
        else:
            print("Sorry , but you must enter a vaild day from saturday to friday or all ")

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

    df["Start Time"] = pd.to_datetime(df["Start Time"])

    df["month"] = df["Start Time"].dt.month

    df["day_of_week"] = df["Start Time"].dt.day_name()
    
    df["start hour"] = df["Start Time"].dt.hour
    

    #filter months
    if month != "all":
        months =["january" , "ferburary" , "march" , "april" , "may" , "june"]  
        month = months.index(month)+1
        df = df[df["month"] == month]
        
     #filter days    
    if day != "all":
        df = df[ df["day_of_week"] == day.title() ]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    most_common_month = df["month"].mode()[0]
    
    print("the most common month is {}".format(most_common_month))
    
    
    

    # TO DO: display the most common day of week
    
    
    most_common_day = df["day_of_week"].mode()[0]
    
    print("the most common day is {}".format(most_common_day))
    
    
    

    # TO DO: display the most common start hour
    most_common_hour = df["start hour"].mode()[0]
    
    print("the most common hour is {}".format(most_common_hour))
    
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start_station = df["Start Station"].mode()[0]
    
    print("the most commonly used start station is {}".format(most_used_start_station))

    # TO DO: display most commonly used end station
    most_used_end_station = df["End Station"].mode()[0]
    
    print("the most commonly used end station is {}".format(most_used_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    
    df["path"] = (df["Start Station"] + " " +df["End Station"]).mode()[0]
    
    print("the most frequent path in trip is {}".format(df["path"]))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("the total time taked for trip is {}".format(total_travel_time))

    # TO DO: display mean travel time
    average_travel_time = df["Trip Duration"].mean()
    print("the average time taked for trip is {}".format(average_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df["User Type"].value_counts()
    print(count_user_type)
    
    
    # TO DO: Display counts of gender
    
    
    
    # washington dataset does't contain a gender column
    if "Gender" in df:
        count_user_gender = df["Gender"].value_counts()
        print(count_user_gender )
    else:
        print("Gender is not availabe to show ")
        
        
    # TO DO: Display earliest, most recent, and most common year of birth
    
    
    
    # washington dataset does't contain a Birth Year column
    if "Birth Year" in df:
        most_earliest_year = int(df["Birth Year"].min())
        print("the most earliest year of birth is {}".format(most_earliest_year))
        
        most_recent_year = int(df["Birth Year"].max())
        print("the most recent year of birth is {}".format(most_recent_year))
        
        most_common_year = int(df["Birth Year"].mode()[0])
        print("the most common year of birth is {}".format(most_common_year))
        

    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_five_rows(df):
    """
    funtion displays first five rows of data and asked to show more five rows if user need 
    """
    
    num = 0             
    pd.set_option("display.max_columns" , None)
    while True:
        user_choose = input("Would you like to display first five rows ? : ").lower()
        if user_choose not in ["yes" , "no"]:
             print("\nyou entered unavailabe choose please choose yes or no")
        elif user_choose == "no":
             print("\nyou do not want to see the first five rows")
             break
        else:
            print(df[num:num+5])
            break
    while True:        
            user_choose_rows = input("\nWould you like to display more five rows ? : ").lower()
            if user_choose_rows  =="yes":
                num =num+5
                print(df[num:num+5])
            elif user_choose_rows =="no":
                print("\nyou do not want to see more five rows")
                break
            else:
                print("\nyou entered unavailabe choose please choose yes or no")
         
        
                
        
    
    
    
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_five_rows(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
