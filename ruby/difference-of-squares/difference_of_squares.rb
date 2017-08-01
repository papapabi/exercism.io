class Squares
  attr_accessor :square_of_sum, :sum_of_squares

  def initialize(n)
    @n = n 
    @sum_of_squares = (1..n).map { |i| i**2 }.reduce(:+)
    @square_of_sum = (1..n).reduce(:+)**2
  end  

  def difference
    square_of_sum - sum_of_squares
  end
end

module BookKeeping
  VERSION = 4
end
