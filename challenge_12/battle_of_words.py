def battle(our_team, opposing_team):
    def calculate_word_value(word):
        value = 0
        for char in word:
            if 'a' <= char <= 'z':
                value += ord(char) - ord('a') + 1
            elif 'A' <= char <= 'Z':
                value += 2 * (ord(char) - ord('A') + 1)
        return value

    your_words = our_team.split()
    opposing_words = opposing_team.split()

    our_wins = 0
    opposing_wins = 0

    for i in range(len(your_words)):
        your_value = calculate_word_value(your_words[i])
        opposing_value = calculate_word_value(opposing_words[i])

        if your_value > opposing_value:
            our_wins += 1
        elif opposing_value > your_value:
            opposing_wins += 1

    if our_wins > opposing_wins:
        return "We win"
    elif opposing_wins > our_wins:
        return "We lose"
    else:
        return "Draw"


print(battle("hello world", "hello word"))
print(battle("Hello world", "hello world"))
print(battle("lorem ipsum", "kitty ipsum"))
print(battle("hello world", "world hello"))
print(battle("git checkout", "git switch"))
print(battle("Cheeseburger with fries", "Cheeseburger with Fries"))
print(battle("We must never surrender", "Our team must win"))