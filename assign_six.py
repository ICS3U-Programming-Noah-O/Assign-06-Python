#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 29, 2022
# This program uses to arrays to detect all of the perfect square numbers
# inputted by a user and can also display a border around an inputted sentence

import math
import time
import colorama
from colorama import Fore, Back, Style


# This function calculates if a number is a perfect square
def calculate_perfect_square(user_num, square_a):
    square = math.sqrt(user_num)
    total_two = user_num % square

    return total_two


# This function determines which number in an array is the longest
def find_longest_word(array):
    longest_word = 0
    for counter in range(len(array)):
        if (len(array[counter]) > longest_word):
            longest_word = len(array[counter])
    return longest_word


# This function determines the number of spaces that
# are needed between each word and the border
def word_spaces(w_array, long_word, symbol, count):
    if (len(w_array[count]) == long_word):
        words = (symbol + " " + w_array[count] + " " + symbol)
        return words
    else:
        words = w_array[count]
        words = symbol + " " + words
        while True:
            if (len(words) != (long_word + 1)):
                words = words + " "
            if (len(words) == (long_word + 1)):
                break
        words = words + "  " + symbol
        return words


# This function determines what question the user wants to pick, gets the
# user input, and makes sure that the input is valid
def main():
    # Display the intro message
    print("Welcome!")
    print("This program can determine perfect square numbers")
    print("and also creates customizable borders around inputted text.")
    time.sleep(2)
    print(" ")
    # Ask the user what question they want to pick
    while True:
        user_choice = input("What would you like to do first?\n" +
                            "Perfect Squares (S)\nText Borders (B)\nS/B : ")
        # Check if the user input is for the perfect squares
        if (user_choice == "S" or user_choice == "s"):
            print("_____________________________________" +
                  "___________________________")
            print("You chose to determine the perfect squares in a list.")
            print(" ")
            time.sleep(2)

            user_array = []
            square_array = []
            while True:
                # Ask user for how many numbers they want
                number_of_numbers = input(
                    "How many numbers would you like on your list? : ")
                # Make sure that the input is valid
                try:
                    number_of_numbers_int = int(number_of_numbers)
                    if (number_of_numbers_int > 0):
                        break
                    else:
                        # Error message if user number is 0 or below
                        print("Your input must be greater than 0.")

                except Exception:
                    # Error message if input is not a number
                    print("Your input must be a whole number.")
            print(" ")
            while True:
                # Ask the user for numbers to add to the list
                num = input("Enter a number to add to the list: ")
                # Make sure that the input is valid
                try:
                    num_int = int(num)
                    if (num_int > 0):
                        # If the number is valid add it to the array
                        user_array.append(num_int)
                        # Call a function to determine if the number
                        # is a perfect square
                        remainder = calculate_perfect_square(
                            num_int, square_array)
                        # If there is no remainder it is a perfect square
                        if (remainder == 0):
                            square_array.append(num)

                        if (len(user_array) == number_of_numbers_int):
                            print(" ")
                            print("______________________" +
                                  "____________________" +
                                  "______________________")
                            # Print all of the perfect squares
                            print("Out of all of your inputs, these numbers" +
                                  "are perfect squares: ")
                            print(" ")
                            for counter in range(len(square_array)):
                                print("{} = {} * {}".format(
                                    square_array[counter], int(math.sqrt(
                                        int(square_array[counter]))), int(
                                            math.sqrt(int(
                                                square_array[counter])))))
                            break
                    else:
                        # Error message if the input is negative
                        print("Your input must be positive.")

                except Exception:
                    # Error message if the input is not a number
                    print("Your input must be a whole number.")
            print(" ")
            # Ask the user if they want to calculate again
            play_again = input(
                "Would you like to use this program again? y/n: ")
            if (play_again == "y" or play_again == "Y" or play_again
               == "Yes"):
                print("_____________________________________________" +
                      "___________________")
                print(" ")
                print(" ")
                continue
            else:
                break
        # Check if the user input is for the border option
        elif (user_choice == "B" or user_choice == "b"):
            print("____________________________________________________" +
                  "____________")
            print("You chose to create a customizable border around text.")
            time.sleep(2)
            print(" ")
            print("This part of the program can make a border around text.")
            print(" ")
            time.sleep(1.5)
            # Ask the user to enter their sentence
            user_word = input("Enter your sentence: ")
            # Ask the user to enter their symbol to make the border
            user_symbol_word = input(
                "Enter the symbol that you want the outline to be: ")
            # Make sure that the symbol is only one character
            user_symbol = user_symbol_word[0]
            # Split the sentence into an array of words
            word_array = user_word.split()
            print(" ")
            # Call a function to find the longest word
            longest = find_longest_word(word_array)

            print((user_symbol) * (longest + 4))

            for counter in range(len(word_array)):
                # Print the border and use a function to calculate
                # the correct amount of spaces
                final_word = word_spaces(word_array, longest,
                                         user_symbol, counter)

                print(final_word)

            print(user_symbol * (longest + 4))
            print(" ")
            # Ask the user if they want to play again
            play_again_2 = input(
                "Would you like to use this program again? y/n: ")
            if (play_again_2 == "y" or play_again_2 == "Y" or play_again_2
               == "Yes"):
                print("________________________________" +
                      "________________________________")
                print(" ")
                print(" ")
                continue
            else:
                break
        # Error message if user input is invalid
        else:
            print("You must pick either 'S' or 'B' ")


if __name__ == "__main__":
    main()
