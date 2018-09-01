# DGMA
Design Dataframe For Google Distance Matrix API

Python script for creating a dataframe of latitude and longitude to be passed to Distance Matrix API.

This is for all pair shortest distance problem.

Points - [a,b,c,d,e,f,g,h]

This script will give us pairs of [

(a,b)(a,c)(a,d)(a,e)(a,f)(a,g)(a,h) = 7

(b,c)(b,d)(b,e)(b,f)(b,g)(b,h) = 6

(c,d)(c,e)(c,f)(c,g)(c,h) = 5

(d,e)(d,f)(d,g)(d,h) = 4

(e,f)(e,g)(e,h) = 3

(f,g)(f,h) = 2

(g,h) = 1

]

Input - Points (n)

Output - Pairs [(n * n-1 )/ 2]
