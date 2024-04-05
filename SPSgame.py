class game:
        def user_input(self):
            
            possible=["stone", "paper", "scissor","STONE","PAPER","SCISSOR"]
            self.possible=possible
            person1=input("person1-enter your's stone/paper/scissor: ")
            self.person1=person1
            person2=input("person2-enter your's stone/paper/scissor: ")
            self.person2=person2

    # class again:
    #     def once_again(self):
            
    #         print("do you want play again")   
    #         final=input("enter Y/N ")  
    #         self.final=final
            

class first(game):
        
        def play(self):
            n=0  
            tie=0
            per1=0
            per2=0
            while n==0:
                

                self.user_input()
            
        
                if self.person1 in self.possible and self.person2 in self.possible:

                            if self.person1==self.person2 :
                                print("game tie") 
                                tie+=1
                                

                            elif self.person1=="scissor" and self.person2=="stone" :
                                print("person2 wins")
                                per2+=1 
                                    
                            elif self.person1=="stone" and self.person2 =="paper" :
                                print("person2 wins")
                                per2+=1 
                                
                            elif self.person1=="paper" and self.person2=="scissor":
                                print("person2 wins")
                                per2+=1 

                            else:
                                print("person1 wins") 
                                per1+=1 

                            
                else:
                    print("you have entered wrong input")

                
                print("do you want play again")   
                choice=input("enter y/n ")
                if choice=="y":
                    n=0

                elif choice=="n":
                    print(tie)
                    print(per1)
                    print(per2)
                    break

                    


                
        
            
            
v=first()
v.play() 



            
