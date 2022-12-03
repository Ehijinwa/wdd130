
with open("/Users/chelseaehijinwa/Downloads/life-expectancy.csv") as file: 
    
    next(file)
    max = 0
    min = 999
    total = 0
    counts = 0
    max_asterik = 0
    min_asterik = 1000
    year_of_interest = input("Enter the year of interest")

    for line in file:
        
        lists = line.split(",")
        

        country = lists[0]
        
        year = lists[2]
        
        life_expectancy = float(lists[3])
        
        
        if life_expectancy > max:
            max = life_expectancy
            max_country = country
            max_year = year
        if life_expectancy < min:
            min = life_expectancy
            min_country = country
            min_year = year
        if year_of_interest == year:
            total = total + life_expectancy 
            counts = counts + 1
            if life_expectancy > max_asterik:
                max_asterik = life_expectancy
                maxx_country = country
                maxx_year = year
            if life_expectancy < min_asterik:
                    min_asterik = life_expectancy
                    minn_country = country
                    minn_year = year
    average = total / counts

    print(max)   
    print(min)
    print(max_country)
    print(max_year)
    print(max_asterik)
    print(f"The overall max life expectancy is: {max} from {max_country} in {max_year}")
    print(f"The overall min life expectancy is: {min} from {min_country} in {min_year}")

    print(f"For the year: {year_of_interest}")
    print(f"The average life expectancy across all countries was {average:.2f}")
    print(f"The max life expectancy was in: {maxx_country} with {max_asterik}")
    print(f"The min life expectancy was in: {minn_country} with {min_asterik}")