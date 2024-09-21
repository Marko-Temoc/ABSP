1. program's current working directory (cwd)
2. root folder; on windows this is 'C:\\', on Linux its '/'
3. 'C:/Users/Al'
4. A `TypeError', since its an inappropriate operand for str types
5. os.getcwd() returns current working directory as a string, and os.chdir() changes current working directory
6. the '.' folder is the cwd, and '..' is the parent directory of the cwd
7. 'C:\\bacon\\eggs\\' is the dir name, and 'spam.txt' is the base name, according to os.path.dirname() and os.path.basename()
8. 'r' for read mode which is the default if no arg is given, 'w' for write mode, and 'a' for append mode (also 'wb' for write binary mode)
9. overrites the opened file entirely (append mode is useful to not do that)
10. read() returns one large string, readlines() returns a list of strs, one for each line including linebreaks at the end
11. a dictionary

