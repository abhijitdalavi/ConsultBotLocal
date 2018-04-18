#Attempts to match the users input to a topic
Topic1 = ["cost", "costs", "money","pay","investment","economy","worth", "expensive"]
Topic2 = ["site","location","area","far","city","nearby","place","traffic","parking","transport","long","infrastructure","pubs"]
Topic_assignment = ""

def topic_match(text): 
    
    if any(word in text for word in Topic1):
        Topic_assignment = "Cost"
    elif any(word in text for word in Topic2):
        Topic_assignment = "Location"
    else:
        Topic_assignment = "Unclear"
    return Topic_assignment

