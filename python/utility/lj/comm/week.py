'''
Created on 2013-4-12

@author: linkcare_l10n_rd
'''
from django.utils.datetime_safe import date
from datetime import timedelta

def weekdayslist(day):
    _days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    weekdaynum = (lambda x:-1 if x == 6 else x)(date.weekday(day))
    _date=day + timedelta(days=-(weekdaynum + 1))
    weekdays = []
    for _day in _days:
        d = {
             'day':_day,
             'date':_date,
             'full':'%s<br>%s' % (_day, _date)
        }
        weekdays.append(d)
        _date += timedelta(days=1)
    return weekdays

def lastweek(day=date.today()):
    onthelastsunday = day + timedelta(days=-(date.weekday(day) + 7))
    onsunday = day + timedelta(days=-(date.weekday(day)))
    return (onthelastsunday, onsunday)
        
def datedelta2list(d1,d2):
    dlist = []
    for i in range((d2-d1).days + 1):
        dlist.append(d1 + timedelta(days=i))
    return dlist

class Weekly():
    def __init__(self, sunday, saturday):
        self.sunday = sunday
        self.saturday = saturday
        
    def workdays(self):
        return 5
    
    def workhours(self, hours_of_day):
        return self.workdays() * hours_of_day

if __name__ == '__main__':
    start,end = lastweek(date.today())
    print start,end
