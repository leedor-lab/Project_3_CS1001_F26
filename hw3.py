import data

#the pursose of this function is to sum all the populations of each county in the country during 2014. loooping over a list returning the int value of a dict. 
def population_total(counties: list[CountyDemographics]) -> int:
    sum=0 
    for county in counties:
        sum+=county.population["2014 Population"]
    return sum

#the purpose of this function is to filter each county by state and return that filtered list where the coiunty matches the state passed into the function. the data is represented as a list.
def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    l=[]
    for county in counties:
        if county.state==state:
            l.append(county)
    return l

#the purpose of this function is to total up the amount of people with specific education in the 2014 county population. the data is represented as a float
def population_by_education(counties: list[CountyDemographics], key: str) -> float:
    total=0
    for county in counties:
        if key in county.education:
            total+=county.population["2014 Population"]*((county.education[key])/100)
    return total 

#the purpose of this function is to total up the amount of people with specific ethnicity in the 2014 county population. the data is represented as a float
def population_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    total=0
    for county in counties:
        if key in county.ethnicities:
            total+=county.population["2014 Population"]*((county.ethnicities[key])/100)
    return total        

#the purpose of this functiom is to total up the amount of people below the povert level across the counties in 2014 population. the data is represented as a float.
def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total=0
    key="Persons Below Poverty Level"
    for county in counties:
        if key in county.income:
            total+=county.population["2014 Population"]*((county.income[key])/100)
    return total     

#The purpose of this function is to calculate the percentage of people with an education in 2014 of all the provided counties. the data is represented as a float.
def percent_by_education(counties: list[CountyDemographics], key: str) -> float:
    total_pop=population_total(counties)
    total_ed=population_by_education(counties,key)
    if total_pop==0:
        return 0
    return 100*(total_ed/total_pop)

#The purpose of this function is to calculate the percentage of people with a specific ethnicity in 2014 of all the provided counties. the data is represented as a float.
def percent_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    total_pop=population_total(counties)
    total_et=population_by_ethnicity(counties,key)
    if total_pop==0:
        return 0
    return 100*(total_et/total_pop)

#The purpose of this function is to calculate the percentage of people below the poverty level in 2014 of all the provided counties. the data is represented as a float.
def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_pop=population_total(counties)
    total_bp=population_below_poverty_level(counties)
    if total_pop==0:
        return 0
    return 100*(total_bp/total_pop)

#the purpose of this function is to check if the county's percentage of a specific education is greater than a given threshold. the data is represented as a list of objects.
def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    l=[]
    for county in counties:
        if key in county.education and county.education[key]>threshold:
            l.append(county)
    return l        


#the purpose of this function is to check if the county's percentage of a specific education is less than a given threshold. the data is represented as a list of objects.
def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    l=[]
    for county in counties:
        if key in county.education and county.education[key]<threshold:
            l.append(county)
    return l    

#the purpose of this function is to check if the county's percentage of a specific ethnicity is greater than a given threshold. the data is represented as a list of objects.
def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    l=[]
    for county in counties:
        if key in county.ethnicities and county.ethnicities[key]>threshold:
            l.append(county)
    return l    

#the purpose of this function is to check if the county's percentage of a specific ethnicity is less than a given threshold. the data is represented as a list of objects.
def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    l=[]
    for county in counties:
        if key in county.ethnicities and county.ethnicities[key]<threshold:
            l.append(county)
    return l    

#the purpose of this function is to check if the county's percentage of people below the povert level is greater than a given threshold. the data is represented as a list of objects.
def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    l=[]
    for county in counties:
        if county.income["Persons Below Poverty Level"]>threshold:
            l.append(county)
    return l    

#the purpose of this function is to check if the county's percentage of people below the povert level is less than a given threshold. the data is represented as a list of objects.
def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    l=[]
    for county in counties:
        if county.income["Persons Below Poverty Level"]<threshold:
            l.append(county)
    return l 



