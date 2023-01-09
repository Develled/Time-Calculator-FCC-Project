def add_time(start, duration, weekday='0'):
    new_start = ''    
    #convert to 24 hour time
        #setting 12:00AM time
    if start[-2:] == "AM" and start.split(':')[0] == "12":
        new_start = "00" + ':' + start.split(':')[1]      
  
        #add 12 to PM times other than 12:00 PM
    elif start[-2:] == "PM" and int(start.split(':')[0]) < 12:
        new_start  = str(int(start.split(':')[0]) + 12) + ':'+ start.split(':')[1]
        
    else:
        new_start = start
    
    ##pull out total minutes
    minutes = int(new_start.split(':')[1].split()[0]) + int(duration.split(':')[1].split()[0])   
    
    #pull out total hours
    hours = int(new_start.split(':')[0]) + int(duration.split(':')[0])
           
    #set up variables
    ampm = ''
    day_counter = 0
    weekday_start = 0
    weekday_total = 0
    weekday_dict = {'sunday':1, 'monday':2, 'tuesday':3, 'wednesday':4, 'thursday':5, 'friday':6, 'saturday':7}
    key_list = list(weekday_dict.keys())
    val_list = list(weekday_dict.values())
    
   #convert minutes over 60 to hours
    if minutes >= 60:
        minutes = minutes - 60
        hours = hours + 1
        
    #calculate days past
    while hours >= 24:
        hours = hours - 24
        day_counter += 1

    #calculate new weekday if paramter is given
    if weekday != '0':
        weekday_start = weekday_dict[weekday.lower()]
        
        weekday_total = weekday_start + day_counter
        
        while weekday_total >7:
            weekday_total -= 7
    
        weekday = key_list[val_list.index(weekday_total)]  
        
    #set am/pm    
    if hours >= 12 and hours <24:
        ampm = 'PM'            
    else:
        ampm = 'AM'
    
    #change back to 12 hour clock    
    if hours > 12:
        hours = hours - 12
    if hours < 1:
        hours = hours + 12
        
    # set date counter text    
    if day_counter == 0:
        date = ''
    if day_counter == 1:
        date = ' (next day)'
    if day_counter > 1:
        date = ' ('+str(day_counter)+' days later)'
        
    if weekday == '0':
        new_time = str(hours)+ ':' + str((minutes)).zfill(2) + ' ' + ampm + date
        
    else:
        new_time = str(hours)+ ':' + str((minutes)).zfill(2) + ' ' + ampm + ', ' + weekday.capitalize() + date  

    return new_time