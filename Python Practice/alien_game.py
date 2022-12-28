import random
aliens = {'green': 5,'yellow': -5,'blue': -5,'orange': 100}
current_points = 0
winning_points = 1000
tries = 0

while current_points < winning_points:
    alien = random.sample(aliens.keys(), 1)[0]
    points = aliens[alien]
    print(f'You currently have {current_points} points. You need {winning_points - current_points} points to win!')
    if points < 5:
        print(f'You shot down a {alien} alien. You are down {str(points)} points.\n')
    elif points >= 5 and points < 100:
        print(f'You shot down a {alien} alien! You win {str(points)} points.\n')
    else:
        print(f'Holy mackerel! You shot down an {alien} alien! You win {str(points)} points!\n')
    current_points += points
    tries += 1
    if current_points >= winning_points:
        print(f'After {tries} tries, you have {current_points} points. You win!')