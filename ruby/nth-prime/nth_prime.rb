class Prime
  class << self
    attr_accessor :primes
    SIEVE_STEP = 10_000

    def nth(index)
      raise ArgumentError.new('N must be positive') unless index > 0
      generate_primes_until(index)
    end

    def generate_primes_until(n)
      c = SIEVE_STEP
      until self.primes.size > n
        sieve(c)
        c += SIEVE_STEP
      end
      self.primes[n - 1]
    end

    def sieve(max)
      sieve = (0..max).to_a
      sieve[0] = sieve[1] = nil
      sieve.each do |p|
        next unless p
        break if p*p > max
        (p*p).step(max, p) { |m| sieve[m] = nil } 
      end
      self.primes = sieve.compact
    end

    def primes
      @primes ||= []
    end
  end
end

module BookKeeping
  VERSION = 1
end

