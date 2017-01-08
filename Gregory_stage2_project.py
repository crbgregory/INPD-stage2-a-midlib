# -*- coding: utf-8 -*-

easy_mad_lib ="If ___1___ loves a flower, of which just one single ___2___ grows in all the millions and millions of stars, it is enough to make him happy just to look at the stars. He can say to himself, Somewhere, my flower is there... But if the sheep eats the flower, in one moment all his stars will be ___3___... And you think that is not ___4___!"
easy_answers = ["someone", "blossom", "darkened", "important"]

medium_mad_lib ="To me, you are still ___1___ more than a little boy who is just like a hundred ___2___ other little boys. And I have no need of you. And you, on your part, have no need of me. To you, I am nothing more than a fox like a hundred thousand other ___3___. But if you tame me, then we shall need each other. To me, you will be ___4___ in all the world. To you, I shall be unique in all the world."
medium_answers = ["nothing", "thousand", "foxes", "unique"]

hard_mad_lib ="The ___1___ ___2___ have nothing to say to me. And that is sad. But you have hair that is the color of gold. Think how ___3___ that will be when you have ___4___ me! The grain, which is also golden, will bring me back the ___5___ of you. And I shall love to listen to the wind in the wheat."
hard_answers = ["wheat", "fields", "wonderful", "tamed", "thought"]

# Welcome
name = raw_input ("Hello! Welcome to my madlibs game!\nWhat is your name? ")
print "Hello", name,"!"

# Choose difficulty level
def game_difficulty():
    intro_level = raw_input('Please select a game difficulty!\nPossible choices: easy, medium, and hard.\n')
    print intro_level
    difficulty_level = intro_level
    if difficulty_level == "easy":
        correct_answer(easy_mad_lib,easy_answers)
    elif difficulty_level == "medium":
        correct_answer(medium_mad_lib, medium_answers)
    elif difficulty_level == "hard":
        correct_answer(hard_mad_lib, hard_answers)
    else:
        print "That's not an option!"
        return game_difficulty()

# Input answer and check
def correct_answer(question, answer):
    chance = 5
    question_id = 0
    to_replace = '___' + str(question_id + 1) + '___'
    while (question_id < len(answer) ) and (chance > 0):
        flag = 0
        while(flag != 1):
            print question
            print "what is the answer for " + "__"+str(question_id + 1) +"__" + "?"
            input_answer = raw_input("")
            if input_answer == answer[question_id]:
                if question_id == len(answer) - 1:
                    print "Congratulations!\n"
                    question = question.replace(to_replace, input_answer)
                    print question
                else:
                    print "Correct!\n"
                    question =  question.replace(to_replace,input_answer)
                question_id += 1
                flag = 1
            else:
                chance -= 1
                if chance == 0:
                    print "you have no chance!\n\n"
                    break
                else:
                    print "Wrong! you still have " + str(chance) + " chance!\n"

game_difficulty()
print "Thanks for playing, Goodbye!!"
