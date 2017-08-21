class Trinary
  attr_accessor :trinary_s

  def initialize(trinary_s)
    @trinary_s = trinary_s
  end

  def to_decimal
    return 0 if not_valid?(trinary_s)
    trinary_s.reverse.each_char.with_index.inject(0) do |d_val, (c, i)|
      d_val += 3**i * c.to_i
    end
  end

  private 
  def not_valid?(s)
    /[^012]/ =~ s
  end
end

module BookKeeping
  VERSION = 1
end
