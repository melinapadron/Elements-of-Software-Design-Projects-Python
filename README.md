# Elements-of-Software-Design-Projects-Python
Description: Chris has to complete a programming assignment overnight. He has to write n lines of code before morning.
He is dead tired and he tries drinking some black coffee to keep him awake. But each time he drinks a cup
of coffee he stays awake for a short amount of time but his productivity goes down by a constant factor k
This is how he plans to write the program. He will write the first v lines of code, then drink his first cup
of coffee.
•Since his productivity has gone down by a factor of k he will write v // k lines of code.
•He will have another cup of coffee and then write v // k**2 lines of code.
•He will have another cup of coffee and write v // k**3 lines of code and so on.
•He will collapse and fall asleep when v // k ** p becomes 0.
Now Chris does want to complete his assignment and maximize on his sleep. So he wants to figure out
the minimum allowable value of v for a given productivity factor that will allow him to write at least n lines of code before he falls asleep. The output will be v lines of code the Chris has to write, as well as the time it took for each function. 

 First, I wrote a function that uses a linear search to solve the problem. Then I wrote a function that uses a modified binary search algorithm to solve it.
again. Both functions will return the same answer, but the binary search method will usually be faster.
