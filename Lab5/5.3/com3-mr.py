from functools import reduce
from mrjob.job import MRJob, MRStep

class MRWordFrequencyCount(MRJob):

    def mapper1(self, _, line):
        cp, precio, fecha = line.split(',')
        
        yield cp, (float(precio), fecha)

    def reducer1(self, cp, values):
        yield cp, min(list(values))
    
    def mapper2(self, cp, value):
        yield value[1], 1
    
    def reducer2(self, fecha, values):
        yield None, (sum(values), fecha)
    
    def reducer3(self, _, values):
        yield 'Dia negro', max(values)

    def steps(self):
        return [
            MRStep(mapper=self.mapper1, reducer=self.reducer1),
            MRStep(mapper=self.mapper2, reducer=self.reducer2),
            MRStep(reducer=self.reducer3)
        ]

if __name__ == '__main__':
    MRWordFrequencyCount.run()