def wise_speak(sentence):
    punctuation = sentence[-1] if sentence[-1] in '.!?' else ''
    words = sentence[:-1].split() if punctuation else sentence.split()

    target_words = ["have", "must", "are", "will", "can"]
    split_index = -1

    for i, word in enumerate(words):
        if word.lower() in target_words:
            split_index = i
            break

    if split_index == -1:
        return sentence

    first_part = words[:split_index + 1]
    second_part = words[split_index + 1:]

    first_part_lower = [word.lower() for word in first_part]

    if second_part:
        new_sentence = " ".join(second_part) + ", " + " ".join(first_part_lower) + punctuation
    else:
        new_sentence = " ".join(first_part_lower) + punctuation

    new_sentence = new_sentence[0].upper() + new_sentence[1:]

    return new_sentence

print(wise_speak("You must speak wisely."))
print(wise_speak("You can do it!"))
print(wise_speak("Do you think you will complete this?"))
print(wise_speak("All your base are belong to us."))
print(wise_speak("You have much to learn."))
