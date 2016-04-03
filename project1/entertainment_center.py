import fresh_tomatoes
import media

""" This file stores all the films and their information, then display them """

pursuit_of_happyness = media.Movie(
    "The Pursuit of Happyness",
    "The film features Will Smith as Gardner, a homeless salesman."
    " Smith's son Jaden co-stars, making his film debut as"
    " Gardner's son, Christopher Jr.",
    "https://upload.wikimedia.org/wikipedia/en/8/81/"
    "Poster-pursuithappyness.jpg",
    "https://www.youtube.com/watch?v=SIZKoak6gp8")

harry_potter = media.Movie(
    "Harry Potter I",
    "A young wizard who discovers his magical heritage as he makes close "
    "friends and a few enemies in his first year at the Hogwarts School of "
    "Witchcraft and Wizardry.",
    "https://upload.wikimedia.org/wikipedia/en/6/6b/Harry_Potter_and_"
    "the_Philosopher%27s_Stone_Book_Cover.jpg",
    "https://www.youtube.com/watch?v=RzCjI3Jy7E8")

forrest_gump = media.Movie(
    "Forrest Gump",
    "The story depicts several decades in the life of Forrest Gump, "
    "a slow-witted and naive, but good-hearted and athletically "
    "prodigious man from Alabama who witnesses, and in some cases"
    " influences, some of the defining events of the latter half of "
    "the 20th century in the United States",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
    "https://www.youtube.com/watch?v=EtYNngO7eq4")

american_beauty = media.Movie(
    "American Beauty",
    "The film is described by academics as a satire of American middle "
    "class notions of beauty and personal satisfaction; analysis has "
    "focused on the film's explorations of romantic, and paternal love,"
    " sexuality, beauty, materialism, self-liberation and redemption.",
    "https://upload.wikimedia.org/wikipedia/en/b/b6/American_Beauty_"
    "poster.jpg",
    "https://www.youtube.com/watch?v=4qVv7xg-uDY&oref=https%3A%2F%2"
    "Fwww.youtube.com%2Fwatch%3Fv%3D4qVv7xg-uDY&has_verified=1")

monalisa_smile = media.Movie(
    "Mona Lisa Smile",
    "Katherine Ann Watson (Julia Roberts), a 30-year-old graduate "
    "student in the department of Art History at Oakland State, "
    "takes a position teaching 'History of Art' at Wellesley "
    "College, a conservative women's private liberal arts college "
    "in Massachusetts, because she wants to make a difference and "
    "influence the next generation of women.",
    "https://upload.wikimedia.org/wikipedia/en/0/0e/Monalisasmile.jpg",
    "https://www.youtube.com/watch?v=qPmc4kvz0l8")

shawshank_redemption = media.Movie(
    "shawshank redemption",
    "The film tells the story of Andy Dufresne, a banker who is "
    "sentenced to life in Shawshank State Penitentiary for the "
    "murder of his wife and her lover, despite his "
    "claims of innocence. During his time at the prison, he "
    "befriends a fellow inmate, Ellis Boyd 'Red' Redding, and "
    "finds himself protected by the guards after the "
    "warden begins using him in his money-laundering operation.",
    "https://upload.wikimedia.org/wikipedia/en/8/81/Shawshank"
    "RedemptionMoviePoster.jpg",
    "https://www.youtube.com/watch?v=6hB3S9bIaco")


movies = [pursuit_of_happyness, harry_potter,
          forrest_gump, shawshank_redemption,
          american_beauty, monalisa_smile]

fresh_tomatoes.open_movies_page(movies)
