#  Create a CSV file called “Movies.csv” with details of 10 movies-  Movie Name, Language, Genre, Rating, Review. 
# a. Read CSV file into a dataframe and find the movie with the highest rating. 
# b. Write the details of all “Hindi movies into a file “HindiMovies.csv”
import pandas as pd

movies = { "Movie Name" : ["3Idiots","Intersteller", "The Imitation Game","Sholay","Dept Q",
                           "The Devil Wears Prada","Kabhi Khushi Kabhi Gam","The Intern","Geostorm",
                           "Om Shanti Om"],
            "Language" : ["Hindi","English","English","Hindi","English","English","Hindi","English","English","Hindi"],
            "Genre": ["Comedy","Sci-Fi","Biographical","Action","Mystery","Drama","Family","Comedy","Sci-Fi","Romance"],
            "Rating": [9.0,8.6,8.0,8.5,7.2,7.0,7.5,7.1,5.3,8.8],
            "Review":["Inspiring and emotional","Visually strong","Brilliant historical drama",
                      "Classic action film","Thrilling mystery","Fashion world drama","Family entertainer",
                      "Feel-good Comedy","Disaster sci-fi","Iconic love story"]
        }
movies_df=pd.DataFrame(movies)
movies_df.to_csv("Week05/Movies.csv", index=False)
movie=pd.read_csv("Week05/Movies.csv")

highest_rating=movie.loc[movie["Rating"].idxmax()]
print("Movie with highest rating: ")
print(highest_rating)

hindi_movies=movie[movie["Language"]=="Hindi"]
hindi_movies.to_csv("Week05/HindiMovies.csv",index=False)
