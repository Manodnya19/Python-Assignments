class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other):
        total_minutes = self.minutes + other.minutes
        extra_hours = total_minutes // 60
        final_minutes = total_minutes % 60
        final_hours = self.hours + other.hours + extra_hours
        return Time(final_hours, final_minutes)

    def displayTime(self):
        print(f"{self.hours} hr and {self.minutes} min")

    def displayMinute(self):
        total = self.hours * 60 + self.minutes
        print(f"Total minutes: {total}")

t1 = Time(2, 50)
t2 = Time(1, 20)

t3 = t1.addTime(t2)

t3.displayTime()      
t3.displayMinute()    
