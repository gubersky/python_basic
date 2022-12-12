text = """
Любіть Україну, як сонце любіть,
як вітер, і трави, і води...

В годину щасливу і в радості мить,
любіть у годину негоди.

Любіть Україну у сні й наяву,
вишневу свою Україну,
красу її, вічно живу і нову,
і мову її солов'їну.

Без неї — ніщо ми, як порох і дим,
розвіяний в полі вітрами...

Любіть Україну всім серцем своїм
і всіми своїми ділами.
"""

new_text = text.replace(',', '').replace('.', '')\
           .replace('—', '').lower().split()

dictionary = {i: new_text.count(i) for i in new_text}

count = 0
word = ""

for i, k in dictionary.items():
    if k > count:
        count = k
        word = i

print(dictionary)
print("The word:", word, "\n" "Occurs most often:", count, "times")
