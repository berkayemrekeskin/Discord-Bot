from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    
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
    else:
        return choice([
            'anlamadim',
            'ne dedin canim??'
        ])
    