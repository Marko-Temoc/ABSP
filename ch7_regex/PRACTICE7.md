1. re.compile()
2. so backslashes are properly detected
3. a regex object
4. `.group()` or `.groups` methods
5. all text, all groups
6. preced with backslash
7. `.findall()` returns a list of strings if
there are no groups in the regex pattern,
returns list of tuples with each group an
item in each tuple
8. or
9. non-greedy match, and optional
10. `+` means one or more, `*` means zero or more
11. `{3}` means repeat three times,
`{3,5}` means repeat three to five times (range)
12. `\d'` means any digit,
`\w` means any letter, digit, or underscore,
`\s` means any space, tab, or newline character
13. `\D, \W, \S` means the opposite
14. `.*` will search greedily and match longest
possible match, `.*?` is non-greedy and will
match shortest possible match
15. [0-9a-z]
16. `re.compile(string, [re.I])`
17. matches everyting except `\n`, unless
re.DOTALL is used
18. 'X drummers, X pipers, five rings, X hens'
19. structure and comment the regex within itself
20. `^(\d{1,3})(,\d{3})*$` specifies capturing numbers with up to 3 digits,
but no more, unless its one or more ",\d\d\d" patterns following
21. 
22. 
