word="python"
for letter in word:
    print(letter)
    if(letter=='t'):
        break;
for letter2 in word:

    if(letter2=='h'):
        continue;  # skip h character printing
    print(letter2)
print("App is done")