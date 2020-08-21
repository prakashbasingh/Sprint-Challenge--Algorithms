'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # base case if word has now letter return 0
    if len(word) <= 0:
        return 0
    if word[0:2] == "th":
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])
        
print(count_th("adkthndthndskth"))
