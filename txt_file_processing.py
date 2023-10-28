

import unidecode

set_of_latin_letters = {" ","a", "A", "b", "B","c","C","d","D","e","E","f","F","g","G","h","H","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z"}
list_of_capitals = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
list_of_small_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#news sentences:
#1) change weird letters and accents in normal letters (specific for each language -> use unidecode)
#2) all capitals become small
#3) everything that is not a normal letter becomes a space
#4) if multiple spaces next to each other make them into 1 space 
def processing_txt_file(txt_file_string):
    j = 0
    end_j = len(txt_file_string)
    while(j < end_j):
        if (txt_file_string[j] == "\n"):
            txt_file_string = txt_file_string[:j] + " " + txt_file_string[j+1:]
        j += 1

    i = 0
    end_i = len(txt_file_string)-1
    while (i < end_i):
        if (txt_file_string[i] == " ") and (txt_file_string[i+1] == " "):
            #remove the i'th element of the string
            txt_file_string = txt_file_string[:i] + txt_file_string[i+1:]
            end_i -= 1
        else:
            i += 1
    return txt_file_string

            
        





lang = ['pl','nl','it','fr','fi','et','es','en','el','de','da','cs']
for l in lang:
    for i in range(1,1001):
        file_raw = open("Language txt files\\testing_texts\\"+l+"_"+str(i)+"_p"+".txt", "r")
        raw_content = file_raw.read()
        file_raw.close()
        processed_content = processing_txt_file(raw_content)
        file_processed = open("Language txt files\\spanish.txt", "w")
        file_processed.write(processed_content)
        file_processed.close()

