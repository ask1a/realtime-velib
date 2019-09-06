import storm
import json

class ParsingBolt(storm.BasicBolt):
    # There's nothing to initialize here,
    # since this is just a split and emit
    # Initialize this instance
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context
        # storm.logInfo("Parsing bolt instance starting...")

    def process(self, tup):
        # Split the inbound sentence at spaces
        station = json.loads(tup.values[0].decode())
        city = station["contract_name"]
        station_id = station["number"]
        date = station["date"]
        available_stands = station["available_bike_stands"]

        # Loop over words and emit
        storm.emit([city, station_id, date, available_stands])

# Start the bolt when it's invoked
ParsingBolt().run()
