unleash = True
longest = ""
shortest = "supercalifragilistiestpealidoish" * 4

while unleash:
    text = input()
    if text == "stop" or text == "STOP":
        unleash = False
        break
    if len(text) > len(longest):
        longest = text
    if len(text) < len(shortest):
        shortest = text

print(longest, shortest)

# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
