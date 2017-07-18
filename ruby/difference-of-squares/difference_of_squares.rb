class Squares
  def initialize(n)
    @n = n 
    @sum_of_squares = (1..n).map { |i| i**2 }.reduce(:+)
    @square_of_sum = (1..n).reduce(:+)**2
  end  
  def square_of_sum
    @square_of_sum
  end
  def sum_of_squares
    @sum_of_squares
  end
  def difference
    @square_of_sum - @sum_of_squares
  end
end
