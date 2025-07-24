class collection:
    def _init_(self, movieList, gameList):
        self.movieList = []
        self.gameList = []
        self.favGame =  ""
        self.favMovie = ""
        
        self.movieList = movieList
        self.gameList = gameList
        
    def Addgame(self, game):
        self.gameList.append(game)
        if game in self.gameList:
            print("game is already in collection")
        else:
            self.gameList.append(game)
        
        
        
    def addmovie(self, movie):
        self.movieList.append(movie)
        
        
        
    def removegame(self, game):
        if game in self.gameList:
            self.gameList.remove(game)
        else:
            print("game not found")
            
    
    def DisplayGames(self):
        for game in self.gameList(self):
            print(game)
            
            
    def displayMovies(self):
        for movies in self.movieList:
            print(movies)
            
            
    def displayfavGame(self):
        print(f'fav Game: {self.favGame}')
        
    def displayfavMovie(self):
        print(f'fav Movie: {self.favMovie}')
        
    
    def displayColletion(self):
        self.DisplayGames()
        self.displayfavGame()
        self.displayMovies()
        self.displayfavMovie()
        
        
    def SetfavMovie(self, movie):
        if movie not in self.movieList:
            self.addmovie(movie)
        self.favMovie = movie
        
        
    def SetfavGame(self, game):
        if game not in self.gameList:
            self.Addgame(game)
        self.favMovie = game