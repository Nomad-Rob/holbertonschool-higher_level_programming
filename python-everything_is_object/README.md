This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should read all documentation first (as usual :)), then take the time to think and brainstorm about what you think and why. Try to do this without coding anything for a few hours.

Trying examples in the Python interpreter will give you most of the answers without having to think about it. Don’t go this route. First read, then think, then brainstorm. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.

Note that during interviews for Python positions, you will most likely have to answer to these type of questions.

All your answers should be only one line in a file. No space before or after the answer.

Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.7.*)
All your files must be executable
The length of your files will be tested using wc
.txt Answer Files
Only one line
No Shebang on the first line (i.e. “#!/usr/bin/python3”)
All your files should end with a new line


Tasks
0. Who am I?
mandatory
What function would you use to print the type of an object?

Write the name of the function in the file, without ().

Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: python-everything_is_object
File: 0-answer.txt

1. Where are you?
mandatory
How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

2. Right count
mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

3. Right count =
mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

4. Right count =
mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

5. Right count =+
mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

6. Is equal
mandatory
What do these 3 lines print?

7. Is the same
mandatory
What do these 3 lines print?

8. Is really equal
mandatory
What do these 3 lines print?

9. Is really the same
mandatory
What do these 3 lines print?

10. And with a list, is it equal
mandatory
What do these 3 lines print?

11. And with a list, is it the same
mandatory
What do these 3 lines print?

12. And with a list, is it really equal
mandatory
What do these 3 lines print?

13. And with a list, is it really the same
mandatory
What do these 3 lines print?

14. List append
mandatory
What does this script print?

15. List add
mandatory
What does this script print?

16. Integer incrementation
mandatory
What does this script print?

17. List incrementation
mandatory
What does this script print?

18. List assignation
mandatory
What does this script print?

19. Copy a list object
mandatory
Write a function def copy_list(a_list): that returns a copy of a list.

The input list can contain any type of objects
Your file should be maximum 3-line long (no documentation needed)
You are not allowed to import any module

20. Tuple or not?
mandatory
a = ()
Is a a tuple? Answer with Yes or No.

21. Tuple or not?
mandatory
a = (1, 2)
Is a a tuple? Answer with Yes or No.

22. Tuple or not?
mandatory
a = (1)
Is a a tuple? Answer with Yes or No.

23. Tuple or not?
mandatory
a = (1, )
Is a a tuple? Answer with Yes or No.

24. Who I am?
mandatory
What does this script print?

a = (1)
b = (1)
a is b

25. Tuple or not
mandatory
What does this script print?

a = (1, 2)
b = (1, 2)
a is b

26. Empty is not empty
mandatory
What does this script print?

a = ()
b = ()
a is b

27. Still the same?
mandatory
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.



28. Same or not?
mandatory
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.

29. Python3: Mutable, Immutable... everything is object!
mandatory
Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):

introduction
id and type
mutable objects
immutable objects
why does it matter and how differently does Python treat mutable and immutable objects
how arguments are passed to functions and what does that imply for mutable and immutable objects
If you worked on advanced tasks, please also include what you did learn in those tasks in the blog post.

Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.

When done, please add all urls below (blog post, LinkedIn post, etc.)

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.
