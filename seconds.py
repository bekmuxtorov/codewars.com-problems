#codewars.com 
#problem 15
#bekmuxtorov
#tocamelcase

def format_duration(seconds):
    if seconds == 0: return 'now'
        
    elif seconds < 60: return f"{seconds} second"
        
    elif seconds >= 60 and seconds < 3600:
        minute = seconds // 60
        second = seconds - minute*60
        if second == 0:
            return f"{minute} minutes"
        
        return f"{minute} minute and {second} seconds"
    
    elif seconds >= 3600 and seconds < 86400:
        s = ""
        hour = seconds // 3600
        minute = seconds - hour*3600
        s += f"{hour} hour"
        if minute > 60:
            minute = (seconds - hour*3600)// 60
            second =(seconds - hour*3600)- minute*60
            if second == 0:
                s += f", {minute} minutes"
            else:
                s += f", {minute} minute and {seconds} seconds"
        return s   
         
        
seconds = 8640
print(format_duration(seconds))
"""
3662 = 3600*1 + 60*1 + 2  
"""




