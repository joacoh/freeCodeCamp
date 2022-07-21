# %%
def add_time(start, duration, day=None):
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    hour = int(start.split()[0].split(':')[0])
    minute = int(start.split()[0].split(':')[1])
    t_format = start.split()[1]

    h_add = int(duration.split(':')[0])
    m_add = int(duration.split(':')[1])
    
    hour_new = hour + h_add
    minute_new = minute + m_add
    
    while minute_new>60:
        hour_new += 1
        minute_new -= 60

    if t_format=='PM':
        hour_new+=12
    
    n_day = int(hour_new/24)

    if n_day>1:
        hour_new -= n_day*24
        if hour_new<12 and hour_new!=0:
            t_format='AM'
        elif hour_new==12:
            t_format='PM'
        elif hour_new==0:
            hour_new=12
            t_format='AM'
        else:
            t_format='PM'
            hour_new-=12
        if day==None:
            new_time = '{}:{:02d} {} ({} days later)'.format(hour_new,minute_new,t_format,n_day)
        else:
            day = day.casefold()
            day = week.index(day)
            day += n_day
            while day>6:
                day-=7
            day = week[day].capitalize()
            new_time = '{}:{:02d} {}, {} ({} days later)'.format(hour_new,minute_new,t_format,day,n_day)
            
    elif n_day==1:
        hour_new -= 24
        if hour_new<12 and hour_new!=0:
            t_format='AM'
        elif hour_new==12:
            t_format='PM'
        elif hour_new==0:
            hour_new=12
            t_format='AM'
        else:
            t_format='PM'
            hour_new-=12
        if day==None:
            new_time = '{}:{:02d} {} (next day)'.format(hour_new,minute_new,t_format)
        else:
            day = day.casefold()
            day = week.index(day)
            day += n_day
            while day>6:
                day-=7
            day = week[day].capitalize()
            new_time = '{}:{:02d} {}, {} (next day)'.format(hour_new,minute_new,t_format,day)
    else:
        if hour_new<12 and hour_new!=0:
            t_format='AM'
        elif hour_new==12:
            t_format='PM'
        elif hour_new==0:
            hour_new=12
            t_format='AM'
        else:
            t_format='PM'
            hour_new-=12
        if day==None:
            new_time = '{}:{:02d} {}'.format(hour_new,minute_new,t_format)
        else:
            day = day.casefold()
            day = day.capitalize()
            new_time = '{}:{:02d} {}, {}'.format(hour_new,minute_new,t_format,day)
    
    return new_time

print(add_time("11:06 PM", "2:02"))
# %%
