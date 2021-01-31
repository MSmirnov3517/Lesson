import time
class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        print(TrafficLight.__color[0])
        time.sleep(7)
        print(TrafficLight.__color[1])
        time.sleep(2)
        print(TrafficLight.__color[2])
        time.sleep(5)

run = TrafficLight()
run.running()
