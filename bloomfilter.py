import math
import mmh3
from bitarray import bitarray

class BloomFilter(object):
    #Class for Bloom filter, using murmur3 hash function
    def __init__(self, items_count, fp_prob):
        '''
        items_count : int
            Number of items expected to be stored in bloom filter
        fp_prob : float
            False Positive probability in decimal
        '''
        self.fp_prob = fp_prob # False possible probability in decimal
        self.size = self.get_size(items_count, fp_prob) # Size of bit array
        self.hash_count = self.get_hash_count(self.size, items_count) # no. of hash fn()
        self.bit_array = bitarray(self.size) # Bit array of given size
        self.bit_array.setall(0) # initialize all bits as 0
        print("n %d p %f bit array sz %d hash count %d" %(items_count, fp_prob, self.size, self.hash_count))

    def add(self, item):
        '''
        Add an item in the filter
        '''
        digests = []
        for i in range(self.hash_count):

            # create digest for given item.
            # i work as seed to mmh3.hash() function
            # With different seed, digest created is different
            digest = mmh3.hash(item, i) % self.size
            digests.append(digest)

            # set the bit True in bit_array
            self.bit_array[digest] = True

    def check(self, item):
        '''
        Check for existence of an item in filter
        '''
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == False:

                # if any of bit is False then,its not present
                # in filter
                # else there is probability that it exist
                return False
        return True

    @classmethod
    def get_size(self, n, p):
        '''
        Return the size of bit array(m) to used
        m = -(n * lg(p)) / (lg(2)^2)
        n : int number of items expected to be stored in filter
        p : float False Positive probability in decimal
        '''
        m = -(n * math.log(p))/(math.log(2)**2)
        return int(m)

    @classmethod
    def get_hash_count(self, m, n):
        '''
        Return the number of hash functions (k) to be used
        k = (m/n) * lg(2)
        m : int size of bit array
        n : int number of items expected to be stored in filter
        '''
        k = (m/n) * math.log(2)
        return int(k)

BloomFilter(40,0.01)
BloomFilter(40000000,0.1)
BloomFilter(40000000,0.01)
BloomFilter(1000000,0.01)

