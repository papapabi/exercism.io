require 'prime'

class PrimeFactors
  def self.for(n)
    return [] if n == 1
    n.prime_division.map do |(prime, exponent)|
      [].tap { |tap| exponent.times { tap << prime } }
    end.flatten
  end
end
