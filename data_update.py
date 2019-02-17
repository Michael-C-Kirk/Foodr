#module for data updating

def update_data_set(text_file_name:str, data:{'Time':int, "Mood":int, "Age":int}):
    '''Given a text file name and data, it will open the text file 
        and update the file with new data in format "int,int,int" '''
    file = open(text_file_name, "a")
    elements_for_data_input=["\n",
                             data['Time'],
                             ',',
                             data['Mood'],
                             ',',
                             data['Age']]
    
    for item in range(len(elements_for_data_input)):
        file.write(str(elements_for_data_input[item]))
    file.close()

