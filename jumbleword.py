#import random module
import random

#function for choosing random word
def choose():
    #list of word
    words=['clear','programmer','computer','tuple','string']
    
    #choice() method randomly choose
    #any word from the list
    pick=random.choice(words)
    return pick

#function for shuffling the characters of the chosen word
def jumble(word):
    #sample()method shuffling the characters of the word
    random_word=random.sample(word,len(word))
    
    #join() method join the elements
    jumbled=''.join(random_word)
    return jumbled

#function for showing the final score 
def show(result):
    print("Your score is :",result)

    
    
#function for playing the game
def play():   
    #variable for counting score
    result=0
    
    #keep looping
    for i in range(1,6):
        #calling choose function 
        picked_word=choose()
        
        #calling jumble function 
        qn=jumble(picked_word)
        print("jumble word is :",qn)
        
        ans=input("What in your mind?")
        #checking ans is correct or not
        if ans==picked_word:
            #increament by 1
            
            result+=1
        else:
            result-=1
        
    #show()funtion calling
    show(result)
        
            
        
#Driver code
if __name__=='__main__':
    #play() function calling
    play()
        
        

    
    
    