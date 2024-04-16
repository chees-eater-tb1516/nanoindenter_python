import re
import numpy as np
import matplotlib.pyplot as plt

filename = "results_files\hfrrwatertest120424_attempt2.TXT"

def line_gen(file):
    for line in file:
        yield line
            
header = False
data = False 
header_lines=[]
data_lines=[]     

#regular expressions that demarkate the position in the file:

header_start = r"Indentation #"
header_end = r"Measured values"
data_start = r"0	0	0	0"
data_end =  r"______________________________________________________________"   
contact_warning = r"Warning: Check contact point" 


def fit_segment(data_array, segment_no):
    segment = data_array[4] == segment_no
    segment_force = data_array[2][segment]
    segment_displacement = data_array[1][segment]

    fit = np.polyfit(segment_displacement**(3/2), segment_force, 1)
    #disp = np.linspace(0,20000,10)    
    #plt.plot(segment_displacement, segment_force)
    #plt.plot(disp, np.polyval(fit, disp**(3/2)))
    return float(fit[0])
results = open ("hfrrwaterresults.txt", 'w')

with open (filename, 'r') as file:
    looping = True
    while(looping):
        #iterate over lines and find one indentation's worth of data
            header = False
            data = False 
            header_lines=[]
            data_lines=[]   
            while True:
                try:
                    line = line_gen(file).__next__()
                except StopIteration:    
                    looping = False
                    break
                #search for the regular expressions defined above and set flags
                if re.search(header_start, line):
                    header = True
                    
                if re.search(header_end, line):
                    header = False
                if re.search(data_start, line):
                    data = True
                    
                if data and re.search(data_end,line):
                    data = False
                    break    
                    
                #append lines to one of two lists depending on the content
                if header:
                    header_lines+=[line]
                
                if data:
                    data_lines+=[line]
        
        
        

            #extract useful info from header
            warning = " good"
            for line in header_lines:
                
                
                if re.search(r"Indentation # ", line):
                    indentation_number = line
                
                if re.search(r"X Position: ", line):
                    x_position = line
           
                if re.search(r"Y Position: ", line):
                    y_position = line
                
                if re.search(contact_warning, line):
                    warning = " bad"
                

            #convert the list of strings in data_lines into a numpy array for analysis

            data_array = np.array([np.fromstring (item, sep='\t') for item in data_lines[:-1]])

            data_array = data_array.transpose()
            
            #occasionally forces may be negative but we need to ignore these [LAZY]
            data_array = np.abs(data_array)


            #analyse data to find 'stiffness'

            segment_nos=[1,3]
            segment_stiffness=[]

            
            for segment in segment_nos:
                segment_stiffness.append(str(fit_segment(data_array, segment)))
         
            
            #plt.show()    
                
            indentation_number = indentation_number.split("# ")[1][:-1]
            x_position = x_position.split(" ")[5]
            y_position = y_position.split(" ")[5]
            results_string = (',').join(segment_stiffness)
            results_string = indentation_number + ',' + x_position + ',' + y_position + ',' + results_string + warning +'\n' 
            results.write (results_string)    
                
            x=1

results.close()
              
    
    
        

x=1
        

            
            
            

    
    