import storm
import os


class SaveCSVBolt(storm.BasicBolt):
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context
        self.path_storage = '/tmp/stockage_ville'

    def process(self, tup):
        city = tup.values[0]
        date = tup.values[1]
        total_available_stands = tup.values[2]
        if not os.path.exists(self.path_storage):
            os.makedirs(self.path_storage)
        if os.path.exists(self.path_storage + '/' + city + '.csv'):
            with open(self.path_storage + '/' + city + '.csv', 'a') as file:
                file.write(str(date) + ';' + str(total_available_stands) + '\n')
        else:
            with open(self.path_storage + '/' + city + '.csv', 'w') as file:
                file.write(str(date) + ';' + str(total_available_stands) + '\n')


# Start the bolt when it's invoked
SaveCSVBolt().run()
