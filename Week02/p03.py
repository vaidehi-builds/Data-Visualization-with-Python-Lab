"""3. Write a Python code block to create a dictionary of cricket World 
Cup winners. Let the key be the year; the value is the country that 
won the World Cup that year. Print the name of the best- 
performing country. Display the unique list of countries that 
have won the World Cup."""
def wcwinners():
    winners={1975:"West Indies",1979:"West Indies",1983:"India",
             1987:"Australia",1992:"Pakistan",1996:"Sri Lanka",
             2003:"Australia",2007:"Australia",2011:"India",
             2015:"Australia",2019:"England"}
    count={}
    for country in winners.values():
        count[country]=count.get(country,0)+1

    bestcountry=max(count,key=count.get)
    print("Best performing country: ",bestcountry)
    print("countries that won the world cup: ",set(winners.values()))

wcwinners()


