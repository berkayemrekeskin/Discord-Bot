from random import choice, randint


def get_response(user_input: str , data: list):
    lowered: str = user_input.lower()
    names = []
    ages = []
    majors = []
    
    for people in data["kaldmu"]:
        names.append(people["name"])
    for people in data["kaldmu"]:
        ages.append(people["age"])
    for people in data["kaldmu"]:
        majors.append(people["major"])

    
    if lowered == '':
        return 'konussana ag'
    elif 'merhaba' in lowered:
        return 'merhaba canim benim'
    elif 'nasilsin' in lowered:
        return 'iyiyim sen?'
    elif 'görüsürüz' in lowered:
        return 'görüsürüzzzz'
    elif 'zar at' in lowered:
        return f'attim bak:  {randint(1,6)}'
    elif 'isimler' in lowered:
        return names
    elif 'bölümler' in lowered:
        return majors
    elif 'yaslar' in lowered:
        return ages
    
    else:
        return choice([
            'anlamadim',
            'ne dedin canim??'
        ])
