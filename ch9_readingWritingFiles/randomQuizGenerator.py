#!/usr/bin/env python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
   'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
   'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#generate 35 quiz files
for quizNum in range(35):
        #create quiz and answer key files
        quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
        answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')
        #write out header for quiz
        quizFile.write('Name:\n\nDate\n\nPeriod:\n\n')
        quizFile.write((' ' * 20) + f'State Capitals Quiz (Form {quizNum + 1})')
        quizFile.write('\n\n')
        #create list of shuffled states
        states = list(capitals.keys())
        random.shuffle(states)
        #loop through all 50 states, making a question for each
        for questionNum in range(50):
                #get right and wrong answers
                #grab capital and store as correct answer
                correctAnswer = capitals[states[questionNum]]
                #make list of all the capitals of the states
                wrongAnswers = list(capitals.values())
                #delete only correct capital from list
                del wrongAnswers[wrongAnswers.index(correctAnswer)]
                #pick 3 random wrong answers for list
                wrongAnswers = random.sample(wrongAnswers, 3)
                #add right answer to 3 incorrect answers to list
                answerOptions = wrongAnswers + [correctAnswer]
                random.shuffle(answerOptions)

                #write question and answer options to quiz file
                quizFile.write(f"{questionNum + 1}. What is the capital of {states[questionNum]}?\n")
                for i in range(4):
                        quizFile.write(f"       {'ABCD'[i]}. { answerOptions[i]}\n")
                quizFile.write('\n')
                #write the answer key to a file
                answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}, ")
        quizFile.close()
        answerKeyFile.close()
