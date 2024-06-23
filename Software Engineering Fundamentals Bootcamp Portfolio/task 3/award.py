# create variable for each event and store as an integer

swim = int(input("Enter athletes time for swimming event in minutes "))
cycle = int(input("Enter athletes time for cycling event in minutes "))
run = int(input("Enter athletes time for running event in minutes "))

# Add the total for all 3 events and store in a new variable

total = swim + cycle + run
print(total)

# use if/elif/else statements to determine award

if total <= 100:
    print("Athlete is awarded Provincial Colours")
elif total >= 101 and total <= 105:
    print("Athlete is awarded Provincial Half Colours")
elif total >= 106 and total <= 110:
    print("Athlete is awarded Provincial Scroll")
else:
    print("Athlete did not qualify for award")
