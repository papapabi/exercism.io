require 'prime'

class PrimeFactors
  def self.for(n)
    factors = []
    return factors if n == 1
    n.prime_division.each do |(prime, exponent)|
      exponent.times { factors << prime }
    end
    factors
  end
end
