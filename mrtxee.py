from asyncio.windows_events import NULL
import json
def explore_obj(o):
    data = {
        "type"      : str(type(o))
        ,"id"       : str(id(o))
        ,"struct"   : json.loads( str(dir(o)).replace('\'','"') )
        }
    print(json.dumps(data, indent=4))

def print_fancy(s1='',s2=''):
    if ''==s1:
        return NULL
    else:
        #print()
        print(f'\n= = = = {s1} = = = =')
        if ''!=s2:
            print(s2)
        #print('\n')