""" def wizards(n, start, duels):
    owner=start
    changed_hands=1
    if (duels[0][1])== owner:
        owner = (duels[0][0])
        print(owner)
        changed_hands+=1
        print(changed_hands) """

""" wizards(3, "A", ["BA", "CB", "DA"])
 """
def wizards(n, start, duels):
    owner=start
    changed_hands=1
    if (duels[0][1])== owner:
        owner = (duels[0][0])
        print(owner)
        changed_hands+=1
        print(changed_hands)
        print(n)
wizards(3, "A", ["BA", "CB", "DA"])