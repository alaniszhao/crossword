from board import *
import openai
import config
openai.api_key = config.api_key

def choose_theme():
    categories = []
    categories.append(("music artists",["pop","rock","country","indie","r&b",
                                        "classical"]))
    categories.append(("well known people",["pop culture","politics","cooking",
                                            "fairytales"]))
    categories.append(("actors and actresses",["television", "movies"]))
    categories.append(("brands",["food","clothing","cars","technology"]))
    categories.append(("geography",["mountains","rivers","lakes","cities",
                                    "countries","continents","oceans",
                                    "deserts"]))
    theme_i = random.randint(0,len(categories)-1)
    theme = categories[theme_i]
    theme_name = theme[0]
    theme_type = (theme[1])[random.randint(0,len(theme)-1)]
    return (theme_name,theme_type)

def long_words(len1, len2):
    return 0

def main():
    #x = Board(15)
    #print(x)
    for i in range(15):
        print(choose_theme())
    """(_,[(len1,_),(len2,_)]) = x.find_longest()
    [word1,word2,word3,word4]=long_words(len1,len2)"""
if __name__ == "__main__":
    main()