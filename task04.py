class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = int(duration) 
        self.rating = float(rating)   

movie1 = Movie("Inception", "action", 148, 8.8)


print("Kino nomi:", movie1.title)
print("Janri:", movie1.genre)
print("Davomiyligi:", movie1.duration, "daqiqalar")
print("IMDB reytingi:", movie1.rating)
