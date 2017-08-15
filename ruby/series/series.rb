class Series
  attr_accessor :num_s

  def initialize(s)
    @num_s = s
  end

  # Returns an array of contiguous 'slices' of length n from num_s.
  # Raises an ArgumentError if n is not in the closed interval [1..num_s.length]
  def slices(n)
    raise ArgumentError unless (1..num_s.length).include? n
    num_s.chars.each_cons(n).map { |cons| cons.join }
  end
end
