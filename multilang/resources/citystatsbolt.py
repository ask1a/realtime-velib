import storm
import datetime
import time


class RollingStatBolt(storm.BasicBolt):

    def initialize(self, conf, context):
        self._conf = conf
        self._context = context
        self.window_sec = 5
        self.tups = {}
        self.last_city = {}
        storm.logInfo("CityStat bolt instance starting...")

    def bike_city(self, city):
        x = []
        for k, v in self.tups[city].items():
            x.append(sum(v) / len(v))
        return int(sum(x))

    def ts_day(self, datee):
        return int(datetime.datetime.strptime(datee, "%Y-%m-%d %H:%M:%S").hour * 60 * 60 + datetime.datetime.strptime(datee, "%Y-%m-%d %H:%M:%S").minute * 60 + datetime.datetime.strptime(datee, "%Y-%m-%d %H:%M:%S").second)

    def date_svg(self, datee, ts_time):
        return datee[:11] + datetime.datetime.strftime(datetime.datetime.utcfromtimestamp(ts_time * self.window_sec), "%H:%M:%S")

    def process(self, tup):
        city = tup.values[0]
        station_id = tup.values[1]
        date = tup.values[2]
        available_stands = tup.values[3]

        try:
            self.last_city[city]
        except KeyError:
            self.last_city[city] = date

        if self.last_city[city] != date:
            if self.ts_day(date) / self.window_sec > self.ts_day(self.last_city[city]) / self.window_sec:
                total_available_stands = self.bike_city(city)
                storm.emit([city, self.date_svg(date, self.ts_day(date) / self.window_sec), total_available_stands])
                self.tups[city] = {}
            self.last_city[city] = date

        if city not in self.tups:
            self.tups[city] = {}
        city_stations = self.tups[city]
        if station_id not in city_stations:
            city_stations[station_id] = []
        city_stations[station_id].append(available_stands)


# Start the bolt when it's invoked
RollingStatBolt().run()
