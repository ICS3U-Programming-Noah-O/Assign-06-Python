#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 29, 2022
# This program uses to arrays to detect all of the perfect square numbers
# inputted by a user and can also dislay a border around an inputted sentence

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


def main():

    print("Welcome!")
    print("This program can determine perfect sqaure numbers")
    print("and also creates customizable borders around inputted text.")
    time.sleep(2)
    print(" ")
    while True:
        user_choice = input("What would you like to do first?\n" +
                            "Perfect Squares (S)\nText Borders (B)\nS/B : ")

        if (user_choice == "S" or user_choice == "s"):
            print("_____________________________________" +
                  "___________________________")
            print("You chose to determine the perfect squares in a list.")
            print(" ")
            time.sleep(2)

            user_array = []
            square_array = []
            while True:

                number_of_numbers = input(
                    "How many numbers would you like on your list? : ")
                try:
                    number_of_numbers_int = int(number_of_numbers)
                    if (number_of_numbers_int > 0):
                        break
                    else:
                        print("Your input must be greater than 0.")

                except Exception:
                    print("Your input must be a whole number.")
            print(" ")
            while True:
                num = input("Enter a number to add to the list: ")
                try:
                    num_int = int(num)
                    if (num_int > 0):
                        user_array.append(num_int)
                        remainder = calculate_perfect_square(
                            num_int, square_array)
                        if (remainder == 0):
                            square_array.append(num)

                        if (len(user_array) == number_of_numbers_int):
                            print(" ")
                            print("______________________" +
                                  "____________________" +
                                  "______________________")
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
                        print("Your input must be positive.")

                except Exception:
                    print("Your input must be a whole number.")
            print(" ")
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

        elif (user_choice == "B" or user_choice == "b"):
            print("____________________________________________________" +
                  "____________")
            print("You chose to create a customizable border around text.")
            time.sleep(2)
            print(" ")
            print("This part of the program can make a border around text.")
            print(" ")
            time.sleep(1.5)
            user_word = input("Enter your sentence: ")
            user_symbol_word = input(
                "Enter the symbol that you want the outline to be: ")
            user_symbol = user_symbol_word[0]

            word_array = user_word.split()
            print(" ")

            longest = find_longest_word(word_array)

            print((user_symbol) * (longest + 4))

            for counter in range(len(word_array)):

                final_word = word_spaces(word_array, longest,
                                         user_symbol, counter)

                print(final_word)

            print(user_symbol * (longest + 4))
            print(" ")
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
        else:
            print("error")


if __name__ == "__main__":
    main()
