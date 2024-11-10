import time

print('Find your boxing style!')
height = input('What is your height in cm? ')
body_type = input('Are you an: 1. Ectomorph 2. Mesomorph 3. Endomorph? ')
defense_or_offence = input('Are you naturally aggressive or naturally passive when fighting? ')

boxing_styles = ['Peekaboo', 'Counter-Puncher', 'Pressure Fighter', 'Slugger', 'Boxer-Puncher', 'Soviet-Style']

peekaboo_style_score = 0
counterpuncher_style_score = 0
pressurefighter_style_score = 0
slugger_style_score = 0
boxerpuncher_style_score = 0
sovietstyle_style_score = 0

try:
    height = float(height)  # Convert height to float
except ValueError:
    print('Your height must be a number!')
    time.sleep(2)
    exit()  # Exit if the input is not a valid number

if height < 135:
    print('Your height cannot be under 135 cm!')
    time.sleep(2)
    exit()  # Exit if height is less than 135 cm
elif 135 <= height < 177:
    peekaboo_style_score += 5
    pressurefighter_style_score += 4
    counterpuncher_style_score -= 1
    slugger_style_score -= 3
    boxerpuncher_style_score -= 2
    sovietstyle_style_score -= 4
elif 177 <= height < 200:
    peekaboo_style_score -= 2
    pressurefighter_style_score -= 2
    counterpuncher_style_score += 3
    slugger_style_score += 4
    boxerpuncher_style_score += 2
    sovietstyle_style_score += 3
elif height >= 200:
    sovietstyle_style_score += 5
    peekaboo_style_score -= 2
    pressurefighter_style_score -= 2
    counterpuncher_style_score -= 3
    slugger_style_score -= 1
    boxerpuncher_style_score -= 2

if body_type == '1':
    counterpuncher_style_score += 4
elif body_type == '2':
    pressurefighter_style_score += 4
elif body_type == '3':
    slugger_style_score += 4
else:
    print('You must select between 1, 2 or 3!')
    time.sleep(2)
    exit()  # Exit if an invalid body type is entered

if defense_or_offence.lower() == 'aggressive':
    peekaboo_style_score += 4
    pressurefighter_style_score += 3
    slugger_style_score += 3
    boxerpuncher_style_score += 3
elif defense_or_offence.lower() == 'passive':
    boxerpuncher_style_score += 3
    sovietstyle_style_score += 3
    counterpuncher_style_score += 3
else:
    print('You must answer "aggressive" or "passive"!')
    time.sleep(2)
    exit()  # Exit if defense or offense is not correctly specified

best_style = max(peekaboo_style_score, counterpuncher_style_score, pressurefighter_style_score,
                 slugger_style_score, boxerpuncher_style_score, sovietstyle_style_score)

if best_style == peekaboo_style_score:
    print("\nYour best boxing style is either Peekaboo or Pressure Fighter! Peekaboo relies more on counter-punching and head movement, but Pressure Fighter is almost only attacks. You have to make the decision yourself :(")
    print(f"Peekaboo: {peekaboo_style_score}")
    print(f"Counter-Puncher: {counterpuncher_style_score}")
    print(f"Pressure Fighter: {pressurefighter_style_score}")
    print(f"Slugger: {slugger_style_score}")
    print(f"Boxer-Puncher: {boxerpuncher_style_score}")
    print(f"Soviet-Style: {sovietstyle_style_score}")
elif best_style == counterpuncher_style_score:
    print("\nYour best boxing style is: Counter-Puncher!")
    print(f"Peekaboo: {peekaboo_style_score}")
    print(f"Counter-Puncher: {counterpuncher_style_score}")
    print(f"Pressure Fighter: {pressurefighter_style_score}")
    print(f"Slugger: {slugger_style_score}")
    print(f"Boxer-Puncher: {boxerpuncher_style_score}")
    print(f"Soviet-Style: {sovietstyle_style_score}")
elif best_style == pressurefighter_style_score:
    print("\nYour best boxing style is either Peekaboo or Pressure Fighter! Peekaboo relies more on counter-punching and head movement, but Pressure Fighter is almost only attacks. You have to make the decision yourself :(")
    print(f"Peekaboo: {peekaboo_style_score}")
    print(f"Counter-Puncher: {counterpuncher_style_score}")
    print(f"Pressure Fighter: {pressurefighter_style_score}")
    print(f"Slugger: {slugger_style_score}")
    print(f"Boxer-Puncher: {boxerpuncher_style_score}")
    print(f"Soviet-Style: {sovietstyle_style_score}")
elif best_style == slugger_style_score:
    print("\nYour best boxing style is: Slugger!")
    print(f"Peekaboo: {peekaboo_style_score}")
    print(f"Counter-Puncher: {counterpuncher_style_score}")
    print(f"Pressure Fighter: {pressurefighter_style_score}")
    print(f"Slugger: {slugger_style_score}")
    print(f"Boxer-Puncher: {boxerpuncher_style_score}")
    print(f"Soviet-Style: {sovietstyle_style_score}")
elif best_style == boxerpuncher_style_score:
    print("\nYour best boxing style is: Boxer-Puncher!")
    print(f"Peekaboo: {peekaboo_style_score}")
    print(f"Counter-Puncher: {counterpuncher_style_score}")
    print(f"Pressure Fighter: {pressurefighter_style_score}")
    print(f"Slugger: {slugger_style_score}")
    print(f"Boxer-Puncher: {boxerpuncher_style_score}")
    print(f"Soviet-Style: {sovietstyle_style_score}")
else:
    print("\nYour best boxing style is: Soviet-Style!")
    print(f"Peekaboo: {peekaboo_style_score}")
    print(f"Counter-Puncher: {counterpuncher_style_score}")
    print(f"Pressure Fighter: {pressurefighter_style_score}")
    print(f"Slugger: {slugger_style_score}")
    print(f"Boxer-Puncher: {boxerpuncher_style_score}")
    print(f"Soviet-Style: {sovietstyle_style_score}")