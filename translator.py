def Translator(word: str):
    #skywars
    if word == 'solo_insane':
        return 'Solo', 'Insane'
    elif word == 'solo_normal':
        return 'Solo', 'Normal'
    elif word == 'teams_insane':
        return 'Teams', 'Insane'
    elif word == 'teams_normal':
        return 'Teams', 'Normal'

    #bedwars
    elif word == 'EIGHT_ONE':
        return 'Solo'
    elif word == 'EIGHT_TWO':
        return 'Doubles'
    elif word == 'FOUR_THREE':
        return '3s'
    elif word == 'FOUR_THREE':
        return '4s'
    
    #duels
    elif word == 'CLASSIC_DUEL':
        return 'Classic Duels'
    elif word == 'BRIDGE_DUEL':
        return 'Bridge Duels'
    elif word == 'SW_DUEL':
        return 'Skywars Duels'
    elif word == 'UHC_DUEL':
        return 'UHC Duels'
'add more !!!'