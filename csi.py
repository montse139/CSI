print "Who ate the ice cream?"
print "To find out who did it we are going to run some tests. "
print "We found DNA on the spoon that was used to eat the ice cream."

test_run = raw_input("Do you want to test the DNA? (yes/no)")

hair_color = {"test": "hair color", "black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blond": "TTAGCTATCGC"}
facial_shape = {"test": "facial shape", "square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"}
eye_color = {"test": "eye color", "blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
gender = {"test": "gender", "female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"}
race = {"test": "race", "white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}

Eva = {"name": "Eva", "gender": "female", "race": "white", "hair color": "blond", "eye color": "blue", "face shape": "oval"}
Larisa = {"name": "Larisa", "gender": "female", "race": "white", "hair color": "brown", "eye color": "brown", "face shape": "oval"}
Matej = {"name": "Matej", "gender": "male", "race": "white", "hair color": "black", "eye color": "blue", "face shape": "oval"}
Miha = {"name": "Miha", "gender": "male", "race": "white", "hair color": "brown", "eye color": "green", "face shape": "square"}

#suspects = [Eva, Larisa, Matej, Miha]
guilty_person = {"gender": "male", "race": "white", "hair_color": "brown", "eye_color": "green", "facial_shape": "square"}
guilty = {}

if test_run == "yes":
    with open("dna.txt", "r") as myfile:
        dna = myfile.read()

    def check_dna(dict):
        for key in dict:
            if dict[key] in dna:
                print "- " + dict["test"] + ". " + "DNA match: " + key

check_dna(hair_color)
check_dna(facial_shape)
check_dna(eye_color)
check_dna(gender)
check_dna(race)

#for item in guilty:
    #print item

def suspect_check(dict):
    for key in dict:
        if dict[1:] == guilty_person[0:]:
            print dict["name"] + " is Guilty!"


suspect_check(Larisa)
suspect_check(Eva)
suspect_check(Matej)
suspect_check(Miha)

# CSI
