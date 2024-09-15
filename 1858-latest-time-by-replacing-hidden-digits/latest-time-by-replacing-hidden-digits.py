class Solution:
    def maximumTime(self, time: str) -> str:
        new_time=''
        if time[0]=='?':
            if time[1] == '?' or int(time[1])<4:
                new_time+='2'
            else :
                new_time+='1'
        else:
            new_time+=time[0]
        if time[1]=='?' and ( new_time[0]=='1' or new_time[0] =='0'):
            new_time+='9'
        elif time[1]=='?' and new_time[0]=='2':
            new_time+='3'
        else:
            new_time+=time[1]
        new_time+=time[2]
        if time[3]=='?':
            new_time+='5'
        else:
            new_time+=time[3]
        if time[4] =='?':
            new_time+='9'
        else:
            new_time+=time[4]
        return new_time