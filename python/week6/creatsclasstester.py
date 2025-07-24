import createclass

movies = ["M3GAN 2.0, Predator: Killer of Killers, Madea's Destination Wedding"]
game = ["overwatch, fortnite, apex legends"]

mycollection = createclass.Collection(movies, game)

mycollection.setfavGame("overwatch")
mycollection.setFavMovie("M3GAN 2.0")
mycollection.displayColletion()