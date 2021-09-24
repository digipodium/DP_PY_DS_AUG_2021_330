
class Movie:
    def __init__(self,title,duration,year,director,cast=[],genre=[]):
        # instance variable
        self.title = title
        self.duration = duration
        self.year = year
        self.director = director
        self.cast = cast
        self.genre = genre

    # instance method
    def info(self):
        print(f'Movie Detail: {self.title}')
        print(f'release year: {self.year}')
        print(f'duration: {self.duration}')
        print(f'director: {self.director}')
        print(f"Cast:")
        for people in self.cast:
            print(f"->{people}")
        print(f"Genre : {'/'.join(self.genre)}")    

m1 = Movie('Rainmaker','95 mins',1997, 'Francis Ford Coppola',genre = ['Crime','Drama'])
m2 = Movie("Avenger", '100 mins', 2015, 'Josh Whedon',cast=['Chris Evans','Chris Hemsworth'])

m1.info()
m2.info()

    



        