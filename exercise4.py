"""
Exercise 4:
    
Step1: Create a small (6 or 7 pair will stored in it) french/english

Step2: Prompt the used for a french word

Step3: Check if the word exists or not, if it exists print its translation in English
if it does not exist you will print a sorted list of all the french words your script could translate

Note: you should be able to enter the french word using any case
"""
fr_en_dict={"Ciel":"Sky", 
            "Terre":"Earth", 
            "Ville":"City", 
            "Voiture":"Car", 
            "Rouge":"Red", 
            "Mer":"Sea"}

print(fr_en_dict)

for k,v in fr_en_dict.items():
    print(k,"->",v)
    

# # Here is another option to create the dict:
# frW=("Ciel", "Terre", "Ville", "Voiture", "Rouge", "Mer")
# enW=("Sky", "Earth", "City", "Car", "Red", "Sea")

# fr_en_dict2=dict(zip(frW, enW))

# print(fr_en_dict2)
     
fr=input("Enter a french word, I'll give you it's translation in English: ")
fr=fr.capitalize()  # This if to "normalize" the input: the french word is
                    # always capitalized

if fr in fr_en_dict: # Is the word present ?
    print(f"The translation of {fr} is {fr_en_dict[fr]}")
else:
    print(f"No translation for {fr} but I can translate:")
    print(sorted(fr_en_dict.keys()))