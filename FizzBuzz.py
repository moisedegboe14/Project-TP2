class FizzBuzz:

    def affiche(self , n):
        reponse = ""
        for i in range(n + 1):
         if i==0:
            pass
         elif i%3==0:
            reponse += "Fizz"
         elif i%5==0:
            reponse += "Buzz"
         elif i%15==0:
            reponse += "FrisBee"    
        else:
            reponse += str(i)
        print(reponse)
        return reponse
