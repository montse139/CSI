print "Who ate the ice cream?"
print "To find out who did it we are going to run some tests. "
print "We found DNA on the spoon that was used to eat the ice cream."

test_run = raw_input("Do you want to test the DNA? (yes/no)")

hair_color = {"test": "hair color", "black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blond": "TTAGCTATCGC"}
face_shape = {"test": "face shape", "square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"}
eye_color = {"test": "eye color", "blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
gender = {"test": "gender", "female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"}
race = {"test": "race", "white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}

Eva = {"name": "Eva", "gender": "female", "race": "white", "hair color": "blond", "eye color": "blue", "face shape": "oval"}
Larisa = {"name": "Larisa", "gender": "female", "race": "white", "hair color": "brown", "eye color": "brown", "face shape": "oval"}
Matej = {"name": "Matej", "gender": "male", "race": "white", "hair color": "black", "eye color": "blue", "face shape": "oval"}
Miha = {"name": "Miha", "gender": "male", "race": "white", "hair color": "brown", "eye color": "green", "face shape": "square"}

guilty = {}

if test_run == "yes":
    with open("dna.txt", "r") as myfile:
        dna = myfile.read()
    print "DNA match:"

    def check_dna(dict):
        for key in dict:
            if dict[key] in dna:
                guilty[dict["test"]] = key
                print "- " + dict["test"] + ": " + key

    def suspect_check(dict):
        diff = set(guilty.iteritems()) - set(dict.iteritems())
        if len(diff) > int(1):
            print dict["name"] + " is innocent (%s discordancies)" % len(diff)
        else:
            print dict["name"] + " DID IT!!!"


check_dna(gender)
check_dna(race)
check_dna(hair_color)
check_dna(eye_color)
check_dna(face_shape)


suspect_check(Larisa)
suspect_check(Eva)
suspect_check(Matej)
suspect_check(Miha)

# CSI
