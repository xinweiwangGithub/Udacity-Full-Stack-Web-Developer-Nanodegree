import fresh_tomatoes
import media


toy_story = media.Movie("Toy",
                        "this is a story",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=GJrzh746lMs")
# print(toy_story.storyline)

harry_potter = media.Movie("Harry PotterI",
                           "A young wizard who discovers his magical heritage as he makes close friends and a few enemies in his first year at the Hogwarts School of Witchcraft and Wizardry.",
                           "https://en.wikipedia.org/wiki/Harry_Potter_and_the_Philosopher%27s_Stone#/media/File:Harry_Potter_and_the_Philosopher%27s_Stone_Book_Cover.jpg",
                           "https://www.youtube.com/watch?v=RzCjI3Jy7E8")
print (harry_potter.storyline)
harry_potter.storyline()


print (media.Movie.VALID_RATINGS)

movies = [toy_story, harry_potter]
fresh_tomatoes.open_movies_page(movies)
print (media.Movie.__doc__)