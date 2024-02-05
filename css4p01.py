# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 19:46:55 2024

@author: Mohau Phiri
"""

# Assignment 1: Movie Dataset

#Descriptive Statitisc and Information of the raw data

import pandas as df

assign1 = df.read_csv("movie_dataset.csv")

print(assign1.info())

print(assign1.describe())

#Cleaning the raw data

assign1_clean = assign1

assign1_clean.rename(columns={"Runtime (Minutes)" : "Runtime_(minutes)"},  inplace=True)

assign1_clean.rename(columns={"Revenue (Millions)" : "Revenue_(millons)"}, inplace=True)

avg_revenue = assign1_clean["Revenue_(millons)"].mean()

avg_metascore = assign1_clean["Metascore"].mean()

assign1_clean["Revenue_(millons)"].fillna(avg_revenue, inplace=True)

assign1_clean["Metascore"].fillna(avg_metascore, inplace=True)

#Descriptive Statitisc and Information of the clean data

print(assign1_clean.info())

print(assign1_clean.describe())


#Codes for the Quiz Questions

highest_rating = assign1_clean["Rating"].max()                      #Question 1

avg_revenue = assign1_clean["Revenue_(millons)"].mean()             #Question 2

grouped_per_year = assign1_clean.groupby("Year")                    #Question 3
avg_rev_year = grouped_per_year["Revenue_(millons)"].mean()         #Question 3

number_of_movies_2016 = assign1_clean[assign1_clean["Year"] > 2015] #Question 4

number_of_movies_christopher = assign1_clean[assign1_clean["Director"] == "Christopher Nolan"] #Question 5

number_of_movies_rating_above_8 = assign1_clean[assign1_clean["Rating"] > 7.99] #Question 6

#arrange the Rating colum for dataset of number_of_movies_christopher in increasing order. #Question7

avg_rating_year = grouped_per_year["Rating"].mean()                 #Question 8

number_of_movies_2006 = assign1_clean[assign1_clean["Year"] < 2007] #Question 9 (movies produced in 2006)
movies_2006 = len(number_of_movies_2006)
number_of_movies_2016 = assign1_clean[assign1_clean["Year"] > 2015] #Question 9 (movies produced in 2016)
movies_2016 = len(number_of_movies_2016)
increased_movies = (movies_2016-movies_2006)
percentage_increase = (increased_movies/movies_2006)*100

grouped_per_actors = assign1_clean.groupby("Actors")                 #Question 10
common_actor = grouped_per_actors["Actors"].value_counts()


grouped_per_genre = assign1_clean.groupby("Genre")                   #Question 11
number_of_genre = grouped_per_genre["Genre"].count()

#Questio 12 - Correlation of the Numerical Features
import matplotlib.pyplot as plt
plt.bar(assign1_clean["Year"], assign1_clean["Revenue_(millons)"])
plt.xlabel("Year")
plt.ylabel("Revenue (millons)")
plt.show()

plt.scatter(assign1_clean["Rating"], assign1_clean["Revenue_(millons)"])
plt.xlabel("Movie Rating")
plt.ylabel("Revenue (millons)")
plt.show()                                

plt.bar(assign1_clean["Rating"], assign1_clean["Votes"])
plt.xlabel("Movie Rating")
plt.ylabel("Number of Votes")
plt.show()

plt.scatter(assign1_clean["Runtime_(minutes)"], assign1_clean["Revenue_(millons)"])
plt.xlabel("Runtime (minutes)")
plt.ylabel("Revenue (millons)")
plt.show()

plt.bar(assign1_clean["Year"], assign1_clean["Votes"])
plt.xlabel("Year")
plt.ylabel("Number of votes")
plt.show()

plt.scatter(assign1_clean["Rating"], assign1_clean["Runtime_(minutes)"])
plt.xlabel("Movie Rating")
plt.ylabel("Runtime (minutes)")
plt.show()

plt.scatter(assign1_clean["Rating"], assign1_clean["Metascore"])
plt.xlabel("Movie Rating")
plt.ylabel("Metascore")
plt.show()








                           

                           