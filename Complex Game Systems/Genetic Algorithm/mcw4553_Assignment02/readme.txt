Name and CLID: Matthew Williamson | mcw4553
Assignment: Assignment 2 | Genetic Algorithm
CMPS 420
--
Has anyone helped you with this assignment: Yes / No
If yes, identify them and describe the level of help:
Yes, the T.A and Dr. Radle



Did you help anyone else with this assignment: Yes / No
If yes, identify them and describe the level of help:
No.



Have you incorporated anything from outside sources (web sites, books, previous semesters, etc?): Yes/ No
If yes, specify the source and level of similarity:
No

(NOTE: There will be a point reduction if you violate the “Academic Integrity” policy in the syllabus. 
But, if described accurately above, there will be no further disciplinary action.)


--
Compiler: Python 3.3
Operating System: Windows 8

List any other nonstandard libraries used:
(NOTE: Your submission must work on a supported configuration.)


--

If compiling requires anything beyond typing "make" or selecting "build", detail it below: 


If the program supports any interaction, options, or parameters, give details below:
N/A

Overview: Genetic Algorithm as described in class. Ran into implementation problems from lack of understanding the problem specification.
Initially sorted the list and picked the top two fitness members for crossover operations. I was told this was bad and to stop sucking
so I adjusted code to accomodate fitness ratios and moooooooooaaaaar randomness. The program runs slow due to what I believe is
too much sorting. This could be optimized further by smarter insertion into lists and maybe less object oriented code. I am
not sure of the performance overhead from my design but can only assume that it can be improved given more time. Another blocker
was not understanding the proper cnf syntax. I spent alot of time evaluating (a + b) * (c + d) instead of (a * b) + (c * d) this 
would have saved alot of time seeing as how ( a * b) does not need to be evaluated as a literal whereas ( a + b) does because it's
list of acceptable values to make it true is larger. Overall the project was implemented to a level of correctness that satisfies
both the tests cases and myself.