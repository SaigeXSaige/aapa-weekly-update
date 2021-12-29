teams = [
    "@tvnkth's NY Kricketots",
    "@DannyMac_15's BK Slowbros",
    "@_PineappleJonez's Raleigh Grimsnarls",
    "@Mackannon's Louisiana Ludicolos",
    "@ItsJustB0bby's QGTM",
    "@CherokeeAmour's Piqua Sol Rockers",
    "@BJStrongArmAHo's Tuskegee Arcanines",
    "@RedScarlettMP's Boston Yujiros",
    "@Jc__Armstrong's Texas Titans",
    "@Jcaste2_'s SA Town Squirtles",
    "@ThugaManLaForge's Sacramento Salamence",
    "@ColdGawd's Murrrland StoneCold Stunnas",
    "@StevieKnicks21's Canarsie Charizards",
    "@ChauceNoSauce's Chicago SauceLords",
]

def print_teams():
    for id, val in enumerate(teams):
        print("[", id + 1, "]", val)
        
def check_correctness():
    is_correct_post = input("\n\n Is this correct? ('yes' or 'no')\n")
    if(is_correct_post == 'yes'):
        return True
    elif(is_correct_post == 'no'):
        return False
    else:
        print("Expected a 'yes' or 'no'\n")
        check_correctness()

def select_rankings():
    print("\n===========================\n","Select the top 5: \n")
    print_teams()

    top_teams_input = input("\n(ex: 1, 3, 4, 5, 10)\n\n")
    top_teams_input = top_teams_input.replace(" ", "").split(",")
    top_teams_index = [int(i) - 1 for i in top_teams_input]
    top_teams = [teams[i] for i in top_teams_index]
    
    is_correct_post = check_correctness()
    if(not is_correct_post):
        return select_rankings()
    return top_teams 
    
def create_custom_status(teams_msg=''):
    print("\n===========================\n")
    custom_status = input("Input this week's message:\n") + teams_msg
    print("\n===========================\n", custom_status.strip())
    
    is_correct_post = check_correctness()
    if(not is_correct_post):
        return create_custom_status(teams_msg)
    return custom_status

def create_rankings_status():
    top_teams = select_rankings()
    
    top_teams_msg = f'\n\n5. {top_teams[4]}\n4. {top_teams[3]}\n3. {top_teams[2]}\n2. {top_teams[1]}\n\n\n1. {top_teams[0]}'
    # default_msg = f'This week\'s top 5: {top_teams_msg}'
    custom_status = create_custom_status(top_teams_msg)
    return custom_status
