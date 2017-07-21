module RomanNumeral
  TO_ROMAN = { 1 => "I", 4 => "IV", 5 => "V", 9 => "IX", 10 => "X",
               40 => "XL", 50 => "L", 90 => "XC", 100 => "C",
               400 => "CD", 500 => "D", 900 => "CM", 1000 => "M" }
  def to_roman
    n, roman = self, String(nil)
    until n == 0
      roman_val = TO_ROMAN.keys.select { |k| k <= n }.last
      n -= roman_val
      roman << TO_ROMAN[roman_val]
    end
    roman
  end
end

class Integer
  include RomanNumeral
end

module BookKeeping
  VERSION = 2
end
