# FILE NAME - coin_toss.py

# NAME: Elizabeth Mautz
# DATE: February 28, 2026
# BRIEF DESCRIPTION: randomly return heads or tails.
# random number 1 to 100 is generated.
# 51 or greater is tails. otherwise it's heads



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

# Don't forget to import random!!!!!
import random
print("===== Coin Flipper =====")
number = random.randint(1,100)

if number >= 51:
    print("Tails")
else:
    print("Heads")








########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 
The hardest part was remembering how to include a random number including both numbers on the range.
I put that as a print statement and ran the range as (1,2) at first to make sure that both values
were included in the range.







'''

########################################
#            ATTESTATION
########################################
'''
It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 
[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[ X] I'm solid. Totally got it.
'''
