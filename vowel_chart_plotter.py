#Author: Jonathan Soelle
import re
import matplotlib.pyplot as plt                                         #this just imports a plt function object                                                                    



#variable declaration                                                                        
vowel_array = [] #list of the vowels from praat analysis
input_char = '' #variable for use in loop to keep track of user input
f1_list = [] #currently unused, potentially might use in future versions
f2_list = [] #currently unused, potentially might use in future versions
iXval = []                                                              #list for x values
iYval = []                                                              #list for y values



#the while loop takes in the input of the vowels, their formants F1 and F2, as well as calculating F2-F1
#then saves those values to a list for plotting the vowel chart

while(input_char != 'q'):
    print("Enter 'q' and enter to exit the loop.")                      #prints message to user about 'q'
    input_char = input("Please enter a vowel: ") 
                                                                        #^^takes input^^
    if(input_char =='q'):                                               #checks for 'q'
        input_char = ''
        break
    # vowel_f1 = int(input("Please input F1 in Hz rounded to the nearest integer: "))
    # vowel_f2 = int(input("Please input F2 in Hz rounded to the nearest integer: ")) #could use later
    vowel_formants = input("Enter F1 and F2 as an ordered pair for the given vowel: ")
    vowel_formants = re. sub(',', '', vowel_formants)
    vowel_formants = vowel_formants.split()
    rounded_f1 = round(float(vowel_formants[0]))
    rounded_f2 = round(float(vowel_formants[1]))
    vowel_array.append(input_char)
    f1_list.append(rounded_f1)
    f2_list.append(rounded_f2)
    x_val = rounded_f2 - rounded_f1
    iXval.append(x_val)
    iYval.append(rounded_f1)
    vowel_formants = ''
    


fig = plt.figure()                                                      #creates figure object
ax = fig.subplots()                                                     #allows for further axis customization
plt.xlim(200,2800)                                                      #sets limits for x axis to give it the same bounds as the paper copy
plt.ylim(200,950)                                                       #sets limits for y axis
plt.gca().invert_xaxis()                                                #inverts axis ticks for x and then y as well
plt.gca().invert_yaxis()


for i in range(0, len(iXval)):
    ax.scatter(iXval[i], iYval[i], color='black')                       #each vowel is plotted
    plt.text(iXval[i] - 75, iYval[i], vowel_array[i])                   #the label for the vowel is plotted
ax.grid(True)                                                           #shows gridlines
ax.yaxis.tick_right()                                                   #moves axis ticks to right
ax.xaxis.tick_top()                                                     #moves axis ticks to top
plt.xlabel('F2 - F1 (Hz)', rotation=0, fontsize=20, labelpad=20)        #rotates x axis label to be horizontal
ax.xaxis.set_label_position("top")                                      #moves x axis label to top
plt.ylabel('F1', rotation=0, fontsize=20, labelpad=20)                  #rotates y axis label to be horizontal
ax.yaxis.set_label_position("right")                                    #moves y axis label to right
plt.title('Vowel Chart Plot')                                           #labels title of chart
                                                                        #shows plot (always have to do this)

input_char = input("\nWould you like to save the created plot to disc? y/n: ")            #takes user input
if(input_char == 'y'):                                                                  #if yes, continues
    output_file = input("What would you like the name of the file to be saved as?: ")   #gets desired filename
    output_file = output_file + '.png'                                                  #concatenates file ext.
    plt.savefig(output_file, bbox_inches="tight")                                                            #saves file to disc
else:
    print("\nSure hope you don't need it for an assignment lol")                        #i'm really funny
plt.show()                                                                              #outputs graphic to view immediately, seperate from saved version
