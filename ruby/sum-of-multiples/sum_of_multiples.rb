require 'set'

class SumOfMultiples
  attr_reader :base_multiples

  def initialize(*args)
    @base_multiples = args.sort
  end

  def to(n)
    total_multiples = Set.new
    base_multiples.each do |multiple|
      multiplier = 1
      while (multiple * multiplier) < n
        total_multiples << multiple * multiplier
        multiplier += 1
      end
    end
    total_multiples.reduce(0, :+)
  end
end

module BookKeeping
  VERSION = 1 
end
