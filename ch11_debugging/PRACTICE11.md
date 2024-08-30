1. `assert spam >= 10, 'Spam is less than ten!'`
2. `assert bacon.lower() != eggs.lower(), 'Spam is less than ten!'`
3. `assert 1 == 0, 'what'`
4. '''
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
'''
5. '''
import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
'''
6. debug, info, warning, error, critical
7. `logging.disable(logging.CRITICAL)`
8. print messages are a pain to find and remove when no longer needed, while logging is more flexible
and emphasizes sending messages to the dev and not the end user
9. I don't have this debugger used
10. I don't have this debugger used
11. I don't have this debugger used
12. I don't have this debugger used

