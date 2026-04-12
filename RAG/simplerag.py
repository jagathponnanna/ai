from llm import generate_response
def retrive_context(query=''):
    return str([
    "In war, knowing yourself and your enemy ensures consistent victory.",
    "In war, deception is essential to confuse and outmaneuver the opponent.",
    "In war, the greatest success is winning without engaging in battle.",
    "In war, speed and adaptability determine who gains the upper hand.",
    "In war, choosing the right battles is more important than fighting every opportunity."
    ])

if __name__=='__main__':
    flag=True
    history=[]
    while(flag):
        q=input("Enter your query:")
        if q=='x':
            break
        context=retrive_context(q)
        response=generate_response(q,context,history)
        history.append(response)
        print(response)



