#!/usr/bin/env python3

import random, time

corrects = 0
for questionNumber in range(1,11):
    num1 = random.randint(2,9)
    num2 = random.randint(2,9)
    prompt = f'Q{questionNumber}: {num1} x {num2} = '
    attempts = 0
    while attempts < 3:
        timer = time.perf_counter()
        answer = input(prompt)
        timer = time.perf_counter() - timer
        if timer > 8.0:
            print('Out of time!')
            time.sleep(1)
            break
        elif answer == str(num1 * num2):
            print('Correct!')
            corrects += 1
            time.sleep(1)
            break
        else:
            print('Incorrect!')
            attempts += 1
            if attempts == 3:
                print('Out of retries!')
            time.sleep(1)
            continue
print(f"Score: {corrects} / 10 correct!")
