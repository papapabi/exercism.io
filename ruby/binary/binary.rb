class Binary
  def self.to_decimal(n)
    raise ArgumentError.new('Input valid binary number') if not_valid?(n)
    n.reverse.each_char.with_index.reduce(0) do |d_val, (c, i)|
      d_val += 2**i * c.to_i
    end
  end

  private 

  def self.not_valid?(n)
    n =~ /[^01]/
  end
end

module BookKeeping
  VERSION = 3
end
