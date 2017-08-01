class Sieve
  attr_accessor :sieve
  attr_reader :primes

  def initialize(max_bound)
    @sieve = {}
    @primes = []
    (2..max_bound).each { |i| @sieve[i] = false }
  end

  def primes
    self.sieve.keys.each do |key|
      next if self.sieve[key] 
      self.sieve.each do |k, v| 
        next if k <= key 
        self.sieve[k] = true if k % key == 0 
      end
    end
    @primes = self.sieve.select { |k, v| v == false }.keys.to_a
  end
end

module BookKeeping
  VERSION = 1
end
